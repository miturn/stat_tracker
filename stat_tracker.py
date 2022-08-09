#!/usr/bin/python3
# should I set up a virtual environment for this project?
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
start = False
kd = False
kills = False
deaths = False
get_kill_cam = False
on_kill_cam = False
greatness = False
game_stat_active = {"kd" : [1,2,3], "kills" : [1,2,3], "deaths" : [1,2,3], "get_kill_cam" : [1,2,3], 
             "in_kill_cam" : [1,2,3], "greatness" : [1,2,3]}
game_stat = [False] * 8


# functions ******put function in different file so I can call it anywhere
#def build_stat():

print("********** Trash talking stat tracker **********")

# main menu
while (start == False):
    print("Select as many as you want. Press s to start.")
    print("1. Standard tracking two players, k/d, on kill cam, you are the kill cam, *You win and kill other player on kill cam")
    print("2. How many players")
    print("3. k/d")
    print("4. kills")
    print("5. deaths")
    print("6. you are the kill cam")
    print("7. on the kill cam")
    print("8. achieve greatness (win match and kill other player on kill your kill cam")
    print("9. Finished selecting")#make it except letters
    try:
        selection = int(input("select one that applies: "))
    except:
        start = True
       
    # main menu inputs, change False to True in List 
    if (selection == 1): # game_stat[0]
        num_players = [None] * 2
        num_players[0] = input("first player: ")
        num_players[1] = input("second player: ")
        kd = True
        get_kill_cam = True
        on_kill_cam = True
        greatness = True
        game_stat[2] == True
        game_stat[5] == True
        game_stat[6] == True
        game_stat[7] == True
        start = True
    if (selection == 2): # game_stat[1]
        try:
            num_player = int(input("How many players? "))
        except:
            print("last chance! enter a number")
            num_player = int(input("How many players? "))
        num_players = [None] * num_player
        for i in range(num_player):
            num_players[i] = input("player {} name: ".format(i))
        game_stat[1] = True
    if (selection == 3): # game_stat[2]
        kd = True
        game_stat[2] = True
    if (selection == 4): # game_stat[3]
        kills = True
        game_stat[3] = True
    if (selection == 5): # game_stat[4]       
        deaths = True
        game_stat[4] = True
        print("5 was selected True")
    if (selection == 6): # game_stat[5]
        get_kill_cam = True
        game_stat[5] = True
    if (selection == 7): # game_stat[6]
        on_kill_cam = True
        game_stat[6] = True
    if (selection == 8): # game_stat[7]
        greatness = True
        game_stat[7] = True
    if (selection == 9): # game_stat[8]
        start = True            
 #start of standard option 2
 #Dictionary to hold variables that are true or False, loop through, if True call function to do the math
  
print("Ready to enter info. press enter if zero")
print(game_stat)

# loop through list, if True call fuction
l = 0
for l < 9:
    if game_stat[l] == False:
        game_stat_active{}
# keep track of total entries
# keep track of totals

kd_function(len(num_players),game_stat_active{"kd":[2]} , game_stat_active{"kd":[3]})

quit()

    
    


# loop to enter the stats 


        
            


    