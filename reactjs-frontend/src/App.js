import React from 'react';
import './App.css';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'
import ProductComponent from './components/ProductComponent';
import HeaderComponent from './components/HeaderComponent';
import SearchComponent from './components/SearchComponent';

function App() {
  return (
    <div>
        <Router>
              <HeaderComponent />
                <div className="container">
                    <Switch> 
                          <Route path = "/" exact component = {ProductComponent}></Route>
                          <Route path = "/search" component = {SearchComponent}></Route>
                    </Switch>
                </div>
        </Router>
    </div>
    
  );
}

export default App;
