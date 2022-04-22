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
import Automotive from './components/ProductTypes/Automotive'
import Babies from './components/ProductTypes/Babies'
import Books from './components/ProductTypes/Books'
import Electronics from './components/ProductTypes/Electronics'
import FoodGrocery from './components/ProductTypes/Food&Grocery'
import Health from './components/ProductTypes/Health'
import MusicMovies from './components/ProductTypes/Music&Movies'
import Outdoors from './components/ProductTypes/Outdoors';
import PetSupplies from './components/ProductTypes/PetSupplies'
import Sports from "./components/ProductTypes/Sports"





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

        <ProtectedRoute path="/Automotive">
          <Automotive />
        </ProtectedRoute>

        <ProtectedRoute path="/Babies">
          <Babies />
        </ProtectedRoute>

        <ProtectedRoute path="/Books">
          <Books />
        </ProtectedRoute>

        <ProtectedRoute path="/Electronics">
          <Electronics />
        </ProtectedRoute>

        <ProtectedRoute path="/Food">
          <FoodGrocery />
        </ProtectedRoute>

        <ProtectedRoute path="/Health">
          <Health />
        </ProtectedRoute>

        <ProtectedRoute path="/Music">
          <MusicMovies />
        </ProtectedRoute>

        <ProtectedRoute path="/Outdoors">
          <Outdoors />
        </ProtectedRoute>

        <ProtectedRoute path="/PetSupplies">
          <PetSupplies />
        </ProtectedRoute>

        <ProtectedRoute path="/Sports">
          <Sports />
        </ProtectedRoute>

        <ProtectedRoute path='/checkout' exact={true}>
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
