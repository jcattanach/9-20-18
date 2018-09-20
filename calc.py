
### MATH FUNCTIONS
def add_function(first_number, second_number):
    return first_number + second_number

def sub_function(first_number, second_number):
    return first_number - second_number

def mul_function(first_number, second_number):
    return first_number * second_number

def div_function(first_number, second_number):
    return first_number / second_number

def operator_selector(first_number,operator,second_number):

    correct_operator = True

    if(operator == '+'):
        result = add_function(first_number,second_number)
    elif(operator == '-'):
        result = sub_function(first_number,second_number)
    elif(operator == '*'):
        result = mul_function(first_number,second_number)
    elif(operator == '/'):
        result = div_function(first_number,second_number)
    else:
        correct_operator = False
        print("Select a valid operator")
        operator = input("Enter a mathmatical operator (+,-,/,*): ")
        resut = operator_selector(first_number, operator, second_number)

    if(correct_operator == True):
        display_result(first_number,operator,second_number,result)


def display_result(first_number,operator,second_number,result):
    print('-------------------------')
    print('       {0} {1} {2} = {3}'.format(first_number, operator, second_number, result))
    print('-------------------------')

while True:
    print("************** WELCOME TO CALCULATOR **************")
    choice = input("Press 'q' to quit or 'enter' to continue: ").lower()

    if(choice == 'q'):
        break

    try:
        first_number = int(input("Choose your first number: "))
        operator = input("Enter a mathmatical operator (+,-,/,*): ")
        second_number = int(input("Choose your second number: "))
        operator_selector(first_number, operator, second_number)
    except ValueError:
        print("You did not enter a valid number")



print("************ YOU HAVE EXITED CALCULATOR ************")
