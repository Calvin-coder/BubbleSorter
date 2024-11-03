import random
#Function that checks next number and if it's bigger it switches the numbers and then goes back from last to first to sort them all.
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

numbers = [random.randint(1, 100) for _ in range(10)]
original_numbers = numbers.copy()
sorted_numbers = bubble_sort(numbers.copy())
print("Original list:", original_numbers)
print("Sorted list:", sorted_numbers)
