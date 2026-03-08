from hammurabi import Hammurabi
from random import Random

# Notes
# All the required arithmetic in this program should be integer. You do not need doubles.

def plagueDeaths(self, population):
    plague_deaths = self.plague_deaths
    if self.rand.random() < 0.15:
        plague_deaths = population // 2
        self.people = population - plague_deaths
    else:
        plague_deaths = 0
    self.plague_deaths = plague_deaths
    return plague_deaths
def starvationDeaths(self, population, bushelsFedToPeople):
# Each person needs 20 bushels of grain to survive. 
# If you feed them more than this, they are happy, but the grain is still gone. 
# You don't get any benefit from having happy subjects. 
# Return the number of deaths from starvation (possibly zero).
def uprising(self, population, howManyPeopleStarved):
# Return True if more than 45% of the people starve. 
# (This will cause you to be immediately thrown out of office, ending the game.)
def immigrants(self, population, acresOwned, grainInStorage):
# Nobody will come to the city if people are starving (so don't call this method). 
# If everyone is well fed, compute how many people come to the city as: (20 * _number of acres you have_ + _amount of grain you have in storage_) / (100 * _population_) + 1.
def harvest(self, acres, bushelsUsedAsSeed):
# Choose a random integer between 1 and 6, inclusive. 
# Each acre that was planted with seed will yield this many bushels of grain. 
# (Example: if you planted 50 acres, and your number is 3, you harvest 150 bushels of grain). 
# Return the number of bushels harvested.
def grainEatenByRats(self, bushels):
# There is a 40% chance that you will have a rat infestation. 
# When this happens, rats will eat somewhere between 10% and 30% of your grain. 
# Return the amount of grain eaten by rats (possibly zero).
def newCostOfLand(self):
# The price of land is random, and ranges from 17 to 23 bushels per acre. 
# Return the new price for the next set of decisions the player has to make. 
# (The player will need this information in order to buy or sell land.)