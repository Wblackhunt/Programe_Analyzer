# test_program.py

def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

if __name__ == "__main__":
    greet("World")
    result = add(5, 3)
    print(f"The sum is: {result}")