
# array = [1, 2, 3]

# array2 = array

# array.append(4)

# print(id(array))

# print(id(array2))

# print(array)

# print(array2)

# # array2 ko reassign krdiya naya memory block
# array2 = [1,2,3,4]

# print(id(array))

# print(id(array2))

# print(array)

# print(array2)

# a = [1,2,3]
# b = [1,2,3]

# print(id(a)) # output - 
# print(id(b)) # output - 


# a = [1,2,3]
# b = a[:] # means start bhi na diya end bhi na diya
# # ab dekhne mein same reference pe lgg skta hai but aisa nahi hai we made a copy here
# print(id(a)) # output - 140172401338048
# print(id(b)) # output - 140172637130368


a = [1,2,3]
b = a

print(b==a)
print(b is a)

b = [1,2,3]
print(b==a)
print(b is a)
