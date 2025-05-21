num_input = 0
num_list = 0
num_total = 0

#num_input = int(input(f"Please give any number: "))
while num_input > 0:
    num_input = int(input(f"Please give any number: "))
    num_total += num_input
    num_list +=1
    #print(f"The sum of the values are: {num_total}")
    #print(f"The count of the values are: {num_list}")
    if num_input == -1:
        num_total += 1
        num_list -= 1
        print(f"The sum of the values are: {num_total}")
        print(f"The count of the values are: {num_list}")
        num_ave = num_total / num_list
        print(f"Average of the numbers entered is: {num_ave}")
    