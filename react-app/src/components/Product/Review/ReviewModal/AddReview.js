import { Modal } from "../../../../context/Modal";
import "./AddReview.css";
import { useState } from "react";
import { addReviewThunk } from "../../../../store/reviews";

import React from "react";
import { useDispatch, useSelector } from "react-redux";

function AddReviewModal({
  showReviewAddModal,
  setShowReviewAddModal,
  name,
  productId,
}) {
  const dispatch = useDispatch()
  const userId = useSelector((state) => state.session.user.id);
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const [rating, setRating] = useState(1);

  const addReview = (e) => {
    e.preventDefault()
    const review = {
      user_id: userId,
      product_id: productId,
      title,
      body,
      rating,
    };
    dispatch(addReviewThunk(review))
    setShowReviewAddModal(false)
  };
  return (
    <Modal onClose={() => setShowReviewAddModal(false)}>
      <div className="addreviewmodal">
        <h2>Review of</h2>
        <h3>{name}</h3>
        <form onSubmit={addReview}>
          <div className="formcontent">
            <input
              className="nameinput"
              placeholder="Review Title"
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />
            <textarea
            className="bodyinput"
              placeholder="Review Content"
              type="field"
              value={body}
              onChange={(e) => setBody(e.target.value)}
            />

            <div className="ratingcontainer">
            <label>Rating: </label>
            <select
              className="colorinput"
              value={rating}
              onChange={(e) => setRating(e.target.value)}
              >
              <option className="rate" value={1}>
              ⭐️
              </option>
              <option className="rate" value={2}>
              ⭐️⭐️
              </option>
              <option className="rate" value={3}>
              ⭐️⭐️⭐️
              </option>
              <option className="rate" value={4}>
              ⭐️⭐️⭐️⭐️
              </option>
              <option className="rate" value={5}>
              ⭐️⭐️⭐️⭐️⭐️
              </option>
            </select>
              </div>
            <button id='sumbitbutton' onChange={addReview} className="addtocart">
              Sumbit Review
            </button>
          </div>
        </form>
      </div>
    </Modal>
  );
}

export default AddReviewModal;
