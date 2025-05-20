num_input = []
num_input = int(input(f"Please give any number: "))

while num_input > 0 :
    num_input = int(input(f"Please give any number: "))
    num_input += num_input
    if num_input == -1:
        continue
    num_ave = num_input / len(num_input)
    print(num_ave)