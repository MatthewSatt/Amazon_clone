import React, { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getProducts } from '../../../store/products'
import {Link} from 'react-router-dom'
import AddReviewModal from '../../Product/Review/ReviewModal/AddReview'

function OrderDisplay({orderId, productId, userId}) {
    const dispatch = useDispatch()
    const products = useSelector(state => state?.productReducer)
    const user = useSelector(state => state.session.user)
    const thisProduct = products.find(product => product?.id === productId)
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

    useEffect(() => {
        dispatch(getProducts())
    }, [dispatch])

  return (
        <div className='productdisplay'>
      <Link to={`/product/${thisProduct?.id}`}>
        <img className='productitemimage'src={thisProduct?.image} alt=''></img>
      </Link>
        <div className='productitemname'>
        <div>{thisProduct?.name}</div>
        <div>${thisProduct?.price}</div>
        </div>
        <div className='productitemdescription'>{thisProduct?.description}</div>
        <div className='productbuttons'>
          <button onClick={handleReview} className='addtocart'>Leave review</button>
        </div>
        {showReviewAddModal && (
            <AddReviewModal showReviewAddModal={showReviewAddModal} setShowReviewAddModal={setShowReviewAddModal} name={thisProduct.name} productId={thisProduct.id}/>
          )}
    </div>
  )
}

export default OrderDisplay
