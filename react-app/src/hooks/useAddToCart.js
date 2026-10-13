import { useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useLocation, useNavigate } from 'react-router'
import { addToCart } from '../features/cartSlice'
import { firstError } from '../features/thunks'
import { notify } from '../features/toastsSlice'
import { selectUser } from '../features/sessionSlice'

// Adds a product to the cart, sending signed-out visitors to sign in first
export default function useAddToCart() {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const location = useLocation()
  const user = useSelector(selectUser)
  const [adding, setAdding] = useState(false)

  const add = async (product, quantity = 1) => {
    if (!user) {
      dispatch(notify('Sign in to add items to your cart.', 'error'))
      navigate('/login', { state: { from: location.pathname + location.search } })
      return false
    }
    setAdding(true)
    const result = await dispatch(addToCart({ productId: product.id, quantity }))
    setAdding(false)
    if (addToCart.fulfilled.match(result)) {
      dispatch(notify(`Added “${product.name.length > 48 ? `${product.name.slice(0, 48)}…` : product.name}” to your cart.`))
      return true
    }
    dispatch(notify(firstError(result.payload), 'error'))
    return false
  }

  return { add, adding }
}
