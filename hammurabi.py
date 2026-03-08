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
        self.plague_deaths = 0
        self.starvation_deaths = 0
        self.harvest = 0

        

        for year in range(1,11):
            # Announce the Current Year and Provide a Summary of the Previous Year's Events
            if year == 1:
                print (f"O great Hammurabi! You are in year 1 of your ten year rule.
                In the previous year 0 people starved to death.
                In the previous year 5 people entered the kingdom.
                The population is now {self.people} people.
                We harvested 3000 bushels at 3 bushels per acre.
                Rats destroyed 200 bushels, leaving {self.bushels} bushels in storage.
                The city owns 1000 acres of land.
                Land is currently worth {self.landValue} bushels per acre.")
            if year > 1:
            print(f"You are now in year {year} of your ten year rule, Sire.
                  Recall that in the previous year............")
            # call methods to make the core decisions
            self.askHowManyAcresToBuy(price, bushels)
            self.askHowManyAcresToSell(acresOwned)
            self.askHowMuchGrainToFeedPeople(bushels, population)
            self.askHowManyAcresToPlant(acresOwned, population, bushels)
            # call methods that govern the game's second order effects
            # Deliver End of Year Summary
            print(f"My Leige, you have concluded year {year} of your rule. Here is the summary of the year's events: 
                  ")
    
if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()