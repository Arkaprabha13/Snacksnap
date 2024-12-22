import React, { createContext, useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { setAuthToken } from '../services/api';
import api from '../services/api';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const history = useHistory();

  useEffect(() => {
    const storedToken = localStorage.getItem('token');
    if (storedToken) {
      setAuthToken(storedToken);
      api.get('/users/me')
        .then(response => setUser(response.data))
        .catch(() => localStorage.removeItem('token'));
    }
  }, []);

  const login = async (email, password) => {
    const response = await api.post('/users/login', { username: email, password });
    const { access_token } = response.data;
    localStorage.setItem('token', access_token);
    setAuthToken(access_token);
    history.push('/');
  };

  const logout = () => {
    localStorage.removeItem('token');
    setAuthToken(null);
    setUser(null);
    history.push('/login');
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
