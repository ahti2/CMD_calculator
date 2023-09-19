# import math module for advanced mathematical operations
import math

# print welcome message and instructions
print("Ahti's Command Line Calculator V1. Type 'guide' for instructions, 'about' for more info, or 'exit' to quit.")

# define calculator function
def calculator():
    # loop until user exits
    while True:
        # get user input
        expression = input("Enter a mathematical expression or command: ")
        # check if user wants to exit
        if expression.lower() == 'exit':
            print("Calculator is closing...")
            break
        # check if user wants to know about the calculator
        elif expression.lower() == 'about':
            print("Welcome to Ahti's CMD Calculator V1")
            print("This calculator is written in Python.")
            print("Feel free to copy and redistribute.")
            print("Tell me ideas to add to this program on GitHub or bugs:)")
            print("or contact me at Ahti.jokirinne@outlook.com")
            print("feel free to change the code")
            continue
        # provide instructions to user
        elif expression.lower() == 'guide':
            print("Welcome to Ahti's Command Line Calculator V1 Guide:")
            print("1. Perform basic arithmetic operations like addition (+), subtraction (-), multiplication (*), and division (/).")
            print("2. Use parentheses to group expressions and control the order of operations.")
            print("3. To round the result, enter the desired number of decimal places when prompted. Leave it blank for no rounding.")
            print("4. Type 'exit' to quit the calculator.")
            continue
        # ahti can make sure its he's software please dont remove or disable this
        elif expression.lower() == 'ahti':
            print('Hello Ahti this is ur software')
            continue
        try:
            # evaluate user input
            result = eval(expression)
            # ask user if they want to round the result
            rounding = input("How many decimal places do you want to round to? (leave blank for no rounding): ")
            # round the result if user wants to
            if rounding == "":
                print("Result: ", round(result))
            else:
                rounding = int(rounding)
                result = round(result, rounding)
                print("Result: ", result)
        except NameError:
            # handle invalid expression
            print("Invalid expression! Please check that all functions and variables are spelled correctly.")
        except ZeroDivisionError:
            # handle division by zero
            print("Invalid expression! Division by zero is not allowed.")
        except SyntaxError:
            # handle syntax error
            print("Invalid expression! Please check that the expression is correctly formatted.")
        except:
            # handle other errors
            print("Invalid expression! Something went wrong.")

# call calculator function
calculator()