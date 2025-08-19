# string_formatting_examples.py

# Example 1: Using f-strings
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Example 2: Using str.format()
price = 49.99
print("The price of this item is ${:.2f}".format(price))

# Example 3: Using % operator
language = "Python"
version = 3.11
print("I am learning %s version %.1f" % (language, version))

# Example 4: Aligning text
print("{:<10} | {:^10} | {:>10}".format("Left", "Center", "Right"))

# Example 5: Padding numbers
for i in range(1, 6):
    print(f"Number: {i:03}")
