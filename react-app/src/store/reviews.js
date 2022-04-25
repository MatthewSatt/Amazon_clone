const GET_PRODUCT_REVIEWS = 'reviews/GET_PRODUCT_REVIEWS';
const ADD_REVIEW = 'reviews/ADD_REVIEW'
const DELETE_REVIEW = 'reviews/DELETE_REVIEW'

const getReviews = (reviews) => ({
  type: GET_PRODUCT_REVIEWS,
  reviews,
});

const addReview = (newReview) => ({
  type: ADD_REVIEW,
  newReview
})

const deleteReview = (review) => ({
  type: DELETE_REVIEW,
  review
})

export const getReviewsThunk = (productId) => async (dispatch) => {
    const res = await fetch(`/api/reviews/${productId}`)
    if(res.ok) {
        const reviews = await res.json()
        console.log(reviews)
        dispatch(getReviews(reviews))
    }
}

export const addReviewThunk = (review) => async (dispatch) => {
  const res = await fetch(`/api/reviews/add`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(
      review
    )
  })
  if(res.ok) {
    const newReview = await res.json()
    dispatch(addReview(newReview))
  }
}

export const deleteReviewThunk = (id) => async (dispatch) => {
  console.log(id)
  const res = await fetch(`/api/reviews/delete/${id}`, {
    method: "DELETE",
  })
  if(res.ok) {
    const review = await res.json()
    dispatch(deleteReview(review))
    return review
  }
}


const initialState = [];
export default function reviewReducer(state = initialState, action) {
    switch (action.type) {
        case GET_PRODUCT_REVIEWS:
           return action.reviews
        case ADD_REVIEW:
          return [...state, action.newReview]
        case DELETE_REVIEW:
          return state.filter((rev) => rev.id !== action.review.id);
    default:
      return state;
  }
}
