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
  const userId = useSelector((state) => state.session.user.id)
  // const products = useSelector((state) => state.productReducer);
  const products = useSelector(state => state.cartReducer)

  useEffect(() => {
    dispatch(getCartThunk(userId));
  }, [dispatch]);

  console.log(products);

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
          {products.length > 0 &&
            products.map((product) => (
              <CartItem
                key={product.id}
                id={product.id}
                name={product.name}
                image={product.image}
                des={product.description}
                price={product.price}
                typeId={product.type_id}
                created={product.created_at}
                updated={product.updated_at}
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
