def find_most_frequent_number(arr):
    # Initialize a dictionary to store the count of each element
    count_dict = {}

    # Iterate through the array
    for num in arr:
        # Update the count for each element
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Find the element with the maximum count
    max_count = 0
    most_frequent_number = None
    for num, count in count_dict.items():
        if count > max_count:
            max_count = count
            most_frequent_number = num

    return most_frequent_number


# Given array
arr = [1, 2, 1, 2, 1, 1, 1]

# Find the most frequent number
result = find_most_frequent_number(arr)

# Print the result
print(f"The number **{result}** appears most frequently in the array.")
