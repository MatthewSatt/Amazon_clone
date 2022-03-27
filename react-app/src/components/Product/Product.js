import React from "react";
import "./Product.css";
import Home from "../Home/Home";

function Product({ id, title, description, image, price, rating, userId }) {
  const addToBasket = () => {};
  return (
    <div className='product'>
        <div className='product__info'>
           <p>{title}</p>
           <p className='product__price'>
               <small>$</small>
               <strong>{price}</strong>
           </p>
           <div className='product__rating'>
             <p>{rating}</p>
             <p>❤️❤️❤️❤️</p>
           </div>
        </div>
        <div>

        </div>
        <img src={image} alt=''/>
        <button onClick={addToBasket}>Add To Basket</button>
    </div>
  );
}

export default Product;
