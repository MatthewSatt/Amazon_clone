import React from 'react'
import {useSelector, useDispatch, } from 'react-redux'
import {useParams} from 'react-router'
import './SingleProduct.css'

function SingleProduct() {
  const productId = +useParams().id
  const products = useSelector(state => Object.values(state.productReducer))
  const thisProduct = products.find(product => product.id === productId)
  console.log(thisProduct)


  return (
    <div className='singleproduct'>
      <div className='imageproductdetails'>
      <div className='singleproductimage'>
        <img src={thisProduct.image}/>
      </div>
        <div className='singleproductbuttons'>
        <div className='productname'>
          {thisProduct.name}
        </div>
          <button>Add to Cart</button>
        <div>
          <small>$</small>{thisProduct.price}
        </div>
        </div>
      </div>
      <div className='producttext'>
        <div className='productdescription'>
          {thisProduct.description}
        </div>
      </div>
    </div>
  )
}

export default SingleProduct
