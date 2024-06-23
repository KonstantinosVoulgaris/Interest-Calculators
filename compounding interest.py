# Parameters
initial_principal = 1000
annual_interest_rate = 0.05  # 5% interest rate
years = 5

# Calculate future value using compound interest
future_value_compound = initial_principal * (1 + annual_interest_rate)**years

# Print the result
print(f"The future value with compound interest after {years} years is ${future_value_compound:.2f}")