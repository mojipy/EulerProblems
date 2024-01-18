def is3or5mult(num):
    if num%3 == 0 or num%5 == 0:
        return True
    else:
        return False
sum = 0
for num in range(1,1000):
    if is3or5mult(num):
        sum += num

print(sum)