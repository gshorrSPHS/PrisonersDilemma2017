####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

import numpy
from numpy import random

team_name = '_Gol_den_' # Only 10 chars displayed.
strategy_name = 'Random'
strategy_description = 'Each set of rounds has a different percent chance of a collude'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    # Colllude in the first 3 rounds, betray the rest
    if len(my_history) < 3:
        if random.uniform() < 0.5:
            return 'c'
        else:
            return 'b'
    elif len(my_history) < 8:
        if random.uniform() < 0.9:
            return 'b'
        else:
            return 'c'
    elif len(my_history) < 13:
        if random.uniform() < 0.6:
            return 'c'
        else:
            return 'b'
    elif len(my_history) < 20:
        if random.uniform() <0.2:
            return 'c'
        else: 
            return 'b'
    elif len(my_history) < 25:
        if random.uniform() < 0.7:
            return 'b'
        else:
            return 'c'
    elif len(my_history) < 33:
        if random.uniform() <0.9:
            return 'c'
        else:
            return 'b'
    elif len(my_history) < 35:
        return 'b'
    elif len(my_history) < 40:
        if random.uniform() <0.5:
            return 'c'
        else:
            return 'b'
    elif len(my_history) < 50:
        if random.uniform() < 0.6:
            return 'c'
        else:
            return 'b'
    elif len(my_history) < 56:
        if random. uniform() < 0.7:
            return 'b'
        else:
            return 'c'
    elif len(my_history) < 60:
        if random.uniform() <0.4:
            return 'c'
        else:
            return 'b'
    elif len(my_history) < 63:
        if random.uniform() <0.9:
            return 'c'
        else:
            return 'b'
    elif len(my_history) < 68:
        if random.uniform() <0.5:
            return 'c'
        else:
            return 'b'
    elif len(my_history) < 72:
        if random.uniform() < 0.2:
            return 'c'
        else:
            return 'b'
    elif len(my_history) < 78:
        if random.uniform() < 0.1:
            return 'b'
        else:
            return 'c'
    elif len(my_history) < 83:
        if random.uniform() < 0.8:
            return 'c'
        else:
            return 'b'
    elif len(my_history) < 87:
        if random.uniform() < 0.7:
            return 'b'
        else: 
            return 'c'
    elif len(my_history) < 90:
        if random.uniform() < 0.9:
            return 'c'
        else:
            return 'b'
    elif len(my_history) < 94:
        if random.uniform() < 0.6:
            return 'c'
        else:
            return 'b'
    elif len(my_history) < 97:
        if random.uniform() < 0.4:
            return 'c'
        else:
            return 'b'
    elif len(my_history) <101:
        if random.uniform() < 0.2:
            return 'c'
        else:
            return 'b'
    elif random.uniform() < 0.5:
        return 'c'
    else:
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
    if test_move(my_history='cbc',
              their_history='bcb', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbbbbb',
              their_history='cccccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             
