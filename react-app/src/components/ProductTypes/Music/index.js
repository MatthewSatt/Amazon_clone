import React from "react";
import "./Music.css";
import { useSelector, useDispatch } from "react-redux";
import { getProductTypesThunk } from "../../../store/products";
import { useParams } from "react-router-dom";
import ProductDisplay from "../ProductDisplay";
import { useEffect } from "react";

function Music() {
  const dispatch = useDispatch();
  const products = useSelector((state) => state?.productReducer);
  const { typeId } = useParams();
  useEffect(() => {
    dispatch(getProductTypesThunk(typeId));
  }, [dispatch]);
  return (
    <div className="electronics">
    <div id="musicimage">
      <h1>Music</h1>
      </div>
      {products &&
        products.map((product) => (
          <div className="productcontainer">
            <ProductDisplay id={product?.id} typeId={product?.type_id} name={product?.name} price={product?.price} image={product.image} desc={product.description} created={product.created_at} updated={product.updated}/>
              </div>
          ))}
  </div>
  )
}

export default Music;
