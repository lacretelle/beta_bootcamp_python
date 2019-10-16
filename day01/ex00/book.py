from recipe import *
import datetime

class Book:
    def __init__(self, name):
        try:
            if isinstance(name, str):
                self.name = name
            self.last_update = datetime.datetime.now()
            self.creation_date = datetime.datetime.now()
            self.recipes_list = { "starter": {}, "main_course": {}, "dessert":{}}
        except ValueError:
            print ("Error format")

    def get_recipe_by_name(self, name):
    """Print a recipe with the name `name` """
        str(name)

    def get_recipes_by_types(self, rtype):
    """Get all recipe names for a given type """
        lst = []
        for c in self.recipes_list.keys():
            if c == rtype:
                lst.append(self.recipes_list[c])
        for b in lst:
            print (b.name)

    def add_recipe(self, recipe): 
    """Add a recipe to the book """
        return Book.recipe.recipe_type.update(recipe)
        
