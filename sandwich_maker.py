# import pyinptplus and time modules
import pyinputplus as pyip, time

# dictionary with prices of everything
prices = {
    "bread": {
        "wheat": 1.5,
        "white": 1,
        "sourdough": 1.25,
    },
    "protein": {
        "chicken": 0.75,
        "turkey": 1,
        "ham": 0.75,
        "tofu": 0.5
    },
    "cheese": {
        "cheddar": 0.25,
        "swiss": 0.25,
        "mozarella": 0.3,
    },
    "mayo": 0.1,
    "mustard": 0.1,
    "lettuce": 0.1,
    "tomato": 0.1,
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
number_of_sandwiches = pyip.inputNum("How many of this sandwich type do you want\n", allowRegexes=[r"[0-9]+"], blockRegexes=(r"(?=.*\.)", "Please enter a whole number"))


time.sleep(0.5)

# display price
total = 0
print('\n'+"RECEIPT".center(20,)+"\n")
print(f"{'Ingredient'.center(11)} - Price ($)")
for sandwich_part in sandwich:
    print(f"{(sandwich_part[0].rjust(11)).title()} - {str(sandwich_part[1]).rjust(9)}")
    total += sandwich_part[1]

if(number_of_sandwiches > 1):
    print(f"X {number_of_sandwiches}")
    total *= number_of_sandwiches
    total = round(total, 2)

print(f"{'Total'.rjust(11)} - {str(total).rjust(9)}")