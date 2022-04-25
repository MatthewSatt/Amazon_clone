import React from 'react'
import "./ProductDisplay.css"
import {Link} from 'react-router-dom'
import {useState, useEffect} from 'react'
import { useSelector } from 'react-redux'
import AddReviewModal from '../../Product/Review/ReviewModal/AddReview'

function ProductDisplay({id, typeId, name, image, price, desc, type_id, created, updated}) {
  const user = useSelector(state => state.session.user)
  const [showReviewAddModal, setShowReviewAddModal] = useState(false)


  const handleReview = async () => {
    if (!user) {
      const div = document.createElement("div");
      div.id = "alertmessagereview";
      const div2 = document.getElementById("alert");
      let parentDiv = div2.parentNode;
      parentDiv.insertBefore(div, div2);
      div.innerText = "You must be logged in to leave reviews";
      setTimeout(() => div.remove(), 3000);
    } else {
      setShowReviewAddModal(true);
    }
  };
  return (
    <div className='productdisplay'>
      <Link to={`/product/${id}`}>
        <img className='productitemimage'src={image} alt='image'></img>
      </Link>
        <div className='productitemname'>
        <div>{name}</div>
        <div>${price}</div>
        </div>
        <div className='productitemdescription'>{desc}</div>
        <div className='productbuttons'>
          <button className='addtocart'>Add to Cart</button>
          <button onClick={handleReview} className='addtocart'>Leave review</button>
        </div>
        {showReviewAddModal && (
            <AddReviewModal showReviewAddModal={showReviewAddModal} setShowReviewAddModal={setShowReviewAddModal} name={name} productId={id}/>
          )}

    </div>
  )
}

export default ProductDisplay
