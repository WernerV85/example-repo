#num_list = []
num_input = ()
num_ave = num_input / len(num_input)
while num_input > 0 :
    num_input = int(input(f"Please give any number: "))
    num_input += num_input
    if num_input == -1:
        print(num_ave)