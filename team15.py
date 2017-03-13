team_name = 'Tri Again' 
strategy_name = 'Trifecta'
strategy_description = 'Attempt to identify patterns of three c\'s or b\'s in a row. If no pattern is identified, program returns a random result'
    
def move(my_history, their_history, my_score, their_score):
    options = ['b','c']
    if len(their_history) > 2: #Stores 
        sequence = their_history[-3:]
    if len(my_history) == 0:
        return 'b'
        my_history += ['b']
    if len(my_history) == 1:
        return 'c'
        my_history += ['c']
    if len(my_history) == 2:
        return 'c'
        my_history += ['c']
    if len(my_history) >= 3 :
        if sequence == 'bbb':
            return 'b'
            my_history += ['b']            
        elif sequence == 'ccc':
            return 'c'
            my_history += ['c']
        else:
            return random.choice(options)  
