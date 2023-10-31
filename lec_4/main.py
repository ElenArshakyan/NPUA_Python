def classify_numbers(int_numbers):
    even_numbers = []
    odd_numbers = []

    for num in int_numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers
user_input = input("Enter numbers : ")
int_numbers = [int(x) for x in user_input.split()]

even_numbers, odd_numbers = classify_numbers(int_numbers)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
