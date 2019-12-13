#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # Create variables that make it much easier to read and compare the data than dictionaries, using comprehensions
  ans = []
  rList = [[key,value] for key, value in recipe.items()]
  iList = [[key,value] for key, value in ingredients.items()]
  # For the length of the recipe, check if the ingredients allow for the creation of at least 1, if not then return 0
  for x in range(0, len(rList)):
    if x < len(iList):
      ans.append(int(iList[x][1]/rList[x][1]))
    else:
      return 0
  # Return the minimum amount of creation allowed by the ingredients
  return min(ans)




if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))