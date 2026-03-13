# Input Principal, Time, and Rate
P = float(input("Enter Principal amount: "))
T = float(input("Enter Time (in years): "))
R = float(input("Enter Rate of interest: "))

# Calculate Compound Amount
A = P * (1 + R/100) ** T

# Calculate Compound Interest
CI = A - P

# Display result
print("Compound Interest =", CI)