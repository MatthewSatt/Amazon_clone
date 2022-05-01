import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { useState, useEffect } from "react";
import { getProducts } from "../../store/products";
import { getTypesThunk } from "../../store/types";
import ProductDisplay from "../ProductTypes/ProductDisplay";
import Dropdown from "../Dropdown";
import "./Home.css";
import { getCartThunk } from "../../store/cart";
import Carousel from "./Carousel";

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
    dispatch(getCartThunk(user.id))
  }, [user.id])

  return (
    <div className="homepage">
      <div className="home">
        <Dropdown showSideNav={showSideNav} setShowSideNav={setShowSideNav} />
      </div>
      <Carousel />
      {/* {products &&
        products.map((product) => (
          <ProductDisplay
            key={product.id}
            id={product.id}
            typeId={product.type_id}
            name={product.name}
            price={product.price}
            image={product.image}
            desc={product.description}
            created={product.created_at}
            updated={product.updated}
          />
        ))} */}
    </div>
  );
}

export default Home;
