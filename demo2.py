from utils import get_user_fraction, get_user_text

# ask the user which conversion they would like to make
conversion = get_user_text("Would you like to convert from (C)elsius to Fahrenheit, or from (F)ahrenheit to Celsius? ")

# get a number from user
temperature = get_user_fraction("Enter the temperature: ")

# convert
if conversion == 'C':
    print(f"The temperature in Fahrenheit is {temperature * 9/5 + 32}")
else:
    print(f"The temperature in Celsius is {(temperature - 32) * 5/9}")
