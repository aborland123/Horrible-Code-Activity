# Violates:
# 1. KISS
# 2. DRY
# 3. Single Responsibility
# 4. Clean Code

def main():
    print("Choose:")
    print("1 - add")
    print("2 - subTract")
    print("3 - multiply")
    print("4 - divide")
    do = input("do operation: ")
    if do == "1":
        x = input("enter num 1: ")
        y = input("enter num 2: ")
        x = float(x)
        y = float(y)
        print("res is " + str(x + y))
    if do == "2":
        x = input("enter num 1: ")
        y = input("enter num 2: ")
        x = float(x)
        y = float(y)
        print("res is " + str(x - y))
    if do == "3":
        x = input("enter num 1: ")
        y = input("enter num 2: ")
        x = float(x)
        y = float(y)
        print("res is " + str(x * y))
    if do == "4":
        x = input("enter num 1: ")
        y = input("enter num 2: ")
        x = float(x)
        y = float(y)
        if y == 0:
            print("nah")
        else:
            print("res is " + str(x / y))
    else:
        print("bruh what is that")

if __name__ == "__main__":
    main()
