import React from 'react'
import { Link } from "react-router-dom";

function DisplayProduct({id, image}) {
  return (
    <div className="eachproduct" key={id}>
    <Link className="linktosinglesong" to={`/product/${id}`}>
      <div className="products">
        <img id="productimage" alt="product" src={image} />
      </div>
    </Link>
  </div>
  )
}

export default DisplayProduct
