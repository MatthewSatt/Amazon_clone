import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getUserThunk, setPrimeThunk } from "../../store/session";
import {Link} from 'react-router-dom'
import "./Prime.css";

function Prime() {
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const users = useSelector((state) => state.userReducer);
  console.log(user.isPrime)

  useEffect(() => {
    dispatch(getUserThunk(user.id));
  }, [dispatch]);

  const setPrime = async () => {
    await dispatch(setPrimeThunk(user.id));
  };

  return (
    <div className="prime">
      {user.isPrime && (
        <div className="primemembers">
          <h1></h1>
          <div className="userprimetext">
            <h3>Prime Membership <span className="active">Active</span></h3>
            <h4>
              You enjoy all the Shipping and Streaming benefits of our members.
            </h4>
          </div>
          <button className="addtocart" onClick={setPrime}>
            Unsubscribe
          </button>
            <Link to='/'>
          <button className="addtocart">
            Start Shopping
          </button>
            </Link>
        </div>
      )}
      {!user.isPrime && (
        <div className="notprimemembers">
          <h1>Prime Membership</h1>
          <h3>Prime Membership <span className="inactive">Inactive</span></h3>
          <div className="notuserprimetext">
            <div className="shipping">
              <h3>Shipping</h3>
              <p>
                FREE Two-Day Shipping on eligible items to addresses in the
                contiguous US and other shipping benefits. For more information,
                go to Amazon Prime Shipping Benefits.
              </p>
              <p>
                FREE Same-Day Delivery in eligible zip codes. For more
                information, go to Order with Prime FREE Same-Day Delivery.
              </p>
              <p>
                FREE Release-Date Delivery on eligible preorder items delivered
                on their release date to ZIP codes within the continental US.
                For more information, go to Release-Date Delivery.
              </p>
              <p>
                FREE No-Rush Shipping. Select No-Rush Shipping and earn rewards
                for future purchases. Amazon Day, where you can choose a weekly
                delivery day for the items you buy throughout the week.
              </p>
            </div>
            <div className="streaming">
              <h3>Streaming</h3>
              <p>
                Prime Video offers unlimited streaming of movies and TV episodes
                for paid or free trial members in the US and Puerto Rico. For
                more information, go to Prime Video.
              </p>
              <p>
                With Amazon Channels, you can watch your favorite shows and
                movies from HBO, SHOWTIME, and STARZ channels. You don't need a
                cable or additional apps and you can cancel anytime. Amazon
                Channels costs $4.99–$14.99/month for Prime members.
              </p>
              <p>
                Prime members can get discounted Amazon Music Unlimited monthly
                plans and there are annual plans available exclusively to Prime
                members. For more information, go to Amazon Music Unlimited.
              </p>
            </div>
          </div>
          <button onClick={setPrime} className="addtocart">
            Sign up for Prime
          </button>
        </div>
      )}
    </div>
  );
}

export default Prime;
