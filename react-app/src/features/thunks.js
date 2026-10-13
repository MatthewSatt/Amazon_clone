import { createAsyncThunk } from '@reduxjs/toolkit'
import { ApiError } from '../api/client'

// createAsyncThunk, but API failures are rejected with { status, errors }
// so reducers and components can show field-level messages
export function createApiThunk(type, handler) {
  return createAsyncThunk(type, async (arg, thunkApi) => {
    try {
      return await handler(arg, thunkApi)
    } catch (error) {
      if (error instanceof ApiError) {
        return thunkApi.rejectWithValue({ status: error.status, errors: error.errors })
      }
      throw error
    }
  })
}

// The first message of an error payload, for toasts
export const firstError = (payload) => {
  const errors = payload?.errors
  if (!errors) return 'Something went wrong. Please try again.'
  return errors.form?.[0] ?? Object.values(errors)[0]?.[0] ?? 'Something went wrong. Please try again.'
}
