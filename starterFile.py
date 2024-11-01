#Your code goes here. 

import math
def main():
    a = float(input("Please input your first number: "))
    b = float(input("Please input your second number: "))
    safe_divide(a,b)
    input_list = []
    process_list(input_list)
    

def safe_divide(a, b):  
    try :
        answer=a/b
        print(answer)
    except ZeroDivisionError:
        print("Cannot divide by zero")

def process_list(input_list):
    totalvalue = 0
    x = 0
    for x in range(4):
        num = float(input("Enter a number: ")) 
        input_list.append(num)
        print(input_list)
    try:
        for i in range(len(input_list)):
            tempval = int(input_list[i])**2
            totalvalue += tempval
    except TypeError or ValueError:
        print("Somethings Up M8 ")
    print(totalvalue)


def nested_operations(a, b):
    

def process_input():
    print("")

main()
