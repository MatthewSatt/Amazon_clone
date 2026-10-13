import { useSelector } from 'react-redux'
import { Navigate, Outlet, useLocation } from 'react-router'
import { selectUser } from '../features/sessionSlice'

// Signed-out visitors are sent to /login and returned here afterwards
export default function ProtectedRoute() {
  const user = useSelector(selectUser)
  const location = useLocation()
  if (!user) return <Navigate to="/login" replace state={{ from: location.pathname + location.search }} />
  return <Outlet />
}
