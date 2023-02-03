# import pyinptplus and time modules
import pyinputplus as pyip, time

# dictionary with prices of everything
prices = {
    "bread": {
        "wheat": 1.50,
        "white": 1.00,
        "sourdough": 1.25,
    },
    "protein": {
        "chicken": 0.75,
        "turkey": 1.00,
        "ham": 0.75,
        "tofu": 0.5
    },
    "cheese": {
        "cheddar": 0.25,
        "swiss": 0.25,
        "mozarella": 0.30,
    },
    "mayo": 0.10,
    "mustard": 0.10,
    "lettuce": 0.10,
    "tomato": 0.10,
}

# sandwich list
sandwich = [] 

# get bread type wheat
bread_type = pyip.inputMenu(["wheat", "white", "sourdough"], prompt="What type of bread🥖 would you like?\n\n", numbered=True, default="white", limit=3)
sandwich.append([f"{bread_type} bread", prices["bread"][bread_type]])

# get protein type
protein_type = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], prompt="\nWhat protein🍗 woukd you like in your sandwich\n\n", numbered=True, default="chicken", limit=3)
sandwich.append([f"{protein_type}", prices["protein"][protein_type]])

# chesse?
cheese = pyip.inputYesNo(prompt="\nWould you like cheese🧀 in your sandwich?\n Enter (y)es or (n)o\n")
if(cheese == "yes"):# cheese type
    cheese_type = pyip.inputMenu(["cheddar", "swiss", "mozarella"], prompt="What type of cheese🧀 would you like in your sandwich\n", numbered=True ,default="cheddar", limit=3)
    sandwich.append([f"{cheese_type} cheese", prices["cheese"][cheese_type]])

# extra condoments?
extra_condoments = (["mayo", ''], ["mustard", ''], ["lettuce", "🥬"], ["tomato", "🍅"])
for condoment in extra_condoments:
    extra_condoment = condoment[0]
    choice = pyip.inputYesNo(prompt=f"\nWould you also want {condoment[0]}{condoment[1]} in your sandwich?\n Enter (y)es or (n)o\n=>: ", limit=3)
    if choice == "yes":
        sandwich.append([f"{condoment[0]}", prices[extra_condoment]])

# no of sandwiches
number_of_sandwiches = pyip.inputNum("How many of this sandwich type do you want\n", allowRegexes=[r"^[0-9]+$"], blockRegexes=[(r"^[0-9]+\.[0-9]*$", "Please enter a whole number")])

time.sleep(0.5) # wait before showing price

# display price
total = 0
print('\n'+"RECEIPT".center(28))
print(f"{'Ingredient'.center(16)} | Price ($)")
print("-"*28)
for sandwich_part in sandwich:
    print(f"{(sandwich_part[0].ljust(16)).title()} - {str(sandwich_part[1]).rjust(9)}")
    total += sandwich_part[1]

print(('-'*5).rjust(28))
print(f"{str(round(total, 2)).rjust(28)}")

if(number_of_sandwiches > 1):
    print(f"X {number_of_sandwiches}")
    total *= number_of_sandwiches

print("-"*28)
print(f"{'Total'.ljust(16)} = {str(round(total, 2)).rjust(9)}")
print("-"*28)