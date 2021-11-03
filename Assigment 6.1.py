#Name: George Sono
#Class: CSE20 Assignment 6.2
#Prof: Harikishna Kuttivelli
#Description of functions:
#load_contact_list: This function should read the contact list file that is passed in, store the contents into a dictionary of dictionaries, and return that dictionary.
#get_email: This function returns the email of the specified contact. 
#get_phone: This function returns the phone number for the specified contact. 
#get_address: This function returns the address for the specified contact. 
#get_email_list: This function returns a list of emails for all specified contacts. 
#get_phone_list: This function returns a list of phone numbers for all specified contacts.
#get_address_list: This function returns a list of addresses for all specified contacts.
#Acknowledgements: Harikishna Kuttivelli, PythonDocs, W1 schools, Class textbook

def load_contact_list(doccument):
  #initilizing the dictionary for contacts
  contacts = dict()
  with open (doccument,"r") as contactlist:
    for contactinfo in contactlist:
      #get rid of punctuation
      contactdict = dict()
      contactinfo = contactinfo.split("\n")
      contactinfo = "".join(contactinfo)
      contactinfo = contactinfo.split(", ")

      #adding info items to the dictionary (as we know the contact list is sorted by 1. name, 2. email, 3. phone, 4. address)
      contactdict['email'] = contactinfo[1]
      contactdict['phone'] = contactinfo[2]
      contactdict['address'] = contactinfo[3]
      #add dictionary to the contact dictionary
      contacts[contactinfo[0]] = contactdict
      #the key name for contacts would be the zeroth index of contact info cause the first index (0) is the name
  return contacts

#helper functions

def get_email(contacts,name):
  try:
    return contacts[name]["email"]
    #we return the email of the dictionary. we use the name as the key in contact and "email" for the key in the nameinfo. "email is already defined in loaded function"
  except KeyError:
    print(f"Error: {name} was not found in contacts")
    #throw an error code if the name is not valid

def get_phone(contacts,name):
  try:
    #we return the phone number of the dictionary. we use the name as the key in contact and "phone" for the key in the nameinfo. "email is already defined in loaded function"
    return contacts[name]["phone"]
  except KeyError:
    print(f"Error: {name} was not found in contacts")
    #throw an error code if the name is not valid
def get_address(contacts,name):
  try:
    return contacts[name]["address"]
    #we return the address of the dictionary. we use the name as the key in contact and "address" for the key in the nameinfo. "email is already defined in loaded function"
  except KeyError:
    print(f"Error: {name} was not found in contacts")
    #throw an error code if the name is not valid

def get_email_list(contacts,listofnames):
  try:
    #we make the wrong names and emails sets on purpose, so this is so there are no duplicates
    wrongnames = set()
    setofnums = set()
    finalnames = []
    for contact in contacts.keys():
      finalnames.append(contact)
    #we make a list of keys

    for eachname in listofnames:
      if finalnames.count(eachname) > 0:
        #if the listofnames is in keys, then we add it to the set of emails
        setofnums.add((contacts[eachname]["email"]))
      else:
        #otherwise we add it to the wrong names set
        wrongnames.add(eachname)
    wrongnames = ", ".join(list(wrongnames))
    #for syntax purposes we make the wrongnames a list and then make it a string
    output = f"{list(setofnums)}\nNames not found: {wrongnames}"
    if len(wrongnames) == 0:
      output = f"{list(setofnums)}"
      return output
    return output
  except KeyError:
    print(f"Error: {eachname} were not found in contacts")
    #throw an error code if the name is not valid


def get_phone_list(contacts,listofnames):
  try:
    #we make the wrong names and phonenums sets on purpose, so this is so there are no duplicates
    setofnums = set()
    finalnames = []
    wrongnames = set()
    
    for contact in contacts.keys():
      finalnames.append(contact)
    #we make a list of keys
    for eachname in listofnames:
      #if the listofnames is in keys, then we add it to the setofnums
      if finalnames.count(eachname) > 0:
        setofnums.add((contacts[eachname]["phone"]))
      else:
        #otherwise we add it to the wrongnums set 
        wrongnames.add(eachname)
    wrongnames = ", ".join(list(wrongnames))
    #for syntax purposes we make the wrongnums a list and then make it a string

    output = f"{list(setofnums)}\nNames not found: {wrongnames}"
    if len(wrongnames) == 0:
      output = f"{list(setofnums)}"
      return output

    return output
  except KeyError:
    print(f"Error: {eachname} were not found in contacts")
    #throw an error code if the name is not valid
def get_address_list(contacts,listofnames):
  try:
    #we make the wrong names and addresses sets on purpose, so this is so there are no duplicates
    setofnums = set()
    finalnames = []
    wrongnames = set()
    
    for contact in contacts.keys():
      finalnames.append(contact)
    #we make a list of keys    
    for eachname in listofnames:
      if finalnames.count(eachname) > 0:
        #if the listofnames is in keys, then we add it to the setofnums
        setofnums.add((contacts[eachname]["address"]))
      else:
        #otherwise we add it to the wrong addresses set
        wrongnames.add(eachname)
    wrongnames = ", ".join(list(wrongnames))
    #for syntax purposes we make the wrongaddresses  a list and then make it a string
    output = f"{list(setofnums)}\nNames not found: {wrongnames}"
    if len(wrongnames) == 0:
      output = f"{list(setofnums)}"
      return output
    return output


  except KeyError:
    print(f"Error: {eachname} not found in contacts")
    #throw an error code if the name is not valid

#defining main
def main():
  #test cases
  contacts = load_contact_list("sample_contact_list.txt")
  print("TEST CASES")
  name = "Sandy Cheeks"
  names = ["Sandy Cheeks","Avatar Aang","Ariana Grande"]
  print(f"\nTEST NAME: {name}")
  print(contacts["Sandy Cheeks"])
  print(f"Output: {get_email(contacts,name)}")
  print(f"Output: {get_phone(contacts,name)}")
  print(f"Output: {get_address(contacts,name)}")

  print(f"\nTEST NAMEs: {names}")
  print(f"Output: {get_email_list(contacts,names)}")
  print(f"Output: {get_phone_list(contacts,names)}")
  print(f"Output: {get_address_list(contacts,names)}")

  name = "Deez Nuts"
  names = ["Sandy Cheeks","Ligma","Ariana Grande","Bofa"]

  print(f"\nTEST NAME: {name}")
  print(f"Output: {get_email(contacts,name)}")
  print(f"Output: {get_phone(contacts,name)}")
  print(f"Output: {get_address(contacts,name)}")
  print(f"\nTEST NAMEs: {names}")
  print(f"Output: {get_email_list(contacts,names)}")
  print(f"Output: {get_phone_list(contacts,names)}")
  print(f"Output: {get_address_list(contacts,names)}")

#calling main
if __name__ == "__main__":
  main()


