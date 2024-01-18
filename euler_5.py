def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def calculate_lcm_of_list(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result

fact_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = calculate_lcm_of_list(fact_list)
print(result)