import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getUserOrdersThunk } from "../../store/orders";
import OrderDisplay from "./OrderDisplay";
import './Orders.css'

function Orders() {
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const orders = useSelector((state) => state.orderReducer);

  useEffect(() => {
    dispatch(getUserOrdersThunk(user.id));
  }, [dispatch]);
  return (
    <div className="orders">
      <div className="userordertitle">{user.username}'s Order History</div>
      {orders &&
        orders.map((order) => (
          <div key={order.id}>
            <OrderDisplay
              orderId={order.id}
              productId={order.product_id}
              userId={order.user_id}
            />
          </div>
        ))}
    </div>
  );
}

export default Orders;
