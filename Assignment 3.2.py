#Name: George Sono
#Class: CSE20 
#Prof: Harikishna Kuttivelli
#Description: A four function program: "is prime" allows you to check if a positive integer is a prime number with a boolean value(true or false), "convert_temp" converts the temp (float or int) from celcius and farrenheit (vice versa), "get_euclidean_dist" calcuates the Euclidean distance by square rooting the sum of squres, and finally "LCM" calculates the lowest common multiple of two given positive integer inputs
#Acknowledgements: Mike Dane, Python Docs, Harikishna Kuttivelli, CueMath (for LCM formula)

import math as m
#imports math library into program
#math commands are functions with m.mathfunction, eg. m.sqrt

#function for is_prime
def is_prime(posint):
  #if the input is an integer...
  if type(posint) == int:
    #if the input is an integer but its negative...
    if posint <= 0:
      print("ERROR: parameter must be a POSITIVE integer")
      return None
    #case for if int is positive
    if posint == 1 or posint == 2:
      return True
    for i in range(2,posint):
      #this for loop basically runs by divding the positive int by every number up until the actual number. But as prime numbers have the two factors which is one and itself, the range of numbers we divide with start from 2 and end at the value of the positive integer minus 1. If the for loop finds a divsor with no remainder, then it means that it's not a prime (returning false). If the divider reaches the value of the positive integer minus 1, without finding a zero remainder divisor, then it's a prime number (returning true) as the only factors are 1 and itself 
      if (posint % i) == 0:
        return False
        break
      if i == posint-1:
        return True
        break
  #this code is for the user misinputs the datatype, eg. float or string
  else:
    print("ERROR: parameter must be an integer")
    return None
    
def LCM(firstop, secondop):
  #used to check if the input types are integer
  if type(firstop) == int and type(secondop) == int:
    #return functon only executes once it is confirmed that firstop and secondop are integers
    if firstop > 0 and secondop > 0:
      # using the LCM formula with the math module
      return (abs(firstop*secondop)) / (m.gcd(firstop,secondop))
    else:
    
      print("ERROR: parameters must be a POSITIVE integer")
      return None
  #this code is for the user misinputs the datatype, eg. float or string
  else:
    print("ERROR: parameters must be a POSITIVE integer")
    return None

def convert_temp(num,conv):
  #used to check num is either a float or num and that conv is a string
  if (type(num) == float or type(num) == int) and type(conv) == str:
    if conv == "FtoC":
      #formula of farrenheit to celcius
      celcius=5/9*(num-32)
      return celcius
    elif conv == "CtoF":
      #inverse formula
      faren = (9/5)*num+32
      return faren
    #else runs when conv is a string but isn't an actual command
    else:
      print("ERROR: First or second operand is invalid. Please use an integer or float for the first operand, the second operand must be either 'CtoF' or 'FtoC'")
      return None
  #this code is for the user misinputs the datatype, eg. float or string
  else:
    print("ERROR: First or second operand is invalid. Please use an integer or float for the first operand, the second operand must be either 'CtoF' or 'FtoC'")
    return None

def get_euclidean_dist(x1,x2):
  #used to check if the input types are integers or floats
  if (type(x1) == float or type(x1) == int) and (type(x2) == float or type(x2) == int):
    #square root of sum of the squares of x1 and x2
    dist = m.sqrt((x1**2)+(x2**2))
    return dist
  #this code is for the user misinputs the datatype, eg. float or string
  else:
    print("ERROR: parameters must be a integer or float")
    return None

#test cases
x = is_prime(5)
print(x)
True

x = is_prime(-0.5)
#Invalid operand. Operand must be a positive integer.
print(x)
#None

x = LCM(5, 4)
print(x)
#20

x = LCM(-4.3, "number")
#Invalid operand(s). Both operands must be positive integers.
print(x)
#None

x = convert_temp(32, "FtoC")
print(x)
#0.0

x = convert_temp(12.4, "nonsense")
#Invalid operand(s). The first operand must be an int or float. The second operand must be "FtoC" and "CtoF".
print(x)
#None

x = get_euclidean_dist(-3, 4)
print(x)
#5

x = get_euclidean_dist(-4, "eight")
#Invalid operand(s). Both operands must be int or float.
print(x)
#None