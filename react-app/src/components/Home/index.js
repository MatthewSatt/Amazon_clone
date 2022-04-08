import React from 'react'
import {useSelector} from 'react-redux'

function Home() {
    const products = useSelector(state => Object.values(state.productReducer))
    console.log(products)
  return (
    <div>Home</div>
  )
}

export default Home
