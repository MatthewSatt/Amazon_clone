import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getCartThunk } from '../../../store/cart'
import "./Subtotal.css"


function Subtotal() {
  const dispatch = useDispatch()
  const user = useSelector(state => state.session.user)
  const products = useSelector(state => state.cartReducer)



  const totalItems = (array) => {
    return array.length
  }

  const priceChecker = (array) => {
    let total = 0
    for(let i = 0; i < array.length; i++) {
      let price = array[i].price
      total += price
    }
    return "$" + total.toFixed(2)
  }

  return (
    <div className='subtotal'>
    <div className='cartitemcount'>
      <h1>Total Items ({totalItems(products)}):</h1>
    </div>
    <div className='cartprice'>
      <h2>Price: {priceChecker(products)}</h2>
    </div>
    <button className='cartbutton'>Purchase</button>

    </div>
  )
}

export default Subtotal
