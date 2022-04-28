import React from 'react'
import { FaArrowAltCircleLeft, FaArrowAltCircleRight } from "react-icons/fa";

function Type({name, id}) {
  return (
    <h2 className="productcategories">
    <FaArrowAltCircleLeft id="left" />
  {name}
    <FaArrowAltCircleRight id="right" />
</h2>
  )
}

export default Type
