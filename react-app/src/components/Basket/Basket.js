import React, { useEffect } from "react";
import "./Basket.css";
import SubTotal from "../SubTotal/SubTotal";
import CheckoutProduct from "../CheckoutProduct/CheckoutProduct";
import { useSelector, useDispatch } from "react-redux";
import {getProducts} from '../../store/products'

function Basket() {
  const dispatch = useDispatch()
 const user = useSelector(state => state.session.user)
 const products = useSelector(state => Object.values(state.productReducer))
 console.warn(products)

 useEffect(() => {
  dispatch(getProducts())
 }, [])
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
        {products && products.map(item =>(
          <CheckoutProduct
          key={item.id}
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
