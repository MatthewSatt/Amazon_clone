import React from 'react'
import { FaArrowAltCircleLeft, FaArrowAltCircleRight } from "react-icons/fa";

function Type({name, id}) {
  return (
    <h2 className="productcategories">
  <div className='typename'>{name}</div>
</h2>
  )
}

export default Type
