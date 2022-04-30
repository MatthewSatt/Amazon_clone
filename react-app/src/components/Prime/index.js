import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import {getUserThunk, setPrimeThunk} from '../../store/session'

function Prime() {
    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)
    const users = useSelector(state => state.userReducer)



    useEffect(() => {
        dispatch(getUserThunk(user.id))
    },[dispatch])

    const setPrime = async () => {
        await dispatch(setPrimeThunk(user.id))
    }



  return (
      <div className='Prime'>
        <div>Amazon Prime</div>
        {user.isPrime && (
            <div>
                <div>You are already a Prime member!</div>
                <button onClick={setPrime}>Unsubscribe to Prime</button>
            </div>
        )}
        {!user.isPrime && (

            <button onClick={setPrime}>Sign up for Prime</button>
        )}


    </div>
  )
}

export default Prime
