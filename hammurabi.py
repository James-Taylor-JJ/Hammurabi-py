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
        # declare local variables here: grain, population, etc.
        # statements go after the declarations

    # Methods for the game's core decisions
    
if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()