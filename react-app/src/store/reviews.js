const GET_PRODUCT_REVIEWS = 'reviews/GET_PRODUCT_REVIEWS';

const getReviews = (reviews) => ({
  type: GET_PRODUCT_REVIEWS,
  reviews,
});

export const getReviewsThunk = (productId) => async (dispatch) => {
    const res = await fetch(`/api/reviews/${productId}`)
    if(res.ok) {
        const products = await res.json()
        dispatch(getReviews(products))
    } else {
        return 'No products Avaliable'
    }
}


const initialState = [];
export default function reviewReducer(state = initialState, action) {
    switch (action.type) {
        case GET_PRODUCT_REVIEWS:
           return action.products
    default:
      return state;
  }
}
