// constants
const GET_ALL_PRODUCTS = 'products/GET_ALL_PRODUCTS';
const TYPES_OF_PRODUCTS = 'products/TYPES_OF_PRODUCTS'
const DELETE_PRODUCT = 'products/DELETE_PRODUCT'

const getAllP = (products) => ({
  type: GET_ALL_PRODUCTS,
  products
});

const getProductTypes = (products) => ({
    type: GET_ALL_PRODUCTS,
    products
})

const deleteProduct = (product) => ({
    type: DELETE_PRODUCT,
    product
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

export const deleteCartItemThunk = (id) => async (dispatch) => {
    const res = await fetch(`/api/products/delete/${id}`, {
        method: "DELETE"
    })
    if(res.ok) {
        const product = await res.json()
        dispatch(deleteProduct(product))
        return product
    }
}


const initialState = [];
export default function productReducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_PRODUCTS:
           return action.products

        case TYPES_OF_PRODUCTS:
            return action.state

        case DELETE_PRODUCT:
            return state.filter((prod) => prod.id !== action.product.id);

    default:
      return state;
  }
}
