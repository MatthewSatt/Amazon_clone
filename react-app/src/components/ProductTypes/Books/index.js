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
    <div className="books">
      <h1>Books</h1>
      {products &&
        products.map((product) => (
              <div className="productcontainer">
            <Link className='productlinks' to={`/product/${product.id}`}>
            <img className='productimage'src={product.image} alt=""/>
            </Link>
            {/* <h1>{product.title}</h1> */}

              </div>
          ))}
    </div>
  );
}

export default Books;
