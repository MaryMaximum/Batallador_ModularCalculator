num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

input("Choose operation: ")

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
def divide_numbers(num_1, num_2):
    return num_1 / num_2
    
if input == 1:
    result = add_numbers(num_1, num_2)
    print(f"Result: {result}")
    
elif input == 2:
    result = subtract_numbers(num_1, num_2)
    print(f"Result: {result}")
    
elif input == 3:
    result = multiply_numbers(num_1, num_2)
    print(f"Result: {result}")
    
elif input == 4:
     result = divide_numbers(num_1, num_2)
     print(f"Result: {result}")
    
elif input == (0, 5-9): print("Invalid. Please select only from 1-4.")






