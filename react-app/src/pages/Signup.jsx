import { useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link, Navigate, useLocation } from 'react-router'
import { selectUser, signUp } from '../features/sessionSlice'
import { notify } from '../features/toastsSlice'
import Logo from '../components/Logo'
import { Field, PasswordInput } from './AuthForm'
import './auth.css'

export default function Signup() {
  const dispatch = useDispatch()
  const location = useLocation()
  const user = useSelector(selectUser)
  const [form, setForm] = useState({ username: '', email: '', password: '', confirm: '' })
  const [errors, setErrors] = useState({})
  const [busy, setBusy] = useState(false)
  const from = location.state?.from ?? '/'

  if (user) return <Navigate to={from} replace />

  const update = (name) => (event) => setForm((f) => ({ ...f, [name]: event.target.value }))

  const onSubmit = async (event) => {
    event.preventDefault()
    if (form.password !== form.confirm) {
      setErrors({ confirm: ['Passwords do not match.'] })
      return
    }
    setBusy(true)
    setErrors({})
    const { username, email, password } = form
    const result = await dispatch(signUp({ username, email, password }))
    setBusy(false)
    if (signUp.rejected.match(result)) {
      setErrors(result.payload?.errors ?? { form: ['Something went wrong. Please try again.'] })
    } else {
      dispatch(notify('Your account is ready. Happy shopping!'))
    }
  }

  const input = (name, label, type, autoComplete, hint) => (
    <Field label={label} id={name} error={errors[name]?.[0]} hint={hint}>
      <input id={name} className="input" type={type} autoComplete={autoComplete} value={form[name]}
        onChange={update(name)} aria-invalid={Boolean(errors[name])}
        aria-describedby={errors[name] ? `${name}-error` : undefined} />
    </Field>
  )

  return (
    <div className="auth container">
      <div className="auth__card card">
        <div className="auth__brand"><Logo /></div>
        <h1>Create account</h1>
        <p className="auth__sub">Save your cart, track orders and leave reviews.</p>

        {errors.form && <div className="alert alert--error" role="alert">{errors.form[0]}</div>}

        <form onSubmit={onSubmit} noValidate>
          {input('username', 'Username', 'text', 'username')}
          {input('email', 'Email', 'email', 'email')}
          <Field label="Password" id="password" error={errors.password?.[0]} hint="At least 6 characters.">
            <PasswordInput id="password" value={form.password} onChange={update('password')}
              autoComplete="new-password" error={errors.password?.[0]} />
          </Field>
          <Field label="Confirm password" id="confirm" error={errors.confirm?.[0]}>
            <PasswordInput id="confirm" value={form.confirm} onChange={update('confirm')}
              autoComplete="new-password" error={errors.confirm?.[0]} />
          </Field>
          <button type="submit" className="btn btn--primary btn--lg btn--block" disabled={busy}>
            {busy ? 'Creating account…' : 'Create account'}
          </button>
        </form>

        <div className="auth__divider">Already a customer?</div>
        <Link to="/login" state={location.state} className="btn btn--secondary btn--block">Sign in instead</Link>
      </div>
    </div>
  )
}
