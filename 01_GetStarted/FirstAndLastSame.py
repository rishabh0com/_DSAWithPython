"""
Problem :  Check if the first and last number of a list is the same.
"""
def sameFirstAndLast(array):
    if array[0] == array[len(array)-1]:
         return (str(array) + "\nresult is true\n");
    else:
        return (str(array) + "\n result is false\n");


print(sameFirstAndLast([10,90,10]))
print(sameFirstAndLast(["ram","radha","krishana","ram"]))
print(sameFirstAndLast([1,2,3,4,5,6]))