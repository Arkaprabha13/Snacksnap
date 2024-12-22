import { useContext } from 'react';
import api from '../services/api';
import AuthContext from '../context/AuthContext';

export const useFollow = (userId) => {
  const { user } = useContext(AuthContext);

  const followUser = async (followedUserId) => {
    try {
      const response = await api.post('/follow', { followed_user_id: followedUserId });
      console.log('Followed user:', response.data);
    } catch (error) {
      console.error('Error following user:', error);
    }
  };

  const unfollowUser = async (followedUserId) => {
    try {
      const response = await api.delete(`/follow/${followedUserId}`);
      console.log('Unfollowed user:', response.data);
    } catch (error) {
      console.error('Error unfollowing user:', error);
    }
  };

  const isFollowing = async (followedUserId) => {
    try {
      const response = await api.get(`/follow/${followedUserId}`);
      return response.data.is_following;
    } catch (error) {
      console.error('Error checking follow status:', error);
    }
  };

  return { followUser, unfollowUser, isFollowing };
};
