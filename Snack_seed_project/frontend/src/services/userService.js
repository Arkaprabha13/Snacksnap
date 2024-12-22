import api from './api';

export const registerUser = (userData) => {
  return api.post('/users/register', userData);
};

export const loginUser = (loginData) => {
  return api.post('/users/login', loginData);
};
