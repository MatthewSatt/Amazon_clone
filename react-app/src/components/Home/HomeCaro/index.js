import React, { useEffect } from "react";
import { useSelector } from "react-redux";
import { useHistory } from "react-router-dom";

function HomeCaro() {
  const user = useSelector(state => state.session.user)
  const history = useHistory()
let slideIndex = 0;

useEffect(() => {
    showSlides()
},[])

function showSlides() {
  if(history.location.pathname === '/' && user.id) {

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
    setTimeout(showSlides, 2000);
  } else {
    return
  }
}
  return (
    <div className="slideshow-container">
      <div className="mySlides fade">
        <img
        alt=''
          className="homeimages"
          src="https://m.media-amazon.com/images/I/71P47BioYqL._SX3000_.jpg"
        />
      </div>

      <div className="mySlides fade">
        <img
        alt=''
          className="homeimages"
          src="https://m.media-amazon.com/images/I/61z+zr8oqXL._SX3000_.jpg"
        />
      </div>
</div>
  );
}

export default HomeCaro;
