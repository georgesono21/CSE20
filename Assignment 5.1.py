#Name: George Sono
#Class: CSE20 Assignment 5.1
#Prof: Harikishna Kuttivelli
#Description: 
# simple_sum: takes two input arguments (both arguments or either float or int) and returns the sum.
# assign_grade: takes in number of points as the single argument (float or int) and returns a string grade ('A', 'B', 'C', 'D', 'F') based on the following criteria:
  # If the number of points is between and including 90 and 100, student gets an A.
  # Between 80 and <90 points, student earns a B.
  # Between 70 and <80 points, student earns a C.
  # Between 60 and <70 points, student earns a D.
  # Between 0 and <60, student earns an F.
  # If inputted points is negative or above 100, function should print an error then return None.

# num_of_words: takes in a sentence as one argument (string with words separated by whitespaces and no punctuation) and returns the number of words in the sentence.

# find_average: takes in one argument that is a list of numbers (a list of floats and ints) and returns the average. You cannot use the math or stats modules, or any built-in mean function.

#main function
def main():

  def simple_sum(x,y):
    return x+y
  #returns the sum of x and yield

  def assign_grade(grade):
    #criteria range for each grade:
    if grade >= 90 and grade <= 100:
      return "A"
    elif grade >= 80 and grade < 90:
      return "B"
    elif grade >= 70 and grade < 80:
      return "c"
    elif grade >= 60 and grade < 70:
      return "D"
    elif grade >= 0 and grade < 60:
      return "F"
    #if grade isnt anything in the criteria then it is a wrong input
    else:
      print("Wrong input")
  
  def num_of_words(string1):
    
    listofwords = string1.split(" ")
    #string split into a list at the instance of a space 
    return len(listofwords)
    #return the length of the stringsplit list
  
  def find_average(listofnums):
    sums = 0
    #defining sums (has no value)
    for x in listofnums:
      sums += x
      #every time it iterates an element through the list of numbers, it adds it to sums
    return (sums/len(listofnums))
      #divides sums by the length of the numslist

if __name__ == "__main__":
  main()
#calling name function