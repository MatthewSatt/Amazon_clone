import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getProducts } from "../../store/products";
import { getTypesThunk } from "../../store/types";
import { FaArrowAltCircleLeft, FaArrowAltCircleRight } from "react-icons/fa";
import { Link } from "react-router-dom";
import "./Splash.css";

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
      <div className="tophalf"></div>
      <div className="splashnav">
        {types &&
          types.map((type) => (
            <div className ='productsections'key={type.id}>
              <h1 className="productcategories">
                  <FaArrowAltCircleLeft id="left" />
                {type.name}
                  <FaArrowAltCircleRight id="right" />
              </h1>
              <div className="productline">
                {products
                  .filter((product) => product.type_id == type.id)
                  .map((filteredProducts) => (
                    <div className="eachproduct" key={filteredProducts.id}>
                      <Link className="linktosinglesong" to={`/product/${filteredProducts.id}`}>
                        <div className="products">
                          <img id="productimage" alt="product" src={filteredProducts.image} />
                        </div>
                      </Link>
                    </div>
                  ))}
              </div>
            </div>
          ))}
      </div>
    </div>
  );
}

export default Splash;
