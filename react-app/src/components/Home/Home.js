import React from "react";
import Product from "../Product/Product";
import { useEffect } from "react";
import './Home.css'
import { getProducts } from "../../store/products";
import { useDispatch, useSelector } from "react-redux";


function Home() {
  const dispatch = useDispatch()
  const products = useSelector((state) => Object.values(state.productReducer))

useEffect(() => {
  dispatch(getProducts())
}, [])

  return (
    <div className="home">
      <div className="home__container">
        <div className="home__row">
          {products && products.map(product => (
            <Product id={product.id} title={product.title} description={product.description} image={product.image} price={product.price} rating={product.rating} userId={product.userId}/>
            ))}
        </div>

            </div>
      </div>
  );
}

export default Home;
