import { splitPrice } from '../utils/format'

// "$12.99" with the cents set small, like a retail price tag
export default function Price({ value, size = 'md' }) {
  const { whole, cents } = splitPrice(value)
  return (
    <span className={`price price--${size}`} aria-label={`$${whole}.${cents}`}>
      <span className="price__symbol" aria-hidden="true">$</span>
      <span className="price__whole" aria-hidden="true">{whole}</span>
      <span className="price__cents" aria-hidden="true">{cents}</span>
    </span>
  )
}
