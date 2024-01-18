number = int(input('Enter your number: '))
num = number
while num%2 == 0:
    num //= 2
    max_pf = 2

for i in range(3, int(num**0.5)+1, 2):
    while num%i ==0:
        num //= i
        max_pf = i

try:
    print('The largest prime factor is %d' %max_pf)
except:
    print('%d is a prime number' %number)

