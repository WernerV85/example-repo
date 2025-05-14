#****Task****

#Create variables for each part of the Triathlon and ask input from user.
#to ensure input is integer, values are cast as integer
swim_time = int(input("Please give your time (in minutes) for the Swimming section of the Triathlon: "))
cycle_time = int(input("Please give your time (in minutes) for the Cycling section of the Triathlon: "))
run_time = int(input("Please give your time (in minutes) for the Running section of the Triathlon: "))

#After input, calculate the sum of the inputs
total_time = swim_time + cycle_time + run_time

#print the sum of the inputs from the calculation above
print(f"Total time to complete the Triathlon: {total_time} minutes")

#start if statement to set the criteria:
#first criteria is to calculate if time is between 0 and 100 minutes
if total_time >= 0 and total_time <= 100:
#if above criteria is true the statement Provincial colours will be printed on screen
    print("Award: Provincial Colours.")
#second criteria is to check if time is between 101 and 105 minutes
elif total_time >= 101 and total_time <= 105:
#if this criteria is true the statement of Provincial half colours will be printed on screen
    print("Award: Provincial Half Coulours.")
#third criteria is to check if time is between 106 and 110 minutes
elif total_time >= 106 and total_time <= 110:
#if criteria 3 is true the statement provincial Scroll will be printed on screen
    print("Award: Provincial Scroll.")
#if none of the criteria above is true, the statement No Award will be printed on screen
else:
    print("No Award!")

    #end

