import React from 'react'
import {useDispatch, useSelector} from 'react-redux'
import {useState, useEffect} from 'react'
import { getProducts } from '../../store/products';
import { getTypesThunk } from '../../store/types';
import Dropdown from '../Dropdown';
import './Home.css'

function Home() {
  const dispatch = useDispatch()
  const user = useSelector(state => state.session.user)
  const products = useSelector(state => state.productReducer);
  const types = useSelector((state) => state.typeReducer);
  const [showSideNav, setShowSideNav] = useState(false)

  useEffect(() => {
    dispatch(getProducts());
    dispatch(getTypesThunk());
  }, []);

  return (
    <div className='home'>
      <Dropdown showSideNav={showSideNav} setShowSideNav={setShowSideNav}/>
    </div>
  )
}

export default Home
