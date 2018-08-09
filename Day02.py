"""Given the meal price (base cost of a meal), tip percent
(the percentage of the meal price being added as tip), and tax percent
(the percentage of the meal price being added as tax)
for a meal, find and print the meal's total cost."""

# Complete the solve function below.


meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
tip_cost = ((tip_percent/100)*meal_cost)
tax_cost = ((tax_percent/100)*meal_cost)
Cost = (tip_cost + tax_cost + meal_cost)
totalCost = round(Cost)
print("The total meal cost is " + str(totalCost) + " dollars.")
