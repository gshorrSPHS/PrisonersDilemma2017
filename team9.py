team_name = 'NUMPY' # Only 10 chars displayed.
strategy_name = 'Numpy 2.0'
strategy_description = 'Our strategy is none of your business, but if you must know, IDK. It does random stuff every 10 rounds.'


    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
from numpy import random

def move(my_history, their_history, my_score, their_score):
    choices = "bc"
    if random.uniform() < 0.1:
        return random.choice(choices)
    if 1 <= len(my_history) + 1 and len(my_history) + 1 <= 10: #rounds 1-10 will be random
        return random.choice("b","c")
    elif 11 <= len(my_history) + 1 and len(my_history) + 1 <= 20: #if they alternate, return b
        if "cbcb" in their_history:
            return "b"
        elif "bbbbb" in their_history:
            return "b"
        elif "ccccc" in their_history:
            return "c"
        else:
            return "c"
    elif 21 <= len(my_history) + 1 and len(my_history) + 1 <= 30: #If they betray > 50%, betray
        countB = 0
        for letter in their_history:
	   if letter == "b":
	       countB += 1
	if float(countB)/len(their_history) > 0.5:
	    return "b"
	else:
	    return "c"
    elif 31 <= len(my_history) + 1 and len(my_history) + 1 <= 40: #if they betray, random. else, betray
        if their_history[len(their_history)] == "b":
            return random.choice(choices)
        else:
            return "b"
    elif 41 <= len(my_history) + 1 and len(my_history) + 1 <= 50: #If collude > 50%, betray
        countC = 0
        for letter in their_history:
	   if letter == "c":
	       countC += 1
	if float(countC)/len(their_history) > 0.5:
	    return "b"
	else:
	    return "c"
    elif 51 <= len(my_history) + 1 and len(my_history) + 1 <= 60: #if "bbb" in their_history, betray
        if "bbb" in their_history:
            return "b"
        else:
            return "c"
    elif 61 <= len(my_history) + 1 and len(my_history) + 1 <= 70: #if "ccc" in their_history, betray
        if "ccc" in their_history:
            return "b"
        else:
            return "c"
    elif 71 <= len(my_history) + 1 and len(my_history) + 1 <= 80: #return their thingy from 5 rounds back
        return their_history[-4]
    elif 81 <= len(my_history) + 1 and len(my_history) + 1 <= 90: #alternate, start on c
        if (len(my_history) + 1) % 2 == 0:
            return "b"
        else:
            return "c"
    elif 91 <= len(my_history) + 1 and len(my_history) + 1 <= 100: #always betray
        return "b"
    elif 101 <= len(my_history) + 1 and len(my_history) + 1 <= 110: #"bcbbcccbbb"
        if len(my_history) + 1 == 101:
            return "b"
        elif len(my_history) + 1 == 102:
            return "c"
        elif len(my_history) + 1 == 103:
            return "b"
        elif len(my_history) + 1 == 104:
            return "b"
        elif len(my_history) + 1 == 105:
            return "c"
        elif len(my_history) + 1 == 106:
            return "c"
        elif len(my_history) + 1 == 107:
            return "c"
        elif len(my_history) + 1 == 108:
            return "b"
        elif len(my_history) + 1 == 109:
            return "b"
        elif len(my_history) + 1 == 110:
            return "b"
        else:
            print "Error in 101-110 range."
            
    elif 111 <= len(my_history) + 1 and len(my_history) + 1 <= 120: #if round number is divisible by 3, do c
        if (len(my_history) + 1) % 3 == 0:
            return "b"
        else:
            return "c"
    elif 121 <= len(my_history) + 1 and len(my_history) + 1 <= 130: #bccbbccbbc
        if len(my_history) + 1 == 121:
            return "b"
        elif len(my_history) + 1 == 122:
            return "c"
        elif len(my_history) + 1 == 123:
            return "c"
        elif len(my_history) + 1 == 124:
            return "b"
        elif len(my_history) + 1 == 125:
            return "b"
        elif len(my_history) + 1 == 126:
            return "c"
        elif len(my_history) + 1 == 127:
            return "c"
        elif len(my_history) + 1 == 128:
            return "b"
        elif len(my_history) + 1 == 129:
            return "b"
        elif len(my_history) + 1 == 130:
            return "c"
        else:
            print "Error in 121-130 range."
    elif 131 <= len(my_history) + 1 and len(my_history) + 1 <= 140: #bbcbcbbbbc
        if len(my_history) + 1 == 131:
            return "b"
        elif len(my_history) + 1 == 132:
            return "b"
        elif len(my_history) + 1 == 133:
            return "c"
        elif len(my_history) + 1 == 134:
            return "b"
        elif len(my_history) + 1 == 135:
            return "c"
        elif len(my_history) + 1 == 136:
            return "b"
        elif len(my_history) + 1 == 137:
            return "b"
        elif len(my_history) + 1 == 138:
            return "b"
        elif len(my_history) + 1 == 139:
            return "b"
        elif len(my_history) + 1 == 140:
            return "c"
        else:
            print "Error in 131-140 range."
    elif 141 <= len(my_history) + 1 and len(my_history) + 1 <= 150: #alternate, start on b
        if (len(my_history) + 1) % 2 == 0:
            return "c"
        else:
            return "b"
    elif 151 <= len(my_history) + 1 and len(my_history) + 1 <= 160: #bccbbbcccc
        if len(my_history) + 1 == 151:
            return "b"
        elif len(my_history) + 1 == 152:
            return "c"
        elif len(my_history) + 1 == 153:
            return "c"
        elif len(my_history) + 1 == 154:
            return "b"
        elif len(my_history) + 1 == 155:
            return "b"
        elif len(my_history) + 1 == 156:
            return "b"
        elif len(my_history) + 1 == 157:
            return "c"
        elif len(my_history) + 1 == 158:
            return "c"
        elif len(my_history) + 1 == 159:
            return "c"
        elif len(my_history) + 1 == 160:
            return "c" 
        else:
            print "Error in 151-160 range."
    elif 161 <= len(my_history) + 1 and len(my_history) + 1 <= 170: #cbbccbbccb
        if len(my_history) + 1 == 161:
            return "c"
        elif len(my_history) + 1 == 162:
            return "b"
        elif len(my_history) + 1 == 163:
            return "b"
        elif len(my_history) + 1 == 164:
            return "c"
        elif len(my_history) + 1 == 165:
            return "c"
        elif len(my_history) + 1 == 166:
            return "b"
        elif len(my_history) + 1 == 167:
            return "b"
        elif len(my_history) + 1 == 168:
            return "c"
        elif len(my_history) + 1 == 169:
            return "c"
        elif len(my_history) + 1 == 170:
            return "b"
        else:
            print "Error in 161-170 range."
    elif 171 <= len(my_history) + 1 and len(my_history) + 1 <= 180: #cbbcccbbbb
        if len(my_history) + 1 == 171:
            return "c"
        elif len(my_history) + 1 == 172:
            return "b"
        elif len(my_history) + 1 == 173:
            return "b"
        elif len(my_history) + 1 == 174:
            return "c"
        elif len(my_history) + 1 == 175:
            return "c"
        elif len(my_history) + 1 == 176:
            return "c"
        elif len(my_history) + 1 == 177:
            return "b"
        elif len(my_history) + 1 == 178:
            return "b"
        elif len(my_history) + 1 == 179:
            return "b"
        elif len(my_history) + 1 == 180:
            return "b" 
        else:
            print "Error in 171-180 range."
    elif 181 <= len(my_history) + 1 and len(my_history) + 1 <= 190: #if round number is divisible by 3, do b
        if (len(my_history) + 1) % 3 == 0:
            return "c"
        else:
            return "b"
    elif 191 <= len(my_history) + 1 and len(my_history) + 1 <= 200: #always betray
        return "b"
    else:
        print "Error. Round number does not match programmed ranges."

    
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
    if test_move(my_history='bbb',
              their_history='ccc', 
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
