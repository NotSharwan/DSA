def EuclideanGCD(a, b):
    a = abs(a)
    b = abs(b)
    if a == 0 and b == 0:
        return None
    if a == 0 and not b == 0:
        return b
    if not a == 0 and b == 0:
        return a
    if a > b:
        return EuclideanGCD(a % b, b)
    else:
        return EuclideanGCD(b % a, a)


def EuclideanLCM(a, b):
    if a == 0 and b == 0:
        return 0
    """
        This is the standard method to calculate the least common multiple.
        
        LCM(a , b) = | a * b |
                     ---------
                     GCD(a , b)  
    """
    return abs(a * b) // EuclideanGCD(a, b)


# Function call
print(EuclideanLCM(4, 8))  # 8
