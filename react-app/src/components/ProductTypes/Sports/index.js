import React from "react";
import "./Sports.css";
import { useSelector, useDispatch } from "react-redux";
import { getProductTypesThunk } from "../../../store/products";
import { useParams } from "react-router-dom";
import { useEffect } from "react";

function Sports() {
  const dispatch = useDispatch();
  const products = useSelector((state) => state.productReducer);
  const { typeId } = useParams();
  useEffect(() => {
    dispatch(getProductTypesThunk(typeId));
  }, []);
  return <div>Sports
          {products && products.map(product => (
        <div key={product.id}>{product.name}</div>
      ))}
  </div>;
}

export default Sports;
