import React, { useEffect } from 'react'
import {useSelector, useDispatch } from 'react-redux'
import {useParams} from 'react-router'
import { getProducts } from '../../store/products'
import './Product.css'

function Product() {
  const dispatch = useDispatch()
  const {productId} = useParams()
  const user = useSelector(state => state.session.user)
  const products = useSelector(state => Object.values(state?.productReducer))
  const thisProduct = products.find(product => product?.id === +productId)

  const handleAddToCart = async() => {
    if(!user) {
      console.log('Not Signed In!')
    } else {
      console.log('Add Product to Cart')
    }
  }

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
          <button onClick={handleAddToCart} className='addtocart'>Add to Cart</button>
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

export default Product
