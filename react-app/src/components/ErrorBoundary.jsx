import { Component } from 'react'
import { useLocation } from 'react-router'
import { TriangleAlert } from 'lucide-react'

class Boundary extends Component {
  state = { failed: false }

  static getDerivedStateFromError() {
    return { failed: true }
  }

  componentDidCatch(error) {
    console.error(error)
  }

  render() {
    if (!this.state.failed) return this.props.children
    return (
      <div className="container">
        <div className="empty card" role="alert">
          <div className="empty__icon"><TriangleAlert size={30} aria-hidden="true" /></div>
          <h2>Something went wrong</h2>
          <p>This page hit an unexpected error. Reloading usually fixes it.</p>
          <button type="button" className="btn btn--primary" onClick={() => window.location.reload()}>Reload page</button>
        </div>
      </div>
    )
  }
}

// Keyed by path, so navigating away from a broken page recovers automatically
export default function ErrorBoundary({ children }) {
  const { pathname } = useLocation()
  return <Boundary key={pathname}>{children}</Boundary>
}
