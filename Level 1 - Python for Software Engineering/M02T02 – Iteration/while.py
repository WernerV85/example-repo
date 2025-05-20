num_input = 0
num_list = 0

num_input = int(input(f"Please give any number: "))
while num_input > 0:
    num_input = int(input(f"Please give any number: "))
    num_input += num_input
    num_list +=1
    num_ave = num_input / num_list
    print(num_ave)
    if num_input < 0:
        continue
    print(num_ave)
    