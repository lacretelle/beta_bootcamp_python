class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        try:
            if isinstance(name, str):
                self.name = name
            value = int(cooking_lvl)
            if value >= 1 and value <= 5:
                self.cooking_lvl = value
            value = int(cooking_time)
            if value >= 0:
                self.cooking_time = value
            count = 0
            for b in ingredients:
                if isinstance(ingredients[b], str):
                    count += 1
            if count == len(list):
                self.ingredients = ingredients
            if description == "" or isinstance(description, str):
                self.description = description
            if isinstance(recipe_type, str):
                self.type = recipe_type
        except ValueError:
            print ("Error format")
            exit()

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt = "Recipe for "+self.name+" :\n"
        txt += "level is "+self.cooking_lvl+" \n"
        txt += "time is "+self.cooking_time+" \n"
        txt += "list of ingredients is "+self.ingredients+" \n"
        txt += "description:  "+self.description+" \n"
        txt += "it recipe is for :  "+self.type+" \n"
        return str(txt)
