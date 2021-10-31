#Name: George Sono
#Class: CSE20 Assignment 5.2
#Prof: Harikishna Kuttivelli
#Description:
# censor: takes in two string arguments (first argument is the message, second argument is the word that should be censored); returns the message with the specified word censored, using the * symbol for each character in the censored word.
# fix_title: takes in a string argument that is formatted as such -- "TYPE:tHe titLe Of tHe ContENT". Should return the title, based on the following criteria:
# get_longest_word: takes in a sentence as a string argument (string with words separated by whitespaces and no punctuation) and returns the longest word in the sentence. If there are two words of equal longest length, it returns the word that occurs first.
# frame: takes in a short sentence (string with words separated by spaces) and returns a string that represents the words with newlines, aligned to the left, surrounded by a frame of '*' symbols.

#defining main function
def main():

  def censor(message,censor):
    messagelist = message.split(" ")
    #splits the string into a list so its iterable by each element (word)
    for i in range(len(messagelist)):
      if messagelist[i] == censor:
        temp = len(messagelist[i])
        messagelist [i] = "*" * temp
      #if an element is equal to the censor word, censor it (the amount of * is determined by the length of the censor word)
    messagelist = " ".join(messagelist)
      #join the list back together with the censored word
    return messagelist

  def fix_title(string):
    stringlist = string.split(":")
      #splits the string into a list at the instane of the colon : so its iterable by each element (word)
    type_title = stringlist[0].lower()
      #lowercase the first element so its interpretable
    titlesec = stringlist[1]
    titleseclist = titlesec.split(" ")
      #split the tite section so its iterable

    #empty list to append stuff to
    list1 = []

    if type_title == "article":
      for x in titleseclist:
        list1.append(x.upper())
        #for each element in the title section, capitalize the whole word to be all caps
      return " ".join(list1)
    elif type_title == "book":
      for x in titleseclist:
        list1.append(x.capitalize())
      return " ".join(list1)
        #for each element in the title section, uppercase the first character
    else:
      for x in titleseclist:
        list1.append(x.lower())
      return " ".join(list1)
        #for each element in the title section, lower the first character

  def get_longest_word(message):
    messagelist = message.split(" ")
    #split the message into a list so its iterable
    return max(messagelist,key=len)
    #return the word with the largest value (by length of the str)

  def frame(sentence):
    sentencelist = sentence.split()
    #split the sentence into a list so its iterable
    width = len(max(sentencelist, key= len))
    #the width of the list would be the length of the largest word
    height = len(sentencelist)
    #the height (the range) would be the amount of words that are in the list, so the length of sentence lsit
    border = "*" * (width+2)
    #the border would be * times by the width + 2 as you have to account for the sides which contain * from the start

    print(f"{border}")
    for i in range(height):
      difference = width-len(sentencelist[i])
      whitespace = " "*difference
      #to calculate how much space is between the side border to the word, we minus the width by the length of each word
      word = sentencelist[i] + whitespace
      #the final word includes the white space so the sides are alligned
      print(f"*{word}*")
      #print the word
    return border
    #once the for loop is done return the border so we don't return None (if we used print to print border)

  
  #test cases

  x = "hello my name is george and I LIKE cs"

  print(frame(x))

  print(get_longest_word(x))
  print(censor(x,"hello"))

  y = "article:abc def"
  z = "book:abc def"
  a = "random:texrdwWt and stuff"

  print(fix_title(y))
  print(fix_title(z))
  print(fix_title(a))

#calling main
if __name__ == "__main__":
  main()


