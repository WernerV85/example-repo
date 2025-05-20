num_list = []
num_input = 0

while num_input > 0 :
    num_input += num_input
    num_list = num_list.append(num_input)
    if num_input == -1:
        print(num_input)
        #num_ave = num_input / len(num_input)
        #print(num_ave)