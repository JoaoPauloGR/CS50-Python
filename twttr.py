# prompt the user for a word
str_input = input("Input: ")
list_output = []
vowels = ["a","e","i","o","u"]
for i in range(len(str_input)):
    if str_input[i].lower() not in vowels:
        list_output.append(str_input[i])

str_output = "".join(list_output)
print("Output:", str_output)