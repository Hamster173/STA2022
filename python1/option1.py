def isPrime(x):
    for i in range(2,x):
        if x % i == 0:
            return str(x)
    return "Prime"


for i in range(30,61):
    print(isPrime(i))

