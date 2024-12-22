import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // FastAPI backend URL
});

export const setAuthToken = (token) => {
  if (token) {
    api.defaults.headers['Authorization'] = `Bearer ${token}`;
  } else {
    delete api.defaults.headers['Authorization'];
  }
};

export default api;
