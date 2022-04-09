import React from 'react'
import './Product.css'
import {Link} from 'react-router-dom'
function Product({id, typeId, name, description, price, image, created, updated}) {
  return (
    <Link className="linktosinglesong" to={`/product/${id}`}>
      <div>
        <img id='productimage' alt='product' src={image} />
      </div>
    </Link>
  )
}

export default Product
