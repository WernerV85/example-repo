num_input = 0
num_list = []

#num_input = int(input(f"Please give any number: "))
while num_input != -1:
    num_input = int(input(f"Please give any number: "))
    num_input += num_input
    num_list.append(num_list)
    num_ave = num_input / len(num_list)
    if num_input == -1:
        print(num_input)
        print(num_list)
        print(float(num_ave))
    else :
        print("Exit!!")