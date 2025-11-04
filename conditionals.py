# from datetime import datetime

# age = int(input("Enter your age : "))

# today = datetime.today()
# day_name = today.strftime("%A")

# if(day_name == "Wednesday") : 
#     if(age >= 18) : 
#         print("Ticket price is 10$");
#     else :
#         print("Ticket price is 6$");
# else : 
#     if(age >= 18) : 
#         print("Ticket price is 12$");
#     else :
#         print("Ticket price is 8$");




password = input("Enter your password: ")
length = len(password)
strength = "Medium"

if(length < 6) : 
    strength = "Weak"
elif(length > 10):  
    strength = "Strong"


print(f"Your password strength is {strength}")

