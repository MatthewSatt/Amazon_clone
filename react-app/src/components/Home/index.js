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
    dispatch(getCartThunk(user.id))
  }, [user.id])

  return (
    <div className="homepage">
      <div className="home">
        <ol>
          To do:
          <li>Likes on reviews?</li>
          <li>
            Fix delete tags and just return cart objects. cart.id,
            cart.product_id, cart.user_id, cart.quantity)<br></br>
            <small>
              Then have different routes to indivdual products(referenced from
              cart.productId) to render them onto the page. But then we can
              delete the cart directly from the id. Which will fix the duplicate
              product mass delete and the the global delete for each user. Idk
              I'm tired
            </small>
          </li>
          <li>Seeds for days I want about 15 of each product type</li>
          <li>Css checkout styling problem is still untouched because nah.</li>
          <li>Searchbar to search for products || product types</li>
          <li>AWS webbuckets</li>
          <li>Web Sockets?</li>
          <li>tbd...</li>
        </ol>

        <Dropdown showSideNav={showSideNav} setShowSideNav={setShowSideNav} />
      </div>
      {products &&
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
        ))}
    </div>
  );
}

export default Home;
