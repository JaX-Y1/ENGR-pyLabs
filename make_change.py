# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Rishi Bandhu
# SK Thippireddy
# Andrew Marshall
# Preston Montgomery
# Section: 522
# Assignment: Lab 4.13
# Date: 09/12/2023

    # Prompt user for input
paid = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))

# Calculate change
change = paid - cost

    # Convert change to cents to avoid floating point errors
change_in_cents = int(change * 100)

    # Calculate number of quarters, dimes, nickels, and pennies
quarters = change_in_cents // 25
dimes = (change_in_cents % 25) // 10
nickels = ((change_in_cents % 25) % 10) // 5
pennies = (((change_in_cents % 25) % 10) % 5) 

    # Print the results
print(f"You received ${change:.2f} in change. That is...")

if quarters > 1:
    print(f"{quarters} quarters")
elif quarters == 1:
    print(f"{quarters} quarter")

if dimes > 1:
    print(f"{dimes} dimes")
elif dimes == 1:
    print(f"{dimes} dime")

if nickels > 1:
    print(f"{nickels} nickels")
elif nickels == 1:
    print(f"{nickels} nickel")
    
if pennies > 1:
    print(f"{pennies} pennies")
elif pennies == 1:
    print(f"{pennies} penny")
if (change_in_cents <= 1):
    print("1 penny")


