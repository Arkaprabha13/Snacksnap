import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getRecipeById } from '../services/recipeService';
import LikeButton from '../components/LikeButton';
import Comment from '../components/Comment';

const RecipePage = () => {
  const { id } = useParams();
  const [recipe, setRecipe] = useState(null);

  useEffect(() => {
    const fetchRecipe = async () => {
      const response = await getRecipeById(id);
      setRecipe(response.data);
    };

    fetchRecipe();
  }, [id]);

  if (!recipe) return <div>Loading...</div>;

  return (
    <div>
      <h1>{recipe.title}</h1>
      <p>{recipe.ingredients}</p>
      <p>{recipe.instructions}</p>
      <LikeButton recipeId={recipe.id} />
      <Comment recipeId={recipe.id} />
    </div>
  );
};

export default RecipePage;
