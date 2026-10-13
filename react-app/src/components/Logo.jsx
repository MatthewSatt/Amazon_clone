import { Link } from 'react-router'

export default function Logo({ className = '' }) {
  return (
    <Link to="/" className={`logo ${className}`} aria-label="Amazon Clone home">
      <span className="logo__word">amazon</span>
      <span className="logo__tag">clone</span>
      <svg className="logo__smile" viewBox="0 0 80 14" aria-hidden="true">
        <path d="M2 3c18 11 48 11 72 -1" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" />
        <path d="M66 0l9 3-5 8" fill="none" stroke="currentColor" strokeWidth="3.4" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    </Link>
  )
}
