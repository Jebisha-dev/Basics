#  String Indexing 

# 1. Write a Python program to print the first character of the string `"Python"`.
# 2. Write a Python program to print the third character of the string `"Computer"`.
# 3. Write a Python program to print the last character of the string `"Machine"`.
# 4. Write a Python program to print the character at index `4` from the string `"Programming"`.
# 5. Write a Python program to print the first and last characters of a string entered by the user.

# a="python"
# print(a[0])

# a="computer"
# print(a[2])

# a="Machine"
# print(a[6])

# a="Programming"
# print(a[4])

# a=input("enter the value:")
# print(a[0])
# print(a[-1])

# B. Negative Indexing (6–9)

# 6. Write a Python program to print the last character of the string `"Python"` using negative indexing.
# 7. Write a Python program to print the second-last character of the string `"Computer"`.
# 8. Write a Python program to print the first character of the string `"Programming"` using negative indexing.
# 9. Write a Python program to print the last three characters of the string `"Education"` using negative indexing.

# a="python"
# print(a[-1])


# a="computer"
# print(a[-2])

# a="Programming"
# print(a[-11])

# a="education"
# print(a[-3:])

# C. String Slicing (10–14)

# 10. Write a Python program to extract the first three characters from the string `"Python"`.
# 11. Write a Python program to extract the characters from index `2` to index `5` from the string `"Programming"`.
# 12. Write a Python program to print the first five characters of the string `"Computer Science"`.
# 13. Write a Python program to extract the last four characters from the string `"Developer"`.
# 14. Write a Python program to reverse the string `"Python"` using string slicing.

# a="python"
# print(a[:3])

# a="Programming"
# print(a[2:5])

# a="computer science"
# print(a[0:5])

# a="developer"
# print(a[5:])

# a="python"
# print(a[::-1])

#  D. If Condition (15–18)

# 15. Write a Python program to check whether a number is positive using `if`.
# 16. Write a Python program to check whether a student scored above 90 marks using `if`.
# 17. Write a Python program to check whether a number is divisible by 5 using `if`.
# 18. Write a Python program to check whether a person's age is 18 or above using `if`.

# a=int(input("enter the number:"))
# if(a>=0):
#     print("a is positive:")

# print("a is negative:")


# a=int(input("enter the mark :"))
# if(a>=90):
#     print("you score is above 90")
# print("you score is below 90")

# a=int(input("enter the value:"))
# if(a%5== 0):
#     print ("the number is divisble by 5 ")

# print("the number is not divisible by 5")

# a=int(input("enter your age :"))

# if(a>=18):
#     print("your age is:",a)

# print("your age is below 18")

# E. If-Else Condition (19–22)

# 19. Write a Python program to check whether a number is even or odd using `if-else`.
# 20. Write a Python program to check whether a student has passed or failed. (Pass mark: 40.)
# 21. Write a Python program to check whether a number is positive or negative using `if-else`.
# 22. Write a Python program to find the larger of two numbers using `if-else`.
 

# a=int(input("enter the number:"))
# if(a%2==0):
#     print("even")
# else:
#     print("odd")

# a=int(input("enter the mark :"))
# if(a>=40):
#     print("Pass")
# else:
#     print("fail")

# a=int(input("enter the number:"))
# if(a>=0):
#     print("a is positive:")
# else:
#     print("a is negative:")

    
# a=int(input("enter number1:"))
# b=int(input("enter number2:"))
# if(a>b):
#     print("a is larger:",a)
# else:
#     print("b is larger")

# F. If-Elif-Else Condition (23–25)

# 23. Write a Python program to check whether a number is positive, negative, or zero using `if-elif-else`.
# 24. Write a Python program to display a grade based on marks:
#     - 90 and above: Grade A
#     - 75–89: Grade B
#     - 50–74: Grade C
#     - Below 50: Grade D

# a=int(input("enter the value:"))
# if(a>0):
#     print("a is positive ")
# elif(a<0):
#     print("a is negative")
# elif(a==0):
#     print("a is zero")
# else:
#     print("not valid")

# a=int(input("enter the mark"))
# if(a>=90):
#     print("Grade A")
# elif(a>=75 and a<=89):
#     print("grade B")
# elif(a>=50 and a<=70):
#     print("Grade C")
# else:
#     print("Grade D")