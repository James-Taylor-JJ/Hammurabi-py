from hammurabi import Hammurabi

# Notes
# All the required arithmetic in this program should be integer. You do not need doubles.


def askHowManyAcresToBuy(price, bushels): 
    price = self.landValue
    bushels = self.bushels
    buy = int(input(f"My Lord, you currently possess {self.acres} acres of land. Land is currently priced at {price} bushels per acre. How many acres does His Majesty wish to purchase?"))
    if buy * price < bushels:
        return buy
    elif buy * price > bushels:
        print(f"Your Majesty, you do not have enough grain to buy {buy} acres of land. A smaller number is required.")
        return askHowManyAcresToBuy(price, bushels)
    elif buy * price == bushels:
        print(f"Your Majesty, you have just enough grain to buy {buy} acres of land. This will leave you with no grain in storage. Are you certain you wish to pursue this policy? (yes/no) ")
        choice = input().lower()
        if choice == "yes":
            return buy
        else:
            return askHowManyAcresToBuy(price, bushels)
    bushels = bushels - (buy * price)
    return bushels
     
def askHowManyAcresToSell(acresOwned):
# Asks the player how many acres of land to sell, and returns that number. 
# You can't sell more than you have.Do not ask this question if the player is buying land; it doesn't make sense to do both in one turn.
# Test whether the answer is possible (you have enough acres), and keep asking until you get a possible value.
def askHowMuchGrainToFeedPeople(bushels):
# Ask the player how much grain to feed people, and returns that number. 
# You can't feed them more grain than you have. You can feed them more than they need to survive.
# Test whether the answer is possible (you have enough grain), and keep asking until you get a possible value.
def askHowManyAcresToPlant(acresOwned, population, bushels):
# Ask the player how many acres to plant with grain, and returns that number. 
# You must have enough acres, enough grain, and enough people to do the planting. 
# Any grain left over goes into storage for next year.
# Test whether the answer is possible (you have enough acres, grain, and people) and keep asking until you get a possible value.
def askHowManyAcresToBuy(price, bushels):
# Asks the player how many acres of land to buy, and returns that number. 
# You must have enough grain to pay for your purchase.
# Test whether the answer is possible (you have enough grain) and keep asking until you get a possible value.
def askHowManyAcresToSell(acresOwned):
# Asks the player how many acres of land to sell, and returns that number. 
# You can't sell more than you have.
# Do not ask this question if the player is buying land; it doesn't make sense to do both in one turn.
# Test whether the answer is possible (you have enough acres), and keep asking until you get a possible value.
def askHowMuchGrainToFeedPeople(bushels):
# Ask the player how much grain to feed people, and returns that number. 
# You can't feed them more grain than you have. 
# You can feed them more than they need to survive.
# Test whether the answer is possible (you have enough grain), and keep asking until you get a possible value.
