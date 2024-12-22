import React, { useEffect, useState } from 'react';
import { getAllRecipes } from '../services/recipeService';
import RecipeCard from '../components/RecipeCard';

const HomePage = () => {
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    const fetchRecipes = async () => {
      const response = await getAllRecipes();
      setRecipes(response.data);
    };

    fetchRecipes();
  }, []);

  return (
    <div>
      <h1>Recipe Feed</h1>
      <div>
        {recipes.map((recipe) => (
          <RecipeCard key={recipe.id} recipe={recipe} />
        ))}
      </div>
    </div>
  );
};

export default HomePage;
