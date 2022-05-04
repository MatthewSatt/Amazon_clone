import React from "react";
import { useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import "./Carousel.css";
import {useEffect} from 'react'

function Carousel() {
  const user = useSelector(state => state.session.user)
  const history = useHistory()
let slideIndex = 0;

useEffect(() => {
  if(history.location.pathname === '/' && !user) {
    showSlides()
  } else {
    return
  }
  },[history.location.pathname, user])

  function showSlides() {
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
    setTimeout(showSlides, 3800);
}
  return (
    <div className="slideshow-container">
      <div className="mySlides fade">
        <img
        alt=''
          className="homeimages"
          src="https://m.media-amazon.com/images/I/61gLca6v8gL._SX3000_.jpg"
        />
      </div>

      <div className="mySlides fade">
        <img
        alt=''
          className="homeimages"
          src="https://m.media-amazon.com/images/I/716CpIc5oeL._SX3000_.jpg"
        />
      </div>

      <div className="mySlides fade">
        <img
        alt=''
          className="homeimages"
          src="https://m.media-amazon.com/images/I/61HiOQNHJKL._SX3000_.jpg"
        />
      </div>

      <div className="mySlides fade">
        <img
        alt=''
          className="homeimages"
          src="https://m.media-amazon.com/images/I/611YB+hYM3L._SX3000_.jpg"
        />
      </div>
</div>
  );
}

export default Carousel;
