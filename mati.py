string = input("Enter a string: ")
input_string = {}
for char in string:
    if char in input_string:
        input_string[char] += 1
    else:
        input_string[char] = 1
print(input_string)
