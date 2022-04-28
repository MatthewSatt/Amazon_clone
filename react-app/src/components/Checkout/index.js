import React, { useState } from "react";
import CartItem from "./CartItem";
import "./Checkout.css";
import Subtotal from "./Subtotal";
import { getCartThunk } from "../../store/cart";
import { getProducts } from "../../store/products";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";

function Checkout() {
  const dispatch = useDispatch();
  const userId = useSelector((state) => state.session.user.id)
  const carts = useSelector(state => state?.cartReducer)
  const products = useSelector((state) => state.productReducer)


  useEffect(() => {
    dispatch(getCartThunk(userId));
  }, [dispatch]);


  useEffect(() => {
    dispatch(getProducts())
  }, [])



  return (
    <div className="checkout">
      <div className="checkoutleft">
        <div className="checkoutimages">
          <img
            className="banner"
            src="https://gadgetstouse.com/wp-content/uploads/2021/01/prime-video.jpg"
            alt=""
          ></img>
          <img
            className="banner"
            src="https://getstreamwise.com/wp-content/uploads/2020/10/Benefits-Of-Amazon-Prime-Membership-about-Which-Only-a-Few-Knows-3.jpg"
            alt=""
          ></img>
          <img
            className="banner"
            src="https://www.intelligencenode.com/blog/wp-content/uploads/2019/06/Prime-day.jpg"
            alt=""
          ></img>
        </div>
        <div className="checkouttitle">
          <h2>Your Basket</h2>
        </div>
        <div className="checkoutproduct">
          {carts.length > 0 &&
            carts.map((cart) => (
              <CartItem
                key={cart.id}
                id={cart.id}
                userId={cart.user_id}
                productId={cart.product_id}
                quantity={cart.quantity}
              />
            ))}
        </div>
      </div>
      <div className="checkoutright">
        <Subtotal />
      </div>
    </div>
  );
}

export default Checkout;
