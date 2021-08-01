import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Home from './Home';
import reportWebVitals from './reportWebVitals';
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom'
import Details from './Details';

ReactDOM.render((
  <Router>
  <Switch>
      <Route exact path="/manhwa/:manhwaSlug" component={Details} />
      <Route path="/" component={Home} />
  </Switch>
  </Router>
  ),
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
