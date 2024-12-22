import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import HomePage from './pages/HomePage';
import RecipePage from './pages/RecipePage';
import LoginPage from './pages/LoginPage';

const App = () => {
  return (
    <AuthProvider>
      <Router>
        <Switch>
          <Route path="/" exact component={HomePage} />
          <Route path="/recipe/:id" component={RecipePage} />
          <Route path="/login" component={LoginPage} />
        </Switch>
      </Router>
    </AuthProvider>
  );
};

export default App;
