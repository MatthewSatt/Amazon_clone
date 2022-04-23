import React from 'react'
import "./CartItem.css"

function CartItem({ id, name, image, des, price, typeId, created, updated }) {
  return (
    <div className='cartitem'>
        <img className='cartitemimage' src={image} />

        <div className='cartiteminfo'>
          <p className='cartitemname'>{name}</p>
          <p className='cartitemprice'><span>$</span>{price}</p>
          <button className='remove'>Remove from Basket</button>

        </div>
    </div>
  )
}

export default CartItem
