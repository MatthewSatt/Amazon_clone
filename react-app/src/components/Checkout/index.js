import React from "react";
import CartItem from "./CartItem";
import "./Checkout.css";
import Subtotal from "./Subtotal";
import { getCartThunk } from "../../store/cart";
import { getProducts } from "../../store/products";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";

function Checkout() {
  const dispatch = useDispatch();
  const user = useSelector((state) => state?.session?.user);
  const carts = useSelector((state) => state?.cartReducer);
  // const products = useSelector(state => state?.productReducer)


  useEffect(() => {
    dispatch(getCartThunk(user.id));
  }, [dispatch, user.id]);

  useEffect(() => {
    dispatch(getProducts())
  }, [dispatch])


  return (
    <div className="checkout">
      <div className="checkouttop">
        <div className="checkoutimages">
        <div className="checkouttitle">
          <h2 className="usernamesbasket">{user.username}'s Basket</h2>
        </div>
          <img
            className="banner"
            src="https://gadgetstouse.com/wp-content/uploads/2021/01/prime-video.jpg"
            alt=""
          ></img>
          <img
            className="banner"
            src="https://www.intelligencenode.com/blog/wp-content/uploads/2019/06/Prime-day.jpg"
            alt=""
          ></img>

        </div>
        <div className="checkoutsubtotal">
          <Subtotal />
        </div>
      </div>
      <div className="checkoutbottom">
        <div className="checkoutproduct">
          {carts.length > 0 &&
            carts?.map((cart) => (
              <CartItem
                key={cart?.id}
                id={cart?.id}
                userId={cart?.user_id}
                productId={cart?.product_id}
                quantity={cart?.quantity}
              />
            ))}
            {carts.length === 0 && (
              <h2 className="nocartitems">You have no items in your cart</h2>
            )}
        </div>
      </div>
    </div>
  );
}

export default Checkout;
