import { createSelector, createSlice } from '@reduxjs/toolkit'
import { api } from '../api/client'
import { createApiThunk } from './thunks'

export const fetchCatalog = createApiThunk('catalog/fetch', async () => {
  const [products, types] = await Promise.all([api('/products/'), api('/types/')])
  return { products, types }
})

// Full product (complete description + fresh rating)
export const fetchProduct = createApiThunk('catalog/fetchProduct', (id) => api(`/products/${id}`))

const catalogSlice = createSlice({
  name: 'catalog',
  initialState: { products: [], types: [], status: 'idle', details: {}, missing: {} },
  extraReducers: (builder) => {
    builder
      .addCase(fetchCatalog.pending, (state) => {
        state.status = 'loading'
      })
      .addCase(fetchCatalog.fulfilled, (state, action) => {
        state.products = action.payload.products
        state.types = action.payload.types
        state.status = 'ready'
      })
      .addCase(fetchCatalog.rejected, (state) => {
        state.status = 'error'
      })
      .addCase(fetchProduct.fulfilled, (state, action) => {
        const product = action.payload
        state.details[product.id] = product
        delete state.missing[product.id]
        // Keep the list's rating in step with the detail view
        const listed = state.products.find((item) => item.id === product.id)
        if (listed) {
          listed.rating = product.rating
          listed.review_count = product.review_count
        }
      })
      .addCase(fetchProduct.rejected, (state, action) => {
        if (action.payload?.status === 404) state.missing[action.meta.arg] = true
      })
  },
})

export const selectProducts = (state) => state.catalog.products
export const selectTypes = (state) => state.catalog.types
export const selectCatalogStatus = (state) => state.catalog.status

export const selectProductsByType = createSelector(
  [selectProducts, (_state, typeId) => typeId],
  (products, typeId) => products.filter((product) => product.type_id === typeId),
)

export const selectProduct = (state, id) => state.catalog.details[id] ?? state.catalog.products.find((p) => p.id === id)
export const selectProductMissing = (state, id) => Boolean(state.catalog.missing[id])

export default catalogSlice.reducer
