from hammurabi import Hammurabi

# Notes
# All the required arithmetic in this program should be integer. You do not need doubles.

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
        return self.askHowManyAcresToBuy(self)
    elif buy * price == bushels:
        print(f"Your Majesty, you have just enough grain to buy {buy} acres of land. This will leave you with no grain in storage. Are you certain you wish to pursue this policy? (yes/no) ")
        choice = input().lower()
        if choice == "yes":
            self.bushels = bushels - (buy * price)
            self.acres = self.acres + buy
            return buy
        else:
            return self.askHowManyAcresToBuy()
     
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
            return feed
        else:
            print(f"A wise decision, My Lord.")
            return self.askHowMuchGrainToFeedPeople(bushels, population)
    elif feed < (20*population):
        decision = input(f"Your Majesty, you have chosen to distribute to your people only {feed} bushels of grain this year. This is not enough to keep them alive and may lead to unrest. I strongly advise against this course of action. Do you wish to proceed?(yes/no)")
        if decision == "yes":
            print(f"Very well, Sire. We will only devote {feed} bushels of grain to the nourishment of your people this year. I pray that you do not come to regret this decision.")
            self.bushels = bushels - feed
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
            return feed
        else: 
            print(f"You are most wise, My Lord.")
            return self.askHowMuchGrainToFeedPeople(bushels, population)
    else:
        print(f"As you command, My Liege. I shall inform the royal steward that he is authorized to distribute up to {feed} bushels of grain to the citizen of the city.")
        self.bushels = bushels - feed
        return feed
    
def askHowManyAcresToPlant(self, acresOwned, population, bushels):
    acresOwned = self.acres
    population = self.people
    bushels = self.bushels
    maxAcresToPlant = min(acresOwned, population * 10, bushels // 2)
   
    while True:
        plant = int(input(f"Your Majesty, in addition the {self.acres} acres of land that you possess, you have {self.people} subjects, and {self.bushels} bushels of grain in storage. Bearing in mind that each acre planted requires 2 bushels of grain and one person can only farm 10 acres, how many acres do you wish to plant with seed this year?"))
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