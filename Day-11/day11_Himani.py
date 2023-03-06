# 1. Declare a function add_two_numbers. It takes two parameters and returns a sum.

from inspect import stack


def add_two_numbers(num1,num2):
    return num1+num2

add_two_numbers(10,20)

# 2. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# Output:
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]

def reverse_list(a):
    list1=[]
    while len(a) > 0:
        list1.append(a.pop())

    i=0
    while i < len(list1):
        a.append(list1[i])
        i+=1
    
    return a
    
        
print(reverse_list([1, 2, 3, 4, 5]))

# 3. Declare a function named evens_and_odds. It takes a positive integer as a parameter and it counts a number of events and odds in the number.
# Output:
#     print(evens_and_odds(100))
#     # The number of odds is 50.
#     # The number of events is 51.

def evens_and_odds(n :int):
    if n % 2 == 0:
        print("No of odds ", n//2)
        print("No of evens ", n//2)
    else:
        print("No of odds ", (n//2)+1)
        print("No of evens ", n//2)

evens_and_odds(100)