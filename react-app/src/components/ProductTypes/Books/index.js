import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getProductTypesThunk } from "../../../store/products";
import { useParams } from "react-router-dom";
import {Link} from 'react-router-dom'
import "./Books.css";

function Books() {
  const dispatch = useDispatch();
  const products = useSelector((state) => state.productReducer);
  const { typeId } = useParams();

  useEffect(() => {
    dispatch(getProductTypesThunk(typeId));
  }, []);

  return (
    <div>
      Books
      {products &&
        products.map((product) => (
            <Link to={`/product/${product.id}`}>
            <h1>{product.name}</h1>
            </Link>
          ))}
    </div>
  );
}

export default Books;
