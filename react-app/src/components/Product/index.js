import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useParams } from "react-router";
import { getProducts } from "../../store/products";
import { getReviewsThunk } from "../../store/reviews";
import Review from "./Review";
import AddReviewModal from "./Review/ReviewModal/AddReview";
import "./Product.css";
import { addToCartThunk, getCartThunk } from "../../store/cart";

function Product() {
  const dispatch = useDispatch();
  const { productId } = useParams();
  const user = useSelector((state) => state.session.user);
  const products = useSelector((state) => Object.values(state?.productReducer));
  const reviews = useSelector((state) => state?.reviewReducer);
  const thisProduct = products.find((product) => product?.id === +productId);
  const [showReviewAddModal, setShowReviewAddModal] = useState(false)



  useEffect(() => {
    if(user) {
      dispatch(getCartThunk(user.id))
    }
  }, [])

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
      const item = {"productId": +productId, "userId": user.id, "quantity": 1}
      dispatch(addToCartThunk(item))
      const div = document.createElement("div");
      div.id = "alertmessage";
      const div2 = document.getElementById("alert");
      let parentDiv = div2.parentNode;
      parentDiv.insertBefore(div, div2);
      div.innerText = `${thisProduct.name} added to your cart`;
      setTimeout(() => div.remove(), 3000);
    }
  };

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
    dispatch(getProducts());
  }, []);

  useEffect(() => {
    dispatch(getReviewsThunk(+productId));
  }, [dispatch]);
  return (
    <div className="singleproduct">
      <div id="alert"></div>
      <div className="imageproductdetails">
        <div>
          <img className="singleproductimage" src={thisProduct?.image} />
        </div>
        <div className="singleproductbuttons">
          <div>
          <div className="productname">{thisProduct?.name}</div>
          <div className="productdescription">{thisProduct?.description}</div>
          </div>
          
          <div className="cart-buttons">
          <div className="price">
            <small>$</small>
            {thisProduct?.price}
          </div>
          <button onClick={handleAddToCart} className="addtocart">
            Add to Cart
          </button>
          <button onClick={handleReview} className="addtocart">Leave a Review</button>
          </div>
         
        </div>
      </div>
      <div className="productreviews">
        {reviews &&
          reviews.map((review) => (
            <div className="singlereview" key={review.id}>
              <Review
                id={review.id}
                userId={review.user_id}
                productId={review.productId}
                title={review.title}
                body={review.body}
                rating={review.rating}
                created={review.created_at}
                updated={review.updated_at}
              />
            </div>
          ))}
          {reviews.length === 0 && (
            <div className="noreviews">
              <h2>No reviews on this product</h2>
              <div className="noreviewoptions">
                <p>Be the first?</p>
                <button onClick={handleReview} className="addtocart">Leave a Review</button>

              </div>
            </div>
          )}
          {showReviewAddModal && (
            <AddReviewModal showReviewAddModal={showReviewAddModal} setShowReviewAddModal={setShowReviewAddModal} name={thisProduct.name} productId={thisProduct.id}/>
          )}
      </div>
    </div>
  );
}

export default Product;
