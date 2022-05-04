import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getProductTypesThunk } from "../../../store/products";
import { useParams } from "react-router-dom";
import "./Books.css";
import ProductDisplay from "../ProductDisplay";

function Books() {
  const dispatch = useDispatch();
  const products = useSelector((state) => state.productReducer);
  const { typeId } = useParams();

  useEffect(() => {
    dispatch(getProductTypesThunk(typeId));
  }, [dispatch, typeId]);

  return (
    <div className="books">
    <div className="booksimage">
      <h1>Books</h1>
      </div>
      {products &&
        products.map((product) => (
          <div className="productcontainer">
            <ProductDisplay id={product.id} typeId={product.type_id} name={product.name} price={product.price} image={product.image} desc={product.description} created={product.created_at} updated={product.updated}/>
              </div>
          ))}
  </div>
  );
}

export default Books;
