import React from 'react';
import { Link } from 'react-router-dom';

const RecipeCard = ({ recipe }) => {
  return (
    <div className="recipe-card">
      <h3>{recipe.title}</h3>
      <p>{recipe.ingredients}</p>
      <Link to={`/recipe/${recipe.id}`}>View Details</Link>
    </div>
  );
};

export default RecipeCard;
