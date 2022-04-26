import React, { useEffect, useState } from "react";
import { Link, useHistory } from "react-router-dom";
import SearchIcon from "@mui/icons-material/Search";
import ShoppingBasketIcon from "@mui/icons-material/ShoppingBasket";
import "./Header.css";
import { useDispatch, useSelector } from "react-redux";
import { logout } from "../../store/session";
import { getCartThunk } from "../../store/cart";


function NavBar() {
  const history = useHistory();
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const products = useSelector(state => state?.cartReducer);
  const [cartAmount, setCartAmount] = useState(products.length)




  useEffect(() => {
    dispatch(getCartThunk(user.id))
    setCartAmount(products.length)
  }, [dispatch])

  const logoutUser = async () => {
    await dispatch(logout(user));
    history.push("/");
  };

  const handleCartError = () => {
    let old = document.getElementById("checkouterror")
    const errorDiv = document.createElement("div")
    errorDiv.innerText = "You must sign in to view your cart"
    errorDiv.id = 'alertmessage'
    old.appendChild(errorDiv)
    setTimeout(() => errorDiv.remove(), 2500)
  }

  return (
    <div className="header">
      <Link to="/">
        <img
          className="headerlogo"
          src="https://logos-world.net/wp-content/uploads/2020/04/Amazon-Emblem.jpg"
        />
      </Link>

      <div className="headersearch">
        <input className="headersearchinput" type="text" />
        <SearchIcon className="headersearchicon" />
      </div>

      <div className="headernav">
        <div className="headeroption">
          <>
            {user && (
              <>
                <span className="headeroptionlineone">
                  Hello {user.username}
                </span>
                <span onClick={logoutUser} className="headeroptionlinetwo">
                  Sign Out
                </span>
              </>
            )}
            {!user && (
              <>
                <span className="headeroptionlineone">Hello</span>
                <Link
                  className="headeroptionlinetwo"
                  id="loginlink"
                  to="/login"
                >
                  <span className="headeroptionlinetwo">Sign In</span>
                </Link>
              </>
            )}
          </>
        </div>

        <div className="headeroption">
          {user && (
            <>
              <span className="headeroptionlineone">View</span>
              <span className="headeroptionlinetwo">Orders</span>
            </>
          )}
          {!user && (
            <>
              <span className="headeroptionlineone">Orders</span>
              <Link
                to="/signup"
                className="headeroptionlineone"
                id="loginlink"
              >
                <span className="headeroptionlinetwo">Sign Up</span>
              </Link>
            </>
          )}
        </div>

        <div className="headeroption">
          <span className="headeroptionlineone">Your</span>
          <span className="headeroptionlinetwo">Prime</span>
        </div>
        {user && (
          <Link to="/checkout">
            <div className="headeroptionbasket">
              <ShoppingBasketIcon />
              <span className="headeroptionlinetwo headerbasketcount">
                {cartAmount}
              </span>
            </div>
          </Link>
        )}
        {!user && (
          <div className="headeroptionbasket">
            <ShoppingBasketIcon onClick={handleCartError}/>
            <span id="checkouterror"></span>
          </div>
        )}
      </div>
    </div>
  );
}

export default NavBar;
