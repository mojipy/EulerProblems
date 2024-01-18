def is_pal(num):
    numstr = str(num)
    ndig = len(numstr)
    ispal = True
    
    for i in range(0, int(ndig/2)): # output of n/2 is float
        if numstr[i] != numstr[-1-i]:
            ispal = False
    return ispal

def twoDigitFactors(num):
    twoDigFacts = []
    for i in range(100, int(num*0.5)+1):      
        if num%i == 0 and len(str(i))==3:
            twoDigFacts.append(i)
           
    for i in twoDigFacts:
        for j in twoDigFacts:
            if i*j == num:
                print(i,j)
                return True
    return False

for number in range(998001, 10001, -1):
    if is_pal(number) and twoDigitFactors(number):
        max_pal = number
        break
print(max_pal)

# def isprime(num):
#     for i in range(2, int(num**0.5)+1):      
#         if num%i == 0:
#             return False # The function ends here?
#     return True