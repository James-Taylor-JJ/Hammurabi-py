import random
class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()

    def playGame(self, people=100, bushels=2800, acres=1000, landValue=19, year=1):
        self.people = people
        self.bushels = bushels
        self.acres = acres
        self.landValue = landValue
        self.rations = 0
        self.starvation_rate = 0
        self.plague_deaths = 0
        self.starvation_deaths = 0
        self.immigrants_in = 0
        self.harvest_amount = 0
        self.yield_per_acre = 0
        self.rat_damage = 0

        Welcome = input(f"Welcome to Hammurabi, a game of resource management and strategy. You are the ruler of ancient Sumer, and your goal is to govern your city for 10 years. Each year, you will make decisions about how much land to buy or sell, how much grain to feed your people, and how much land to plant with seed. Your decisions will have consequences, and you must balance the needs of your people with the resources at your disposal. Would you like to play? (Y/N)")
        if Welcome == "Y":
            name = input("Marvelous! I am Jayms, your Grand Vizier. Who shall I announce sits on the throne of Sumer? ")
            print("A noble name for a noble ruler. Best wishes for an auspicious reign!")
        else:
            print("Perhaps another time.")
            exit()

        for year in range(1,12):
            # Announce the Current Year and Provide a Summary of the Previous Year's Events
            if year == 1:
                print (f"O great {name}! You are in year 1 of your ten year rule.In the previous year 0 people starved to death. In the previous year 5 people entered the kingdom. The population is now {self.people} people. We harvested 3000 bushels at 3 bushels per acre. Rats destroyed 200 bushels, leaving {self.bushels} bushels in storage. The city owns 1000 acres of land. Land is currently worth {self.landValue} bushels per acre.")
            elif year == 11:
                print(f"Congratulations, Great {name}! You have completed your ten year rule. Here is the summary of your reign: {self.starvation_deaths} people starved to death, {self.immigrants_in} people entered the kingdom, which left population at {self.people} people. We harvested {self.harvest_amount} bushels at {self.yield_per_acre} bushels per acre. Rats destroyed {self.rat_damage} bushels, leaving {self.bushels} bushels in storage. The city owns {self.acres} acres of land. Land is currently worth {self.landValue} bushels per acre.")
                break
            elif year > 1:
                print(f"You are now in year {year} of your ten year rule, Great {name}. Recall that in the previous year {self.starvation_deaths} people starved to death. {self.immigrants_in} people entered the kingdom, which left population at {self.people} people. We harvested {self.harvest_amount} bushels at {self.yield_per_acre} bushels per acre. Rats destroyed {self.rat_damage} bushels, leaving {self.bushels} bushels in storage. The city owns {self.acres} acres of land. Land is currently worth {self.landValue} bushels per acre.")
             
            # call methods to make the core decisions
            self.askHowManyAcresToBuy(self.landValue, self.bushels)
            self.askHowManyAcresToSell(self.acres)
            self.askHowMuchGrainToFeedPeople(self.bushels, self.people)
            self.askHowManyAcresToPlant(self.acres, self.people, self.bushels)
            # call methods that govern the game's second order effects
            self.plagueDeaths(self.people)
            self.starvationDeaths(self.people, self.rations)
            if self.uprising(self.people, self.starvation_rate):
                break
            self.immigrants(self.people, self.acres, self.bushels)
            self.harvest(self.acres, self.rations)
            self.grainEatenByRats(self.bushels)
            self.newCostOfLand()
            # Deliver End of Year Summary
            print(f"My Leige, you have concluded year {year} of your rule. Here is the summary of the year's events: {self.starvation_deaths} people starved to death. {self.immigrants_in} people entered the kingdom. The population is now {self.people} people. We harvested {self.harvest_amount} bushels at {self.yield_per_acre} bushels per acre. Rats destroyed {self.rat_damage} bushels, leaving {self.bushels} bushels in storage. The city owns {self.acres} acres of land. Land is currently worth {self.landValue} bushels per acre.")
        
    # Core Decisions
    def askHowManyAcresToBuy(self, price, bushels): 
        price = self.landValue
        bushels = self.bushels
        buy = int(input(f"My Lord, you currently possess {self.acres} acres of land. Land is currently priced at {price} bushels per acre. How many acres does His Majesty wish to purchase?"))
        if buy * price < bushels:
            self.bushels = bushels - (buy * price)
            self.acres = self.acres + buy
            return buy
        elif buy * price > bushels:
            print(f"Your Majesty, you do not have enough grain to buy {buy} acres of land. A smaller number is required.")
            return self.askHowManyAcresToBuy(price, bushels)
        elif buy * price == bushels:
            print(f"Your Majesty, you have just enough grain to buy {buy} acres of land. This will leave you with no grain in storage. Are you certain you wish to pursue this policy? (yes/no) ")
            choice = input().lower()
            if choice == "yes":
                self.bushels = bushels - (buy * price)
                self.acres = self.acres + buy
                return buy
            else:
                return self.askHowManyAcresToBuy(price, bushels)
     
    def askHowManyAcresToSell(self, acresOwned):
        acresOwned = self.acres
        sell = int(input(f"Now, Your Majesty, do wish to sell any of your {self.acres} acres of land? If so, how many?"))
        if sell == 0:
            print(f"Very well, Your Majesty. We will not sell any land this year.")
            return 0
        elif sell > acresOwned:
            print(f"My Lord, you do not have {sell} acres of land to sell ... . Please decide on a smaller number.")
            return self.askHowManyAcresToSell(acresOwned)
        elif sell < acresOwned:
            self.acres = acresOwned - sell
            self.bushels = self.bushels + (sell * self.landValue)
            return sell
        elif sell == acresOwned:
            print(f"My Lord, are you quite alright? What you're suggesting is tantamount to abdication, or worse ... theft. Please reconsider.")
            choice = input("Do you wish to sell all your land? (yes/no) ").lower()
            if choice == "yes":
                self.acres = acresOwned - sell
                self.bushels = self.bushels + (sell * self.landValue)
                return sell
            else:
                return self.askHowManyAcresToSell(acresOwned)

    def askHowMuchGrainToFeedPeople(self, bushels, population):
        bushels = self.bushels
        population = self.people
        feed = int(input(f"Your Majesty, you have {self.bushels} bushels of grain in your grain stores. Bearing in mind that each of your {population} subjects require at least 20 bushels per year to survive, how many do you wish to devote to feeding your people?"))
        
        if feed > bushels:
            print(f"Sire, your inclination toward largesse is admirable, but you do not have {feed} bushels of grain to feed your people. Have you another figure in mind?")
            return self.askHowMuchGrainToFeedPeople(bushels, population)
        elif feed == bushels:
            print(f"Your Majesty, this is an incredibly generous decision, but devoting all {feed} bushels of grain in storage to feeding your people this year will empty the city's reserves and render you unable to sow the seeds that will grow into next year's grain. Are you sure you wish to follow through with this decisoion? (yes/no) ")
            decision_3 = input().lower()
            if  decision_3 == "yes":
                print(f"Very well, Sire. We will devote all {feed} bushels of grain in storage to feeding your people this year. I pray that you do not come to regret this decision.")
                self.bushels = bushels - feed
                self.rations = feed
                return feed
            else:
                print(f"A wise decision, My Lord.")
                return self.askHowMuchGrainToFeedPeople(bushels, population)
        elif feed < (20*population):
            decision = input(f"Your Majesty, you have chosen to distribute to your people only {feed} bushels of grain this year. This is not enough to keep them alive and may lead to unrest. I strongly advise against this course of action. Do you wish to proceed?(yes/no)")
            if decision == "yes":
                print(f"Very well, Sire. We will only devote {feed} bushels of grain to the nourishment of your people this year. I pray that you do not come to regret this decision.")
                self.bushels = bushels - feed
                self.rations = feed
                return feed
            else:
                print(f"I am most relieved that you have reconsidered, My Lord.")
                return self.askHowMuchGrainToFeedPeople(bushels, population)
        elif feed == (20*population):
            print(f"Your Majesty, you have chosen to devote {feed} bushels of grain to feeding your people this year. This is just enough to keep them alive, but they will not be happy. Are you sure you wish to pursue this course of action? (yes/no) ")
            decision_2 = input().lower()
            if decision_2 == "yes":
                print(f"As you wish, Sire. We will shall proceed with austerity measures, as you have instructed. I have instructed the royal steward to distribute no more than {feed} from the grain stores.")
                self.bushels = bushels - feed
                self.rations = feed
                return feed
            else: 
                print(f"You are most wise, My Lord.")
                return self.askHowMuchGrainToFeedPeople(bushels, population)
        else:
            print(f"As you command, My Liege. I shall inform the royal steward that he is authorized to distribute up to {feed} bushels of grain to the citizen of the city.")
            self.bushels = bushels - feed
            self.rations = feed
            return feed
        
    def askHowManyAcresToPlant(self, acresOwned, population, bushels):
        acresOwned = self.acres
        population = self.people
        bushels = self.bushels
    
        while True:
            plant = int(input(f"Your Majesty, in addition the {acresOwned} acres of land that you possess, you have {self.people} subjects, and {self.bushels} bushels of grain in storage. Bearing in mind that each acre planted requires 2 bushels of grain and one person can only farm 10 acres, how many acres do you wish to plant with seed this year?"))
            if plant < 0:
                print(f"Most amusing my Leige. However, are you certain that you wish to forgo planting any of your land this year? (yes/no) ")
                decision = input().lower()
                if decision == "yes":
                    print(f"Very well, Sire. We will not plant any land this year.")
                    return 0
                else:
                    continue
            elif plant > self.acres:
                print(f"My Lord, you do not have {plant} acres of land to plant. Please choose a smaller number.")
                continue
            elif plant > (population * 10):
                print(f"Your Majesty, you have only {population} subjects, and each can only farm 10 acres of land. Let us Please choose a smaller number.")
                continue
            elif plant > (bushels // 2):
                print(f"Your Majesty, you do not have enough grain in storage to plant {plant} acres of land. Please choose a smaller number.")
                continue
            else:            
                self.bushels = bushels - (plant * 2)
                print(f"Very good, Sire. {plant} bushels shall be sown this year. After planting {plant} acres of land with seed, we have {self.bushels} bushels of grain left in storage.")
                return plant
        
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
        population = self.people
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
            self.immigrants_in = immigrants
            self.people = population + immigrants
            print(f"My Lord, your stewarship of the city has attacted {immigrants} immigrants to your city.")
            return immigrants
        else:
            print(f"My Lord, due to the starvation of {self.starvation_rate}% of your people, no immigrants emigrated to your city this year.")
            return 

    def harvest(self, acres, bushelsUsedAsSeed):
        yield_per_acre = self.rand.randint(1, 6)
        harvest = acres * yield_per_acre
        self.harvest_amount = harvest
        self.bushels = self.bushels + harvest
        self.yield_per_acre = yield_per_acre
        return harvest

    def grainEatenByRats(self, bushels):
        bushels = self.bushels
        if self.rand.random() < 0.40:
            percentEaten = self.rand.randint(10, 30)
            eaten = bushels * (percentEaten / 100)
            self.rat_damage = eaten
            self.bushels = bushels - eaten
            print(f"My Lord, the city was smitten by a rat infestation this year. The vermin have reduced the grain in your granaries by {percentEaten}%, which amounts to {eaten} bushels.")
            return eaten
        else:
            return 0

    def newCostOfLand(self):
        new_Cost = self.rand.randint(17, 23)
        self.landValue = new_Cost
        return new_Cost
    
if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()