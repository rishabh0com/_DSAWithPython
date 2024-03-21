tup = ("Orange", [10, 20, 30], (5, 15, 25))

print("tup[0]:", tup[0])
# Orange
print("tup[1: : ]:", tup[0][1::])  # range
print("tup[1][0]:", tup[1][0])
# 10
print("tup[1][2]:", tup[1][2])
# 30
print("tup[2][0]:", tup[2][0])
# 5
print("tup[1][1: :],tup[2][1: :-1]:", tup[1][1::1], tup[2][1::-1])
