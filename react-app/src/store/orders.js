const GET_USER_ORDERS = "orders/GET_USER_ORDERS";
const SUMBIT_NEW_ORDER = "orders/SUBMIT_NEW_ORDER"

const getUserOrders = (orders) => ({
  type: GET_USER_ORDERS,
  orders,
});

const sumbitOrder = (orders) => ({
  type: SUMBIT_NEW_ORDER,
  orders,
})


export const getUserOrdersThunk = (userId) => async (dispatch) => {
  const res = await fetch(`/api/orders/${userId}`);
  if (res.ok) {
    const orders = await res.json();
    dispatch(getUserOrders(orders));
  }
};
export const submitOrderThunk = (payload) => async (dispatch) => {
  console.log(payload)
  const res = await fetch("/api/orders/add", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(
      payload
    )
  })
  if(res.ok){
    const orders = await res.json()
    dispatch(sumbitOrder(orders))
  }
}
const initialState = [];
export default function orderReducer(state = initialState, action) {
  switch (action.type) {
    case GET_USER_ORDERS:
        return action.orders
    case SUMBIT_NEW_ORDER:
      return [...state, action.orders]
    default:
      return state;
  }
}
