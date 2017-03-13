# Cole C Daniel L
team_name = 'lel' # Only 10 chars displayed.
strategy_name = 'monkey see monkey do'
strategy_description = 'starts with betray then does what opponent did last turn'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
        return 'b'
    else:
        return their_history[-1]
