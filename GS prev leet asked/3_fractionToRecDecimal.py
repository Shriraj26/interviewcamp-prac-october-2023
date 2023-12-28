'''
TC - 
SC - 
'''
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Edge cases - if denominator is 0 then return empty string
        if denominator == 0:
            return ""
        if numerator == 0:
            return "0"

        # Init result and the signs
        result = ""
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            result += "-"
        numerator, denominator = abs(numerator), abs(denominator)

        # Store the integer part
        result += str(numerator // denominator)

        # if no fraction part, return result
        if numerator % denominator == 0:
            return result
        
        result += "."
        # init the dictionary and reminder
        remDict = {}
        rem = numerator % denominator

        while rem != 0 and rem not in remDict:
            # store the index at result at this dict
            remDict[rem] = len(result)
            rem = rem * 10
            # store the number at that index
            result += str(rem // denominator)
            rem = rem % denominator

        # Check if there is repeating part
        if rem in remDict:
            indexToInsertBrackets = remDict[rem]
            result = result[:indexToInsertBrackets] + "(" + result[indexToInsertBrackets: ] + ")"

        return result

