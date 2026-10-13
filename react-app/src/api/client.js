export class ApiError extends Error {
  constructor(status, errors) {
    super(errors?.form?.[0] ?? 'Request failed')
    this.status = status
    // { field: [messages] }, with form-level messages under "form"
    this.errors = errors
  }
}

// Flask sets this cookie on every page/API response; it must be echoed back
// in a header on anything that changes data
function csrfToken() {
  const cookie = document.cookie.split('; ').find((row) => row.startsWith('csrf_token='))
  return cookie ? decodeURIComponent(cookie.split('=')[1]) : ''
}

export async function api(path, { method = 'GET', body } = {}) {
  const headers = { Accept: 'application/json' }
  if (body !== undefined) headers['Content-Type'] = 'application/json'
  if (method !== 'GET') headers['X-CSRFToken'] = csrfToken()

  let response
  try {
    response = await fetch(`/api${path}`, {
      method,
      headers,
      body: body === undefined ? undefined : JSON.stringify(body),
      credentials: 'same-origin',
    })
  } catch {
    throw new ApiError(0, { form: ['Network error. Check your connection and try again.'] })
  }

  const data = await response.json().catch(() => null)
  if (!response.ok) {
    // The session ended behind our back (not just a failed sign-in attempt)
    if (response.status === 401 && !path.startsWith('/auth/')) {
      window.dispatchEvent(new Event('auth:expired'))
    }
    throw new ApiError(response.status, data?.errors ?? { form: ['Something went wrong. Please try again.'] })
  }
  return data
}
