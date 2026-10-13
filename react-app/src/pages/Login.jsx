import { useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link, Navigate, useLocation } from 'react-router'
import { selectUser, login } from '../features/sessionSlice'
import { notify } from '../features/toastsSlice'
import Logo from '../components/Logo'
import { Field, PasswordInput } from './AuthForm'
import './auth.css'

export default function Login() {
  const dispatch = useDispatch()
  const location = useLocation()
  const user = useSelector(selectUser)
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [errors, setErrors] = useState({})
  const [busy, setBusy] = useState(false)
  const from = location.state?.from ?? '/'

  if (user) return <Navigate to={from} replace />

  const signIn = async (credentials) => {
    setBusy(true)
    setErrors({})
    const result = await dispatch(login(credentials))
    setBusy(false)
    if (login.rejected.match(result)) {
      setErrors(result.payload?.errors ?? { form: ['Something went wrong. Please try again.'] })
    } else {
      dispatch(notify('Welcome back!'))
    }
  }

  const onSubmit = (event) => {
    event.preventDefault()
    signIn({ email, password })
  }

  return (
    <div className="auth container">
      <div className="auth__card card">
        <div className="auth__brand"><Logo /></div>
        <h1>Sign in</h1>
        <p className="auth__sub">Welcome back. Enter your details to continue.</p>

        {errors.form && <div className="alert alert--error" role="alert">{errors.form[0]}</div>}

        <form onSubmit={onSubmit} noValidate>
          <Field label="Email" id="email" error={errors.email?.[0]}>
            <input id="email" className="input" type="email" autoComplete="email" value={email}
              onChange={(e) => setEmail(e.target.value)} aria-invalid={Boolean(errors.email)}
              aria-describedby={errors.email ? 'email-error' : undefined} autoFocus />
          </Field>
          <Field label="Password" id="password" error={errors.password?.[0]}>
            <PasswordInput id="password" value={password} onChange={(e) => setPassword(e.target.value)}
              autoComplete="current-password" error={errors.password?.[0]} />
          </Field>
          <button type="submit" className="btn btn--primary btn--lg btn--block" disabled={busy}>
            {busy ? 'Signing in…' : 'Sign in'}
          </button>
        </form>

        <div className="auth__divider">New here?</div>
        <div className="auth__alt">
          <Link to="/signup" state={location.state} className="btn btn--secondary btn--block">Create your account</Link>
          <button type="button" className="btn btn--ghost btn--block" disabled={busy}
            onClick={() => signIn({ email: 'demo@aa.io', password: 'password' })}>
            Continue as demo user
          </button>
        </div>
        <p className="auth__fineprint">
          This is a portfolio project: no real orders are placed and the demo account is shared.
        </p>
      </div>
    </div>
  )
}
