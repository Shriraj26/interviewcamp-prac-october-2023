def powerOfNumber(num, power):

    # Handle the case where number is 0 and power is negative
    if num == 0 and power <= 0:
        return None

    # Calculate power for positive  number and power
    result = positivePower(abs(num), abs(power))    

    # handle the negative power
    if power < 0:
        result = 1 / result

    # Handle negative number and odd power
    if num < 0 and power % 2 != 0:
        result = -result

    return result


def positivePower(num, pow):

    
    # BAse case 1
    if pow == 0:
        return 1

    # BAse case 2
    if pow == 1:
        return num
    
    halfPower = positivePower(num, pow // 2)
    if pow % 2 == 0:
        return halfPower * halfPower
    else:
        return num * halfPower * halfPower
    

print(powerOfNumber(2, -3))