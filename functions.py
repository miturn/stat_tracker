# functions for stat_tracker.py

# add some trash talking if ratio gets too great


def build_stat():
    if kd is True:
        game_stat.append(kd)
        
    
def k_d_function(kills, deaths): 
    temp_kd = float(kills / deaths)
    return temp_kd
    