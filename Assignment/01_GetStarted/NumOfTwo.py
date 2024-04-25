"""
Problem : Given two integer numbers, 
return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
"""


# declaring a fuction for problem :
def multiplyOrSum(n1, n2):
    if n1 * n2 <= 1000:
        return n1 * n2
    else:
        return n1 + n2


print("for 20 , 30 : ", multiplyOrSum(20, 30))  # it will return multiply
print("for 1000, 2 : ", multiplyOrSum(1000, 2))  # it will return sum
