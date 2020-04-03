# Prompt the user for a number in degrees Celsius, and convert the value to degrees in Fahrenheit and display it to the user.

result = 0.0
temp_C = 0.0
temp_F = 0.0

temp_C = float(input('Temperature in C? '))

temp_F = (temp_C * (9/5)) + 32
result = f'{temp_F} F'

print(result)
