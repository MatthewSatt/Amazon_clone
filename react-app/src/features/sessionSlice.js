import { createSlice } from '@reduxjs/toolkit'
import { api } from '../api/client'
import { createApiThunk } from './thunks'

export const fetchSession = createApiThunk('session/fetch', () => api('/auth/'))

export const login = createApiThunk('session/login', (credentials) =>
  api('/auth/login', { method: 'POST', body: credentials }))

export const signUp = createApiThunk('session/signUp', (details) =>
  api('/auth/signup', { method: 'POST', body: details }))

export const logout = createApiThunk('session/logout', () => api('/auth/logout', { method: 'POST' }))

export const setPrime = createApiThunk('session/setPrime', (isPrime) =>
  api('/users/prime', { method: 'PUT', body: { isPrime } }))

const sessionSlice = createSlice({
  name: 'session',
  initialState: { user: null, ready: false },
  reducers: {
    sessionExpired: (state) => {
      state.user = null
    },
  },
  extraReducers: (builder) => {
    const setUser = (state, action) => {
      state.user = action.payload.user
    }
    builder
      .addCase(fetchSession.fulfilled, (state, action) => {
        state.user = action.payload.user
        state.ready = true
      })
      .addCase(fetchSession.rejected, (state) => {
        state.ready = true
      })
      .addCase(login.fulfilled, setUser)
      .addCase(signUp.fulfilled, setUser)
      .addCase(logout.fulfilled, setUser)
      .addCase(setPrime.fulfilled, setUser)
  },
})

export const { sessionExpired } = sessionSlice.actions
export const selectUser = (state) => state.session.user
export default sessionSlice.reducer
