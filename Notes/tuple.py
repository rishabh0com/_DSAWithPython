"""
    This function demonstrates the usage of a Python tuple.

    A tuple is an immutable sequence of elements, enclosed in parentheses ().
    It can contain elements of different data types, such as integers, strings, or even other tuples.

    Returns:
        tuple: A tuple containing the elements specified in the code.

    Example:
        >>> my_tuple = (1, 'hello', 3.14)
        >>> print(my_tuple)
        (1, 'hello', 3.14)
"""
# It is also possible to use the tuple() constructor to make a tuple.
thisTuple = tuple(("apple", "banana", "cherry"));

## ACCESS Tuples

# Accessing elements of a tuple is similar to accessing elements of a list.
# You can use the index of the element to access it.
# Note that the index starts at 0.
print("thisTuple[0] #", thisTuple[0]);

# you can also use negative indexing to access elements from the end of the tuple.
print("thisTuple[-2] #", thisTuple[-2]);

# range of indexes can be specified to access multiple elements. 
# The range will include the start index but exclude the end index.
print("thisTuple[1:3] #", thisTuple[1:3]);

## UPDATE Tuples

# Tuples are immutable, which means you cannot change the values of the elements in a tuple.
# However, you can convert the tuple to a list, change the values, and then convert it back to a tuple.
# Or, you can create a new tuple with the desired values.
# The following code demonstrates how to update a tuple by converting it to a list.
thisList = list(thisTuple);
thisList[1] = "kiwi";
thisTuple = tuple(thisList);
print("thisTuple #", thisTuple);

# You can also concatenate two or more tuples to create a new tuple.
tuple1 = ("a", "b", "c");
tuple2 = (1, 2, 3);
newTuple = tuple1 + tuple2;
print("newTuple #", newTuple);

# Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)