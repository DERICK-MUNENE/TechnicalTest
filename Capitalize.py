#Write a program that accepts a string as input, capitalizes the first letter of each word in the
#string, and then returns the result string.


def capitalize_first_letter(input_string):

    result_string = input_string.title()
    return result_string

user_input = input("Enter a string: ")

result = capitalize_first_letter(user_input)
print("Capitalized String:", result)