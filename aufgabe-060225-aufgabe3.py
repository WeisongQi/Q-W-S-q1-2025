# Reverse Word Order
# strings
# Exercise 15 (and Solution)
# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.


def string_list(str):
    s_list = str.split(" ")
    return s_list


str = input("Enter a string: ")

# s_list = str.split(" ")

print(string_list(str)[::-1])
