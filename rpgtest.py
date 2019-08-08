from os import system, name
import time
import random

# Clearing the screen so it doesn't get messy
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux
    else: 
        _ = system('clear') 

# Checking if the user has a save file
def start():
    print("Do you have a savefile?")
    print("Type '1' to start a new save file, or '2' to load your save file.")
    saveCheck = input("")
    if saveCheck == "1":
        createSave()
    elif saveCheck == "2":
        loadSave()
    else:
        start()

# The actual game, involves fighting monsters automatically and seeing the numbers rise
def game(chrName, chrClass, chrLvl, chrXp, chrStr, chrDef, chrMaxHp, chrGold):
    clear()
    levelFormula(chrLvl, chrXp)
    chrHp = chrMaxHp
    print("@---------------------@)")
    print(chrName + " the " + chrClass)
    print("Level " + str(chrLvl))
    print("XP " + str(chrXp) + "/" + str(maxXp))
    print("Strength: " + str(chrStr))
    print("Defence: " + str(chrDef))
    print("Health: " + str(chrHp) + "/" + str(chrMaxHp))
    print("Gold: " + str(chrGold))
    print("@---------------------@)")
    
# Setting up the level formula for the game and handles checking for a levelup
def levelFormula(chrLvl, chrXp):
    global maxXp
    maxXp = (chrLvl + 3) * chrLvl
    if chrXp >= maxXp:
        chrLvl + 1
    else:
        pass
    
# Loading savefile for user
def loadSave():
    clear()
    # Opening save file in read-only for transfer to the script
    # Reading all the lines individually as each line is different data
    f = open("save.txt","r")
    lines = f.readlines()
    f.close()
    # Stripping the input as it usually includes the terminating newline character \n
    chrName = (lines[0].strip())
    chrClassNum = int(lines[1].strip())
    print(chrClassNum)
    if chrClassNum == 0:
        chrClass = "Berserker"
    elif chrClassNum == 1:
        chrClass = "Warrior"
    elif chrClassNum == 2:
        chrClass = "Tank"
    # Bug check, incase the user manages to break the program
    else:
     print("Somehow you got here. The script broke.")
     time.sleep(100)
     exit()
    chrLvl = int(lines[2].strip())
    chrXp = int(lines[3].strip())
    chrStr = int(lines[4].strip())
    chrDef = int(lines[5].strip())
    chrHp = int(lines[6].strip())
    chrGold = int(lines[7].strip())
    print("@--------------@")
    print("Name: " + chrName)
    print("Class: " + chrClass)
    print("Level: " + str(chrLvl))
    print("XP: " + str(chrXp))
    print("Strength: " + str(chrStr))
    print("Defence: " + str(chrDef))
    print("Health: " + str(chrHp))
    print("Gold: " + str(chrGold))
    print("@--------------@")
    game(chrName, chrClass, chrLvl, chrXp, chrStr, chrDef, chrHp, chrGold)
    
# Setting up savefile for user
def createSave():
    clear()
    # Creating save file for the user
    f = open("save.txt","w+") 
    print("What is your name?")
    name = input("")
    # Will be organized in lines, \n is used to create a new paragraph
    f.write(name + "\n")
    f.close()
    clear()
    # Setting up which class the user would like to be, this determines their statistics
    # Using a while loop instead of a new function to save space
    classPicked = 0
    while classPicked == 0:
        print("What class would you like to be?")
        print("Berserker has high attack, low defence and health. Type 0 to pick this class.")
        print("Warrior has medium attack, medium defence and health. Type 1 to pick this class.")
        print("Tank has low attack, low defence but high health. Type 2 to pick this class.")
        chrClass = input("")
    # Opening file in append mode to add new lines
        if chrClass == ("0" or "1" or "2"):
            f = open("save.txt","a+")
            f.write(chrClass + "\n")
            f.close()
            break
        elif chrClass == ("1"):
            f = open("save.txt","a+")
            f.write(chrClass + "\n")
            f.close()
            break
        elif chrClass == ("2"):
            f = open("save.txt","a+")
            f.write(chrClass + "\n")
            f.close()
            break
    # Returns user back to start of loop because an invalid option was picked
        else:
            pass
    # Transferring our character class number to the other function
    setupChar(chrClass)

# Setting up advanced statistics for player eg: gold, exp, level, damage, defence and health
# Reminder: Line 1 = Name, Line 2 = Class, Line 3 = Level, Line 4 = XP, Line 5 = Strength
# --------: Line 6 = Defence, Line 7 = Health, Line 8 = Gold
def setupChar(classNum):
    f = open("save.txt","a+")
    # This is the starting level of the user
    f.write("1" + "\n")
    # This is the starting XP of the user
    f.write("0" + "\n")
    # Generating random stats based on the user's class
    # 0 = Berserker, 1 = Warrior, 2 = Tank
    if classNum == ("0"):
        strength = random.randint(11,18)
        f.write(str(strength) + "\n")
        defence = random.randint(4,11)
        f.write(str(defence) + "\n")
        health = random.randint(10,15)
        f.write(str(health) + "\n")
    elif classNum == ("1"):
        strength = random.randint(8,14)
        f.write(str(strength) + "\n")
        defence = random.randint(8,14)
        f.write(str(defence) + "\n")
        health = random.randint(20,30)
        f.write(str(health) + "\n")
    elif classNum == ("2"):
        strength = random.randint(4,11)
        f.write(str(strength) + "\n")
        defence = random.randint(4,11)
        f.write(str(defence) + "\n")
        health = random.randint(45,60)
        f.write(str(health) + "\n")
    # Bug check, incase the user manages to break the program
    else:
     print("Somehow you got here. The script broke.")
     time.sleep(100)
     exit()
    # Writing final starting gold value to the save file
    f.write("0" + "\n")
    f.close()

start()
