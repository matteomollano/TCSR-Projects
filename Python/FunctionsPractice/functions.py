
def hello(name):
    print(f"Hello {name}")

def add(number1, number2):
    return number1 + number2

def pentation(number):
    answer = number
    for i in range(5):
        answer = answer ** number
    return answer

# main.py
import functions as f

f.hello("Julian")

answer = f.add(8, 9)
print(f"Answer is {answer}")

pentation = f.pentation(2)
print(f"Pentation of 2 is {pentation}")