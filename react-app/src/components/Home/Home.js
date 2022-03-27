import React from "react";
import Product from "../Product/Product";
import './Home.css'

function Home() {
  return (
    <div className="home">
      <div className="home__container">
        <img
          className="home__image"
          src="https://images.hdqwalls.com/download/purple-blue-moving-down-abstract-4k-nq-1920x1080.jpg"
          alt="home"
        />
        {/* loop products here */}
        <div className="home__row">
            row1
        </div>
        <div className="home__row">
            row2
        </div>
        <div className="home__row">
          row3
        </div>
      </div>
    </div>
  );
}

export default Home;
