#!/usr/bin/python3

import random
import sys
import os

#from turtle import clear
#from typing_extensions import TypeVarTuple
#from tkinter import N 
from time import sleep
from functions import k_d_function, fselection, current_score, addTo, averageSolution


# what to keep track of? Ability to add more
# Features
    # make short cuts to add amounts to which stat. ex. kd2 kd3.2 will add the k/d of 2 to player one 
    # and 3.2 to player 2. Add a charactor to initialize the insersion of expressions sytle entries.
    
# setup variables    
name_done = False
start = False
game_stat_active = {}
players = []
num_players = 0
whole_end = False
kd_end = False
skip = False
type_kd = False
selection = 0
repeatStop = True


#game_stat_active = {"kd" : [0(kills),1(deaths),2(kd),3(#ofgames)], "kills" : [1,2,3], "deaths" : [1,2,3,4], "get_kill_cam" : [1,2,3,4], 
#             "in_kill_cam" : [1,2,3,4], "greatness" : [1,2,3,4]}
game_stat = [False] * 8 


# functions ******put function in different file so I can call it anywhere


print("********** Trash talking stat tracker **********")

# main menu
while (start == False): #selection menu, creating selection list
    os.system('clear')
    print("Select as many as you want. Press 9 to start.")
    if game_stat[0] == True:
        print("X: 1. Standard tracking two players, k/d, on kill cam, you are the kill cam, *You win and kill other player on kill cam")
    else:
        print("1. Standard tracking two players, k/d, on kill cam, you are the kill cam, *You win and kill other player on kill cam")
    if game_stat[1] == True:
        print("X: 2. k/d")
    else:
        print("2. k/d")
    if game_stat[2] == True:
        print("X: 3. kills")
    else:
        print("3. kills")
    if game_stat[3] == True:
        print("X: 4. deaths")
    else:
        print("4. deaths")
    if game_stat[4] == True:
        print("X: 5. you are the kill cam")
    else:
        print("5. you are the kill cam")
    if game_stat[5] == True:
        print("X: 6. in the kill cam")
    else:
        print("6. in the kill cam")
    if game_stat[6] == True:
        print("X: 7. achieve greatness (win match and kill other player on your kill cam")
    else:
        print("7. achieve greatness")    
    if game_stat[7] == True:
        print("X: 8. Wins")
    else:
        print("8. Wins")
    print("9. Finished selecting")#make it except letters
    try:
        selection = int(input("select one that applies: "))
    except:
        print("Please enter a number from the menu.")
       
    # main menu inputs, change False to True in List 
    if (selection == ""): print("Make a selection. enter 8 if finished.")
    if (selection == 1): # game_stat[0]  ******************need to check if this is correct code!!!!!!
        players = [None] * 2
        players[0] = input("first player: ")
        players[1] = input("second player: ")
        game_stat_active['player0'] = players[0]
        game_stat_active['player1'] = players[1]
        game_stat_active.update({"player0" : {"name" : players[0]}})
        game_stat_active.update({"player1" : {"name" : players[1]}})
        game_stat_active["player0"]['kd'] = [None, None, None, None]
        game_stat_active["player0"]['get_kill_cam'] = [None, None, None, None]
        game_stat_active["player0"]['in_kill_cam'] = [None, None, None, None]
        game_stat_active["player0"]['greatness'] = [None, None, None, None]
        game_stat_active["player1"]['kd'] = [None, None, None, None]
        game_stat_active["player1"]['get_kill_cam'] = [None, None, None, None]
        game_stat_active["player1"]['in_kill_cam'] = [None, None, None, None]
        game_stat_active["player1"]['greatness'] = [None, None, None, None]
        start = True
        skip = True
    if (selection == 2):
        game_stat[1] = fselection(game_stat[1])
    if (selection == 3):
        game_stat[2] = fselection(game_stat[2])
    if (selection == 4):
        game_stat[3] = fselection(game_stat[3])
    if (selection == 5):
        game_stat[4] = fselection(game_stat[4])
    if (selection == 6):
        game_stat[5] = fselection(game_stat[5])
    if (selection == 7):
        game_stat[6] = fselection(game_stat[6])
    if (selection == 8):
        game_stat[7] = fselection(game_stat[7])
    if (selection == 9):
        start = True  
    os.system('clear')    
