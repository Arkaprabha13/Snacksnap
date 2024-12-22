import { useContext } from 'react';
import api from '../services/api';
import AuthContext from '../context/AuthContext';

export const useComments = () => {
  const { user } = useContext(AuthContext);

  const addComment = async (recipeId, commentText) => {
    try {
      const response = await api.post('/comments', {
        recipe_id: recipeId,
        content: commentText,
        user_id: user.id,
      });
      console.log('Comment added:', response.data);
    } catch (error) {
      console.error('Error adding comment:', error);
    }
  };

  return {
    addComment,
  };
};
