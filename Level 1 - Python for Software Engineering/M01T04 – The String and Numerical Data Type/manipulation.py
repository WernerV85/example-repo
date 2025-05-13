str_manip = input("Please supply any sentence: ")
print(f"Length of sentence is {len(str_manip)} characters")

last_char = str_manip[-1]
print(last_char)

str_manip = str_manip.replace(last_char, "@")
print(f"str_manip.replace(): {str_manip}")

print(str_manip[len(str_manip):len(str_manip)-4:-1])

print(str_manip[0:3:1] + str_manip[len(str_manip):len(str_manip)-3:-1])