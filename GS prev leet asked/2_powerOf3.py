'''
TC - O(log3 N) as N gets divided by 3 till it reaches 1 or 0
   - O(1) for the log approach
SC - O(1) for both
'''
import math
def isPowerOfThree(n: int) -> bool:
    
    while n > 0:
        if n == 1:
            return True
        n = n / 3
        
    return False

    # if n <= 0:
    #     return False
    
    # log = math.log10(n) / math.log10(3)
    # return int(log) == log

print(isPowerOfThree(1000))
print(isPowerOfThree(1))
print(isPowerOfThree(120))