import { useSelector } from 'react-redux'
import { Link } from 'react-router'
import { ArrowUp } from 'lucide-react'
import { selectTypes } from '../features/catalogSlice'
import { selectUser } from '../features/sessionSlice'
import Logo from './Logo'
import './Footer.css'

export default function Footer() {
  const types = useSelector(selectTypes)
  const user = useSelector(selectUser)

  return (
    <footer className="site-footer">
      <button type="button" className="site-footer__top" onClick={() => window.scrollTo({ top: 0 })}>
        <ArrowUp size={16} aria-hidden="true" /> Back to top
      </button>
      <div className="container site-footer__grid">
        <div>
          <h2>Shop</h2>
          <ul>
            {types.slice(0, 6).map((type) => (
              <li key={type.id}><Link to={`/category/${type.id}`}>{type.name}</Link></li>
            ))}
          </ul>
        </div>
        <div>
          <h2>More categories</h2>
          <ul>
            {types.slice(6).map((type) => (
              <li key={type.id}><Link to={`/category/${type.id}`}>{type.name}</Link></li>
            ))}
          </ul>
        </div>
        <div>
          <h2>Your account</h2>
          <ul>
            {user ? (
              <>
                <li><Link to="/orders">Your orders</Link></li>
                <li><Link to="/cart">Your cart</Link></li>
              </>
            ) : (
              <>
                <li><Link to="/login">Sign in</Link></li>
                <li><Link to="/signup">Create account</Link></li>
              </>
            )}
            <li><Link to="/prime">Prime</Link></li>
          </ul>
        </div>
        <div>
          <h2>About</h2>
          <p>
            A full-stack portfolio project built with React, Redux, Flask and PostgreSQL.
            Not affiliated with Amazon.com, Inc.; no real purchases are made.
          </p>
        </div>
      </div>
      <div className="site-footer__bottom">
        <Logo />
        <span>© {new Date().getFullYear()} Matthew Satterwhite</span>
      </div>
    </footer>
  )
}
