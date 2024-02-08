#Write a program that takes an integer as input and returns an integer with reversed digit
#ordering.



def reverse_digits(num):

    reversed_num = int(str(num)[::-1])
    return reversed_num


user_input = int(input("Enter an integer: "))


result = reverse_digits(user_input)
print("Reversed Integer:", result)