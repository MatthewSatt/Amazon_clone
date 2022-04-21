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
      const div = document.createElement("div")
      div.id = 'alertmessage'
      const div2 = document.getElementById("alert")
      let parentDiv = div2.parentNode
      parentDiv.insertBefore(div,div2)
      div.innerText = "You must be logged in to add to your cart"
      setTimeout(() => div.remove(), 3000)

    } else {
      console.log('Add Product to Cart')
    }
  }

  useEffect(() => {
    dispatch(getProducts())
  }, [])
  return (
    <div className='singleproduct'>
      <div id='alert'></div>
      <div className='imageproductdetails'>
      <div>
        <img className='singleproductimage' src={thisProduct?.image}/>
      </div>
        <div className='singleproductbuttons'>
        <div className='productname'>
          {thisProduct?.name}
        </div>
        <div className='price'>
          <small>$</small>{thisProduct?.price}
        </div>
          <button onClick={handleAddToCart} className='addtocart'>Add to Cart</button>
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
