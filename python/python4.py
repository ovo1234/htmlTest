# ## 4주차

# year = eval(input("Enter a year : "))

# isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# print(year , isLeapYear)

# import random as r

# lottery = r.randint(0,99)

# guess = eval(input("Enter your lottery pick(two digits) : "))

# lotteryDigit1 = lottery // 10
# lotteryDigit2 = lottery % 10

# guessDigit1 = guess // 10
# guessDigit2 = guess % 10

# print("The lottery number is", lottery)

# if guess == lottery:
#     print("Exact match : you win $10,000")
# elif(guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit2):
#     print("Match all digits : you win $ 3,000")
# elif(guessDigit1 == lotteryDigit1 or guessDigit2 == lotteryDigit2 or guessDigit2 == lotteryDigit1 or guessDigit2 == lotteryDigit2):
#     print("Match one digit : you win $1,000")
# else : 
#     print("Sorry, no match")

# import turtle

# x1, y1 = eval(input("Enter the center of a circle x, y: "))
# radius = eval(input("Enter the radius of the circle: "))
# x2, y2 = eval(input("Enter a point x, y: "))

# # Draw the circle
# turtle.penup() # Pull the pen up
# turtle.goto(x1, y1 - radius)
# turtle.pendown() # Pull the pen down
# turtle.circle(radius)

# # Draw the point
# turtle.penup() # Pull the pen up
# turtle.goto(x2, y2)
# turtle.pendown() # Pull the pen down
# turtle.begin_fill() # Begin to fill color in a shape
# turtle.color("red")
# turtle.circle(3) 
# turtle.end_fill() # Fill the shape

# # Display the status
# turtle.penup() # Pull the pen up
# turtle.goto(x1 - 70, y1 - radius - 20)
# turtle.pendown() 
# d = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5

# if d <= radius:
#     turtle.write("The point is inside the circle") 
# else:
#     turtle.write("The point is outside the circle") 

# turtle.hideturtle()
# turtle.done() 

NUMBER_OF_PRIMES = 50  # Number of primes to display
NUMBER_OF_PRIMES_PER_LINE = 10 # Display 10 per line
count = 0 # Count the number of prime numbers
number = 2 # A number to be tested for primeness
print("The first 50 prime numbers are")

# Repeatedly find prime numbers
while count < NUMBER_OF_PRIMES:
    # Assume the number is prime
    isPrime = True #Is the current number prime?

    # Test if number is prime
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, the number is not prime
            isPrime = False  # Set isPrime to false
            break  # Exit the for loop
        divisor += 1
    
    # Display the prime number and increase the count
    if isPrime:
        count += 1 # Increase the count
        print(format(number, '5d'), end = '')

        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            # Display the number and advance to the new line
            print() # Jump to the new line

    # Check if the next number is prime
    number += 1