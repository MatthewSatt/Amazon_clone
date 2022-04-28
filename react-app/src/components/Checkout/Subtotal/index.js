import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getCartThunk } from '../../../store/cart'
import "./Subtotal.css"


function Subtotal() {
  const dispatch = useDispatch()
  const user = useSelector(state => state.session.user)
  const cart = useSelector(state => state.cartReducer)
  const products = useSelector(state => state.productReducer)
  const [length, setLength] = useState(0)
  const [price, setPrice] = useState(0)



useEffect(() => {
  setLength(cart.length)
}, [cart.length])

useEffect(() =>  {
  let total = 0
  cart.forEach((item) => {
    for(let i = 0; i < products.length; i++) {
      let product = products[i]
      if(product.id === item.product_id) {
        total += product.price
      }
      setPrice(total.toFixed(2))
    }
  }, [cart.length])


  // setPrice()
})

  return (
    <div className='subtotal'>
    <div className='cartitemcount'>
      <h1>Total Items ({length}):</h1>
    </div>
    <div className='cartprice'>
      <h2>Price: {`$${price}`}</h2>
    </div>
    <button className='cartbutton'>Purchase</button>

    </div>
  )
}

export default Subtotal
