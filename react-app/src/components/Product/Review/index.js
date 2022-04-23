import React, { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { getUsersThunk } from '../../../store/users';
import { FaStar } from "react-icons/fa";
import "./Review.css"

function Review({ id, userId, productId, title, body, rating, created, updated }) {
    const dispatch = useDispatch()
    const users = useSelector((state) => state?.userReducer?.users)
    let author = users?.find(user => user?.id === id)
    console.log(author)

  const starFiller = (num, value) => {
    Array(num).fill().map((_, i) => {
      console.log(value)
    })
  }

    useEffect(() => {
        dispatch(getUsersThunk())
    }, [])

  return (
    <div className='review'>
      <div className='reviewheader'>
        <div>
      {Array(rating).fill().map((_, i) => (
        <FaStar id='starrating' icon="fa-solid fa-star" />
      ))}
      <span className='author'>{author?.username}</span>
      </div>
      <div className='time'>{created}</div>
        </div>
        <div className='reviewdescription'>
          {body}
        </div>
    </div>
  )
}

export default Review
