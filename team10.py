# -*- coding: utf-8 -*-
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a strings
#     move: A function that returns 'c' or 'b'
####
import random

team_name = 'The Zone' # Only 10 chars displayed.
strategy_name = 'PLAN Anaikin'
strategy_description = 'CLASSIFIED'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    
    if len(my_history) < 10 or len(their_history) < 10:
        return random.choice('bc')
        
    count = 0   
    if len(their_history) >= 10:
         for betray in their_history: 
            if betray == 'b':
                count += 1
    
    percent = float(count) / len(their_history)
    if percent != 0.5:
        return 'b'
    else:
       return 'c'
    
    if their_history[-1] == 'b':
        return 'b'
        
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='bbbbbbbbbbbb',
              their_history='bbbbbbcccccc', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Test passed'
     

    
    
    
    
    
    
