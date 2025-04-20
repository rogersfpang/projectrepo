# add_numbers.py

def add_two_numbers(var1, var2):
    return var1 + var2

if __name__ == "__main__":
    # create 2 variables
    num1 = 3
    num2 = 5
    
    # call add number function
    result = add_two_numbers(num1, num2)

    # display result on terminal
    print(f"The sum of {num1} and {num2} is {result}")
