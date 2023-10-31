def main():
    print("Simple Calculator")

    while True:
        try:
            expression = input("Enter an expression (e.g., 2 + 3): ")

            if expression.lower() == "exit":
                print("Goodbye!")
                break

            result = eval(expression)
            print("Result: " + str(result))
        except Exception as e:
            print("Error: " + str(e))

if __name__ == "__main__":
    main()