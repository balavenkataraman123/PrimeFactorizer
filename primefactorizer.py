def isprime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif not n == 3 and n % 3 == 0:
        return False
    elif not n == 5 and n % 5 == 0:
        return False
    else:
        for i in range(int(n ** 0.5) + 1):
            if not i <= 1 and n % i == 0:
                return False
        return True
if __name__ == "__main__":
    print('Prime Factorizer')
    num = int(input('enter number')) 
    factors = []
    while num > 1:
        for i in range(int((num + 1) ** 0.5)):
            if not i == 1 and not i == 0 and num % i == 0 and isprime(i):
                num = int(num / i)
                factors.append(i)
                if num == 1:
                    break
    for i in factors:
        print(i)
    
                

                    
