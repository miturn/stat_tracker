# functions for stat_tracker.py

# add some trash talking if ratio gets too great


def build_stat():
    if kd is True:
        game_stat.append(kd)
        
    
def k_d_function(kills, deaths): #kill divided by death
    temp_kd = float(kills / deaths)
    return temp_kd
    
def fselection(current): #changes bool for choosing what to track
    if (current == True):    
        return False
    else: 
        return True


def current_score(gameDictionary, player_list):
    print("Current score: \n")
    current_end = False
    j = 0 
    while (current_end == False):
        if ('kd' in gameDictionary["player"+str(j)]):
            k = 0
            kdCurrentWinner = 0
            tempPlayervar = -1
            for i in player_list:
                print("{}'s kd: ".format(i), end = "")
                print(gameDictionary["player"+str(k)]['kd'][2])
                tempKdCurrentWinner = gameDictionary["player"+str(k)]['kd'][2]
                if (tempKdCurrentWinner > kdCurrentWinner):
                    kdCurrentWinner = tempKdCurrentWinner
                    tempPlayervar = k 
                k += 1
            
            print("Current winner: {}".format(gameDictionary["player"+str(tempPlayervar)]['name']))        
        if ('kills' in gameDictionary["player"+str(j)]):
            k = 0
            killsCurrentWinner = 0
            tempPlayervar = 0
            for i in player_list:
                print("{}'s kills: ".format(i), end = "")
                print(gameDictionary["player"+str(k)]['kills'][0])
                tempKillsCurrentWinner = gameDictionary["player"+str(k)]['kills'][0]
                if (tempKillsCurrentWinner > killsCurrentWinner):
                    killsCurrentWinner = tempKillsCurrentWinner
                    tempPlayervar = k 
                k += 1
            print("Current winner: {}".format(gameDictionary["player"+str(tempPlayervar)]['name']))
        if ('deaths' in gameDictionary["player"+str(j)]):
            k = 0
            deathsCurrentWinner = 10000
            tempPlayervar = 0
            for i in player_list:
                print("{}'s deaths: ".format(i), end = "")
                print(gameDictionary["player"+str(k)]['deaths'][0])
                tempDeathsCurrentWinner = gameDictionary["player"+str(k)]['deaths'][0]
                if (tempDeathsCurrentWinner < deathsCurrentWinner):
                    deathsCurrentWinner = tempDeathsCurrentWinner
                    tempPlayervar = k 
                k += 1
            print("Current winner: {}".format(gameDictionary["player"+str(tempPlayervar)]['name']))
        if ('get_kill_cam' in gameDictionary["player"+str(j)]):
            k = 0
            getKillCamCurrentWinner = 0
            tempPlayervar = 0
            for i in player_list:
                print("{}'s kill cam: ".format(i), end = "")
                print(gameDictionary["player"+str(k)]['get_kill_cam'][0])
                tempDeathsCurrentWinner = gameDictionary["player"+str(k)]['get_kill_cam'][0]
                if (tempDeathsCurrentWinner > getKillCamCurrentWinner):
                    getKillCamCurrentWinner = tempDeathsCurrentWinner
                    tempPlayervar = k 
                k += 1
            print("Current winner: {}".format(gameDictionary["player"+str(tempPlayervar)]['name']))
        if ('in_kill_cam' in gameDictionary["player"+str(j)]):
            k = 0
            inKillCamCurrentWinner = 10000
            tempPlayervar = 0
            for i in player_list:
                print("{}'s in kill cam: ".format(i), end = "")
                print(gameDictionary["player"+str(k)]['in_kill_cam'][0])
                tempInKillCamCurrentWinner = gameDictionary["player"+str(k)]['in_kill_cam'][0]
                if (tempInKillCamCurrentWinner < inKillCamCurrentWinner):
                    inKillCamCurrentWinner = tempInKillCamCurrentWinner
                    tempPlayervar = k 
                k += 1
            print("Current winner: {}".format(gameDictionary["player"+str(tempPlayervar)]['name']))    
        if ('greatness' in gameDictionary["player"+str(j)]):
            k = 0
            greatnessCurrentWinner = 0
            tempPlayervar = 0
            for i in player_list:
                print("{}'s kill cam: ".format(i), end = "")
                print(gameDictionary["player"+str(k)]['greatness'][0])
                tempgreatnessCurrentWinner = gameDictionary["player"+str(k)]['greatness'][0]
                if (tempgreatnessCurrentWinner > greatnessCurrentWinner):
                    greatnessCurrentWinner = tempgreatnessCurrentWinner
                    tempPlayervar = k 
                k += 1
            print("Current winner: {}".format(gameDictionary["player"+str(tempPlayervar)]['name']))
        if ('wins' in gameDictionary["player"+str(j)]):
            k = 0
            winsCurrentWinner = 0
            tempPlayervar = 0
            for i in player_list:
                print("{}'s kill cam: ".format(i), end = "")
                print(gameDictionary["player"+str(k)]['wins'][0])
                tempwinsCurrentWinner = gameDictionary["player"+str(k)]['wins'][0]
                if (tempwinsCurrentWinner > winsCurrentWinner):
                    winsCurrentWinner = tempwinsCurrentWinner
                    tempPlayervar = k 
                k += 1
            print("Current winner: {}".format(gameDictionary["player"+str(tempPlayervar)]['name']))
        current_end = True
    return (gameDictionary, player_list)

def addTo(currentScore, addedScore):
    if (currentScore == None):
        currentScore = 0
    currentScore = currentScore + addedScore
    return (currentScore)
def averageSolution (currentAverage, addAverage):
    currentAverage = (currentAverage + addAverage)/2
    return(currentAverage)

def isItTie(gameDictionary, player_list):
    return