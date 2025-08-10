def sort_numbers(numbers):
    """
    Sorts a list of numbers in ascending order.

    Args:
        numbers (list): A list of numbers to sort.

    Returns:
        list: Sorted list of numbers.
    """
    return sorted(numbers)

# Take input from console
input_str = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_str.strip().split()))
sorted_numbers = sort_numbers(numbers)
print("Sorted numbers:", sorted_numbers)

