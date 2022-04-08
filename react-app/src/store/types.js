const GET_TYPES = 'types/GET_TYPES'

const getTypes = (types) => ({
    type: GET_TYPES,
    types,
})

export const getTypesThunk = () => async (dispatch) => {
    const response = await fetch(`api/types/all`, {
        method: "GET"
    })
    if(response.ok) {
        const types = await response.json()
        dispatch(getTypes(types))
    }
}


const initialState = [];
export default function typeReducer(state = initialState, action) {
    switch (action.type) {
        case GET_TYPES:
           return action.types
    default:
      return state;
  }
}
