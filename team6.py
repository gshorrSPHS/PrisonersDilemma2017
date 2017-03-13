  ####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The Senses' # Only 10 chars displayed.
strategy_name = "Larry's super secret strategy"
strategy_description = 'Collude for the first 3 turns no matter what, collude evry time until they beray, thn collude one more time, then betray them, but if they have betrayed 3 times in a row before, then betray them immediately. And then betray them everytime after that, then collude once, and betray them again, and then collude every time after that, and repeat'
    
def move(my_history, their_history, my_score, their_score):
  # Arguments accepted: my_history, their_history are strings.
    #my_score, their_score are ints.
    
   # Make my move.
   # Returns 'c' or 'b'. 
    

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    #######ACTUAL CODE########
    
    
    if len(my_history) == 0 or len(my_history) == 1 or len(my_history) == 2 or len(my_history) == 3:
        return 'c'
    else:
        if 'b' in their_history[-2]:
            return 'b'
        elif 'b' in their_history[-1] and 'bbb' in their_history:
            return 'b'
        elif 'c' in their_history[-1] and 'b' in their_history[-2]:
            return 'b'
        else:
            return 'c'
            
    ########END CODE##########     
            
        

    
#def test_move(my_history, their_history, my_score, their_score, result):
  #  '''calls move(my_history, their_history, my_score, their_score)
   # from this module. Prints error if return value != result.
   # Returns True or False, depending on whether result was as expected.
   # '''
   # real_result = move(my_history, their_history, my_score, their_score)
   # if real_result == result:
  #      return True
  #  else:
   #     print ("it returned "  + "'"+ real_result + "'" + " and should have returned" + "'" + result + "'")
  #      return False

#if __name__ == '__main__':
    
   # if test_move(my_history='c', their_history='b', my_score='0', their_score='0',result='c'):
       # print "Passed"

     
    # Test 1: Betray on first move.
   # if test_move(my_history='',
    #          their_history='', 
     #         my_score=0,
    #          their_score=0,
    #          result='b'):
     #    print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
  #  test_move(my_history='bbbbbb',
          #    their_history='cccccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
            #  my_score=0, 
           #   their_score=0,
             # result='b') 
  
