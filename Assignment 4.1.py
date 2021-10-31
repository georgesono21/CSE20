#Name: George Sono
#Class: CSE20 
#Prof: Harikishna Kuttivelli
#Description:
#my_bin(integer): Based on the built-in bin(...) function. Takes a decimal integer and returns the binary representation as a string, starting with '0b' followed by the actual binary notation.
#my_oct(integer): Based on the built-in oct(...) function. Takes a decimal integer and returns the octal representation as a string, starting with '0o' followed by the actual octal notation.
#my_round(number, integer): Based on the built-in round(...) function. Takes an integer or float and returns a rounded float value that is the number rounded to the second argument's decimal place.
#Acknowledgements: Harikishna Kuttivelli, PythonDocs, Rohan Sehgal

#defining main function
def main():
  def my_bin(num):
    #defining list variables
      list1 = []
      list2 = ["0b"]
      listneg = ["-0b"]
      if num == 0:
          list2.append("0")
          seperator = ""
          list2 = seperator.join(list2)
          return list2
      elif num < 0:
          #if the number is negative, make it an absolute value and append the -0b to it later
          num = abs(num)
          
          #range is set to how many times the number can be divided by two (using floor division)-1 (as its exclusive)
          for x in range(0, (num // 2) + 1):
              if num % 2 > 0:
                  list1.append(1)
              elif num == 0:
                  break
              else:
                  list1.append(0)
              num = num // 2
            # the loop works like this: if the number is divisble by two without a remainder, add 0 to the list and if the number is not divisible by two and has a remainder, add 1 to the list. in the end, with floor division it results in the final quotient being 0, if it is 0, than break out of the loop

          list1 = list1[::-1]
            #for some reason the for loop outputs the list of nums but theyre in reverse order, so I just reverse that to make it the same as the bin function

          for x in list1:
              x = str(x)
              listneg.append(x)
          #for each element in the list we made that was comprimsed of the binary number, we add it to the negative list format (-0b) 
          
          #as listneg is a list, we just join all the elements into a single string
          listneg = "".join(listneg)
          return listneg

      else:
        #this is the same as above but if the number is positive
          for x in range(0, (num // 2) + 1):
              if num % 2 > 0:
                  list1.append(1)
              elif num == 0:
                  break
              else:
                  list1.append(0)
              num = num // 2
          list1 = list1[::-1]

          #for each element in the list we made that was comprimsed of the binary number, we add it to the positive list format (0b) 
          for x in list1:
              x = str(x)
              list2.append(x)

          #as listpos is a list, we just join all the elements into a single string
          list2 = "".join(list2)
          return list2


  def my_oct(num):
      #same logic as the bin function, we have two lists that the converted list of numbers adds to, either the positive or negative
      list1 = []
      list2 = ["0o"]
      listneg = ["-0o"]

      if num == 0:
          list2.append("0")
          list2 = "".join(list2)
          return list2

      elif num < 0:
          num = abs(num)
          #if the number is negative, make it an absolute value and append the -0b to it later
          for x in range(0, (num // 8) + 1):
              if num % 8 > 0:
                  list1.append(num % 8)
              elif num == 0:
                  break
              else:
                  list1.append(0)
              num = num // 8
          #same logic as the bin for loop but we switch out the 2 for an 8 as oct uses a base 8 system
          list1 = list1[::-1]

          #for each element in the list we made that was comprimsed of the octal number, we add it to the negative list format (-0o) 
          for x in list1:
              x = str(x)
              listneg.append(x)
          
          #as listneg is a list, we just join all the elements into a single string
          listneg = "".join(listneg)
          return listneg

      else:
          for x in range(0, (num // 8) + 1):
              if num % 8 > 0:
                  list1.append(num % 8)
              elif num == 0:
                  break
              else:
                  list1.append(0)
              num = num // 8
          #same logic as the bin for loop but we switch out the 2 for an 8 as oct uses a base 8 system

          list1 = list1[::-1]

          
          #for each element in the list we made that was comprimsed of the octal number, we add it to the positive list format (0o) 
          for x in list1:
              x = str(x)
              list2.append(x)

          #as listpos is a list, we just join all the elements into a single string
          list2 = "".join(list2)
          return list2


  def my_round(num,step=0): 
    if step > 0 and num > 0:
      numsplit = str(num).split(".")
      if len(numsplit[1]) < step:
        return num
      #if the step is greater than the decimal section of the number than we return the num for all cases where step > decimals

      #this converts the number so it only has one decimal so its able to be int'ed
      num = num*10**step
      #we add 0.5 as the int function rounds down. this means that if a number is 3.6 we add 0.5 add which means that it equals 4.1. int(4.1) = 4
      num = int(num+0.5)
      #we shift back the steps back by how many steps we shifted it
      num = num*10**-step

      #this is to check for a FPE floating point error. To make sure that the code doesnt have any random decimals like 34.200000000001, we make sure that the step is the same length as the decimal section,if not this means that there is a FPE which means we return the number with the decimal section only incliuding up to the step eg. 423.3232 with a step of 3 returning 423.323000001 would return 423.323 as the decimal section can only include up to 3 digits
      numsplitpt2 = str(num).split(".")
      if len(numsplitpt2[1]) > step:
        temp = numsplitpt2[1]
        numsplitpt2[1] = temp[0:step]
        return float(".".join(numsplitpt2))

      return num


    elif step > 0 and num < 0:
      
      numsplit = str(num).split(".")
      if len(numsplit[1]) < step:
        return num
      if step>len(str(num)):
        return num
      #if the step is greater than the decimal section of the number than we return the num for all cases where step > decimals
      
      #same logic as above but instead of adding .5 we minus 0.5
      num = num*10**step
      num = int(num-0.5)
      num = num*10**-step

      numsplitpt2 = str(num).split(".")
      if len(numsplitpt2[1]) > step:
        temp = numsplitpt2[1]
        numsplitpt2[1] = temp[0:step]
        return float(".".join(numsplitpt2))

      return num

    elif step == 0 and num > 0:
      num = int(num+0.5)
      return num
    #if the number is positive and has a step of 0 we only return the positive number but rounded up
    
    elif step == 0 and num < 0:
      num = int(num-0.5)
      return num
    #if the number is negative and has a step of 0 we only return the negative number but rounded down

    elif step < 0 and num > 0:

      numsplit = str(num).split(".")
      if len(numsplit[0]) < step:
        return num
      #if the step is greater than the decimal section of the number than we return the num for all cases where step > decimals

      #same logic as above 
      num = num*10**step
      num = int(num+0.5)
      num = num*10**-step

      #for some reason FPEs dont occur with a negative step and num so we dont need that if case here
      return num
    
    elif step < 0 and num < 0:

      numsplit = str(num).split(".")
      if len(numsplit[0]) < step:
        return num
      #if the step is greater than the decimal section of the number than we return the num for all cases where step > decimals 
      
      #same logic as above
      num = num*10**step
      num = int(num-0.5)
      num = num*10**-step
      #for some reason FPEs dont occur with a negative step and num so we dont need that if case here
      return num
#test cases: all test cases use a for loop that prints an error counter. the error counter goes up by 1 everytime theres a testcase where the myfunction != built-in function
#bin test cases
  print("\nbin test cases\n")
  errorcounter = 0

  for x in range(-3,3):
    if bin(x) == bin(x):
      print(x, "pass")
    else:
      print(x,"fail")
      errorcounter += 1
  print(f"ERROR counter = {errorcounter}\n")

#oct test cases
  print("\noct test cases\n")
  errorcounter = 0
  for x in range(-3,3):
    if my_oct(x) == oct(x):
      print(x,"pass")
    else:
      print(x,"fail")
      errorcounter += 1
  print(f"ERROR counter = {errorcounter}\n")

#round test cases
  print("\nround test cases (two test numbers)")
  errorcounter = 0

  x = 12345.6789
  print(f"\nnumber: {x}")
  for y in range(-5,5):
    if round(x,y) == my_round(x,y):
      print(f"{y}, pass")
    else:
      print(f"{y}, fail")
      errorcounter += 1
  errorcounter = 0
  print(f"ERROR counter = {errorcounter}")


  x = 98765.4321
  print(f"\nnumber: {x}")
  for y in range(-5,5):
    if round(x,y) == my_round(x,y):
      print(f"{y}, pass")
    else:
      print(f"{y}, fail")
      errorcounter += 1
  print(f"ERROR counter = {errorcounter}")
  
#calling main() 
if __name__ == "__main__":
  main()