i = 0
while (i != 10 and skip != True):#input names, create data dictionary
    print("Press Enter if no more players.")
    enter_name = input("player {} name: ".format(i))
    if (enter_name == ""):
        break 
    else:
        players.append(enter_name)
        num_players = num_players + 1
        game_stat_active.update({"player"+str(i) : {"name" : enter_name}}) #, "kd" : [1,2,3,4], "kills" : [1,2,3,4], "deaths" : [1,2,3,4], "get_kill_cam" : [1,2,3,4], 
             #"in_kill_cam" : [1,2,3,4], "greatness" : [1,2,3,4]}})
        if (game_stat[1] == True):
            game_stat_active["player"+str(i)]['kd'] = [None, None, None, None]
        if (game_stat[2] == True):
            game_stat_active["player"+str(i)]["kills"] = [None, None, None, None]
        if (game_stat[3] == True):      
            game_stat_active["player"+str(i)]["deaths"] = [None, None, None, None]
        if (game_stat[4] == True): 
            game_stat_active["player"+str(i)]["get_kill_cam"] = [None, None, None, None]
        if (game_stat[5] == True): 
            game_stat_active["player"+str(i)]["in_kill_cam"] = [None, None, None, None]
        if (game_stat[6] == True): 
            game_stat_active["player"+str(i)]["greatness"] = [None, None, None, None]
        if (game_stat[7] == True): 
            game_stat_active["player"+str(i)]["wins"] = [None, None, None, None]    
        if (selection == 8):
            start = True  
        i += 1

print("enter the stats\n") #Main loop to enter all the stats
j = 0 #counts for players in game_stat_active for kd
l = 0
enter_kill = False
enter_death = False
deaths_end = False
get_kill_cam_end = True
in_kill_cam_end = True
get_greatness = True
get_wins = True
repeatStop = False

