import React, { useState } from 'react';
import { useContext } from 'react';
import { useComments } from '../hooks/useComments';

const Comment = ({ recipeId }) => {
  const [commentText, setCommentText] = useState('');
  const { addComment } = useComments();

  const handleCommentSubmit = (e) => {
    e.preventDefault();
    addComment(recipeId, commentText);
    setCommentText('');
  };

  return (
    <div>
      <form onSubmit={handleCommentSubmit}>
        <textarea
          value={commentText}
          onChange={(e) => setCommentText(e.target.value)}
          placeholder="Add a comment"
        ></textarea>
        <button type="submit">Post Comment</button>
      </form>
    </div>
  );
};

export default Comment;
