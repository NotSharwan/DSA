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


# Function calls
print(EuclideanGCD(49, 21))  # 7
print(EuclideanGCD(24, 12))  # 12
print(EuclideanGCD(64, 8))  # 8
print(EuclideanGCD(0, 2))  # 2
