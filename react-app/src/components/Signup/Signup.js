import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Redirect, useHistory } from "react-router-dom";
import { signUp } from "../../store/session";
import { Link } from "react-router-dom";
import "./Signup.css";

const SignUp = () => {
  const history = useHistory();
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState("")
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();

  const handleExistingUser = () => {
    history.push("/login");
  };

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(signUp(username, email, password));
      if (data) {
        setErrors(data);
      }
    }
  };
  console.warn(username)
  console.warn(email)
  console.warn(password)
  console.warn(repeatPassword)

  const updateUsername = (e) => {
      setUsername(e.target.value)
  }

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div className="login">
      <img
        className="login__logo"
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/1024px-Amazon_logo.svg.png"
      />

      <div className="login__container">
        <h1>Sign-In</h1>
        <div>
          {errors.map((error, ind) => (
            <div key={ind}>{error}</div>
          ))}
        </div>
        <form onSubmit={onSignUp}>

          <h5>Username</h5>
          <input value={username} type="text" onChange={updateUsername} />

          <h5>Email</h5>
          <input value={email} type="text" onChange={updateEmail} />

          <h5>Password</h5>
          <input value={password} type="password" onChange={updatePassword} />

          <h5>Update Password</h5>
          <input
            value={repeatPassword}
            type="password"
            onChange={updateRepeatPassword}
          />

          <button className="login__signInButton">Sign Up</button>
        </form>
        <p>
          By continuing, you agree to Amazon Clones Conditions of Use and
          Privacy Notice.
        </p>
        <button onClick={handleExistingUser} className="login__registerButton">
          Already have an account?
        </button>
      </div>
    </div>
  );
};

export default SignUp;
