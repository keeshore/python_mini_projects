def add(x, y):
    #add the total sum of numbers
    return f'The Sum of Two Numbers:{x + y}'

def sub(x, y):
    #subract the total sum of numbers
    return f'The Subraction of Two Numbers:{x - y}'

def mul(x, y):
    #Multiplcatoin the total sum of numbers
    return f"The Multiplcation of Two Numbers:{x * y}"

def div(x, y):
    #division the total sum of numbers
    return f"The Division of Two Numbers:{x / y}"

def module(x, y):
    #module the total sum of numbers
    return f"The Module of Two Numbers:{x % y}"

def fun(x, y, operator):

    if operator == '+':
        print(add(x, y))

    elif operator == '-':
        print(sub(x, y))

    elif operator == '/':
        print(div(x, y))

    elif operator == '*':
        print(mul(x, y))
    elif operator == '%':
        print(module(x, y))

    else:
        print("invalid operator")

#input from the user
num_1 = int(input("ENTER THE NUMBER: "))
operator = input("ENTER YOUR OPERTATOR: ")
num_2 = int(input("ENTER THE NUMBER: "))
fun(num_1, num_2, operator)