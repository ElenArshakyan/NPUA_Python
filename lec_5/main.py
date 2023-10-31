# Function to calculate the sum of elements, optionally excluding negatives
def sum_of_elements(numbers, exclude_negative=False):
    if exclude_negative:
        filtered_numbers = [num for num in numbers if num >= 0]
        total = sum(filtered_numbers)
    else:
        total = sum(numbers)
    return total
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

exclude_negative_input = input("Do you want to exclude negative numbers? (yes or no): ").strip().lower()
exclude_negative = exclude_negative_input == "yes"

result = sum_of_elements(numbers, exclude_negative)

if exclude_negative:
    print("Sum of non-negative numbers:", result)
else:
    print("Sum of all numbers:", result)
