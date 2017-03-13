####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'print team' # Only 10 chars displayed.
strategy_name = 'Tit for Tat and Pavlov'
strategy_description = 'I would tell you our stategy description, but then I\'d have to kill you. '
    
def move(my_history, their_history, my_score, their_score):
    round = len(my_history) + 1
    if round <= 5:
        return 'c'
    elif (round > 5) and (round <= 10):
        return 'b'
    elif (round >= 11 and round <= 34):
  	betrayals = 0.0
        count =0.0
        for i in their_history[0:9]:
            if i== 'b':
                betrayals += 1.0
            count +=1.0
        if (float(betrayals)/count) > .74 or (float(betrayals)/count) < .26:
            return tit_for_tat(my_history, their_history)
        else:
            return pavlov(my_history, their_history)
    elif (round >= 35 and round <= 49):
  	betrayals = 0.0
        count =0.0
        for i in their_history[10:33]:
            if i== 'b':
                betrayals += 1.0
            count +=1.0
        if (float(betrayals)/count) > .74 or (float(betrayals)/count) < .26:
            return tit_for_tat(my_history, their_history)
        else:
            return pavlov(my_history, their_history)
    elif (round >= 50 and round <= 74):
        betrayals = 0.0
        count =0.0
        for i in their_history[35:48]:
            if i == 'b':
                betrayals += 1.0
            count +=1.0
            if (float(betrayals)/count) > .74 or (float(betrayals)/count) < .26:
                return tit_for_tat(my_history, their_history)
            else:
                return pavlov(my_history, their_history)
    elif (round >= 75 and round <= 99):
        betrayals = 0.0
        count =0.0
        for i in their_history[50:73]:
            if i == 'b':
                betrayals += 1.0
            count +=1.0
            if (float(betrayals)/count) > .74 or (float(betrayals)/count) < .26:
                return tit_for_tat(my_history, their_history)
            else:
                return pavlov(my_history, their_history)
    elif (round >= 100 and round <= 124):
        betrayals = 0.0
        count =0.0
        for i in their_history[75:98]:
            if i == 'b':
                betrayals += 1.0
            count +=1.0
            if (float(betrayals)/count) > .74 or (float(betrayals)/count) < .26:
                return tit_for_tat(my_history, their_history)
            else:
                return pavlov(my_history, their_history)
    elif (round >= 125 and round <= 149):
        betrayals = 0.0
        count =0.0
        for i in their_history[100:123]:
            if i == 'b':
                betrayals += 1.0
            count +=1.0
            if (float(betrayals)/count) > .74 or (float(betrayals)/count) < .26:
                return tit_for_tat(my_history, their_history)
            else:
                return pavlov(my_history, their_history)
    elif (round >= 150 and round <= 174):
        betrayals = 0.0
        count =0.0
        for i in their_history[125:148]:
            if i == 'b':
                betrayals += 1.0
            count +=1.0
            if (float(betrayals)/count) > .74 or (float(betrayals)/count) < .26:
                return tit_for_tat(my_history, their_history)
            else:
                return pavlov(my_history, their_history)
    elif (round >= 175 and round <= 200):
        betrayals = 0.0
        count =0.0
        for i in their_history[150:173]:
            if i == 'b':
                betrayals += 1.0
            count +=1.0
            if (float(betrayals)/count) > .74 or (float(betrayals)/count) < .26:
                return tit_for_tat(my_history, their_history)
            else:
                return pavlov(my_history, their_history)
def pavlov(my_history, their_history):
        TL = their_history[-1] 
	ML = my_history[-1] 
        if TL == 'c' and ML == 'b':
            return 'b'
        elif TL == 'b' and ML == 'b':
            return 'c'
        elif TL == 'c' and ML == 'c':
            return 'c'
        else:
            return 'b' 
def tit_for_tat(my_history, their_history): 
        if their_history[-1] == 'c':
            return 'c'
        elif their_history[-1] == 'b':
            return 'b'

def test(my_history, their_history):
    return 'give me money'

    
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
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='cccccb',
              their_history='cccccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='c')             
