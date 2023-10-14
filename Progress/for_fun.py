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

# 6. Create a function that checks whether a given number is prime.


# def is_prime(number):
#     if number <= 1:
#         return "This is not prime number"
#     elif number == 2:
#         return "2 is always prime number"
#     elif number % 2 == 0:
#         return "This is not prime number"
#     else:
#         for i in range(3, int(number**0.5) + 1):
#             if number % i == 0:
#                 return "This is not a prime number"
#         return "This is prime number"


# number = int(input(" Enter your digit: "))

# result = is_prime(number)
# print(result)

# 7.Create a list of integers and use list comprehension to create a new list containing only even numbers.

# def numbers(list):
#     even_numbers = [number for number in list if number % 2 == 0]
#     return even_numbers


# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = numbers(list)
# print(result)

# 8.Create a set containing unique items from a given list.


# def unique(list):
#     unique_set = set(list)
#     return unique_set


# list = ["something", "is", "bad", "something", "is", "good"]
# result = unique(list)
# print(result)


# 9.Create a Car class with several attributes such as make, year of manufacture, and top speed.

# class Car:
#     def __init__(self, make, year_of_manufacture, top_speed):
#         self.make = make
#         self.year_of_manufacture = year_of_manufacture
#         self.predkosc = 0
#         self.top_speed = top_speed

#     def fast(self, top_speed_changing):
#         if self.predkosc + top_speed_changing <= self.top_speed:
#             self.predkosc += top_speed_changing
#         else:
#             self.predkosc = top_speed_changing
#         return self.predkosc


# car = Car("Mazda", 2010, 120)
# print(car.fast(100))


# 10 Create a text file with a list of names.
# Write a program that reads these names from a file and sorts them alphabetically.

# with open("Progress\imiona.txt", "r") as file:
#     data = file.read().splitlines()
# data.sort()
# for imie in data:
#     print(imie)

# 11. Create an abstract Shape class with a calculate_surfaces method.
# Create classes that inherit from Shape, representing various geometric shapes such as square and triangle.

# from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass


# class Triangle(Shape):
#     def __init__(self, side, height):
#         self.side = side
#         self.height = height

#     def calculate_area(self):
#         return 0.5 * self.height * self.side


# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def calculate_area(self):
#         return self.side * self.side


# triangle = Triangle(4, 5)
# square = Square(4)

# area_triangle = triangle.calculate_area()
# area_square = square.calculate_area()

# print(f"Area of triangle is {area_triangle}")
# print(f"Area of square is {area_square}")


# 12
