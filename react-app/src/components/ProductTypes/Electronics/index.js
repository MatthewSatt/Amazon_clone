import React from 'react'
import "./Electronics.css"
import { useSelector, useDispatch } from 'react-redux'
import { getProductTypesThunk } from '../../../store/products'
import { useParams } from 'react-router-dom'
import {useEffect} from 'react'

function Electronics() {
  const dispatch = useDispatch()
  const products = useSelector(state => state.productReducer)
  const {typeId} = useParams()
  useEffect(() => {
    dispatch(getProductTypesThunk(typeId))
  }, [])
  return (
    <div>Electronics</div>
  )
}

export default Electronics
