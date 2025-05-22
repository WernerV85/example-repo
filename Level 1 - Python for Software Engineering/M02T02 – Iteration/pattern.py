## Auto Graded task 1

print("Auto-graded task 1")


# Assign value to created varible 
count_num = 0

# Start for loop with inbedded if statement
# if statement is to look for the range of value
# if range reaches 5 count down stated
for i in range (0, 8):
    if i == 0 or i < 5:
        i += 1
        count_num = i
        print("*" * count_num)
    elif i == 5 or i < 8:
        count_num -= 1
        print("*" * count_num)
