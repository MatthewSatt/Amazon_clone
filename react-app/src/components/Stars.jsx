import { Star } from 'lucide-react'

// Read-only star rating; `value` can be fractional (e.g. 4.3)
export default function Stars({ value = 0, count, size = 16, showValue = false }) {
  const percent = Math.max(0, Math.min(5, value)) / 5 * 100
  const row = Array.from({ length: 5 }, (_, i) => <Star key={i} size={size} />)
  const label = value ? `${value.toFixed(1)} out of 5 stars` : 'No ratings yet'

  return (
    <span className="rating" role="img" aria-label={count != null ? `${label}, ${count} reviews` : label}>
      <span className="stars" aria-hidden="true">
        <span className="stars__row stars__row--empty">{row}</span>
        <span className="stars__row stars__row--fill" style={{ width: `${percent}%` }}>{row}</span>
      </span>
      {showValue && value > 0 && <span className="rating__value">{value.toFixed(1)}</span>}
      {count != null && <span className="rating__count">({count.toLocaleString()})</span>}
    </span>
  )
}
