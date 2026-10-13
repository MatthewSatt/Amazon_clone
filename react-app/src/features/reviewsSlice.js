import { createSlice } from '@reduxjs/toolkit'
import { api } from '../api/client'
import { createApiThunk } from './thunks'
import { fetchProduct } from './catalogSlice'

export const fetchReviews = createApiThunk('reviews/fetch', async (productId) => ({
  productId,
  reviews: await api(`/reviews/product/${productId}`),
}))

// Creates a review, or updates it when `id` is given
export const saveReview = createApiThunk('reviews/save', async ({ id, productId, ...fields }, { dispatch }) => {
  const review = id
    ? await api(`/reviews/${id}`, { method: 'PUT', body: fields })
    : await api(`/reviews/product/${productId}`, { method: 'POST', body: fields })
  dispatch(fetchProduct(productId))
  return review
})

export const deleteReview = createApiThunk('reviews/delete', async ({ id, productId }, { dispatch }) => {
  await api(`/reviews/${id}`, { method: 'DELETE' })
  dispatch(fetchProduct(productId))
  return { id, productId }
})

const reviewsSlice = createSlice({
  name: 'reviews',
  initialState: { byProduct: {} },
  extraReducers: (builder) => {
    builder
      .addCase(fetchReviews.fulfilled, (state, action) => {
        state.byProduct[action.payload.productId] = action.payload.reviews
      })
      .addCase(saveReview.fulfilled, (state, action) => {
        const review = action.payload
        const list = state.byProduct[review.product_id] ?? []
        const index = list.findIndex((item) => item.id === review.id)
        if (index >= 0) list[index] = review
        else list.unshift(review)
        state.byProduct[review.product_id] = list
      })
      .addCase(deleteReview.fulfilled, (state, action) => {
        const { id, productId } = action.payload
        state.byProduct[productId] = (state.byProduct[productId] ?? []).filter((item) => item.id !== id)
      })
  },
})

export const selectReviews = (state, productId) => state.reviews.byProduct[productId]

export default reviewsSlice.reducer
