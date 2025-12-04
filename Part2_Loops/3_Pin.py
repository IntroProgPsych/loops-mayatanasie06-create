# https://www.w3schools.com/python/python_while_loops.asp

# Write a program that keeps asking the user for a PIN code until they type 4321.
# The program must print "Wrong" for every incorrect attempt.
# When the user enters the correct PIN, print how many attempts it took.
#
# Sample output:
# PIN: 3245
# Wrong
# PIN: 1234
# Wrong
# PIN: 0000
# Wrong
# PIN: 4321
# Correct! It took you 4 attempts
#
# If the user gets it right on the first try:
# PIN: 4321
# Correct! It only took you one single attempt!


# Write your code here:
correct_PIN = 2609
attempts = 0
PIN=int(input("Write a PIN code: "))
attempts += 1

while PIN != correct_PIN:
    print ("Wrong")
    PIN=int(input("PIN: "))
    attempts +=1

if attempts ==1:
    print ("Correct! It took you one attempt")
else:
    print ("Correct! It took you" , attempts , "attempts")