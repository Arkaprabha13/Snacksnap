import api from './api';

export const createRecipe = (recipeData) => {
  return api.post('/recipes', recipeData);
};

export const getAllRecipes = () => {
  return api.get('/recipes');
};

export const getRecipeById = (id) => {
  return api.get(`/recipes/${id}`);
};

export const updateRecipe = (id, recipeData) => {
  return api.put(`/recipes/${id}`, recipeData);
};

export const deleteRecipe = (id) => {
  return api.delete(`/recipes/${id}`);
};
