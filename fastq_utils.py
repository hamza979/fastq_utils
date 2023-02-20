import argparse

def add(num1, num2):
    """Add two numbers"""
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")


def main():
    parser = argparse.ArgumentParser(description="simple command line tool")
    parser.add_argument("operation", choices=["add"], help="operation to perform")
    parser.add_argument("num1", type=int, help="first number")
    parser.add_argument("num2", type=int, help="second number")
    args = parser.parse_args()

    if args.operation == "add":
        add(args.num1, args.num2)

if __name__ == "__main__":
    main()
