# Input total number of days
days = int(input("Enter number of days: "))

# Calculate years
years = days // 365
remaining_days = days % 365

# Calculate weeks
weeks = remaining_days // 7

# Remaining days
days_left = remaining_days % 7

# Display result
print("Years =", years)
print("Weeks =", weeks)
print("Days =", days_left)