import React, { useState, useEffect } from 'react';
import { useFollow } from '../hooks/useFollow';

const FollowButton = ({ userId }) => {
  const { followUser, unfollowUser, isFollowing } = useFollow(userId);
  const [following, setFollowing] = useState(false);

  useEffect(() => {
    setFollowing(isFollowing(userId));
  }, [userId, following]);

  const handleFollow = async () => {
    if (following) {
      await unfollowUser(userId);
    } else {
      await followUser(userId);
    }
    setFollowing(!following);
  };

  return (
    <button onClick={handleFollow}>
      {following ? 'Unfollow' : 'Follow'}
    </button>
  );
};

export default FollowButton;
