import React from "react";
import "./Basket.css";
import SubTotal from "../SubTotal/SubTotal";
import { useStateValue } from "../StateProvider";
import CheckoutProduct from "../CheckoutProduct/CheckoutProduct";

function Basket() {
  const [{basket} , dispatch] = useStateValue()
  return (
    <div className="checkout">
      <div className="checkout__left">
        <img
          className="checkout__ad"
          src="http://memberlitetheme.com/wp-content/uploads/2017/02/memberlite_banner-bottom-cta.png"
        />
      <div>
        <h3>Hello, MatthewSatterwhiteMs@gmail.com</h3>
        <h2 className="checkout__title">Your shopping Basket</h2>
        {basket && basket.map(item =>(
          <CheckoutProduct
          id={item.id}
          title={item.title}
          image={item.image}
          price={item.price}
          rating={item.rating}

          />
        ))}
      </div>
      </div>
      <div className="checkout__right">
        <SubTotal />
      </div>
    </div>
  );
}

export default Basket;
