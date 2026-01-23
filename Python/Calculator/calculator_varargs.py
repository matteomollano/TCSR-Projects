
def add(*nums):
    # for-each loop
    sum = 0
    for number in nums:
        sum += number
    return sum

def subtract(*nums):
    # nums = [12, 6, 2] -> 4
    dif = nums[0]
    for i in range(1, len(nums)):
        dif -= nums[i]
    return dif

def multiply(*nums):
    # nums = [2, 4, 8] -> 64
    pro = 1
    for number in nums:
        pro *= number
    return pro

def divide(*nums):
    # nums = [20, 2, 5] -> 2
    try:
        quo = nums[0]
        for i in range(1, len(nums)):
            quo /= nums[i]
        return quo
    except ZeroDivisionError:
        return "undefined"
        
sum = add(1, 2, 3, 4, 5)
print(f"The sum is {sum}")

dif = subtract(12, 6, 2)
print(f"The difference is {dif}")

pro = multiply(3, 4)
print(f"The product is {pro}")

quo = divide(12, 6, 2, 0)
print(f"The quotient is {quo}")