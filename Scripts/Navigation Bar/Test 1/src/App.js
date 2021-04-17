import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './pages/Home';
import Reports from './pages/Reports/Reports';
import Products from './pages/Products/Products';
import Team from './pages/Team/Team';
import User from './pages/User/User';

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/user' component={User} />
          <Route path='/reports' component={Reports} />
          <Route path='/products' component={Products} />
          <Route path='/team' component={Team} />
        </Switch>
      </Router>
    </>
  );
}

export default App;