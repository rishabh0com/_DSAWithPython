S = "Welcome to class XII";
print(S);
S = "Thank you";
# The line S[0] = '@'; will give an error.
# Strings in Python are immutable, which means you cannot change individual characters of a string directly.
# If you want to modify a string, you need to create a new string with the desired changes.
S = S + "Thank you";

print(S)