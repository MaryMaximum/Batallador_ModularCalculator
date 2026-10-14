num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
# added new variable to improve structure and code.
choice = int(input("Choose operation from 1-4:"))

print("1 = addition")
print("2 = subtraction")
print("3 = multiplication")
print("4 = division")

def add_numbers(num_1, num_2):
    return num_1 + num_2
def subtract_numbers(num_1, num_2):
    return num_1 - num_2
def multiply_numbers(num_1, num_2):
    return num_1 * num_2

# improved defining the division function and return value.

def divide_numbers(num_1, num_2):
    if num_2 == 0:
        return "Undefined."
    return num_1 / num_2
    
    
if choice == 1:
    result = add_numbers(num_1, num_2)
    print(f"Result: {result}")
    
elif choice == 2:
    result = subtract_numbers(num_1, num_2)
    print(f"Result: {result}")
    
elif choice == 3:
    result = multiply_numbers(num_1, num_2)
    print(f"Result: {result}")
    
elif choice == 4:
     result = divide_numbers(num_1, num_2)
     print(f"Result: {result}")
    
else: print("Invalid. Please select only from 1-4.")

