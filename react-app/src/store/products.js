// constants
const GET_ALL_PRODUCTS = 'products/GET_ALL_PRODUCTS';
const REMOVE_USER = 'session/REMOVE_USER';

const getAllP = (products) => ({
  type: GET_ALL_PRODUCTS,
  products
});

export const getProducts = () => async (dispatch) => {
    const res = await fetch('/api/products/all')
    if(res.ok) {
        const products = await res.json()
        dispatch(getAllP(products))
    } else {
        return 'No products Avaliable'
    }
}


const initialState = {};
export default function productReducer(state = initialState, action) {
    let newState
    switch (action.type) {
        case GET_ALL_PRODUCTS:
            const allProducts = {};
            action.products.forEach(product => {
                allProducts[product.id] = product

            })
            return {...allProducts}
    default:
      return state;
  }
}
