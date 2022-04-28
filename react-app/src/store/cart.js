const GET_CART_ITEMS = "cart/GET_CART_ITEMS";
const DELETE_CART_PRODUCT = "cart/DELETE_CART_PRODUCT";
const ADD_TO_CART = "cart/ADD_TO_CART";

const getCart = (cartProducts) => ({
  type: GET_CART_ITEMS,
  cartProducts,
});

const deleteProduct = (product) => ({
  type: DELETE_CART_PRODUCT,
  product,
});

const addToCart = (product) => ({
  type: ADD_TO_CART,
  product,
});

export const getCartThunk = (userId) => async (dispatch) => {
  const res = await fetch(`/api/carts/${userId}`);
  if (res.ok) {
    const cartProducts = await res.json();
    dispatch(getCart(cartProducts));
  }
};

export const deleteCartItemThunk = (id) => async (dispatch) => {
  const res = await fetch(`/api/carts/delete/${id}`, {
    method: "DELETE",
  });
  if (res.ok) {
    const product = await res.json();
    dispatch(deleteProduct(product));
    return product;
  }
};

export const addToCartThunk = (item) => async (dispatch) => {
  const res = await fetch(`/api/carts/add`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(item),
  });
  if (res.ok) {
    const product = await res.json();
    dispatch(addToCart(product));
  }
};

const initialState = [];
export default function cartReducer(state = initialState, action) {
  switch (action.type) {
    case GET_CART_ITEMS:
      return action.cartProducts;
    case DELETE_CART_PRODUCT:
        return state.filter((item) => item.id !== action.product.id);
    case ADD_TO_CART:
      return [...state, action.product];
    default:
      return state;
  }
}
