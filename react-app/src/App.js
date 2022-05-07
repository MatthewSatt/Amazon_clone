import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import LoginForm from './components/Login/LoginForm';
import NavBar from './components/Header/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import { authenticate } from './store/session';
import SignUp from './components/Signup/Signup';
import Splash from './components/Splash'
import Home from './components/Home'
import Product from './components/Product';
import Babies from './components/ProductTypes/Babies';
import Automotive from './components/ProductTypes/Automotive'
import Books from './components/ProductTypes/Books'
import Electronics from './components/ProductTypes/Electronics'
import Food from './components/ProductTypes/Food'
import Health from './components/ProductTypes/Health'
import Outdoors from './components/ProductTypes/Outdoors';
import Pets from './components/ProductTypes/Pets'
import Sports from "./components/ProductTypes/Sports"
import Music from './components/ProductTypes/Music';
import Movies from "./components/ProductTypes/Movies"
import Checkout from './components/Checkout';
import Prime from './components/Prime'
import Orders from './components/Orders';
//AWS WebBuckets







function App() {
  const user = useSelector(state => state.session.user)
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
        {!user && (
          <>
        <Route path='/' exact={true}>
          <Splash />
        </Route>

        <Route path='/login' exact={true}>
          <LoginForm />
        </Route>

        <Route path='/signup' exact={true}>
          <SignUp />
        </Route>

        <Route path='/product/:productId'>
          <Product />
        </Route>

        <Route path="/prime">
          <Prime />
        </Route>

          </>
        )}
        <ProtectedRoute path='/' exact={true} >
          <Home />
        </ProtectedRoute>

        <Route path='/login' exact={true}>
          <LoginForm />
        </Route>

        <Route path='/signup' exact={true}>
          <SignUp />
        </Route>

        <Route path='/product/:productId'>
          <Product />
        </Route>

        <Route path="/prime">
          <Prime />
        </Route>

        <ProtectedRoute path="/:typeId/Automotive">
          <Automotive />
        </ProtectedRoute>

        <ProtectedRoute path="/:typeId/Babies">
          <Babies />
        </ProtectedRoute>

        <ProtectedRoute path="/:typeId/Books">
          <Books />
        </ProtectedRoute>

        <ProtectedRoute path="/:typeId/Electronics">
          <Electronics />
        </ProtectedRoute>

        <ProtectedRoute path="/:typeId/Food">
          <Food />
        </ProtectedRoute>

        <ProtectedRoute path="/:typeId/Health">
          <Health />
        </ProtectedRoute>

        <ProtectedRoute path="/:typeId/Music">
          <Music />
        </ProtectedRoute>

        <ProtectedRoute path="/:typeId/Movies">
          <Movies />
        </ProtectedRoute>

        <ProtectedRoute path="/:typeId/Outdoors">
          <Outdoors />
        </ProtectedRoute>

        <ProtectedRoute path="/:typeId/Pets">
          <Pets />
        </ProtectedRoute>

        <ProtectedRoute path="/:typeId/Sports">
          <Sports />
        </ProtectedRoute>

        <ProtectedRoute path='/orders' exact={true}>
          <Orders />
        </ProtectedRoute>

        <ProtectedRoute path='/checkout' exact={true}>
          <Checkout />
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
