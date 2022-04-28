
const GET_SINGLE_PRODUCT = 'products/GET_SINGLE_PRODUCT'


const getSingleProduct = (product) => ({
    type: GET_SINGLE_PRODUCT,
    product
})

export const getSingleProductThunk = (productId) => async (dispatch) => {
    const res = await fetch(`/api/products/single/${productId}`)
    if(res.ok) {
        const product = await res.json()
        dispatch(getSingleProduct(product))
    }
}


const initialState = [];
export default function singleProductReducer(state = initialState, action) {
    switch (action.type) {
        case GET_SINGLE_PRODUCT:
            return action.product
    default:
      return state;
  }
}
