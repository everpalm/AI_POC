"""
This script is a simple calculator that can perform basic
arithmetic operations: addition, subtraction, multiplication, and
division. The user can input two numbers and choose an operation.

Usage:
1. Run the script.
2. Input the first number when prompted.
3. Input the second number when prompted.
4. Choose the operation by entering 1 for addition, 2 for subtraction,
   3 for multiplication, or 4 for division.
5. The result will be displayed.
"""

def add(x, y):
    """Return the sum of x and y."""
    return x + y


def subtract(x, y):
    """Return the difference of x and y."""
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def divide(x, y):
    """Return the quotient of x and y. Raises an error if y is 0."""
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y


def main():
    """Main function to run the calculator logic."""
    print('Welcome to the Simple Calculator!')
    # Input first number
    num1 = float(input('Enter first number: '))
    # Input second number
    num2 = float(input('Enter second number: '))
    
    # Ask user for operation choice
    print('Choose an operation:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    choice = input('Enter choice (1/2/3/4): ')
    
    # Perform the calculation based on user choice
    if choice == '1':
        print(f'The result is: {add(num1, num2)}')
    elif choice == '2':
        print(f'The result is: {subtract(num1, num2)}')
    elif choice == '3':
        print(f'The result is: {multiply(num1, num2)}')
    elif choice == '4':
        try:
            print(f'The result is: {divide(num1, num2)}')
        except ValueError as e:
            print(e)
    else:
        print('Invalid input! Please enter a number between 1 and 4.')


if __name__ == '__main__':
    main()