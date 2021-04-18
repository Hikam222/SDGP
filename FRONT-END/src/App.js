import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './pages/Home';
import Reports from './pages/Reports/Reports';
import Products from './pages/Products/Products';
import Team from './pages/Team/Team';
import User from './pages/User/User';
import Form from './User login/Form';
import './User login/UserLogin.css';

function App() {
  return (

      <Router>
        <Form />
        <Navbar/>
        <Switch>
        
          <Route path='/home' exact component={Home} />
          <Route path='/user' component={User} />
          <Route path='/reports' component={Reports} />
          <Route path='/products' component={Products} />
          <Route path='/team' component={Team} />
          
        </Switch>
      </Router>
  
  );
}

export default App;