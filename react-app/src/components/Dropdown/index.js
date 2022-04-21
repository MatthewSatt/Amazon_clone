import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { FaAlignJustify, FaArrowAltCircleLeft } from "react-icons/fa";
import { Modal } from "../../context/Modal";
import {getProducts} from '../../store/products'
import {Link} from 'react-router-dom'
import "./Dropdown.css";

function Dropdown({ showSideNav, setShowSideNav }) {
  const dispatch = useDispatch();
  const products = useSelector((state) => state?.productReducer);
  const types = useSelector((state) => state?.typeReducer);

  const openDropdown = () => {
    setShowSideNav(true);
  };

  const closeModel = () => {
      setShowSideNav(false)
  }

  useEffect(() => {
      dispatch(getProducts())
  }, [])
  return (
    <div className="dropdownmenu">
      <FaAlignJustify onClick={openDropdown} />
      <div className="dropdownopen">
      {showSideNav &&
      <Modal onClose={() => setShowSideNav(false)}>
          <h2>Product Categories</h2>
            <div className="producttypelinks">
            {types && types?.map(type => (
                <div className="navproducts" key={type?.id}>
                    <Link id='navlinks'to={`/${type?.name}`}>
                    {type?.name}
                    </Link>
                </div>
            ))}
            </div>
            <div>
            <FaArrowAltCircleLeft id='close' onClick={closeModel}/>

            </div>
        </Modal>}
        </div>
    </div>
  );
}

export default Dropdown;
