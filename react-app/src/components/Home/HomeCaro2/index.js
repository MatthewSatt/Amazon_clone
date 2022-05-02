import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { useHistory } from "react-router-dom";

function HomeCaro2() {
  const user = useSelector(state => state.session.user)
  const history = useHistory()
let slideIndex1 = 0;

useEffect(() => {
    showSlides1()
},[])

function showSlides1() {
  if(history.location.pathname === '/' && user.id) {

    let i;
    let slides = document.getElementsByClassName("mySlides1");
    for (i = 0; i < slides?.length; i++) {
      slides[i].style.display = "none";
    }
    slideIndex1++;
    if (slideIndex1 > slides.length) {slideIndex1 = 1}
    if(slides === 0) {
      slides[slideIndex1].style.display = "block";
    } else {
      slides[slideIndex1-1].style.display = "block";
    }
    setTimeout(showSlides1, 2400);
  } else {
    return
  }
}
  return (
    <div className="slideshow-container">
      <div className="mySlides1 fade">
        <img
          className="homeimages"
          src="https://m.media-amazon.com/images/I/611YB+hYM3L._SX3000_.jpg"
        />
      </div>

      <div className="mySlides1 fade">
        <img
          className="homeimages"
          src="https://m.media-amazon.com/images/I/61lZZvJoB7L._SX3000_.jpg"
        />
      </div>
</div>
  );
}

export default HomeCaro2;
