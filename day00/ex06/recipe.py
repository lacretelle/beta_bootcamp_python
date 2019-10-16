cookbook = {
        "sandwich": {
            "ingredients": ["ham","bread","cheese","tomatoes"],
            "meal": "lunch",
            "prep_time": "10"
            },
        "cake": {
            "ingredients": ["flour","sugar","eggs"],
            "meal": "dessert",
            "prep_time": "60"
            },
        "salad": {
            "ingredients": ["avocado", "arugula","tomatoes","spinach"],
            "meal": "lunch",
            "prep_time": "15"
            }
        }
#1
#for k in cookbook.keys():
#    print (k)
#for k in cookbook:
#    print cookbook[k]
#for k in cookbook:
#    print (k, cookbook[k])

#2
def print_recipe(name):
    print ("Recipe for", name, ":", cookbook.get(name))
    return

#3
def del_recipe(name):
    new_dict = cookbook.pop('salad')
    return new_dict

#4
def add_recipe(name, ing, meal, prep):
    new_recipe = { name:{
            "ingredients": ing,
            "meal": meal,
            "prep_time": prep
            }
            }
    return cookbook.update(new_recipe)

#5
def print_all():
    for i in cookbook:
        print ("Recipe for %s" % i)
        print ("Ingredients list: %s" % cookbook.get(i).get("ingredients"))
        print ("To be eaten for %s" % cookbook.get(i).get("meal"))
        print ("Takes %s minutes of cooking" % cookbook.get(i).get("prep_time"))
    return

#6
print ("Please select an option by typing the corresponding number:")
print ("1: Add a recipe")
print ("2: Delete a recipe")
print ("3: Print a recipe")
print ("4: Print the cookbook")
print ("5: Quit")
x = int(input())
if x < 1 and x > 5:
    print ("ERROR, quit.")
    exit()
else:
    if x == 1:
        print ("Please enter the name for recipe")
        name = input()
        print ("Please enter ingredients you need, like this ['tomate', 'carotte']")
        ingredients = input()
        print ("Please enter meal")
        meal = input()
        print ("Please enter time for preparation")
        time = input()
        add_recipe(name, ingredients, meal, time)
    elif x == 2:
        print ("Please enter the recipe's name you want to dleete")
        y = input()
        del_recipe(y)
    elif x == 3:
        print ("Please enter the recipe's name to get details:")
        y = input()
        print_recipe(y)
    elif x == 4:
        print_all()
    else:
        exit()
