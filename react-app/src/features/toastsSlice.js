import { createSlice } from '@reduxjs/toolkit'

let nextId = 1

const toastsSlice = createSlice({
  name: 'toasts',
  initialState: [],
  reducers: {
    toastAdded: {
      reducer: (state, action) => {
        state.push(action.payload)
      },
      prepare: (message, kind = 'success') => ({ payload: { id: nextId++, message, kind } }),
    },
    toastDismissed: (state, action) => state.filter((toast) => toast.id !== action.payload),
  },
})

export const { toastAdded, toastDismissed } = toastsSlice.actions

// Shows a toast and removes it again after a few seconds
export const notify = (message, kind = 'success') => (dispatch) => {
  const action = toastAdded(message, kind)
  dispatch(action)
  setTimeout(() => dispatch(toastDismissed(action.payload.id)), kind === 'error' ? 6000 : 3500)
}

export default toastsSlice.reducer
