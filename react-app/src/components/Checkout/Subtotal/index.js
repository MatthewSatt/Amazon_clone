import React from 'react'
import "./Subtotal.css"

function Subtotal() {

  return (
    <div className='subtotal'>
    <div className='cartitemcount'>
      <h1>Total Items (3):</h1>
    </div>
    <div className='cartprice'>
      <h2>Price: $54.32</h2>
    </div>
    <button className='cartbutton'>Purchase</button>

    </div>
  )
}

export default Subtotal
