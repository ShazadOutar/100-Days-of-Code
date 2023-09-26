"""
Instructions
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.
"""
#Write your code below this line 👇

def prime_checker(number):
    #assume the value is prime to start with
    is_prime = True
    #if it's one, it's a prime
    #if number == 1:
    #    print("1 is prime")
    #if the number is even it's not a prime
    if number % 2 == 0:
        #print("Num is even")
        is_prime = False
    #search through the remaining numbers
    for i in range(3, number, 2):
        #print(f"Value of i is: {i}")
        #print(number % i)
        #print(f"Value of i % num is: {i % number}")
        #print(f"Value of num % i is: {number % i}")
        #print(f"Value of {number} % {i} is: {number % i}")
        if (number % i == 0):
            is_prime = False
    #print(f"is_prime = {is_prime}") 
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

