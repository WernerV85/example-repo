#-----Auto grade task2

#String Manipulation

#set variable as well as request input from user for sentence
str_manip = input("Please supply any sentence: ")
#print the lenght of the input sentence from user
print(f"Length of sentence is {len(str_manip)} characters")

#Identify last character in sentence
#create variable for last character for later use
last_char = str_manip[-1]
#print last character
print(last_char)

#replacing last character with @ through the whole sentence
str_manip = str_manip.replace(last_char, "@")
#printing new sentence with replacement in place
print( {str_manip} )

#Undo replace script
str_manip = str_manip.replace("@", last_char)

#printing the last 3 letters of the sentence
print(str_manip[len(str_manip):len(str_manip)-4:-1])

#printing the first 3 and last 2 letters of the sentence to create a new word
print(str_manip[0 : 3 : 1] + str_manip[len(str_manip)-2 : len(str_manip) : 1])