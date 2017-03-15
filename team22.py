import random

####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Ima G. Nary' # Only 10 chars displayed.
strategy_name = 'Smoke Bomb'
strategy_description = 'Start by playing bad, then poof, they lose'
 


def move(my_history, their_history, my_score, their_score):
    if len(my_history) < 5:
        return random.choice('cb')
    
    else:
        counter = 0
        total = 0    
        for i in their_history:
            if i == 'b':
                counter += 1
            total += 1
        good_bad = check_score(my_score, their_score)
        if float(counter)/total <= .49:
            if good_bad[0] > good_bad[1]:
                return 'c'
            else:
                return 'b'
        else:
            if good_bad[0] <= good_bad[1]:
                return 'b'
        
def check_score(my_score, their_score):
    good = 0
    bad = 0
    score_diff = my_score - their_score
    if score_diff < 0:
        bad += 1
    elif score_diff == 0:
        bad += 1
    else:
        good += 1
    return [good,bad]
        
def count(their_history):
    counter = 0
    total = 0    
    for i in their_history:
        if i == 'b':
            counter += 1
        total += 1
    return float(counter)/total
