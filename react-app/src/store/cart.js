const GET_CART_ITEMS = 'cart/GET_CART_ITEMS';
const DELETE_PRODUCT = 'cart/DELETE_PRODUCT';
const ADD_TO_CART = 'cart/ADD_TO_CART'

const getCart = (cartProducts) => ({
    type: GET_CART_ITEMS,
    cartProducts,
})


const deleteProduct = (product) => ({
    type: DELETE_PRODUCT,
    product
})

const addToCart = (product) => ({
    type: ADD_TO_CART,
    product
})


export const getCartThunk = (userId) => async (dispatch) => {
    const res = await fetch(`/api/carts/${userId}`)
    if (res.ok) {
        const cartProducts = await res.json()
        dispatch(getCart(cartProducts))
    }
}


export const deleteCartItemThunk = (id) => async (dispatch) => {
    console.log(id)
    const res = await fetch(`/api/carts/delete/${id.productId}`, {
        method: "DELETE",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(
            id,
        )
    })
    if (res.ok) {
        const product = await res.json()
        dispatch(deleteProduct(product))
        return product
    }
}

export const addToCartThunk = (item) => async (dispatch) => {
    console.log("ITEM", item)
    const res = await fetch(`/api/carts/add`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(
            item
        )
    })
    if (res.ok) {
        const product = await res.json()
        dispatch(addToCart(product))
    }
}





const initialState = [];
export default function cartReducer(state = initialState, action) {
    switch (action.type) {
        case GET_CART_ITEMS:
            return action.cartProducts.cart_product
        case DELETE_PRODUCT:
            console.log('........',action.product.product_id)
            return state.filter((prod) => prod.id !== action.product.product_id);
        case ADD_TO_CART:
            return [...state, action.product]
        default:
            return state;
    }
}
