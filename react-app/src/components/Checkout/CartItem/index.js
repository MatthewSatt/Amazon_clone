import React, { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
// import { getSingleProduct } from '../../../store/products'
import {deleteCartItemThunk, getCartThunk} from "../../../store/cart"
import "./CartItem.css"

function CartItem({id, userId, productId, quanity}) {
  const dispatch = useDispatch()
  const products = useSelector((state) => state?.productReducer)
  const thisProduct = products.find(product => product?.id === productId)

  const handleDelete = () => {
    dispatch(deleteCartItemThunk(id))
  }


  useEffect(() => {
    dispatch(getCartThunk(userId))
  }, [dispatch])

  return (
    <div className='cartitem'>
        <img className='cartitemimage' src={thisProduct?.image} />
        <div className='cartiteminfo'>
          <p className='cartitemname'>{thisProduct?.name}</p>
          <p className='cartitemprice'><span>$</span>{thisProduct?.price}</p>
          <button onClick={handleDelete} className='remove'>Remove from Basket</button>

        </div>
    </div>
  )
}

export default CartItem
