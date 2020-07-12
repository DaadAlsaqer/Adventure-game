import time
import random

characters = ["troll", "gorgon", "pirate", "wicked fairie"]
character = random.choice(characters)


def print_pause(message):
    print(message)
    time.sleep(2)


def introduction():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {character} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")

def vaild_input(prompt, option1, option2):
    while True:
        choice5 = input(prompt)
        if option1 in choice5:
            break
        elif option2 in choice5:
            break
    return choice5

def field():
	print_pause("You run back to the field. Luckily, "
				"you don't seem to have been followed.")

def second_choice(items):
    second_choice = vaild_input("Would you like to (1) "
                                "fight or (2) run away?\n", "1", "2")
    if second_choice == "1":
        if "Sword" in items:
            attack()
            play_again()
        else:
            death()
            play_again()
    elif second_choice == "2":
        field()
        choices(items)


def house(items):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door "
                f"opens and out steps a {character}.")
    print_pause(f"Eep! This is the {character}'s house!")
    print_pause(f"The {character} attacks you!")
    second_choice(items)

def cave(items):
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical sword of Ogoroth!")
    print_pause("You discard your silly old dagger "
                "and take the sword with you.")
    print_pause("You walk back out to the field.\n")
    items.append("Sword")


def attack():
    print_pause(f"As the {character} moves to attack, "
                "you unsheath your new sword.")
    print_pause("The Sword of Ogoroth shines brightly in your"
                " hand as you brace yourself for the attack.")
    print_pause(f"But the {character} takes one look "
                "at your shiny new toy and runs away!")
    print_pause(f"You have rid the town of the {character}.\n"
                "You are victorious!")

def death():
	print_pause("You do your best..")
	print_pause(f"but your dagger is no match for the {character}")
	print_pause("You have been defeated!")


def back_to_the_cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("You've been here before, and gotten all the"
                " good stuff. It's just an empty cave now.")
    print_pause("You walk back out to the field.\n")


def choice1(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")


def choices(items):
    choice1(items)
    choice = vaild_input("What would you like to do?\n(Please enter 1 or 2)\n", "1", "2")
    if choice == "1":
        house(items)      
    elif choice == "2":
        if "Sword" in items:
            back_to_the_cave()
            choices(items)
        else:
            cave(items)
            choices(items)


def play_again():
    play_again = vaild_input("Would you like to play again ? (y/n)", "y", "n")
    if play_again == "y":
        play()
    elif play_again == "n":
    	print_pause("Thanks for playing! see you next time :)")


def play():
    items = []
    introduction()
    choices(items)


play()
