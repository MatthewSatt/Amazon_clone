import React from 'react'
import "./ProductDisplay.css"
import {Link} from 'react-router-dom'
import {useState} from 'react'
import { useSelector } from 'react-redux'
import AddReviewModal from '../../Product/Review/ReviewModal/AddReview'
import { addToCartThunk } from '../../../store/cart'
import {useDispatch} from 'react-redux'
import { FaCheckCircle } from "react-icons/fa";

function ProductDisplay({id, name, image, price, desc, created, updated}) {
  const dispatch = useDispatch()
  const user = useSelector(state => state.session.user)
  const [showReviewAddModal, setShowReviewAddModal] = useState(false)
  const [addAlert, setAddAlert] = useState("")


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

  const handleAddToCart = async () => {
    if (!user) {
      const div = document.createElement("div");
      div.id = "alertmessage";
      const div2 = document.getElementById("alert");
      let parentDiv = div2.parentNode;
      parentDiv.insertBefore(div, div2);
      div.innerText = "You must be logged in to add to your cart";
      setTimeout(() => div.remove(), 3000);
    } else {
      const item = {"productId": id, "userId": user.id, "quantity": 1}
      dispatch(addToCartThunk(item))
      setAddAlert(<FaCheckCircle className='iconalert'/>)
      setTimeout(() => setAddAlert(""), 1000);

    }
  };
  return (
    <div className='productdisplay'>
      <div id='alert'></div>
      <Link to={`/product/${id}`}>
        <img className='productitemimage'src={image} alt=''></img>
      </Link>
        <div className='productitemname'>
        <div>{name}</div>
        <div>${price}</div>
        </div>
        <div className='productitemdescription'>{desc}</div>
        <div className='productbuttons'>
          <button onClick={handleAddToCart} className='addtocart'>Add to Cart<span>{addAlert}</span></button>

          <button onClick={handleReview} className='addtocart'>Leave review</button>
        </div>
        {showReviewAddModal && (
            <AddReviewModal showReviewAddModal={showReviewAddModal} setShowReviewAddModal={setShowReviewAddModal} name={name} productId={id}/>
          )}

    </div>
  )
}

export default ProductDisplay
