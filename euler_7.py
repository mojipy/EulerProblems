def isprime(num):
    for i in range(2, int(num**0.5)+1):      
        if num%i == 0:
            return False # The function ends here?
    return True
num = 1
c = 0
while c < 10001:
    num += 1
    if isprime(num):
        c += 1
        
print('The 10001st prime number is %d' %num)
