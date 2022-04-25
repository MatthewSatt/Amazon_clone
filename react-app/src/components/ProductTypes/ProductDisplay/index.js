import React from 'react'
import "./ProductDisplay.css"
import {Link} from 'react-router-dom'

function ProductDisplay({id, typeId, name, image, price, desc, type_id, created, updated}) {
  return (
    <div className='productdisplay'>
      <Link to={`/product/${id}`}>
        <img className='productitemimage'src={image} alt='image'></img>
      </Link>
        <div className='productitemname'>
        <div>{name}</div>
        <div>${price}</div>
        </div>
        <div className='productitemdescription'>{desc}</div>
        <div className='productbuttons'>
          <button className='addtocart'>Add to Cart</button>
          <button className='addtocart'>Leave review</button>
        </div>

    </div>
  )
}

export default ProductDisplay
