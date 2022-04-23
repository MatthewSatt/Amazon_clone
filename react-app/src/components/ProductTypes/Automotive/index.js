import React from "react";
import "./Automotive.css";
import { useSelector, useDispatch } from "react-redux";
import { getProductTypesThunk } from "../../../store/products";
import { useParams } from "react-router-dom";
import { useEffect } from "react";

function Automotive() {
  const dispatch = useDispatch();
  const products = useSelector((state) => state.productReducer);
  const { typeId } = useParams();

  useEffect(() => {
    dispatch(getProductTypesThunk(typeId));
  }, []);

  return (
    <div>
      Automotive
      {products &&
        products.map((product) => <div key={product.id}>{product.name}</div>)}
    </div>
  );
}

export default Automotive;
