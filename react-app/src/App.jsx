import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { BrowserRouter, Route, Routes } from 'react-router'
import { fetchSession, sessionExpired } from './features/sessionSlice'
import { notify } from './features/toastsSlice'
import Layout from './components/Layout'
import ProtectedRoute from './components/ProtectedRoute'
import Home from './pages/Home'
import { CategoryPage, SearchPage } from './pages/Listing'
import Product from './pages/Product'
import Cart from './pages/Cart'
import Orders from './pages/Orders'
import Prime from './pages/Prime'
import Login from './pages/Login'
import Signup from './pages/Signup'
import NotFound from './pages/NotFound'

export default function App() {
  const dispatch = useDispatch()
  const ready = useSelector((state) => state.session.ready)

  useEffect(() => {
    dispatch(fetchSession())
    // The API reports a 401 when the session ends while the app is open
    const onExpired = () => {
      dispatch(sessionExpired())
      dispatch(notify('Your session expired. Please sign in again.', 'error'))
    }
    window.addEventListener('auth:expired', onExpired)
    return () => window.removeEventListener('auth:expired', onExpired)
  }, [dispatch])

  if (!ready) {
    return (
      <div className="fullpage-loader" role="status" aria-label="Loading">
        <div className="spinner" />
      </div>
    )
  }

  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="category/:typeId" element={<CategoryPage />} />
          <Route path="search" element={<SearchPage />} />
          <Route path="product/:productId" element={<Product />} />
          <Route path="prime" element={<Prime />} />
          <Route path="login" element={<Login />} />
          <Route path="signup" element={<Signup />} />
          <Route element={<ProtectedRoute />}>
            <Route path="cart" element={<Cart />} />
            <Route path="orders" element={<Orders />} />
          </Route>
          <Route path="*" element={<NotFound />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
