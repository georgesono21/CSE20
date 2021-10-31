#Name: George Sono
#Class: CSE20 
#Prof: Harikishna Kuttivelli
#Description: 
#parse_string: takes two input arguments (the first argument must be a string and the second argument must be a single character); returns a new string that is a copy of the first argument up until the first occurrence of the second argument
#get_string_length: takes an input argument (must be a string) and returns the integer length of the inpu
# reverse_string: takes an input argument (must be a string) and returns a new string that is the reverse of the input string.
#rev_string: reverses a string without the range function
#Acknowledgements: Mike Dane, Python Docs, Harikishna Kuttivelli, W3Schools (for range function), Hoa Nguyen (stringsplit)

#parse string function
def parse_str(string,char):
  #if parameters are string and the second is a only one character...
  if type(string) == str and type(char) == str and len(char) == 1:
    #use stringsplit at the instance of the char, splitting the string into two words (that are in a list)
    strsplit = string.split(char)
    return strsplit[0]
    #return the first (zero indexing) element of the list (the string before the instance of char)
  else:
    #case if user input isnt the correct datatype
     print("ERROR: The first parameter must be a string. The second parameter must be a character")
     return None

def get_string_length(string):
  
  if type(string) == str:
    counter = 0
    for i in string:
      #for each letter of string, the counter increases by 1. Once i is iterated through all letters of string, the loop ends and the total counter value is returned
      counter += 1 
    return counter
  else:
    #case if user input isnt the correct datatype
    print("ERROR: The parameter must be a string")
    return None

def reverse_string(string):
  if type(string) == str:
     #revstring = variable for the reverse string
    revstring = ""
    for i in range(-1,-(len(string))-1,-1) :
      #this for loop iterates backwards with the range function decreasing with a step of -1. But as python indexes first with 0, the starting value has to begin with -1 or else the 0th index would be at the very beginning. The len of the string is negative so it works with the negative step of -1.
      revstring = revstring + string[i]
    return revstring
  else:
    #case if user input isnt the correct datatype
    print("ERROR: The parameter must be a string")
    return None

#test cases

x = parse_str("one message*two message", "*")
print(x)
# one message

x = parse_str("one message*two message", 5)
#Invalid argument(s). parse_str takes a string argument and a character argument.
print(x)
#None

x = get_string_length("hello world")
print(x)
#11

x = get_string_length(5)
#Invalid argument(s). get_string_length takes one string argument.
print(x)
#None

x = reverse_string("hello world")
print(x)
#dlrow olleh

x = reverse_string(5)
#Invalid argument(s). reverse_string takes one string argument.
print(x)
#None



