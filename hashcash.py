import string
import time
import random
import hashlib

example_challenge = '9Kzs52jsfxjGJ54Sfjz5gZ1IIs'

def generation(challenge=example_challenge,size=25):
    answer = ''.join(random.choice(string.ascii_lowercase +
                                   string.ascii_uppercase +
                                   string.digits) for x in range(size))


    attempt = challenge+answer

    return attempt, answer
    
shaHash = hashlib.sha256()


def testAttempt():
    Found = False
    start = time.time()
    while Found == False:
        attempt, answer = generation()
        shaHash.update(attempt)
        solution = shaHash.hexdigest()
        if solution.startswith('0000'):
            timeTook = time.time() - start
            print solution
            print 'time took:',timeTook
            Found = True
    print answer

testAttempt()


