# Principles used:
# 1. KISS
# 2. DRY
# 3. Single Responsibility
# 4. Clean Code

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

def get_user_input():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Please enter valid numbers.")
        return get_user_input()

def show_menu():
    print("\nChoose operation:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")

def main():
    show_menu()
    choice = input("Enter choice (1/2/3/4): ")

    a, b = get_user_input()

    if choice == '1':
        print("Result:", add(a, b))
    elif choice == '2':
        print("Result:", subtract(a, b))
    elif choice == '3':
        print("Result:", multiply(a, b))
    elif choice == '4':
        print("Result:", divide(a, b))
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
