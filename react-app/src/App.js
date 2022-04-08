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
        <Route path='/login' exact={true}>
          <LoginForm />
        </Route>
        <Route path='/signup' exact={true}>
          <SignUp />
        </Route>
        {!user && (
        <Route path='/'>
          <Splash />
        </Route>
        )}
        <ProtectedRoute path='/' exact={true} >
          <Home />
        </ProtectedRoute>
        <ProtectedRoute path='/checkout' exact={true}>
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
