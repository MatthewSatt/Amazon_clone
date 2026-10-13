import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link, NavLink, useLocation, useNavigate } from 'react-router'
import { Menu, ShoppingCart, X, Crown, LogIn, LogOut, Package } from 'lucide-react'
import { selectUser, logout } from '../features/sessionSlice'
import { selectTypes } from '../features/catalogSlice'
import { fetchCart, selectCartCount } from '../features/cartSlice'
import { notify } from '../features/toastsSlice'
import Logo from './Logo'
import SearchBox from './SearchBox'
import './Header.css'

export default function Header() {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const location = useLocation()
  const user = useSelector(selectUser)
  const types = useSelector(selectTypes)
  const cartCount = useSelector(selectCartCount)
  const [drawerPath, setDrawerPath] = useState(null)
  // The drawer closes itself on navigation: it only counts as open for the page it was opened on
  const drawerOpen = drawerPath === location.pathname

  useEffect(() => {
    if (user) dispatch(fetchCart())
  }, [dispatch, user])

  useEffect(() => {
    if (!drawerOpen) return
    const onKey = (event) => event.key === 'Escape' && setDrawerPath(null)
    document.addEventListener('keydown', onKey)
    return () => document.removeEventListener('keydown', onKey)
  }, [drawerOpen])

  const signOut = async () => {
    setDrawerPath(null)
    await dispatch(logout())
    dispatch(notify('You have been signed out.'))
    navigate('/')
  }

  return (
    <header className="site-header">
      <div className="site-header__main">
        <div className="container site-header__row">
          <button type="button" className="icon-btn site-header__menu" aria-label="Open menu"
            aria-expanded={drawerOpen} onClick={() => setDrawerPath(location.pathname)}>
            <Menu size={24} />
          </button>
          <Logo />
          <div className="site-header__search"><SearchBox /></div>

          <nav className="site-header__actions" aria-label="Account">
            {user ? (
              <div className="hdr-link hdr-link--static">
                <span className="hdr-link__small">Hello, {user.username}</span>
                <button type="button" className="hdr-link__strong hdr-link__button" onClick={signOut}>
                  <LogOut size={14} aria-hidden="true" /> Sign out
                </button>
              </div>
            ) : (
              <Link to="/login" className="hdr-link">
                <span className="hdr-link__small">Hello, sign in</span>
                <span className="hdr-link__strong"><LogIn size={14} aria-hidden="true" /> Account</span>
              </Link>
            )}
            {user && (
              <Link to="/orders" className="hdr-link hdr-link--hide-sm">
                <span className="hdr-link__small">Returns &amp;</span>
                <span className="hdr-link__strong">Orders</span>
              </Link>
            )}
            <Link to="/prime" className="hdr-link hdr-link--hide-sm">
              <span className="hdr-link__small">{user?.isPrime ? 'You are' : 'Try'}</span>
              <span className="hdr-link__strong hdr-prime"><Crown size={14} aria-hidden="true" /> Prime</span>
            </Link>
            <Link to="/cart" className="hdr-cart" aria-label={`Cart, ${cartCount} items`}>
              <ShoppingCart size={28} aria-hidden="true" />
              <span className="hdr-cart__count" aria-hidden="true">{cartCount}</span>
              <span className="hdr-cart__label">Cart</span>
            </Link>
          </nav>
        </div>
        <div className="container site-header__mobile-search"><SearchBox /></div>
      </div>

      <nav className="subnav" aria-label="Categories">
        <div className="container subnav__row">
          <button type="button" className="subnav__all" onClick={() => setDrawerPath(location.pathname)}>
            <Menu size={18} aria-hidden="true" /> All
          </button>
          {types.map((type) => (
            <NavLink key={type.id} to={`/category/${type.id}`} className="subnav__link">{type.name}</NavLink>
          ))}
          <NavLink to="/prime" className="subnav__link subnav__link--prime"><Crown size={14} aria-hidden="true" /> Prime</NavLink>
        </div>
      </nav>

      {drawerOpen && (
        <div className="drawer" role="dialog" aria-modal="true" aria-label="Menu">
          <div className="drawer__overlay" onClick={() => setDrawerPath(null)} />
          <aside className="drawer__panel">
            <div className="drawer__top">
              <span>{user ? `Hello, ${user.username}` : 'Hello, sign in'}</span>
              <button type="button" className="icon-btn" aria-label="Close menu" onClick={() => setDrawerPath(null)} autoFocus>
                <X size={22} />
              </button>
            </div>
            <div className="drawer__body">
              <h2>Shop by category</h2>
              {types.map((type) => (
                <Link key={type.id} to={`/category/${type.id}`} onClick={() => setDrawerPath(null)}>{type.name}</Link>
              ))}
              <h2>Your account</h2>
              {user ? (
                <>
                  <Link to="/orders" onClick={() => setDrawerPath(null)}><Package size={16} /> Your orders</Link>
                  <Link to="/cart" onClick={() => setDrawerPath(null)}><ShoppingCart size={16} /> Your cart</Link>
                  <Link to="/prime" onClick={() => setDrawerPath(null)}><Crown size={16} /> Prime</Link>
                  <button type="button" onClick={signOut}><LogOut size={16} /> Sign out</button>
                </>
              ) : (
                <>
                  <Link to="/login" onClick={() => setDrawerPath(null)}><LogIn size={16} /> Sign in</Link>
                  <Link to="/signup" onClick={() => setDrawerPath(null)}>Create account</Link>
                  <Link to="/prime" onClick={() => setDrawerPath(null)}><Crown size={16} /> Prime</Link>
                </>
              )}
            </div>
          </aside>
        </div>
      )}
    </header>
  )
}
