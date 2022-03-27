import React from 'react'
import './Product.css'


function Product({ id, title, description, image, price, rating, userId}) {

  const addToBasket = () => {
    //dispatch item into datalayer

    //   type: 'ADD_TO_BASKET',
    //   item: {
    //       id: id,
    //       title: title,
    //       description: description,
    //       image: image,
    //       price: price,
    //       rating: rating,
    //       userId: userId
    //   }
    // })
  }
  return (
    <div className='product'>
        <div className='product__info'>
           <p>The product info</p>
           <p className='product__price'>
               <small>$</small>
               <strong>49.99</strong>
           </p>
           <div className='product__rating'>
             <p>❤️❤️❤️❤️</p>
           </div>
        </div>
        <img src='https://m.media-amazon.com/images/I/51nhpuLVAmL._AC_SX466_.jpg' alt=''/>
        <button onClick={addToBasket}>Add To Basket</button>
    </div>
  )
}

export default Product
