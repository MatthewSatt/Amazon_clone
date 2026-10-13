import { useEffect, useMemo, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link, useLocation } from 'react-router'
import { CheckCircle2, Package, RotateCcw, Star } from 'lucide-react'
import { fetchOrders } from '../features/ordersSlice'
import useAddToCart from '../hooks/useAddToCart'
import EmptyState from '../components/EmptyState'
import ProductImage from '../components/ProductImage'
import { longDate, money, pluralize } from '../utils/format'
import ReviewModal from './ReviewModal'
import './Orders.css'

// Every line of one checkout shares a timestamp, so that's what groups them
function groupOrders(orders) {
  const groups = new Map()
  for (const order of orders) {
    if (!groups.has(order.created_at)) groups.set(order.created_at, [])
    groups.get(order.created_at).push(order)
  }
  return [...groups.entries()].map(([placedAt, lines]) => ({
    placedAt,
    lines,
    number: Math.min(...lines.map((l) => l.id)),
    itemsTotal: lines.reduce((sum, l) => sum + l.price * l.quantity, 0),
    count: lines.reduce((sum, l) => sum + l.quantity, 0),
  }))
}

function OrderLine({ line, onReview }) {
  const { add, adding } = useAddToCart()
  const { product } = line
  return (
    <li className="order-line">
      <Link to={`/product/${product.id}`} className="order-line__media" aria-hidden="true" tabIndex={-1}>
        <ProductImage src={product.image} />
      </Link>
      <div className="order-line__info">
        <h3><Link to={`/product/${product.id}`}>{product.name}</Link></h3>
        <p className="muted">
          {line.quantity > 1 ? `${line.quantity} × ` : ''}{money(line.price)}
        </p>
        <div className="order-line__actions">
          <button type="button" className="btn btn--primary btn--sm" disabled={adding} onClick={() => add(product)}>
            <RotateCcw size={14} /> Buy it again
          </button>
          <button type="button" className="btn btn--secondary btn--sm" onClick={() => onReview(product)}>
            <Star size={14} /> Write a review
          </button>
        </div>
      </div>
    </li>
  )
}

export default function Orders() {
  const dispatch = useDispatch()
  const location = useLocation()
  const { items, status } = useSelector((state) => state.orders)
  const [reviewing, setReviewing] = useState(null)
  const placed = location.state?.placed

  useEffect(() => {
    dispatch(fetchOrders())
  }, [dispatch])

  const groups = useMemo(() => groupOrders(items), [items])

  return (
    <div className="container orders">
      <h1 className="page-title">Your orders</h1>

      {placed && (
        <div className="alert alert--success orders__placed" role="status">
          <CheckCircle2 size={20} />
          <div>
            <strong>Order placed. Thank you!</strong>
            <div>
              You were charged {money(placed.total)}
              {placed.shipping_saved > 0 ? ` and saved ${money(placed.shipping_saved)} on shipping with Prime` : ''}.
              (Demo store: no real payment was taken.)
            </div>
          </div>
        </div>
      )}

      {status === 'loading' || status === 'idle' ? (
        <div className="skeleton" style={{ height: 240 }} aria-busy="true" aria-label="Loading orders" />
      ) : groups.length === 0 ? (
        <EmptyState icon={Package} title="No orders yet" action={{ to: '/', label: 'Start shopping' }}>
          When you place an order, it will show up here.
        </EmptyState>
      ) : (
        groups.map((group) => (
          <section key={group.placedAt} className="order card" aria-label={`Order ${group.number}`}>
            <header className="order__head">
              <div><span>Order placed</span><strong>{longDate(group.placedAt)}</strong></div>
              <div><span>Items total</span><strong>{money(group.itemsTotal)}</strong></div>
              <div><span>Items</span><strong>{pluralize(group.count, 'item')}</strong></div>
              <div className="order__number"><span>Order #</span><strong>{String(group.number).padStart(6, '0')}</strong></div>
            </header>
            <ul>
              {group.lines.map((line) => <OrderLine key={line.id} line={line} onReview={setReviewing} />)}
            </ul>
          </section>
        ))
      )}

      {reviewing && <ReviewModal product={reviewing} onClose={() => setReviewing(null)} />}
    </div>
  )
}
