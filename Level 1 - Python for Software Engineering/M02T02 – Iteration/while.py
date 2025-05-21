num_input = 1
num_count = 0
num_total = 0


while num_input >= 1:
    num_input = int(input(f"Please give any number: "))
    num_total += num_input
    num_count +=1

    if num_input == -1:
        num_total += 1
        num_count -= 1
        print(f"The sum of the values are: {num_total}")
        print(f"The count of the values you've entered is: {num_count}")
        num_ave = num_total / num_count
        print(f"Average of the numbers entered is: {num_ave}")

    elif num_input == 0:
        print(f"Invalid input")

    