import { configureStore } from '@reduxjs/toolkit'
import session from '../features/sessionSlice'
import catalog from '../features/catalogSlice'
import cart from '../features/cartSlice'
import orders from '../features/ordersSlice'
import reviews from '../features/reviewsSlice'
import toasts from '../features/toastsSlice'

export const store = configureStore({
  reducer: { session, catalog, cart, orders, reviews, toasts },
})
