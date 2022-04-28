// constants
const GET_ALL_PRODUCTS = 'products/GET_ALL_PRODUCTS';
const TYPES_OF_PRODUCTS = 'products/TYPES_OF_PRODUCTS'

const getAllP = (products) => ({
  type: GET_ALL_PRODUCTS,
  products
});

const getProductTypes = (products) => ({
    type: GET_ALL_PRODUCTS,
    products
})

export const getProducts = () => async (dispatch) => {
    const res = await fetch('/api/products/all')
    if(res.ok) {
        const products = await res.json()
        dispatch(getAllP(products))
    } else {
        return 'No products Avaliable'
    }
}

export const getProductTypesThunk = (typeId) => async (dispatch) => {
    const res = await fetch(`/api/products/${typeId}`)
    if(res.ok) {
        const products = await res.json()
        dispatch(getProductTypes(products))
    }
}

const initialState = [];
export default function productReducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_PRODUCTS:
           return action.products
        case TYPES_OF_PRODUCTS:
            return action.state
    default:
      return state;
  }
}
