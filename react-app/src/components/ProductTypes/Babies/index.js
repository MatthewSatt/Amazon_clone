import React from 'react'
import "./Babies.css"
import { useSelector, useDispatch } from 'react-redux'
import { getProductTypesThunk } from '../../../store/products'
import { useParams } from 'react-router-dom'
import {useEffect} from 'react'

function Babies() {
  const dispatch = useDispatch()
  const products = useSelector(state => state.productReducer)
  const {typeId} = useParams()

  useEffect(() => {
    dispatch(getProductTypesThunk(typeId))
  }, [])
  
  return (
    <div>Babies</div>
  )
}

export default Babies
