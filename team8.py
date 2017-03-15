####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random

team_name = 'M-K8 Dread' # Only 10 chars displayed.
strategy_name = 'Evolution'
strategy_description = 'Survival of the fittest strategies'

biases = {"":0, "bb" : 0, "bc" : -1, "cb" : 2, "cc" : 3}

beforeS = 0
lastS = 0
lastMove = ""

def evolve(score, lastScore, beforeScore, lastMove):
    lastDiff = beforeScore - lastScore
    thisDiff = lastScore - score
    print str(lastDiff) + str(thisDiff)
    if lastDiff > thisDiff:
        biases[lastMove] += 1
    else:
        biases[lastMove] -= .75
    global beforeS
    global lastS
    beforeS = lastScore
    lastS = score

def getPerc(history, let):
    tot = 0
    cou = 0
    for i in history:
        if i == let:
            cou+=1
        tot+=1
    return (1.0*cou)/tot

def getMove(my_history, their_history, my_score, their_score):
    if(getPerc(their_history,"c") > .80):
        return "cb"
    elif getPerc(their_history, "b") > .8:
        return "bb"
    else:
        if (their_history[-1] == "b"):
            if biases["bb"] > biases["bc"]:
                return "bb"
            else:
                return "bc"
        elif (their_history[-1] == "c"):
            if biases["cb"] > biases["cc"]:
                return "cb"
            else:
                return "cc"

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    global beforeS
    global lastS
    if len(my_history) == 0:
        if (random.random() < .5):
            evolve(my_score,lastS,beforeS,"")
            return 'b'
        else:
            evolve(my_score,lastS,beforeS,"")
            return 'c'
    elif (len(my_history) < 1):
        if (random.random() < .5):
            evolve(my_score,lastS,beforeS,"")
            return 'b'
        else:
            evolve(my_score,lastS,beforeS,"")
            return 'c'
    elif (len(my_history) < 2):
        if (random.random() < .5):
            lastMove = their_history[-1] + my_history[-1]
            print str(lastS) + " " + str(beforeS)
            evolve(my_score,lastS,beforeS,lastMove)
            print biases
            return 'b'
        else:
            lastMove = their_history[-1] + my_history[-1]
            print str(lastS) + " " + str(beforeS)
            evolve(my_score,lastS,beforeS,lastMove)
            print biases
            return 'c'
    else:
        print their_history[-1] + my_history[-1]
        lastMove = their_history[-1] + my_history[-1]
        print str(lastS) + " " + str(beforeS)
        evolve(my_score,lastS,beforeS,lastMove)
        print biases
        return getMove(my_history, their_history, my_score, their_score)[1]
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
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
    #if test_move(my_history='',
     #         their_history='', 
     #         my_score=0,
     #         their_score=0,
     #         result='b'):
     #    print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    #test_move(my_history='cccccc',
              their_history='bbbbbb', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              #my_score=0, 
              #their_score=0,
              #result='b')   
