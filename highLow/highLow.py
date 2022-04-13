import random
from highLow_data import data
import highLow_art

def item_call(n):
    print("name:",data[n]["name"])
    print("description:",data[n]["description"])
    print("country:",data[n]["country"])
    return data[n]["follower_count"]
    
def compare(a,b,guess):
    if a>b and guess == "low":
        return True
    elif a>b and guess == "high":
        return False
    elif a<b and guess == "low":
        return False
    elif a<b and guess == "high":
        return True
    else:
        return "WRONG INPUT"
    
game_end = False
count =0
e1 = random.randint(0,49)
while not game_end:
    print(highLow_art.logo)
    e2 = random.randint(0,49)
    # making sure both entity isn't same
    if e1 == e2:
        if e1 == 0:
            e2 = 1
        else:
            e2 = 0
        
    f1 = item_call(e1)
    print(highLow_art.vs)
    f2 = item_call(e2)
    print(f1,f2)
    guess = input("high or low : ").lower()
    ans = compare(f1,f2,guess)
    if ans == False:
        game_end = True
        print("GAME OVER !!  your score is",count)
    elif ans == True:
        e1 = e2
        count +=1
    else:
        print ("________ERROR________")
        
        
    
