import React from 'react'
import "./Food.css"
import { useSelector, useDispatch } from 'react-redux'
import { getProductTypesThunk } from '../../../store/products'
import { useParams } from 'react-router-dom'
import ProductDisplay from '../ProductDisplay'
import {useEffect} from 'react'

function Food() {
  const dispatch = useDispatch()
  const products = useSelector(state => state.productReducer)
  const {typeId} = useParams()
  useEffect(() => {
    dispatch(getProductTypesThunk(typeId))
  }, [])
  return (
    <div className="electronics">
    <div className="foodimage">
      <h1>Food and Beverage</h1>
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

export default Food
