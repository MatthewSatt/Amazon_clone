import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getUsersThunk } from "../../../store/users";
import { deleteReviewThunk, getReviewsThunk } from "../../../store/reviews";
import { FaStar } from "react-icons/fa";
import "./Review.css";
import EditReviewModal from "./ReviewModal/EditReview";
import { useParams } from "react-router-dom";

function Review({ id, userId, title, body, rating, created, updated }) {
  const dispatch = useDispatch();
  const product = useParams();
  const user = useSelector((state) => state?.session?.user);
  const users = useSelector((state) => state?.userReducer?.users);
  let author = users?.find((user) => user?.id === userId);
  const productId = +product.productId;

  const [showReviewEditModal, setShowReviewEditModal] = useState(false);

  const deleteReview = (id) => {
    dispatch(deleteReviewThunk(id));
  };

  const editReview = () => {
    setShowReviewEditModal(true);
  };

  useEffect(() => {
    dispatch(getUsersThunk());
  }, [dispatch]);

  return (
    <div className="review">
      <div className="reviewheader">
        <div>
          {Array(rating)
            .fill()
            .map((_, i) => (
              <FaStar id="starrating" icon="fa-solid fa-star" />
            ))}
          <span className="author">
            {author?.username}
            {user?.id === userId && <span>(you)</span>}
          </span>
        </div>
        <div className="time">{created}</div>
      </div>
      <div className="reviewdescription">
        <h4>{title}</h4>
        <br></br>
        {body}
      </div>
      {user?.id === userId && (
        <div className="reviewcrud">
          <button onClick={(e) => editReview(id)} className="addtocart">
            Edit Review
          </button>
          <button onClick={(e) => deleteReview(id)} className="addtocart">
            Remove Review
          </button>
        </div>
      )}
      {showReviewEditModal && (
        <EditReviewModal
          showReviewEditModal={showReviewEditModal}
          setShowReviewEditModal={setShowReviewEditModal}
          id={id}
          userId={userId}
          productId={productId}
          title={title}
          body={body}
          rating={rating}
          created={created}
          updated={updated}
        />
      )}
    </div>
  );
}

export default Review;
