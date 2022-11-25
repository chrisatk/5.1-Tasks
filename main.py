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

while True:
  print ("Which task would you like to run? ")
  print ("1 - Q1Pythagoras")
  print ("2 - Q2RandomRange")
  print ("3 - Q3")
  print ("4 - Q4")
  print ("5 - exit")
  task = input("My choice: ")
  if (task == "1"):
    Q1Pythagoras()
  elif (task == "2"):
    Q2RandomRange()
  elif (task == "3"):
    print ("Not done yet")
  elif (task == "4"):
    print ("Not done yet")
  elif (task == "5"):
    print ("Goodbye!")
    break
  print (" ")