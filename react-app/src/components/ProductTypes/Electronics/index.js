import React from 'react'
import "./Electronics.css"
import { useSelector, useDispatch } from 'react-redux'
import { getProductTypesThunk } from '../../../store/products'
import { useParams } from 'react-router-dom'
import {useEffect} from 'react'
import ProductDisplay from '../ProductDisplay'

function Electronics() {
  const dispatch = useDispatch()
  const products = useSelector(state => state.productReducer)
  const {typeId} = useParams()
  useEffect(() => {
    dispatch(getProductTypesThunk(typeId))
  }, [])
  return (
    <div className="books">
    <div className="electronicsimage">
      <h1>Electronics</h1>
      </div>
      {products &&
        products.map((product) => (
          <div className="productcontainer">
            <ProductDisplay id={product.id} name={product.name} price={product.price} image={product.image} desc={product.description} created={product.created_at} updated={product.updated}/>
              </div>
          ))}
  </div>
  )
}

export default Electronics
