import { Modal } from "../../../../context/Modal";
import "./AddReview.css";
import { useState } from "react";
import { editReviewThunk } from "../../../../store/reviews";

import React from "react";
import { useDispatch, useSelector } from "react-redux";

function EditReviewModal({
  showReviewEditModal,
  setShowReviewEditModal,
  id,
  productId,
  title,
  body,
  rating,
  updated,
}) {
  const dispatch = useDispatch();
  const userId = useSelector((state) => state.session.user.id);
  const [newTitle, setNewTitle] = useState(title);
  const [newBody, setNewBody] = useState(body);
  const [newRating, setNewRating] = useState(rating);

  const editReview = (e) => {
    e.preventDefault();
    const payload = {
        id,
        userId,
        productId,
        title: newTitle,
        body: newBody,
        rating: newRating,
    };
    dispatch(editReviewThunk(payload));
    setShowReviewEditModal(false);
  };
  return (
    <Modal onClose={() => setShowReviewEditModal(false)}>
      <div className="addreviewmodal">
        <h2>Edit Review of...</h2>
        <h3>{title}</h3>
        <form onSubmit={editReview}>
          <div className="formcontent">
            <input
              className="nameinput"
              placeholder="Review Title"
              type="text"
              value={newTitle}
              onChange={(e) => setNewTitle(e.target.value)}
            />
            <textarea
              className="bodyinput"
              placeholder="Review Content"
              type="field"
              value={newBody}
              onChange={(e) => setNewBody(e.target.value)}
            />

            <div className="ratingcontainer">
              <label>Rating: </label>
              <select
                className="colorinput"
                value={newRating}
                onChange={(e) => setNewRating(e.target.value)}
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
            <button
              id="sumbitbutton"
              onChange={editReview}
              className="addtocart"
            >
              Update Review
            </button>
          </div>
        </form>
      </div>
    </Modal>
  );
}

export default EditReviewModal;
