# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Function to reverse a string
def reverse_string(text):
    return text[::-1]

# Function to count the number of vowels in a string
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

# Function to calculate factorial of a non-negative integer
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Decorator function
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

# Function to apply decorator
def apply_decorator(func):
    return decorator_func(func)

# Function to sort list of tuples by age
def sort_by_age(data):
    return sorted(data, key=lambda x: x[1])

# Function to merge two dictionaries with summed values for common keys
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

# Class definition
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Example usage
if __name__ == "__main__":
    # Test functions
    print(add_numbers(2, 3))  # Output: 5
    print(is_even(2))         # Output: True
    print(reverse_string("hello"))  # Output: "olleh"
    print(count_vowels("hello"))  # Output: 2
    print(calculate_factorial(5))  # Output: 120

    @apply_decorator
    def sample_function():
        return "Function Called"
    
    print(sample_function())  # Output: "Decorator Applied" and "Function Called"

    data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    print(sort_by_age(data))  # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]

    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    print(merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 5, 'c': 4}

    car = Car("Toyota", "Corolla", 2020)
    car.display_info()  # Output: Make: Toyota, Model: Corolla, Year: 2020
