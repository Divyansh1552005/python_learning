# class Car:

#     oke = "class variable"

#     def __init__(self,brand,model):
#         print("Constuctor ran!")
#         self.brand = brand
#         self.model = model

#     def display(self):
#         return f"Car Brand: {self.brand}, Model: {self.model}"



# # object banana

# first_car = Car("a1", "asc")


# # print(first_car.display())


# first_car.oke = "awdcs"

# print(first_car.oke)

# second_car = Car("a2", "bsc")

# print(first_car.oke)



# static method, class method
class emp:
    ct = 0

    def __init__(self):
        emp.ct += 1

    def show(self):
        print(f"Count = {emp.ct}")

    def aise_hi():
        print("aise hi")
    
    @classmethod
    def show_count(cls):
        print(f"Total objects = {cls.ct}")

    @staticmethod
    def greet():
        print("Static method")


obj1 = emp()
obj2 = emp()

obj1.show()
emp.show_count()
emp.greet()
emp.aisa_hi()