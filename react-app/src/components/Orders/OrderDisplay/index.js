import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getProducts } from '../../../store/products'

function OrderDisplay({orderId, productId, userId}) {
    const dispatch = useDispatch()
    const products = useSelector(state => state.productReducer)
    const thisProduct = products.find(product => product.id === productId)

    useEffect(() => {
        dispatch(getProducts())
    }, [])
  return (
    <div className='orderdisplay'>
        <h2>{thisProduct.name}</h2>
        <img src={thisProduct.image} />
    </div>
  )
}

export default OrderDisplay
