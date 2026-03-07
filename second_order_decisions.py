from hammurabi import Hammurabi

# Notes
# All the required arithmetic in this program should be integer. You do not need doubles.

def plagueDeaths(population):
# Each year, there is a 15% chance of a horrible plague. 
# When this happens, half your people die. 
# Return the number of plague deaths (possibly zero).
def starvationDeaths(population, bushelsFedToPeople):
# Each person needs 20 bushels of grain to survive. 
# If you feed them more than this, they are happy, but the grain is still gone. 
# You don't get any benefit from having happy subjects. 
# Return the number of deaths from starvation (possibly zero).
def uprising(population, howManyPeopleStarved):
# Return True if more than 45% of the people starve. 
# (This will cause you to be immediately thrown out of office, ending the game.)
def immigrants(population, acresOwned, grainInStorage):
# Nobody will come to the city if people are starving (so don't call this method). 
# If everyone is well fed, compute how many people come to the city as: (20 * _number of acres you have_ + _amount of grain you have in storage_) / (100 * _population_) + 1.
def harvest(acres, bushelsUsedAsSeed):
# Choose a random integer between 1 and 6, inclusive. 
# Each acre that was planted with seed will yield this many bushels of grain. 
# (Example: if you planted 50 acres, and your number is 3, you harvest 150 bushels of grain). 
# Return the number of bushels harvested.
def grainEatenByRats(bushels):
# There is a 40% chance that you will have a rat infestation. 
# When this happens, rats will eat somewhere between 10% and 30% of your grain. 
# Return the amount of grain eaten by rats (possibly zero).
def newCostOfLand():
# The price of land is random, and ranges from 17 to 23 bushels per acre. 
# Return the new price for the next set of decisions the player has to make. 
# (The player will need this information in order to buy or sell land.)

def printSummary ():
#When the computations are finished, call a method  to print the summary for the year. This method will take several parameters.
# Summary text is as follows:
"You are in year 1 of your ten year rule. 
In the previous year 0 people starved to death.
In the previous year 5 people entered the kingdom.
The population is now 100.
We harvested 3000 bushels at 3 bushels per acre.
Rats destroyed 200 bushels, leaving 2800 bushels in storage.
The city owns 1000 acres of land.
Land is currently worth 19 bushels per acre."
def finalSummary ():
# When the game ends, use a method finalSummary to print out a final summary, and to tell the player how good a job he/she did. I'll leave the details up to you, but the usual evaluation is based on how many people starved, and how many acres per person you end up with.