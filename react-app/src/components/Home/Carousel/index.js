import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import "./Carousel.css";

function Carousel() {
  const history = useHistory()
let slideIndex = 0;

useEffect(() => {
    showSlides()
},[])

function showSlides() {
  if(history.location.pathname === '/') {

    let i;
    let slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides?.length; i++) {
      slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    if(slides === 0) {
      slides[slideIndex].style.display = "block";
    } else {
      slides[slideIndex-1].style.display = "block";
    }
    setTimeout(showSlides, 2900);
  } else {
    return
  }
}
  return (
    <div className="slideshow-container">
      <div className="mySlides fade">
        <img
          className="homeimages"
          src="https://m.media-amazon.com/images/I/61gLca6v8gL._SX3000_.jpg"
        />
      </div>

      <div className="mySlides fade">
        <img
          className="homeimages"
          src="https://m.media-amazon.com/images/I/716CpIc5oeL._SX3000_.jpg"
        />
      </div>

      <div className="mySlides fade">
        <img
          className="homeimages"
          src="https://m.media-amazon.com/images/I/61HiOQNHJKL._SX3000_.jpg"
        />
      </div>

      <div className="mySlides fade">
        <img
          className="homeimages"
          src="https://m.media-amazon.com/images/I/611YB+hYM3L._SX3000_.jpg"
        />
      </div>
</div>
  );
}

export default Carousel;
