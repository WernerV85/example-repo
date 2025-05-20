#num_list = []
num_input = int(input(f"Please give any number: "))
while num_input > 0 :
    num_input += num_input
    if num_input == -1:
        num_ave = num_input #/ len(num_list)
        print(num_ave)