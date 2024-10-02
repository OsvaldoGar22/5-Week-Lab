
# Exercise 1 - Kilometer Converter

# CONVERSION_FACTOR = 0.6214
#
# def main():
#     kilometers = float(input("Enter a distance in Kilometers: "))
#     show_miles(kilometers)
#
# def show_miles(km):
#     miles = km * CONVERSION_FACTOR
#     print(f"{km:.2f} kilometers equals {miles:.2f} miles.")
#
# main()

#---------------------------------------------------------------------------------

# Exercise 2 - Sales Tax Program Refactoring

# def main():
#     price = float(input("How much does the item cost? $"))
#     tax(price)
#
# def tax(amount):
#     sales_tax = amount * 0.05
#     county_sales_tax = amount * 0.025
#     total = amount + sales_tax + county_sales_tax
#     print(f"Total: ${total:.2f}")
#
# main()

#---------------------------------------------------------------------------------

# Exercise 3 - How much insurance?

# replacement_cost = float(input("What is the replacement cost of the building: $"))
#
# min_insurance = replacement_cost * 0.80
# print(f"The minimum amount of insurance you should buy for the propertyh is: ${min_insurance:.2f}")

#---------------------------------------------------------------------------------

# Exercise 4 - Automobile costs

# def calculate_car_costs():
#     loan = float(input("How much is your monthly car loan payment: $"))
#     insurance = float(input("How much is your monthly car insurance: $"))
#     gas = float(input("How much do you pay for gas every month: $"))
#     oil = float(input("How much do you pay for oil change every month: $"))
#     tires = float(input("How much do you pay for tires every month: $"))
#     maintenance = float(input("How much do you pay for general car maintenance every month: $"))
#
#     monthly_costs = loan + insurance + gas + oil + tires + maintenance
#     annual_costs = monthly_costs * 12
#     print(f"Your monthly costs is ${monthly_costs:.2f}.")
#     print(f"You yearly costs is ${annual_costs:.2f}.")
#
# calculate_car_costs()

#---------------------------------------------------------------------------------

# Exercis 5 - Property Tax

# def main():
#     actual_value = float(input("What is the Actual Value of the property: $"))
#
#     assessed_value = assessment_value(actual_value)
#
#     property_tax = calc_tax(assessed_value)
#
#     print(f"Assessment Value: ${assessed_value:.2f}") 
#     print(f"Property Tax: ${property_tax:.2f}")
#
# def assessment_value(value):
#     return value * 0.6 
#
# def calc_tax(value):
#     hundreds = value / 100
#     return hundreds * 0.72
#
# main()

#---------------------------------------------------------------------------------

# Exercise 6 - Stadium Seating

# def main():
#     class_a = int(input("How many Class A seats were sold? "))
#     class_b = int(input("How many Class B seats were sold? "))
#     class_c = int(input("How many Class C seats were sold? "))
#     total_seats = calc_seats(class_a, class_b, class_c)
#     print(f"The total generated income from ticket sales was ${total_seats:.2f}")
#
# def calc_seats(seat_a, seat_b, seat_c):
#     high_seats = seat_a * 20 
#     mid_seats = seat_b * 15 
#     low_seats = seat_c * 10 
#
#     total = high_seats + mid_seats + low_seats
#     return total
#
# main()

#---------------------------------------------------------------------------------

# Exercise 7 - Paint Job Estimator

# import math
#
# def main():
#     square_feet = float(input("Enter the square feet of wall space to be painted: "))
#     price_per_gallon = float(input("Enter the prince of paint per gallon: "))
#
#     gallons_required = math.ceil(square_feet / 112)
#
#     labor_hours = gallons_required * 8
#
#     print(f"Number of gallons of paint required: {gallons_required}")
#     print(f"Hours of labor required: {labor_hours}")
#
# main()

#---------------------------------------------------------------------------------

# Exercise 8 - Monthly Sales Tax

# def main():
#     total_sales = float(input("Enter the total sales for the month: "))
#
#     county_tax_rate = 0.025
#     state_tax_rate = 0.05
#
#     county_sales_tax = total_sales * county_tax_rate
#     state_sales_tax = total_sales * state_tax_rate
#     total_sales_tax = county_sales_tax + state_sales_tax
#
#     print(f"County Sales Tax: ${county_sales_tax:.2f}")
#     print(f"State Sales Tax: ${state_sales_tax:.2f}")
#     print(f"Total Sales Tax: ${total_sales_tax:.2f}")
#
# main()

#---------------------------------------------------------------------------------

# Exercise 9 - Feet to Inches

# INCHES_PER_FOOT = 12
#
# def main():
#     feet = int(input("Entre a number of feet: "))
#     print(f"{feet} feet equals {feet_to_inches(feet)} inches")
#
# def feet_to_inches(feet):
#     return feet * INCHES_PER_FOOT 
#
# main()

#---------------------------------------------------------------------------------

# Exercise 10 - Math Quiz

# import random
#
# def main():
#     num1 = random.randint(1, 500)
#     num2 = random.randint(1, 500)
#
#     print(f"What is {num1} + {num2}?")
#
#     guess = int(input("Your Answer: "))
#
#     correct_answer = check_answer(num1, num2, guess) 
#
# def check_answer(num1, num2, guess):
#     correct = num1 + num2
#     if guess == correct:
#         print("Congratulations! That's Correct")
#     else:
#         print(f"That is wrong. The correct answer is {correct}")
#
# main()