while (whole_end == False):#receive data from user
    print(game_stat_active)
    if ("kd" in game_stat_active["player"+str(j)]): #kd[(0)kills,(1)deaths,(3)k/d]
        while (kd_end == False):
            while (type_kd == False):#input kill and death or k/d ratio
                kd_or_kd = int(input("Do you want to enter 1. kills & deaths or 2. k/d ratio\n")) 
                if (kd_or_kd < 1 or kd_or_kd > 2):
                    print("please enter (1) or (2)")       
                else:
                    type_kd = True
            if (kd_or_kd == 1):#input kill and deaths              
                k = 0 #counts for dictionary player key
                for i in players:
                    while(enter_kill == False):
                        print("{}'s kills: ".format(i))
                        try:
                            kills = int(input(""))
                        except:
                            print("Please enter a number.")
                        if ('kills' in game_stat_active["player"+str(k)]):
                                game_stat_active["player"+str(k)]['kills'][0] = addTo(game_stat_active["player"+str(k)]['kills'][0], kills) 
                                enter_kill = True
                                repeatStop = True
                        game_stat_active["player"+str(k)]['kd'][0] = addTo(game_stat_active["player"+str(k)]['kd'][0], kills) 
                    while (enter_death == False):
                        print("{}'s deaths: ".format(i))
                        try:
                            deaths = int(input(""))
                        except:
                            print("Please enter a number.")
                        if ('deaths' in game_stat_active["player"+str(k)]):
                                game_stat_active["player"+str(k)]['deaths'][1] = addTo(game_stat_active["player"+str(k)]['deaths'][1], deaths)
                                enter_death = True
                                repeatStop = True
                        temp_k_d = (k_d_function(kills, deaths))
                    game_stat_active["player"+str(k)]['kd'][0] = addTo(game_stat_active["player"+str(k)]['kd'][0], kills)
                    game_stat_active["player"+str(k)]['kd'][1] = addTo(game_stat_active["player"+str(k)]['kd'][1], deaths)
                    game_stat_active["player"+str(k)]['kd'][2] = averageSolution(game_stat_active["player"+str(k)]['kd'][2], temp_k_d)
                    enter_death = False 
                    enter_kill = False
                    k += 1
            kd_end = True           
            if (kd_or_kd == 2):#input k/d ratio
                k = 0 #counts for dictionary player key
                for i in players:
                    enter_kd = False
                    while(enter_kd == False):
                        print("{}'s K/D: ".format(i))
                        try:
                            kd = float(input(""))
                            enter_kd = True                           
                        except:
                            print("Please enter only numbers and a decimal")
                    game_stat_active["player"+str(k)]['kd'][2] = kd
                    k += 1 
                kd_end = True
    kills_end = False
    enter_kills = True
    if ("kills" in game_stat_active["player"+str(j)]): 
        while (kills_end == False):
            k = 0 #counts for dictionary player key
            for i in players:
                #If deaths is entered in K/D then it is transfered to kills without repeat input
                if (game_stat_active["player"+str(k)]['kd'][0] != None and repeatStop == True):
                    only_kills = game_stat_active["player"+str(k)]['kills'][0]
                    repeatStop = False
                else:
                    enter_kills = True
                    while (enter_kills == True):
                        print("{}'s kills: ".format(i))
                        try:
                            only_kills = int(input(""))
                            enter_kills = False
                        except:
                            print("Please enter a number.")
                    game_stat_active["player"+str(k)]['kills'][0] = only_kills
                    k += 1
                    #repeatStop = False
                kills_end = True
    if ("deaths" in game_stat_active["player"+str(j)]):
        while (deaths_end == False):
            k = 0 #counts for dictionary player key
            for i in players:
                if ('kd' in game_stat_active["player"+str(k)]):
                    deaths = game_stat_active["player"+str(k)]['kd'][1]
                else:
                    deaths_end = True
                    while (deaths_end == True):
                        print("{}'s deaths: ".format(i))
                        try:
                            deaths = int(input(""))
                            deaths_end = False
                        except:
                            print("Please enter a number.")
                    game_stat_active["player"+str(k)]['deaths'][0] = deaths
                k += 1
            deaths_end = True        
    if ("get_kill_cam" in game_stat_active["player"+str(j)]):
        while (get_kill_cam_end == True):
            k = 0 #counts for dictionary player key
            for i in players:
                getKillCam = True
                while (getKillCam == True):
                    print("{}'s kill cam: ".format(i))
                    try:
                        get_kill_cam = int(input(""))
                        getKillCam = False
                    except:
                        print("Please enter a number.")
                    game_stat_active["player"+str(k)]['get_kill_cam'][0] = addTo(game_stat_active["player"+str(k)]['get_kill_cam'][0], get_kill_cam)
                k += 1
            get_kill_cam_end = False       
    if ("in_kill_cam" in game_stat_active["player"+str(j)]):
        while (in_kill_cam_end == True):
            k = 0 #counts for dictionary player key
            for i in players:
                inKillCam = True
                while (inKillCam == True):
                    print("{}'s in kill cam: ".format(i))
                    try:
                        in_kill_cam = int(input(""))
                        inKillCam = False
                    except:
                        print("Please enter a number.")
                    game_stat_active["player"+str(k)]['in_kill_cam'][0] = in_kill_cam
                k += 1
            in_kill_cam_end = False
    if ("greatness" in game_stat_active["player"+str(j)]):
        while (get_greatness == True):
            k = 0 #counts for dictionary player key
            for i in players:
                getGreatness = True
                while (getGreatness == True):
                    print("{}'s achieved GREATNESS: ".format(i))
                    try:
                        get_greatnessCount = int(input(""))
                        getGreatness = False
                    except:
                        print("Please enter a number.")
                    game_stat_active["player"+str(k)]['greatness'][0] = get_greatnessCount
                k += 1
            get_greatness = False           
    if ("wins" in game_stat_active["player"+str(j)]):
        while (get_wins == True):
            k = 0 #counts for dictionary player key
            for i in players:
                getWin = True
                while (getWin == True):
                    print("{}'s achieved GREATNESS: ".format(i))
                    try:
                        getWinCount = int(input(""))
                        getWin = False
                    except:
                        print("Please enter a number.")
                    game_stat_active["player"+str(k)]['wins'][0] = getWinCount
                k += 1
            get_Wins = False           
    else:
        toEnd = input('Press "enter" to continue, "results" or "r" for results, or "stop" or "s" to end tracker')
        toEnd = toEnd.lower()
        if (toEnd == "enter" or toEnd == ""):
            os.system('clear')
            whole_end = False
            kd_end = False
            kills_end = False
            deaths_end = False
            get_kill_cam_end = True
            in_kill_cam_end = True
            get_greatness = True
            get_wins = True 
            continue
        elif (toEnd == "results" or toEnd == "r"):
            os.system('clear')
            print(current_score(game_stat_active, players))
            continue
        elif (toEnd == "stop" or toEnd == "s"):
            os.system('clear')
            whole_end = True
            continue
        else:
            print("Please enter one of the options above.")
            

current_score(game_stat_active, players)
quit()


        
            


    
