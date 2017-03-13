team_name = 'Bananas'
strategy_name = 'Purple Banana strategy'
strategy_description = 'Classified'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''
    count = 0
    for letter in their_history:
        if letter == "b":
            count += 1
      
    float(count)/len(their_history)       
         
    if count > 40:
        return 'b'
        
    if len(my_history) < 5:
        return 'c'
    if 25< len(my_history) < 40:
        return 'b'
    if 65< len(my_history) < 80:
        return 'c'
    if 100< len(my_history) < 114:
        return 'c'
    else:
        return 'b'
        
    if len(their_history) % 2 == 'b':
        return 'b'
    if 'bcbcbcbcbcbcb' in their_history:
        return 'c'
    if 'cbcbcbcbcbcc' in their_history:
        return 'c'
    if 'bbbbbb' in their_history:
        return 'b'
    if 'cccccc' in their_history:
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
     
    if test_move(my_history='c',
              their_history='b', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Test passed'
     
    test_move(my_history='bbbbbb',
              their_history='cccccc', 
              my_score=0, 
              their_score=0,
              result='b')
