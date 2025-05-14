swim_time = int(input("Please give your time (in minutes) for the Swimming section of the Triathlon: "))
cycle_time = int(input("Please give your time (in minutes) for the Cycling section of the Triathlon: "))
run_time = int(input("Please give your time (in minutes) for the Running section of the Triathlon: "))

total_time = swim_time + cycle_time + run_time

print(f"Total time to complete the Triathlon: {total_time} minutes")

if total_time >= 0 or total_time <= 100:
    print("Award: Provincial Colours.")
elif total_time >= 101 and total_time <= 105:
    print("Award: Provincial Half Coulours.")
elif total_time >= 106 and total_time <= 110:
    print("Award: Provincial Scroll.")
else:
    print("No Award!")
    
