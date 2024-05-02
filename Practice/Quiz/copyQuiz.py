def copy_list():
    """
    This function demonstrates the usage of the copy() method to create a shallow copy of a list.
    It creates a copy of the list 'x' and appends an element to the original list.
    """

    x = [1, 2, 3]
    y = x.copy()  # Creates a shallow copy of the list 'x'
    x.append(4)  # Appends an element to the original list 'x'
    print(f"Original list: {x}, Copied list: {y}")

copy_list()