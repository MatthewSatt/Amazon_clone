import { useEffect } from 'react'
import { useDispatch } from 'react-redux'
import { Outlet, useLocation } from 'react-router'
import { fetchCatalog } from '../features/catalogSlice'
import Header from './Header'
import Footer from './Footer'
import Toasts from './Toasts'
import ErrorBoundary from './ErrorBoundary'

function ScrollToTop() {
  const { pathname } = useLocation()
  useEffect(() => {
    window.scrollTo(0, 0)
  }, [pathname])
  return null
}

export default function Layout() {
  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(fetchCatalog())
  }, [dispatch])

  return (
    <>
      <ScrollToTop />
      <a href="#main" className="skip-link">Skip to content</a>
      <Header />
      <main id="main" className="page">
        <ErrorBoundary>
          <Outlet />
        </ErrorBoundary>
      </main>
      <Footer />
      <Toasts />
    </>
  )
}
