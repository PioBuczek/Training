# 1. Write a program that accepts a sentence from the user and prints it backwards.

# enter_sentence = input("Enter your sentence: ")
# print(enter_sentence[::-1])

# 2. Create a function that removes all duplicates from the list.

# def delete(lists):
#     new = []
#     for word in lists:
#         if word not in new:
#             new.append(word)
#     return new


# lists = ["my", "yours", "my"]
# result = delete(lists)
# print(result)


# 3.Create a dictionary to represent your shopping list,
# and then write a function that calculates the total price of your purchases.

# def shopping(shopping_list):
#     sum = 0
#     for key in shopping_list.keys():
#         sum += shopping_list[key]
#     return sum


# shopping_list = {"banan": 1.5, "snacks": 2.43}

# result = shopping(shopping_list)
# for key, values in shopping_list.items():
#     print(f"You bought: {key} and pay {values} $.")
# print(f"In total you spent {result} $")


# 4.Create a function that accepts a sentence and returns a dictionary
# in which the keys are words and the values are the number of their occurrences.


# def occurences(sentences):
#     new = sentences.split()
#     dict = {}
#     for word in new:
#         if word.isalpha():
#             if word not in dict:
#                 dict[word] = 1
#             elif word in dict:
#                 dict[word] += 1
#     return dict


# sentences = input(" Enter your sentences: ")

# result = occurences(sentences)
# print(result)

# 5.Write a function that calculates the factorial of a number.


# def factorial(numbers):
#     sum = 1
#     while numbers > 0:
#         sum *= numbers
#         numbers -= 1
#     return sum


# numbers = int(input("Enter your digit: "))
# result = factorial(numbers)
# print(result)
