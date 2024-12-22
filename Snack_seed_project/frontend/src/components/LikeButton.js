import React, { useState, useEffect } from 'react';
import { useLikes } from '../hooks/useLikes';

const LikeButton = ({ recipeId }) => {
  const { likeRecipe, getLikesForRecipe } = useLikes();
  const [likesCount, setLikesCount] = useState(0);
  const [isLiked, setIsLiked] = useState(false);

  useEffect(() => {
    const fetchLikes = async () => {
      const response = await getLikesForRecipe(recipeId);
      setLikesCount(response.likes_count);
      setIsLiked(response.is_liked);
    };

    fetchLikes();
  }, [recipeId, isLiked]);

  const handleLike = () => {
    likeRecipe(recipeId);
    setIsLiked(true);
  };

  return (
    <div>
      <button onClick={handleLike} disabled={isLiked}>
        {isLiked ? "Liked" : "Like"}
      </button>
      <span>{likesCount} Likes</span>
    </div>
  );
};

export default LikeButton;
