#!/usr/bin/python3
# Before switching to all info in dictionary
import random
import sys
# from tkinter import N 
from functions import build_stat
from functions import k_d_function
# Create stock templetes
# how many players
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
kd_end = True
skip = False

#game_stat_active = {"kd" : [1,2,3,4], "kills" : [1,2,3,4], "deaths" : [1,2,3,4], "get_kill_cam" : [1,2,3,4], 
#             "in_kill_cam" : [1,2,3,4], "greatness" : [1,2,3,4]}
game_stat = [False] * 8 # game_stat = [0kd, 1kills, 2deaths, 3you are the kill cam, 4in the kill cam, 5greatness]


# functions ******put function in different file so I can call it anywhere
#def build_stat():

print("********** Trash talking stat tracker **********")

# main menu
while (start == False):
    print("Select as many as you want. Press s to start.")
    print("1. Standard tracking two players, k/d, on kill cam, you are the kill cam, *You win and kill other player on kill cam")
    print("2. k/d")
    print("3. kills")
    print("4. deaths")
    print("5. you are the kill cam")
    print("6. in the kill cam")
    print("7. achieve greatness (win match and kill other player on kill your kill cam")
    print("8. Finished selecting")#make it except letters
    try:
        selection = int(input("select one that applies: "))
    except:
        start = True
       
    # main menu inputs, change False to True in List 
    if (selection == 1): # game_stat[0]
        players = [None] * 2
        players[0] = input("first player: ")
        players[1] = input("second player: ")
        game_stat_active['player0'] = players[0]
        game_stat_active['player1'] = players[1]
        game_stat_active.update({"player0" : {"name" : players[0]}})
        game_stat_active.update({"player1" : {"name" : players[1]}})
        game_stat_active["player0"]['kd'] = [1, 2, 3]
        game_stat_active["player0"]['get_kill_cam'] = [1, 2, 3, 4]
        game_stat_active["player0"]['in_kill_cam'] = [1, 2, 3, 4]
        game_stat_active["player0"]['greatness'] = [1, 2, 3, 4]
        game_stat_active["player1"]['kd'] = [1, 2, 3, 4]
        game_stat_active["player1"]['get_kill_cam'] = [1, 2, 3, 4]
        game_stat_active["player1"]['in_kill_cam'] = [1, 2, 3, 4]
        game_stat_active["player1"]['greatness'] = [1, 2, 3, 4]
        start = True
        skip = True
    if (selection == 2):
        game_stat[0] = True
    if (selection == 3):
        game_stat[1] = True
    if (selection == 4):      
        game_stat[2] = True
    if (selection == 5): 
        game_stat[3] = True
    if (selection == 6): 
        game_stat[4] = True
    if (selection == 7): 
        game_stat[5] = True
    if (selection == 8):
        start = True  
i = 0
while (i != 10 and skip != True):
    print("Press Enter if no more players.")
    enter_name = input("player {} name: ".format(i))
    if (enter_name == ""):
        break 
    else:
        players.append(enter_name)
        num_players = num_players + 1
        game_stat_active.update({"player"+str(i) : {"name" : enter_name}}) #, "kd" : [1,2,3,4], "kills" : [1,2,3,4], "deaths" : [1,2,3,4], "get_kill_cam" : [1,2,3,4], 
             #"in_kill_cam" : [1,2,3,4], "greatness" : [1,2,3,4]}})
        if (game_stat[0] == True):
            game_stat_active["player"+str(i)]['kd'] = [1, 2, 3]
        if (game_stat[1] == True):
            game_stat_active["player"+str(i)]["kills"] = [1, 2, 3, 4]
        if (game_stat[2] == True):      
            game_stat_active["player"+str(i)]["deaths"] = [1, 2, 3, 4]
        if (game_stat[3] == True): 
            game_stat_active["player"+str(i)]["get_kill_cam"] = [1, 2, 3, 4]
        if (game_stat[4] == True): 
            game_stat_active["player"+str(i)]["in_kill_cam"] = [1, 2, 3, 4]
        if (game_stat[5] == True): 
            game_stat_active["player"+str(i)]["greatness"] = [1, 2, 3, 4]
        if (selection == 8):
            start = True  
        i += 1


print(game_stat_active)    
 # loop through dictionary to input data and do calculations..

print("enter the stats\n") #Main loop to enter all the stats
j = 0
while (whole_end == False):
    if ("kd" in game_stat_active["player"+str(j)]):
        while (kd_end == True):
            kd_or_kd = int(input("Do you want to enter 1. kills & deaths or 2. k/d ratio\n"))
            kd_end = False
        if (kd_or_kd == 1):
            k = 0
            for i in players:
                print("Enter kills then deaths")
                kills = int(input("kills: "))
                deaths = int(input("deaths: "))
                game_stat_active["player"+str(k)]['kd':[3]] = k_d_function(kills, deaths) #********************
                print(game_stat_active["player"+str(k)]['kd':3])
                k += 1
                
print(game_stat_active)
                 
                
                #temp_kd = input("Enter kill and death for ", i,":" )
            
 #https://www.geeksforgeeks.org/python-nested-dictionary/ ?dict in dict?                
            



#kd_function(len(players),game_stat_active{"kd":[2]} , game_stat_active{"kd":[3]})

quit()

    
    


# loop to enter the stats 


        
            


    