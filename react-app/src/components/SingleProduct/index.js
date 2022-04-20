import React, { useEffect } from 'react'
import {useSelector, useDispatch } from 'react-redux'
import {useParams} from 'react-router'
import { getProducts } from '../../store/products'
import './SingleProduct.css'

function SingleProduct() {
  const dispatch = useDispatch()
  const {productId} = useParams()

  const products = useSelector(state => Object.values(state?.productReducer))
  const thisProduct = products.find(product => product?.id === +productId)

  useEffect(() => {
    dispatch(getProducts())
  }, [])


  return (
    <div className='singleproduct'>
      <div className='imageproductdetails'>
      <div className='singleproductimage'>
        <img src={thisProduct?.image}/>
      </div>
        <div className='singleproductbuttons'>
        <div className='productname'>
          {thisProduct?.name}
        </div>
          <button className='addtocart'>Add to Cart</button>
        <div>
          <small>$</small>{thisProduct?.price}
        </div>
        </div>
      </div>
      <div className='producttext'>
        <div className='productdescription'>
          {thisProduct?.description}
        </div>
      </div>
    </div>
  )
}

export default SingleProduct
