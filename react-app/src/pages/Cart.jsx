import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link, useNavigate } from 'react-router'
import { Crown, ShoppingCart, Trash2 } from 'lucide-react'
import { fetchCart, removeFromCart, selectCart, updateQuantity } from '../features/cartSlice'
import { placeOrder } from '../features/ordersSlice'
import { selectUser } from '../features/sessionSlice'
import { firstError } from '../features/thunks'
import { notify } from '../features/toastsSlice'
import EmptyState from '../components/EmptyState'
import Price from '../components/Price'
import ProductImage from '../components/ProductImage'
import QuantitySelect from '../components/QuantitySelect'
import { money, pluralize } from '../utils/format'
import './Cart.css'

function CartLine({ item }) {
  const dispatch = useDispatch()
  const [busy, setBusy] = useState(false)
  const { product } = item

  const run = async (action, successMessage) => {
    setBusy(true)
    const result = await dispatch(action)
    setBusy(false)
    if (result.error) dispatch(notify(firstError(result.payload), 'error'))
    else if (successMessage) dispatch(notify(successMessage))
  }

  return (
    <li className="cart-line">
      <Link to={`/product/${product.id}`} className="cart-line__media" aria-hidden="true" tabIndex={-1}>
        <ProductImage src={product.image} />
      </Link>
      <div className="cart-line__info">
        <h2><Link to={`/product/${product.id}`}>{product.name}</Link></h2>
        <p className="cart-line__stock">In stock</p>
        <div className="cart-line__controls">
          <QuantitySelect value={item.quantity} disabled={busy}
            onChange={(quantity) => run(updateQuantity({ id: item.id, quantity }))} />
          <button type="button" className="btn btn--danger btn--sm" disabled={busy}
            onClick={() => run(removeFromCart(item.id), 'Item removed from your cart.')}>
            <Trash2 size={14} /> Remove
          </button>
        </div>
      </div>
      <div className="cart-line__price">
        <Price value={product.price * item.quantity} />
        {item.quantity > 1 && <span className="muted">{money(product.price)} each</span>}
      </div>
    </li>
  )
}

export default function Cart() {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const user = useSelector(selectUser)
  const { items, summary, loaded } = useSelector(selectCart)
  const [placing, setPlacing] = useState(false)

  useEffect(() => {
    dispatch(fetchCart())
  }, [dispatch])

  const checkout = async () => {
    setPlacing(true)
    const result = await dispatch(placeOrder())
    setPlacing(false)
    if (placeOrder.fulfilled.match(result)) {
      navigate('/orders', { state: { placed: result.payload.summary } })
    } else {
      dispatch(notify(firstError(result.payload), 'error'))
    }
  }

  if (!loaded) {
    return (
      <div className="container" aria-busy="true" aria-label="Loading cart">
        <div className="skeleton" style={{ height: 320 }} />
      </div>
    )
  }

  if (items.length === 0) {
    return (
      <div className="container">
        <EmptyState icon={ShoppingCart} title="Your cart is empty" action={{ to: '/', label: 'Continue shopping' }}>
          Add something you love and it will show up here.
        </EmptyState>
      </div>
    )
  }

  return (
    <div className="container cart">
      <section className="cart__items card" aria-labelledby="cart-title">
        <header className="cart__head">
          <h1 id="cart-title" className="page-title">Shopping cart</h1>
          <span className="muted">{pluralize(summary.count, 'item')}</span>
        </header>
        <ul>{items.map((item) => <CartLine key={item.id} item={item} />)}</ul>
        <p className="cart__subtotal-inline">
          Subtotal ({pluralize(summary.count, 'item')}): <strong>{money(summary.subtotal)}</strong>
        </p>
      </section>

      <aside className="cart__summary card" aria-label="Order summary">
        <h2>Order summary</h2>
        <dl>
          <div><dt>Items ({summary.count})</dt><dd>{money(summary.subtotal)}</dd></div>
          <div>
            <dt>Shipping</dt>
            <dd className={user.isPrime ? 'is-free' : ''}>{user.isPrime ? 'FREE' : money(summary.shipping)}</dd>
          </div>
          {user.isPrime && summary.shipping_saved > 0 && (
            <div className="cart__saved"><dt><Crown size={14} /> Prime savings</dt><dd>−{money(summary.shipping_saved)}</dd></div>
          )}
          <div className="cart__total"><dt>Order total</dt><dd>{money(summary.total)}</dd></div>
        </dl>
        <button type="button" className="btn btn--primary btn--lg btn--block" onClick={checkout} disabled={placing}>
          {placing ? 'Placing order…' : 'Place your order'}
        </button>
        <p className="muted cart__note">Demo store: no payment is collected.</p>
        {!user.isPrime && (
          <Link to="/prime" className="cart__upsell">
            <Crown size={18} />
            <span>Join Prime and save <strong>{money(summary.subtotal * 0.05)}</strong> on shipping.</span>
          </Link>
        )}
      </aside>
    </div>
  )
}
