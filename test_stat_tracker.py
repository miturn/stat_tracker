#!/usr/bin/python3
# Before switching to all info in dictionary
import random 
from functions import build_stat
from functions import kd_function
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
num_players = []
whole_end = False
kd_end = True

#game_stat_active = {"kd" : [1,2,3], "kills" : [1,2,3], "deaths" : [1,2,3], "get_kill_cam" : [1,2,3], 
#             "in_kill_cam" : [1,2,3], "greatness" : [1,2,3]}
#game_stat = [False] * 8


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
        num_players = [None] * 2
        num_players[0] = input("first player: ")
        num_players[1] = input("second player: ")
        game_stat_active['kd'] = [1,2,3]
        game_stat_active['get_kill_cam'] = [1,2,3]
        game_stat_active['in_kill_cam'] = [1,2,3]
        game_stat_active['greatness'] = [1,2,3]
        start = True
    if (selection == 2):
        game_stat_active['kd'] = [1,2,3]
    if (selection == 3):
        game_stat_active['kills'] = [1,2,3]
    if (selection == 4):      
        game_stat_active['deaths'] = [1,2,3]
    if (selection == 5): 
        game_stat_active['get_kill_cam'] = [1,2,3]
    if (selection == 6): 
        game_stat_active['in_kill_cam'] = [1,2,3]
    if (selection == 7): 
        game_stat_active['greatness'] = [1,2,3]
    if (selection == 8):
        start = True  
i = 0
while (i != 10):
    print("Press Enter if no more players.")
    enter_name = input("player {} name: ".format(i))
    if (enter_name == ""):
        break 
    else:
        num_players.append(enter_name)
        globals()["player"+str(i)] = game_stat_active.copy()#creates stat_active dict for each player 
        i += 1                                                 
        
 # loop through dictionary to input data and do calculations..

print("enter the stats")
while (whole_end == False):
    if ("kd" in game_stat_active):
        while (kd_end == True):
            kd_or_kd = input("Do you want to enter 1. kills & deaths or 2.")
            kd_end = False
        if (kd_or_kd == 1):
            for i in len(num_players - 1):
                print("Enter kill and death for each player")
                player+str(i)["kd"][1] = input("kills: ")
 #https://www.geeksforgeeks.org/python-nested-dictionary/ ?dict in dict?                
            
    


#kd_function(len(num_players),game_stat_active{"kd":[2]} , game_stat_active{"kd":[3]})

quit()

    
    


# loop to enter the stats 


        
            


    