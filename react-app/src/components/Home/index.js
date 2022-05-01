import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { useState, useEffect } from "react";
import { getProducts } from "../../store/products";
import { getTypesThunk } from "../../store/types";
import ProductDisplay from "../ProductTypes/ProductDisplay";
import Dropdown from "../Dropdown";
import "./Home.css";
import { getCartThunk } from "../../store/cart";

function Home() {
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const products = useSelector((state) => Object.values(state.productReducer));
  const types = useSelector((state) => state.typeReducer);
  const [showSideNav, setShowSideNav] = useState(false);

  useEffect(() => {
    dispatch(getProducts());
    dispatch(getTypesThunk());
  }, []);

  useEffect(() => {
    dispatch(getCartThunk(user.id));
  }, [user.id]);

  return (
    <div className="homepage">
      <div className="headerhome">
        <Dropdown showSideNav={showSideNav} setShowSideNav={setShowSideNav} />
      </div>
      <div className="homecarousels">
        <div className="homecarousel1">

        </div>
        <div className="homecarousel2">

        </div>
      </div>
      <div className="homerow1">
        <div className="box">
          <div className="box1title">Favorite Books</div>
          <div>

          <img src=""className="boximage"></img>
          <img src=""className="boximage"></img>
          <img src=""className="boximage"></img>
          <img src=""className="boximage"></img>
          </div>
        </div>
        <div className="box">
          <div className="box2title">Electronics</div>
          <div>
          <img src=""className="boximage"></img>
          <img src=""className="boximage"></img>
          <img src=""className="boximage"></img>
          <img src=""className="boximage"></img>
          </div>
        </div>
        <div className="box">
          <div className="box3title">Pets</div>
          <div>
          <img src=""className="boximage"></img>
          <img src=""className="boximage"></img>
          <img src=""className="boximage"></img>
          <img src="" className="boximage"></img>
          </div>
        </div>
        <div className="box">
          <div className="box4title">Food</div>
          <div>
          <img src="" className="boximage"></img>
          <img src="" className="boximage"></img>
          <img src="" className="boximage"></img>
          <img src="" className="boximage"></img>
          </div>
        </div>
      </div>
      <div className="homerow2">
        <div className="box">
          <div className="box1title">Sports</div>
          <div className="images">
          <img src="" className="boximage"></img>
          <img src="" className="boximage"></img>
          <img src="" className="boximage"></img>
          <img src="" className="boximage"></img>
          </div>
        </div>
        <div className="box">
          <div className="boxtitle">Outdoors</div>
          <div>
          <img src="" className="boximage"></img>
          <img src="" className="boximage"></img>
          <img src="" className="boximage"></img>
          <img src="" className="boximage"></img>
          </div>
        </div>
        <div className="box">
          <div className="box3title">Cars</div>
          <div>
          <img src=""className="boximage"></img>
          <img src=""className="boximage"></img>
          <img src=""className="boximage"></img>
          <img src=""className="boximage"></img>
          </div>
        </div>
        <div className="box">
          <div className="boxtitle">Music</div>
          <div>
          <img src=""className="boximage"></img>
          <img src=""className="boximage"></img>
          <img src=""className="boximage"></img>
          <img src=""className="boximage"></img>
          </div>
        </div>
      </div>
      <div className="homerow3">
        <div className="homepagemoviestitle">Movies</div>
        <img src=""className="movieimage"></img>
        <img src=""className="movieimage"></img>
        <img src=""className="movieimage"></img>
        <img src=""className="movieimage"></img>
        <img src=""className="movieimage"></img>
        <img src=""className="movieimage"></img>
        <img src=""className="movieimage"></img>
        <img src=""className="movieimage"></img>
      </div>
    </div>
  );
}

export default Home;
