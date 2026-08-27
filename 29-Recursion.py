def calculateFactorial(num):
    if num == 0 :
        return 1
    else:
        return num * calculateFactorial(num - 1)

print(calculateFactorial(10))

def calculateContigousSum(num):
    if num == 0:
        return 0
    else:
        return num + calculateContigousSum(num - 1)
print(calculateContigousSum(100))