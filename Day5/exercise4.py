#You are going to write a program that automatically prints the solution to the FizzBuzz game.
#Your program should print each number from 1 to 100 in turn.
#When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#When the number is divisible by 5, then instead of printing the number it should print "Buzz".
#And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

#the range is [1, 100]
for num in range(1, 100 + 1):
    #print(num)
    #if the number is a factor of both 3 and 5, print fizzbuzz first without checking for 3 or 5 indiviually
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    elif (num % 3 == 0):
        print("Fizz")
    elif (num % 5 == 0):
        print("Buzz")
    else:
        print(num)
