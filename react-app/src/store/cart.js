const GET_CART_ITEMS = 'cart/GET_CART_ITEMS';
const DELETE_PRODUCT = 'products/DELETE_PRODUCT'

const getCart = (cartProducts) => ({
    type: GET_CART_ITEMS,
    cartProducts,
})


const deleteProduct = (product) => ({
    type: DELETE_PRODUCT,
    product
})


export const getCartThunk = (userId) => async (dispatch) => {
    const res = await fetch(`/api/carts/${userId}`)
    if(res.ok) {
        const cartProducts = await res.json()
        dispatch(getCart(cartProducts))
    }
}



export const deleteCartItemThunk = (id) => async (dispatch) => {
    const res = await fetch(`/api/carts/delete/${id}`, {
        method: "DELETE"
    })
    if(res.ok) {
        const product = await res.json()
        dispatch(deleteProduct(product))
        return product
    }
}



const initialState = [];
export default function cartReducer(state = initialState, action) {
    switch (action.type) {
        case GET_CART_ITEMS:
            return action.cartProducts.cart_product
        case DELETE_PRODUCT:
            return state.filter((prod) => prod.id !== action.product.id);
    default:
      return state;
  }
}
