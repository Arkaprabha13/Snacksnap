import { useContext } from 'react';
import api from '../services/api';
import AuthContext from '../context/AuthContext';

export const useLikes = () => {
  const { user } = useContext(AuthContext);

  const likeRecipe = async (recipeId) => {
    try {
      const response = await api.post('/likes', { recipe_id: recipeId });
      console.log('Recipe liked:', response.data);
    } catch (error) {
      console.error('Error liking recipe:', error);
    }
  };

  const getLikesForRecipe = async (recipeId) => {
    try {
      const response = await api.get(`/likes/${recipeId}`);
      return response.data;
    } catch (error) {
      console.error('Error fetching likes:', error);
    }
  };

  return { likeRecipe, getLikesForRecipe };
};
