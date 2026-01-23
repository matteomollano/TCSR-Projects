def hello(name): # function header
    print("Hello", name)

# hello("Jaydan")

# create a function that will take 2 parameters (num1, num2)
# they should add the numbers together
def add(num1, num2):
    print(num1 + num2)
    
# add(4, 9)

# create a function that will compute the mean, median, mode for a list of numbers
# [2, 4, 5, 2, 3, 9, 8, 7, 0, 2]
def stats(nums):
    # mean
    total = 0
    length = 0
    for num in nums:
        total += num
        length += 1
    mean = total / length
    print("Mean is", mean)
    
    # median
    nums_sorted = sorted(nums)
    if len(nums_sorted) % 2 == 0: # even
        first_idx = len(nums_sorted) // 2
        second_idx = first_idx + 1
        