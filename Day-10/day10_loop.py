# 1. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######

for x in range(8):
    print('#' * x)

# 2. Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

i =0
while i <=10:
    print(i , " X " ,i," = ",i*i)
    i+=1

# 3. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# Output: The sum of all numbers is 5050.

sum=0
for i in range(0,101):
    sum+=i

print(sum)