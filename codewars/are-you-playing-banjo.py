# https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python

def are_you_playing_banjo(name):
    banjo_player = {"R", "r"}
    
    if name[0] in banjo_player:
        return name + " plays banjo"
    
    return name + " does not play banjo"
