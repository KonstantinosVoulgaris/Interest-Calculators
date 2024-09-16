initial_principal = 1000
annual_interest_rate = 0.05  
years = 5
future_value_compound = initial_principal * (1 + annual_interest_rate)**years
print(f"The future value with compound interest after {years} years is ${future_value_compound:.2f}")
