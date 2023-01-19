from utils import get_user_text


# ask the user for their name
name = get_user_text("What is your name? ")

# ask the user for their age
age = get_user_text("What is your age? ")

# print out a personalized message
print("Hello, " + name + "! You are " + age + " years old.")
