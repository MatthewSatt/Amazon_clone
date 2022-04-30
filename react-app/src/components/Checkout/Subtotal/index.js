import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getCartThunk } from '../../../store/cart'
import "./Subtotal.css"


function Subtotal() {
  const dispatch = useDispatch()
  const user = useSelector(state => state.session.user)
  const cart = useSelector(state => state.cartReducer)
  const products = useSelector(state => state.productReducer)
  const [length, setLength] = useState(0.00)
  const [shipping, setShipping] = useState(0.00)
  const [itemPrice, setItemPrice] = useState(0.00)
  const [total, setTotal] = useState(0.00)
  const [savings, setSavings] = useState(0.00)



useEffect(() => {
  setLength(cart.length)
  setShipping(0.00)
  setItemPrice(0.00)
  setTotal(0.00)
  setSavings(0.00)
}, [cart.length])

useEffect(() =>  {
  let itemPrice = 0
  let shippingCost = 0
  let total = 0
  if(cart.length === 0) {
    setTotal(0)
  }
  cart.forEach((item) => {
    for(let i = 0; i < products.length; i++) {
      let product = products[i]
      if(product.id === item.product_id) {
        shippingCost += product.price * 0.05
        itemPrice += product.price
        total += (product.price + product.price * 0.05)
      }
    }
    setShipping(shippingCost.toFixed(2))
    setItemPrice(itemPrice.toFixed(2))
    setTotal(total.toFixed(2))
    if(user.isPrime) {
      setTotal(total-shippingCost)
      setSavings(shipping)

    }
  }, [cart.length])

})

  return (
    <div className='subtotal'>
    <div className='cartitemcount'>
      <h2>Total Items: ({length}):</h2>
    </div>
      <h4>Item Cost: ${itemPrice}</h4>
      <h4>Shipping: ${shipping}</h4>
      {user.isPrime && (
        <h4>Prime Discount: -${savings}</h4>
      )}
    <div className='totalcheckout'>

      <h2>Total: {`$${Number.parseFloat(total).toFixed(2)}`}</h2>
    <button className='cartbutton'>Purchase</button>
    </div>

    </div>
  )
}

export default Subtotal
