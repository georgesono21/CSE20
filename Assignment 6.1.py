#Name: George Sono
#Class: CSE20 
#Prof: Harikishna Kuttivelli
# dict_equal(dict1, dict2): return True if dict1 and dict2 are the same, false otherwise.
# count_words(sentence): returns a dictionary with all the words in sentence in lower case as keys, and the value of each key is the number of times that word appears in a sentence.
# morse(sentence): returns a string that is a conversion of sentence into Morse code.
#Acknowledgements: Harikishna Kuttivelli, PythonDocs

#defining main function

def dict_equal(d1,d2):
  #how it works: we make four lists. this is because each dictionary has key and values. we the compare the keylists together to see if they have the same elements, if not we return false (same with the valuelists)
  keycheck_d1 = []
  valcheck_d1 = []
  keycheck_d2 = []
  valcheck_d2 = []

  #adding each key and value to an empty list
  for x in d1.keys():
    keycheck_d1.append(x)
    valcheck_d1.append(d1[x])
  for x in d2.keys():
    keycheck_d2.append(x)
    valcheck_d2.append(d2[x])

  #if theres more keys in one keylist than the other, than return False
  if len(keycheck_d1) != len(keycheck_d2):
    return False
  else:
    #if the dict1 key is not in dict2keylist return false (same with value)
    for x in range(len(keycheck_d1)):
      if keycheck_d1[x] not in keycheck_d2:
        return False
      if valcheck_d1[x] not in valcheck_d2:
        return False
    #returns True if the for loop is finished, this means that the dicts are same
    return True

def count_words(sentence):
  #how it works: to process the sentence, we get rid of any punctuation and lower  case all the letters in the sentence. we then string split it at the blank spaces to form it into a list (so its iterable). then we use a for loop to check how many times a word is in the sentencelist.
  sentencedict = {}
  #getting rid of any punctuation
  sentence = sentence.split(",")
  sentence = "".join(sentence)
  sentence = sentence.split(".")
  sentence = "".join(sentence)
  sentence = sentence.split()

  #lower casing all elements in the sentencelist
  for i in range(len(sentence)):
    sentence[i] = sentence[i].lower()

  for x in sentence:
    counter = 0
    for i in range(len(sentence)):
      if x == sentence[i]:
        counter += 1
      #this for loop keeps checking if the word (x) is in the sentence. as we already know theres one of it (as were using that to compare) the range includes the whole entire list (so x is counted). it checks if its in the sentence by checking it with the index value at i in the sentence list.

    sentencedict[x] = counter
    #assigning the key value pair in the sentence dictionary
  return sentencedict

def morse(message):
  #how it works: we split the message at the spaces so we get an iterable list. we then make a for loop inside of a for loop (forloopception) that iterates each letter in the word and translates it to its morse counterpart.
  #defining the dictionary for morse code (thank you Hari)
  code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    }
  #splitting the mssage
  message = message.split()

  #what the morsemessage is gonna be (we just defining it rn tho)
  actualmessage = ""

  #for loop ception: the first for loop is so all the words in the message list are iterated
  
  for x in range(len(message)):
    wordinmorse = ""
    #forloop pt2: so we iterate each letter in the word from messagelist
    counter = 0
    for i in message[x]:
      counter += 1
      if message[x] == message[-1] and counter == len(message[x]):
        wordinmorse += code[i.upper()]
      else:
        wordinmorse += code[i.upper()] + " "
      #as the morsecode thing only accepts uppercase letters, we translate that into an upper character so it has a value because its a key
      

      
    if x == (len(message)-1):
      actualmessage += wordinmorse
      #if we are on the last number of the list we dont use the / for a space
    else:
      #else we just add the / as theres gonna be another word
      actualmessage += wordinmorse + "/ "
  return actualmessage

def main():
  
  #TEST CASES

  print(dict_equal({"name1": "Alice", "name2": "Bob"}, {"name2": "Bob", "name1": "Alice"}))
  #--> True
  print(dict_equal({}, {}))
  #--> True
  print(dict_equal({"Name1": "Alice", "Name2": "Bob"}, {"name2": "Bob", "name1": "Alice"}))
  #--> False
  print(dict_equal({"fruit": "banana"}, {"fruit": "banana", "meat": "beef"}))
  #--> False

  print(count_words("The good, the bad, and the ugly."))
  #--> {"the": 3, "good": 1, "bad": 1, "and": 1, "ugly": 1}
  print(count_words("One fish, two fishes, red fish, blue fish"))
  #--> {"one": 1, "fish": 3, "two": 1, "fishes": 1, "red": 1, "blue": 1}
  print(count_words("One and one, two and two.")) 
  #--> {"one": 2, "and": 2, "two": 2}

  print(morse("hello"))
  #--> ".... . .-.. .-.. ---"
  print(morse("World")) 
  #--> ".-- --- .-. .-.. -.."
  print(morse("Hello World"))
  #--> ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
  print(morse("SOS"))
  #--> "... --- ..."

#calling the main function
if __name__ == "__main__":
  main()
