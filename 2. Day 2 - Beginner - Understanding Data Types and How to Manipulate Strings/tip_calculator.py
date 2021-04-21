# Tip Calculator

#1. Create a greeting for your program.
print("Welcome to the tip calculator")

#2. Ask the user to input the total bill
bill = float(input('What is the total bill? Kshs\n'))

#3. Ask the user for tip percentage of the total amount
tip = int(input('How much tip would you like to give? 10, 12 or 15?\n'))

#4. How many people are splitting the bill
people = int(input('How many people are splitting the bill?\n'))

#5. Tip as percent
tip_as_percent = tip/100

#5. Calculate total tip amount 
total_tip_amount = bill * tip_as_percent

#6. Calculate total amount to be paid

total_bill = total_tip_amount + bill 


#7. divide by number of people to get individual contribution
bill_per_person = total_bill / people

# Rounding off to the nerarest 2 decimal places
final_amount = round(bill_per_person, 2)

print(f'Individual Contribution {final_amount} Kshs')

