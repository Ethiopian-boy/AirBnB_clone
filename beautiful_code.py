#!/usr/bin/python3

class Robot:
    """Represents a robot with a name"""

    # A class variable counting the number of robots

    population = 0

    def __init__(self, name):
        """intializes the data"""

        self.name = name
        print("(Intializing {})".format(self.name))
        Robot.population += 1

    def die(self):
        """I'm dying"""

        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """Greeting by the robot"""

        print("Greating, my master call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the currrent population"""
        print("we have {:d} robots.".format(cls.population))


new = Robot("Alexa")
current = Robot("Google_assistance")
top = Robot("Waw")
new.say_hi()
current.say_hi()
top.say_hi()
Robot.how_many()
print("All done robots finished their task")
new.die()
top.die()
Robot.how_many()
current.die()
Robot.how_many()
print("Today is awesome")
