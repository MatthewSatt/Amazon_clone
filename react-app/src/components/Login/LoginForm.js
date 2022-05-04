import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Redirect, useHistory } from "react-router-dom";
import { login } from "../../store/session";
import "./Login.css";

const LoginForm = () => {
  const history = useHistory()
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();


  const handleNewUser = () => {
    history.push('/signup')
  }

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const handleDemo = async (e) => {
    e.preventDefault()
    await dispatch(login('demo@aa.io', 'password'))
  }

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div className="login">

        <img
        alt=''
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
        <form onSubmit={onLogin}>
          <h5>Email</h5>
          <input value={email} type="text" onChange={updateEmail} />

          <h5>Password</h5>
          <input value={password} type="password" onChange={updatePassword} />

          <button className="login__signInButton">Sign In</button>
          <button onClick={handleDemo} className='login__signInButton'>Demo User</button>
        </form>
        <p>
          By continuing, you agree to Amazon Clones Conditions of Use and
          Privacy Notice.
        </p>

        <button onClick={handleNewUser} className='login__registerButton'>Create Account</button>
      </div>
    </div>
  );
};

export default LoginForm;
