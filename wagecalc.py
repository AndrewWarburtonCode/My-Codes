# --- Display a greeting ---
greeting = "Hello "
name = input("Enter name: ")
print(greeting + name)

# --- Calculate the yearly income ---

hourly_wage = int(input("Hourly pay: "))
hours_per_week = int(input("Hours per week: "))
income_per_week = (hourly_wage * hours_per_week)
weeks_per_year = (48)
income_per_year = (weeks_per_year * income_per_week)

print(name + "'s yearly income is:")
print(income_per_year)

# --- Calculate the yearly spend ---
spend_per_week = int(input("Spend per week: "))
spend_per_year = (spend_per_week * 52)
print(name + "'s yearly spend is:")
print(spend_per_year)


# --- Calculate the yearly savings ---
savings_per_year = (income_per_year - spend_per_year)
print(name + "'s yearly savings:")
print(savings_per_year)
