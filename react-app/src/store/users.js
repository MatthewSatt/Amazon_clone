
const GET_USERS = 'session/GET_USERS'



const getUsers = (users) => ({
    type: GET_USERS,
    users
  })





export const getUsersThunk = () => async (dispatch) => {
    const res = await fetch('/api/users')
    if(res.ok) {
      const users = await res.json()
      dispatch(getUsers(users))
    }
  }



const initialState = []
  export default function userReducer(state = initialState, action) {
    switch (action.type) {
      case GET_USERS:
          return action.users
      default:
        return state;
    }
  }
