
#*****Auto grade task 1*******

#create sentence to save
save_sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

#create replace function and charcters to replace
save_sentence = save_sentence.replace("!", " ")
#print function
print(f"save_sentence.replace(): {save_sentence}")


#***Print as uppercase**
save_sentence = save_sentence.upper()
print(f"save_Sentance.upper(): {save_sentence}")

#printing sentence in reverse
print(save_sentence[::-1])