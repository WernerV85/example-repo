num_input = 0
num_list = 0

num_input = int(input(f"Please give any number: "))
while num_input > 0:
    num_input = int(input(f"Please give any number: "))
    num_input += num_input
    num_list +=1
    
    
    if num_input == -1:
        num_ave = num_input / num_list
        print(f"Average of the numbers entered is: {float(num_ave)}")
    