# import pyinptplus and time modules
import pyinputplus as pyip, time, pprint

# dictionary with prices of everything
prices = {
    "wheat bread": 1.50,
    "white bread": 1.00,
    "sourdough bread": 1.25,
    "chicken": 0.75,
    "turkey": 1.00,
    "ham": 0.75,
    "tofu": 0.50,
    "cheddar cheese": 0.25,
    "swiss cheese": 0.25,
    "mozarella cheese": 0.30,
    "mayo": 0.10,
    "mustard": 0.10,
    "lettuce": 0.10,
    "tomato": 0.10,
}

# sandwiches list
sandwiches = [] 
total = 0 # price

while True:
    current_sandwich = []
    # get bread type wheat
    bread_type = pyip.inputMenu(["wheat bread", "white bread", "sourdough bread"], prompt="What type of bread🥖 would you like?\n\n", numbered=True, default="white bread", limit=3)
    current_sandwich.append((f"{bread_type}", prices[bread_type]))

    # get protein type
    protein_type = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], prompt="\nWhat protein🍗 woukd you like in your sandwich\n\n", numbered=True, default="chicken", limit=3)
    current_sandwich.append((f"{protein_type}", prices[protein_type]))

    # chesse?
    cheese = pyip.inputYesNo(prompt="\nWould you like cheese🧀 in your sandwich?\n Enter (y)es or (n)o\n")
    if(cheese == "yes"):# cheese type
        cheese_type = pyip.inputMenu(["cheddar cheese", "swiss cheese", "mozarella cheese"], prompt="What type of cheese🧀 would you like in your sandwich\n", numbered=True ,default="cheddar cheese", limit=3)
        current_sandwich.append((f"{cheese_type}", prices[cheese_type]))

    # extra condoments?
    extra_condoments = (["mayo", ''], ["mustard", ''], ["lettuce", "🥬"], ["tomato", "🍅"])
    for condoment in extra_condoments:
        extra_condoment = condoment[0]
        choice = pyip.inputYesNo(prompt=f"\nWould you also want {condoment[0]}{condoment[1]} in your sandwich?\n Enter (y)es or (n)o\n=>: ", limit=3)
        if choice == "yes":
            current_sandwich.append((f"{condoment[0]}", prices[condoment[0]]))

    # no of sandwiches
    number_of_sandwiches = pyip.inputNum("How many of this sandwich type do you want\n", allowRegexes=[r"^[0-9]+$"], blockRegexes=[(r"^[0-9]+\.[0-9]*$", "Please enter a whole number")])            

    make_another = pyip.inputYesNo(prompt="Would you like to order another sandwich?\n", limit=3)
    sandwiches.append((current_sandwich, number_of_sandwiches))
    pprint.pprint(sandwiches)
    if make_another == 'yes':
        continue
    else:
        break

time.sleep(0.5) # wait before showing price

def sort_ingredients(parent_list):
    """This function neatly sorts the ingredients used into a dictionary"""
    ingredients = {}

    for child_list in parent_list:
        for ingredient in child_list[0]:
            ingredients.setdefault(ingredient[0], 0)
            ingredients[ingredient[0]] += (1*child_list[1]) 

    print(ingredients)
    return ingredients

ingredients = sort_ingredients(sandwiches)
sandwich_1 = sort_ingredients([sandwiches[0]])

def compute_price(dictionary):
    """This function displays the price of the sandwiches"""
    total = 0
    for key, value in dictionary.items():
        total += (value * prices[key])

    print(f"${str(round(total, 2)).ljust(5, '0')}")

compute_price(ingredients)

# display price

# print('\n'+"RECEIPT".center(28))
# print(f"{'Ingredient'.center(16)} | Price ($)")
# print("-"*28)
# for sandwich_part in sandwich:
#     print(f"{(sandwich_part[0].ljust(16)).title()} - {str(sandwich_part[1]).rjust(9)}")
#     total += sandwich_part[1]

# print(('-'*5).rjust(28))
# print(f"{str(round(total, 2)).rjust(28)}")

# if(number_of_sandwiches > 1):
#     print(f"X {number_of_sandwiches}")
#     total *= number_of_sandwiches

# print("-"*28)
# print(f"{'Total'.ljust(16)} = {str(round(total, 2)).rjust(9)}")
# print("-"*28)
# print(sandwich)