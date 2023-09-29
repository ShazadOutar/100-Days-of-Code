#Calculator project
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#operations in a dictonary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#function = operations["/"]
#print(function(6, 3))
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
    
  #loop until the user says no
  keep_playing = True
  while keep_playing :
        
  
    #display all the operation options
    for key in operations:
        print(f"{key}")
    
    #get the operation the user picked
    operation_symbol = input("Pick an operation from the options above: ")
    #print(f"oper sym is {operation_symbol} and is of type {type(operation_symbol)}")
    
    num2 = float(input("What's the next number?: "))
    
    #use the users input (string) as the key to find the function to call
    #the key value pair for this is {operation string: operation function}
    calculation_function = operations[operation_symbol]
    #print(f"cal funct is {calculation_function} and is of type {type(calculation_function)}")
    
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}") 
    #check the options from the input, exit is the default case
    keep_playing_input = input(f"Type 'y' to continue calculating with {answer}, type 'e' to exit, or type 'n' to start a new calculation: ").lower()
    if keep_playing_input == "y":
      keep_playing = True
      #keep looping and carry answer over through num1 
      num1 = answer
    elif keep_playing_input == "n":
      #if the user presses n, end the while loop but call the calculator function to reset the program
      keep_playing = False
      calculator()
    else:
      return


calculator()
