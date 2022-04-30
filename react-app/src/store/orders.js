const GET_USER_ORDERS = "orders/GET_USER_ORDERS";


const getUserOrders = (orders) => ({
  type: GET_USER_ORDERS,
  orders,
});


export const getUserOrdersThunk = (userId) => async (dispatch) => {
  const res = await fetch(`/api/orders/${userId}`);
  if (res.ok) {
    const orders = await res.json();
    dispatch(getUserOrders(orders));
  }
};


const initialState = [];
export default function orderReducer(state = initialState, action) {
  switch (action.type) {
    case GET_USER_ORDERS:
        return action.orders
    default:
      return state;
  }
}
