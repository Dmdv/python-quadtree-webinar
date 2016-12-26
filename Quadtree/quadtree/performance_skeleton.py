import random
import timeit

# This file shows how to use timeit to report on performance results of Python code.

def performance():
    """Demonstrate execution performance."""
    n = 16
    numTrials = 20
    
    # print header
    print ("n", "GCD_sub", "GCD_div")
    while n <= 4096:
        naive_gcd = mod_gcd = 0
        
        # Experiment: compare performance of two GCD variations.
        # Start with same pair of random integers in range (1000, 1000000000)
        pairs = []
        for _ in range (n):
            pairs.append((random.randint(1000, 1000000000), random.randint(1000,1000000000)))
            
        # setup contains code that executes BEFORE the designated code. Use this to
        # construct values of initial variables. Don't forget the imports clauses.
        setup= '''
pairs = []'''
        for pair in pairs:
            setup = setup + "\npairs.append((%d,%d))" % (pair[0], pair[1])
        
        # Euclid gcd using subtraction method
        naive_gcd += min(timeit.Timer('''
checksum = 0
for pair in pairs:
    a = pair[0]
    b = pair[1]
    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    checksum += a
#print (checksum) # uncomment this line to print total to validate results (not needed for timing)
'''
                                        , setup=setup).repeat(5,numTrials))
         
        # GCD by division  
        mod_gcd += min(timeit.Timer('''
checksum = 0
for pair in pairs:
    a = pair[0]
    b = pair[1]
    while b:
        a, b = b, a % b
    checksum += a
#print (checksum) # uncomment this line to print total to validate results (not needed for timing)
'''
                                        , setup=setup).repeat(5,numTrials))
            
        print ("%d %5.4f %5.4f" % (n, 1000*naive_gcd/numTrials, 1000*mod_gcd/numTrials))

        # advance to next problem size
        n *= 2
        
if __name__ == '__main__':
    performance()
        
# Sample Run:
"""
n GCD_sub GCD_div
16 0.2411 0.0508
32 0.6614 0.0993
64 6.7517 0.2080
128 2.6772 0.4056
256 7.4513 0.8343
512 13.3395 1.6672
1024 26.7778 3.3044
2048 72.3874 8.0088
4096 190.7916 16.5209
"""