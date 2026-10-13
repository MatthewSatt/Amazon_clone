import { Link } from 'react-router'

export default function EmptyState({ icon: Icon, title, children, action }) {
  return (
    <div className="empty card">
      {Icon && <div className="empty__icon"><Icon size={30} aria-hidden="true" /></div>}
      <h2>{title}</h2>
      {children && <p>{children}</p>}
      {action && <Link to={action.to} className="btn btn--primary">{action.label}</Link>}
    </div>
  )
}
