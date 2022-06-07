import time
import random
from datetime import datetime


tools = random.choice(["machete", "walking stick"])
place = random.choice(["bridge", "waterfall"])
creatures = random.choice(["fairies", "trolls"])


def confirmation(message):
    for n in range(len(message)):
        print(message[n])
        time.sleep(1)


def print_pause(statement):
    print(statement)
    time.sleep(2)


def intro():
    print_pause(f"Hello Adventurer!")
    print_pause("You are wandering through an unfamiliar forest")
    print_pause(f"When you are attacked by a group of {creatures}!")
    print_pause(f"Your only weapon is your {tools}")
    print_pause("Do you want to fight or"
                " ignore them and continue your journey")


def journey(collection):
    if "unicorn dust" in collection:
        print_pause("You continue on your journey through the forest")
        print_pause("Now you are surrounded")
        print_pause(f"The {creatures} won't give up! They want to fight!")
    else:
        print_pause(f"You make it to a {place} and"
                    " you find a group of Unicorns!")
        print_pause("The unicorns warn you that you will be"
                    " attacked again and will die if you"
                                " don't have unicorn dust")
        print_pause(f"The {creatures} are ruthless to"
                    " those without protection!")
        print_pause(f"The Unicorns from the {place}"
                    " sprinkle you with unicorn dust for"
                                " protection on your journey back.")
        print_pause("You begin your journey back to the forest entrance.")
        print_pause(f"Sure enough, you encounter the {creatures} once again!")
        collection.append("unicorn dust")
    options(collection)


def fight(collection):
    if "unicorn dust" in collection:
        print_pause(f"Protected by the unicorn dust you"
                    f" use your {tools} to fight!")
        print_pause(f"The {creatures} are destroyed.")
        confirmation("YOU WIN")
    else:
        print_pause(f"You attack! But the {creatures} have magical powers!\n"
                    " They use their magic.")
        print_pause("You are taken out.")
        confirmation("GAME OVER")


def options(collection):
    response = input(f"Enter command: \n(1) Fight the {creatures} "
                     "\n(2) Continue your journey\n")
    if response == "1":
        fight(collection)
    elif response == "2":
        journey(collection)
    else:
        print_pause("Please enter a valid response!")
        options(collection)


def game_restart():
    print_pause("\nWould like to restart another adventure?")
    restart = input("Enter your command:\n(1) yes\n(2) no\n")
    if restart == "1":
        print_pause("Resetting adventure")
        print_pause("New adventure begins in")
        confirmation("54321")
        play_adventurer()
    elif restart != "2":
        print_pause("Please enter a valid response!\n")
        game_restart()
    else:
        print_pause(f"Thank you for playing! Goodbye Adventurer!")


def play_adventurer():
    collection = []
    intro()
    options(collection)
    game_restart()


play_adventurer()