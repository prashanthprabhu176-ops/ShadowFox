your_expenses = {
    "Travel": 2500,
    "Food": 1200,
    "Stay": 1900,
    "Attractions": 2650,
    "Other Expense": 600
}

partner_expenses = {
    "Travel": 2300,
    "Food": 1000,
    "Stay": 1900,
    "Attractions": 1800,
    "Other Expense": 600
}

# totals
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())
print()
print("Your total:", your_total)
print("Partner total:", partner_total)
print()

if(your_total>partner_total):
    print("You spent more than your partner")
elif(your_total<partner_total):
    print("Your partner spent more than you")

print()

# find max difference
max_diff = 0
max_category = ""

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])

    if diff > max_diff:
        max_diff = diff
        max_category = category

print(f"Highest difference is in '{max_category}' with a difference of {max_diff}")
print()

#output : 

# Your total: 8850
# Partner total: 7600

# You spent more than your partner

# Highest difference is in 'Attractions' with a difference of 850
