def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    total_cost = meal_cost + tip + tax

    print(round(total_cost))

solve(12.00, 20, 8)
