import React from "react";
import { Link, useHistory } from "react-router-dom";
import SearchIcon from "@mui/icons-material/Search";
import ShoppingBasketIcon from "@mui/icons-material/ShoppingBasket";
import "./Header.css";
import { useDispatch, useSelector } from "react-redux";
import { logout } from "../../store/session";

function NavBar() {
  const history = useHistory();
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);

  const logoutUser = async () => {
    await dispatch(logout(user));
  };

  return (
    <div className="header">
      <Link to="/">
        <img
          className="header__logo"
          src="https://logos-world.net/wp-content/uploads/2020/04/Amazon-Emblem.jpg"
        />
      </Link>

      <div className="header__search">
        <input className="header__searchInput" type="text" />
        <SearchIcon className="header__searchIcon" />
      </div>

      <div className="header__nav">
        <div className="header__option">
          <>
            {user && (
              <>
                <span className="header__optionLineOne">
                  Hello {user.username}
                </span>
                <span onClick={logoutUser} className="header__optionLineTwo">
                  Sign Out
                </span>
              </>
            )}
            {!user && (
              <>
                <span className="header__optionLineOne">Hello</span>
                <Link
                  className="header__optionLineTwo"
                  id="login-link"
                  to="/login"
                >
                  <span className="header__optionLineTwo">Sign In</span>
                </Link>
              </>
            )}
          </>
        </div>

        <div className="header__option">
          {user && (
            <>
              <span className="header__optionLineOne">View</span>
              <span className="header__optionLineTwo">Orders</span>
            </>
          )}
          {!user && (
            <>
              <span className="header__optionLineOne">Orders</span>
            <Link to='/signup'
            className="header__optionLineOne"
            id='login-link'>
              <span className="header__optionLineTwo">Sign Up</span>
            </Link>
            </>
          )}
        </div>

        <div className="header__option">
          <span className="header__optionLineOne">Your</span>
          <span className="header__optionLineTwo">Prime</span>
        </div>
        <Link to="/checkout">
          <div className="header__optionBasket">
            <ShoppingBasketIcon />
            <span className="header__optionLineTwo header__basketCount">
              {}
            </span>
          </div>
        </Link>
      </div>
    </div>
  );
}

export default NavBar;
