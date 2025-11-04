# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# sz = len(numbers)
# i = 0
# ct = 0

# while i < sz :
#     if(numbers[i] > 0):
#         print(numbers[i])
#         ct = ct + 1
    
#     i = i+1


# print("The positive number count is " , ct)




# sum = 0

# n = int(input("Enter the number upto which ya want sum : "))

# for i in range(n+1):
#     if(n & 1 == 0):
#         sum += i

# print("The reqd sum is ", sum)

# reverse string using a loop

# calc factorial

# n = int(input("Enter the number upto which ya want factorial : "))

# fact = n
# i = n-1

# while i != 1:
#     fact = fact * i
#     i -= 1

# print(fact)

# n = int(input("Enter the number upto which ya want to check if its prime or not : "))

# is_prime = True

# for i in range(2,n):
#     if(n % i == 0):
#         is_prime = False
#         break;


# print(is_prime)



# list uniqueness check
items = ["apple", "banana", "orange", "apple", "mango"]

hashmap = {}
has_duplicate = False

for item in items:
    if item not in hashmap:
        hashmap[item] = 1
    else:
        hashmap[item] += 1
        has_duplicate = True
        break

print(has_duplicate)
