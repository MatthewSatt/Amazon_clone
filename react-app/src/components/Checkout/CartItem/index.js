import React, { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { getProducts } from '../../../store/products'
import {deleteCartItemThunk, getCartThunk} from "../../../store/cart"
import "./CartItem.css"

function CartItem({ id, name, image, des, price, typeId, created, updated }) {
  const dispatch = useDispatch()
  const products = useSelector((state) => state.productReducer)
  const userId = useSelector((state) => state.session.user.id)

  const handleDelete = () => {
    dispatch(deleteCartItemThunk({productId: id, userId}))
  }

  useEffect(() => {
    dispatch(getCartThunk(userId))
  }, [dispatch])

  return (
    <div className='cartitem'>
        <img className='cartitemimage' src={image} />
          {id}
        <div className='cartiteminfo'>
          <p className='cartitemname'>{name}</p>
          <p className='cartitemprice'><span>$</span>{price}</p>
          <button onClick={handleDelete} className='remove'>Remove from Basket</button>

        </div>
    </div>
  )
}

export default CartItem
