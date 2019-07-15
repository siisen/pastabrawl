#Setup
import random
import time
round = 0
divider = "------------------------------------------------------------"

#Class for the fighters
class Superhero:
    
    def __init__(self, hero_name, health, strenght):
        self.hero_name = hero_name
        self.health = health
        self.strenght = strenght

    def eating(self, food):
        if food == "1":
            self.strenght = 1
            print(input("\nMmmh. Quite healthy. Fingers crossed for the fight!\nWhen you are ready to fight, press 'Enter'."))
        elif food == "2":
            self.strenght = 2
            print(input("\nYum! Very healthy choice, " + user_name + "! That fight should be easy!\nWhen you are ready to fight, press 'Enter'.\n"))
        elif food == "3":
            self.strenght = -1
            print(input("\nMeh. Not so healthy. You'll need an extra mug of luck in the fight. Fingers crossed.\nWhen you are ready to fight, press 'Enter'.\n"))
        elif food == "4":
            self.strenght = -2
            print(input("\nYuk, " + user_name + ". Very unhealthy. You are lactose intolerant, don't u remember? Let's hope the monster has a bad day...\nPress 'Enter' if you are ready to fight.\n"))
        else:
            self.health = self.health
            print(input("\nYou are not hungry? Well, ok, good luck!\nPress 'Enter' if you are ready to fight.\n\n"))
        return self.strenght

    def attack(self):
        defend_strenght =  random.randint(1, 10)
        self.strenght = self.strenght + random.randint(1, 10)
        result = defend_strenght - self.strenght
        if result < 0:
            enemy.health = enemy.health + result
            user_health_level= int(100 / 15 * self.health)
            monster_health_level = int(100 / 15 * enemy.health)
            print("\nYeah, you WON this round! Keep going!")
        elif result > 0:
            self.health = self.health - result
            user_health_level = int(100 / 15 * self.health)
            monster_health_level = int(100 / 15 * enemy.health)
            print("\nOh no, you LOST this round.")
        else:
            self.health = self.health
            enemy.health = enemy.health
            user_health_level = int(100 / 15 * self.health)
            monster_health_level = int(100 / 15 * enemy.health)
            print("\nNo winner in this round!")
        
        if user_health_level > 0 and monster_health_level > 0:
            print("\nYour health level is at " + str(user_health_level) + " %! The monster's is at " + str(monster_health_level) +" %!\n\n" + divider)
        else:
            print("The battle is over!\n\n" + divider)

#Intro
print("\n\nWelcome to 'Pasta Brawl'!\n~~~~~~~~~~~~~~~~~~~~~~~~\n" )
print(input("In this game, you have to fight the incredible Spaghetti Monster! Are you ready to fight and to become a hero?\nPress 'Enter'."))

user_name = input("Great! Under what name shall you be remembered as a hero? Enter your hero's name! \n")

#Build objects from class (User and Monster)
user = Superhero("user_name", 15, 0)
enemy = Superhero("Spagetthi Monster", 15, 0)

#Introduction
print(input("\nAlright, " + user_name + ", we count on you! Let's get going, the incredible Spaghetti Monster is very hangry today.\nAre you ready? Press 'Enter'. "))

print(input("Well, not quite, I know. Before every fight, you first need to grab a snack!\nBut remember, we are what we eat. A healthy option will increase your strength in the fight, an unhealhy option weakens you, ok? Press 'Enter'."))

#Game loop while both fighters alive
while int(user.health) > 0 and int(enemy.health) > 0:
    round = round + 1
    print("What would you like to eat?")
    print("\n[1] Pasta Salad\n[2] Sauerkraut\n[3] Kale Chips\n[4] Greek Yogurt\n")
    food_choice = input("Choose wisely! Enter '1', '2', '3' or '4' ")
    user.eating(food_choice)
    print("\nAlright, brace yourself " + user_name + "! Round " + str(round) + " is in progress! Wait for it...\n" + divider )
    time.sleep(2)
    user.attack()
    if user.health > 0 and enemy.health > 0:
        print(input("\nLet's move on. Press enter if you are ready for the next round. "))
    else:
        print("")

#Outro
if user.health > enemy.health:
    message = "\nYou won and defeated the incredible Spaghetti Monster in just " + str(round) + "rounds! Glory to " +user_name + "!\n"
else:
    message = "\nYou lost. So sad. The incredible Spaghetti Monster was too strong today. Let's try again!\n"

print(message)
print(input(""))
print("That's it. The program has terminated\n" + str(divider) + "\n\n")