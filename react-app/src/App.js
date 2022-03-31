import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/Login/LoginForm';
import NavBar from './components/Header/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import { authenticate } from './store/session';
import Home from './components/Home/Home'
import SignUp from './components/Signup/Signup';
import Product from './components/Product/Product';
import Basket from './components/Basket/Basket';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route path='/login' exact={true}>
          <LoginForm />
        </Route>
        <Route path='/signup' exact={true}>
          <SignUp />
        </Route>
        <ProtectedRoute path='/' exact={true} >
          <Home />
          <Product />
        </ProtectedRoute>
        <ProtectedRoute path='/checkout' exact={true}>
          <Basket />
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
