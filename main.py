import math
import random

def Q1Pythagoras():
  a = float(input("What is the length of side a? "))
  b = float(input("What is the length of side b? "))
  c = math.sqrt((a**2) + (b**2))
  print ("Side c is ",c)

def Q2RandomRange():
  a = int(input("What is the lowest value? "))
  b = int(input("What is the highest value? "))
  c = random.randrange(a, b)
  print ("Your random number in range is ",c)

def Q3Addition():
  a = random.randrange(1, 100)
  b = random.randrange(1, 100)
  c = input ("What is "+str(a)+" plus "+str(b)+"? ")
  print("")
  if (int(c) == (a+b)):
    print ("Correct!")
  else: 
    print ("Better luck next time")

while True:
  print ("Which task would you like to run? ")
  print ("1 - Q1Pythagoras")
  print ("2 - Q2RandomRange")
  print ("3 - Q3")
  print ("4 - exit")
  task = input("My choice: ")
  if (task == "1"):
    Q1Pythagoras()
  elif (task == "2"):
    Q2RandomRange()
  elif (task == "3"):
    Q3Addition()
  elif (task == "4"):
    print("")
    print ("Goodbye!")
    break
  print ("")