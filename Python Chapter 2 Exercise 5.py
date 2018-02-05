# Katelyn Simonton - Python Chapter 2 Exercise 5

# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

inp = int(input("Enter Celsius Temperature: "))
cel = int(inp)
fah = (int(cel) * 1.8) + 32
print(str(fah))