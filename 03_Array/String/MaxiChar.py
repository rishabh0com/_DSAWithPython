def find_max_char(s):
    # Initialize a dictionary to store the count of each character
    count_dict = {}

    # Iterate through the string
    for char in s:
        # Update the count for each character
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    # Find the character with the maximum count
    max_count = 0
    max_char = None
    for char, count in count_dict.items():
        if count > max_count:
            max_count = count
            max_char = char

    return max_char


# Given string
s = "aabcaa"

# Find the maximum character
result = find_max_char(s)

# Print the result
print(f"The maximum character that occurs in the string '{s}' is '{result}'.")
