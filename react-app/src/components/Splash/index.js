import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getProducts } from "../../store/products";
import { getTypesThunk } from "../../store/types";
import Type from "./Type";
import DisplayProduct from "./DisplayProduct";
import "./Splash.css";
import Carousel from "./Carousel";
//productsections
function Splash() {
  const dispatch = useDispatch();
  const products = useSelector((state) => state.productReducer);
  const types = useSelector((state) => state.typeReducer);

  useEffect(() => {
    dispatch(getProducts());
    dispatch(getTypesThunk());
  }, [dispatch]);

  return (
    <div className="splashpage">
        <Carousel />
      <div className="splashnav">
        {types &&
          types.map((type) => (
            <div className ='productsections'key={type.id}>
                  <Type id={type.id} name={type.name}/>
              <div className="productline">
                {products
                  .filter((product) => product.type_id === type.id)
                  .map((filteredProducts) => (
                      <DisplayProduct id={filteredProducts.id} image={filteredProducts.image}/>
                  ))}
              </div>
            </div>
          ))}
      </div>
    </div>
  );
}

export default Splash;
