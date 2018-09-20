#calculator function using while loops, except, try, if and else

#This function displays the results of the calculator function
def display_result(first_number,second_number,operator,result):
    print("**********************")
    print("      {0} {1} {2} = {3}     ".format(first_number,operator,second_number,result))
    print("**********************")

#these are the mathmatical operation functions
def add_function(first_number, second_number):
    return first_number + second_number

def sub_function(first_number, second_number):
    return first_number - second_number

def mul_function(first_number, second_number):
    return first_number * second_number

def div_function(first_number, second_number):
    return first_number / second_number

#below is the calculator function with if and else statements
#   that determine which math function to use
def calculator(first_number, operator, second_number):

    correct_operator = True

    if (operator == '+'):
        result = add_function(first_number, second_number)
    elif (operator == '-'):
        result = sub_function(first_number, second_number)
    elif (operator == '/'):
        result = div_function(first_number, second_number)
    elif (operator == '*'):
        result = mul_function(first_number, second_number)
    else:
        # this else statement will prompt the user for a correct operator
        #   and change the operator in the result if a correct operator is selected
        correct_operator = False
        print("Please enter a valid operator...")
        operator = input("Enter a mathmatical operator (+,-,/,*): ")
        result = calculator(first_number, operator, second_number)

    if correct_operator == True:
        display_result(first_number, second_number, operator, result)

result = 0
# This while loop will keep the calculator running and prompting user for input
#   unless 'q' is selected
while True:

    choice = input("WELCOME TO CALCULATOR. PRESS 'q' TO QUIT OR 'enter' TO CONTINUE: ")

    if(choice == "q"):
        break

    try:
        first_number = int(input("Choose your first number: "))
        operator = input("Enter a mathmatical operator (+,-,/,*): ")
        second_number = int(input("Choose your second number: "))
        calculator(first_number, operator, second_number)

    except ValueError:
        print("You did not enter a valid number")

print("Thank you for using calculator.")
