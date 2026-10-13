import { useState } from 'react'
import { Eye, EyeOff } from 'lucide-react'

export function Field({ label, id, error, hint, children }) {
  return (
    <div className="field">
      <label className="field__label" htmlFor={id}>{label}</label>
      {children}
      {hint && !error && <span className="muted" style={{ fontSize: 12 }}>{hint}</span>}
      {error && <span className="field__error" id={`${id}-error`}>{error}</span>}
    </div>
  )
}

export function PasswordInput({ id, value, onChange, autoComplete, error }) {
  const [shown, setShown] = useState(false)
  return (
    <div className="password">
      <input id={id} className="input" type={shown ? 'text' : 'password'} value={value} onChange={onChange}
        autoComplete={autoComplete} aria-invalid={Boolean(error)} aria-describedby={error ? `${id}-error` : undefined} />
      <button type="button" className="password__toggle" onClick={() => setShown((s) => !s)}
        aria-label={shown ? 'Hide password' : 'Show password'}>
        {shown ? <EyeOff size={18} /> : <Eye size={18} />}
      </button>
    </div>
  )
}
