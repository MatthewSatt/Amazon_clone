import { Compass } from 'lucide-react'
import EmptyState from '../components/EmptyState'

export default function NotFound() {
  return (
    <div className="container">
      <EmptyState icon={Compass} title="We can’t find that page" action={{ to: '/', label: 'Go to the home page' }}>
        The link may be broken, or the page may have been removed.
      </EmptyState>
    </div>
  )
}
