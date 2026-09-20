# wap for log()
#
#
# from math import *
# n=float(input("enter the number "))
# ans=log(n)
# print("the value is ",ans)
# ==========================================================
# marks = [23,45,67,89,87]
# sum = 0
# for i in marks:
#     sum += i
# print(sum)
# =========================================================
# array = [54,64,74,45,37]
# count=0
# for i in array:
#     if (i%2!=0):
#         count+=1
# print(count)
# =======================================================
# marks = [23,56,78,34,67]
# num = int(input("Enter a number: "))
# found=False
# for i in marks:
#     if num == i:
#         found=True
#         break
# if found:
#     print("found")
# else:
#     print("not found")
# =========================================================================================================================================
# n = int(input("how many number"))
# largest = None
# for i in range(n):
#     num = int(input("Enter a number: "))
#     if largest is None or num > largest:
#         largest = num
# print("largest number is ",largest)
# ==========================================================================
# num = int(input('how many number: '))
# count = 0
# largest = None
# while count < num:
#     num = int(input("Enter a number: "))
#     if largest is None or num >largest:
#         largest = num
#         count = count + 1
# print("largest number is ",largest)
# ============================================================
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#         else:
#             print(num,"is a prime number")
#     else:
#         print(num, "is a prime number")
# ====================================================================================
num = int(input("enter the number: "))
i = 2
prime = True
if num <=1:
    prime = False
while i <= num and prime:
    if num % i == 0:
        prime = False
        i +=1
    if prime:
        print(num,"is prime")
    else:
        print(num,"is not prime")
