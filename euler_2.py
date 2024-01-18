def iseven(num):
    if num%2 == 0:
        return True
    else:
        return False

fib_list = [1, 2]

while fib_list[-1]<4000000:
    fib_list.append(fib_list[-1]+fib_list[-2])

sum = 0
for num in fib_list:
    if num<4000000 and iseven(num):
        sum +=num

print(sum)

## Jadi
# first = 1
# second = 2
# while first<40:
#     new = first + second
#     first = second
#     second = new
