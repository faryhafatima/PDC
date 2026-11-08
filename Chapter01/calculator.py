
def multiply(a, b):
    return a * b
 
 
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
 
 
def add(a, b):
    return a + b
 
 
def subtract(a, b):
    return a - b
 
 
def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
 
    print(f"\nMultiplication: {a} * {b} = {multiply(a, b)}")
    try:
        print(f"Division:       {a} / {b} = {divide(a, b)}")
    except ZeroDivisionError as e:
        print(f"Division:       Error - {e}")
    print(f"Addition:       {a} + {b} = {add(a, b)}")
    print(f"Subtraction:    {a} - {b} = {subtract(a, b)}")
 
 
if __name__ == "__main__":
    main()
 