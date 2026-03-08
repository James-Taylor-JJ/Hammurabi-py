from hammurabi import Hammurabi
from random import Random

# Notes
# All the required arithmetic in this program should be integer. You do not need doubles.

def plagueDeaths(self, population):
    population = self.people
    plague_deaths = self.plague_deaths
    if self.rand.random() < 0.15:
        plague_deaths = population // 2
        self.people = population - plague_deaths
    else:
        plague_deaths = 0
    self.plague_deaths = plague_deaths
    return plague_deaths

def starvationDeaths(self, population, bushelsFedToPeople):
    starvation_deaths = 0
    bushelsFedToPeople = self.rations
    if bushelsFedToPeople < population * 20:
        starvation_deaths = population - bushelsFedToPeople // 20
        self.people = population - starvation_deaths
    self.starvation_deaths = starvation_deaths
    self.starvation_rate = (starvation_deaths / population) * 100 if population > 0 else 0
    return starvation_deaths  

def uprising(self, population, howManyPeopleStarved):
    howManyPeopleStarved = self.starvation_rate
    if howManyPeopleStarved > 45:
        print(f"My Lord, your subjects are revolting! {howManyPeopleStarved}% of your people starved to death this year. You have been deposed. Game over.")
        return True
    else:
        return False
    
def immigrants(self, population, acresOwned, grainInStorage):
    population = self.people
    acresOwned = self.acres
    grainInStorage = self.bushels
    if self.starvation_rate == 0:
        immigrants = (20 * acresOwned + grainInStorage) // (100 * population) + 1
        self.people = population + immigrants
        print(f"My Lord, your stewarship of the city has attacted {immigrants} immigrants to your city.")
        return
    else:
        print(f"My Lord, due to the starvation of {self.starvation_rate}% of your people, no immigrants emigrated to your city this year.")
        return 

def harvest(self, acres, bushelsUsedAsSeed):
    yield = self.rand.randint(1, 6)
    harvest = acres * yield
    self.harvest = harvest
    self.bushels = self.bushels + harvest
    return harvest

def grainEatenByRats(self, bushels):
    bushels = self.bushels
    if self.rand.random() < 0.40:
        percentEaten = self.rand.randint(10, 30)
        eaten = bushels * (percentEaten / 100)
        self.bushels = bushels - eaten
        print(f"My Lord, the city was smitten by a rat infestation this year. The vermin have reduced the grain in your granaries by {percentEaten}%, which amounts to {eaten} bushels.")
        return eaten
    else:
        return 0

def newCostOfLand(self):
    new_Cost = self.rand.randint(17, 23)
    self.landValue = new_Cost
    return new_Cost
# The price of land is random, and ranges from 17 to 23 bushels per acre. 
# Return the new price for the next set of decisions the player has to make. 
# (The player will need this information in order to buy or sell land.)