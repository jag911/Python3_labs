laps = 45
fuel_per_lap = 2.25

min_fuel = laps * fuel_per_lap
contengent_fuel = min_fuel * 1.5
print(f"minimum: {min_fuel}  contingent: {contengent_fuel}")

qual_time = 80.45
multiplier = (contengent_fuel - 5) / 10
first_lap = (multiplier * .35) + qual_time

print(f"multiplier: {multiplier}  first_lap: {first_lap}")
