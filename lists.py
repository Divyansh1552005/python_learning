# l1 = list()

# l1 = [1,2,3,4]
# l1.extend([5,6,7])
# print(l1)

# for i, elem in enumerate(l1):
#     print(i, end="->")
#     print(elem)



l1 = [1,2,3,4]
print(id(l1))
l1[0:2] = ["yo", "yo"]
print(l1)
print(id(l1))


a = 2
print(id(a))
a = 4
print(id(a))

tp = (1,2,3)
print(id(tp))



