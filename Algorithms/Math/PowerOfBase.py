"""
This program basically checks if the power that you passed in is composed of the base that you passed in.                                    
There are multiple ways to do this, and this is just one of them. Let's take a look at the code.
"""


def isPowerOfBase(power, base):
    if power <= 1:
        return False
    while not power == 1:
        if not power % base == 0:
            return False
        power = power / base
    return True


# Funtion call
print(isPowerOfBase(8, 2))  # True
print(isPowerOfBase(3, 2))  # False
