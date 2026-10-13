import { createSlice } from '@reduxjs/toolkit'
import { api } from '../api/client'
import { createApiThunk } from './thunks'
import { logout, sessionExpired } from './sessionSlice'
import { placeOrder } from './ordersSlice'

const empty = { items: [], summary: { count: 0, subtotal: 0, shipping: 0, shipping_saved: 0, total: 0 } }

export const fetchCart = createApiThunk('cart/fetch', () => api('/carts/'))

export const addToCart = createApiThunk('cart/add', ({ productId, quantity = 1 }) =>
  api('/carts/', { method: 'POST', body: { productId, quantity } }))

export const updateQuantity = createApiThunk('cart/updateQuantity', ({ id, quantity }) =>
  api(`/carts/${id}`, { method: 'PUT', body: { quantity } }))

export const removeFromCart = createApiThunk('cart/remove', (id) => api(`/carts/${id}`, { method: 'DELETE' }))

const cartSlice = createSlice({
  name: 'cart',
  initialState: { ...empty, loaded: false },
  extraReducers: (builder) => {
    const setCart = (state, action) => {
      state.items = action.payload.items
      state.summary = action.payload.summary
      state.loaded = true
    }
    const clear = () => ({ ...empty, loaded: false })
    builder
      .addCase(fetchCart.fulfilled, setCart)
      .addCase(addToCart.fulfilled, setCart)
      .addCase(updateQuantity.fulfilled, setCart)
      .addCase(removeFromCart.fulfilled, setCart)
      .addCase(placeOrder.fulfilled, () => ({ ...empty, loaded: true }))
      .addCase(logout.fulfilled, clear)
      .addCase(sessionExpired, clear)
  },
})

export const selectCart = (state) => state.cart
export const selectCartCount = (state) => state.cart.summary.count

export default cartSlice.reducer
