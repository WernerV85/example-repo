num_list = []
num_list = int(input(f"Please give any number: "))
num_input = 0
while num_input > 0 :
    num_input = int(input(f"Please give any number: "))
    num_input += num_list
    if num_input == -1:
        break
print(num_input)
        #num_ave = num_input / len(num_input)
        #print(num_ave)