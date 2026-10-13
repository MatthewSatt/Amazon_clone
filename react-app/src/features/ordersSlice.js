import { createSlice } from '@reduxjs/toolkit'
import { api } from '../api/client'
import { createApiThunk } from './thunks'

export const fetchOrders = createApiThunk('orders/fetch', () => api('/orders/'))

// Checks out the signed-in user's cart; resolves with { orders, summary }
export const placeOrder = createApiThunk('orders/place', () => api('/orders/', { method: 'POST' }))

const ordersSlice = createSlice({
  name: 'orders',
  initialState: { items: [], status: 'idle' },
  extraReducers: (builder) => {
    builder
      .addCase(fetchOrders.pending, (state) => {
        if (state.status === 'idle') state.status = 'loading'
      })
      .addCase(fetchOrders.fulfilled, (state, action) => {
        state.items = action.payload
        state.status = 'ready'
      })
      .addCase(fetchOrders.rejected, (state) => {
        state.status = 'error'
      })
      .addCase(placeOrder.fulfilled, (state, action) => {
        state.items = [...action.payload.orders, ...state.items]
        state.status = 'ready'
      })
      .addMatcher(
        (action) => action.type === 'session/logout/fulfilled' || action.type === 'session/sessionExpired',
        () => ({ items: [], status: 'idle' }),
      )
  },
})

export default ordersSlice.reducer
