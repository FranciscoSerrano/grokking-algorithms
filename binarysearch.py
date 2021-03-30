def binary_search(numbers, number_to_find):
	low = 0
	high = len(numbers) - 1
	while low <= high:
		middle = low + (high - low) // 2

		if numbers[middle] == number_to_find:
			return middle
		elif numbers[middle] < number_to_find:
			low = middle + 1
		else:
			high = middle - 1
	return -1

numbers = [7, 9, 14, 22, 34]
number_to_find = 22

final = binary_search(numbers, number_to_find)

if final == -1:
	print("\nThis item was not found in the list.")
else:
	print("\nThe number " + str(number_to_find) + " was found at index position " + str(final) + ".")

