# Create a kyc app that collect info from users
# info includes : name, surname, age, gender, state of Origin, occupation, tribe

name = input("Enter your first name: ")
lastname = input("Enter your surname: ")
age = input("Enter your age: ")
gender = input("Are you male or female?: ")
state = input("Enter your state of origin: ")
occupation = input("What is your occupation?: ")
tribe = input("What Nigerian tribe are you from?: ")
print()
print("Customer Profile:\t")
print("\tFull Name -",name, lastname)
print("\tAge -",age)
print("\tGender -",gender)
print("\tState of origin -",state)
print("\tOccupation -",occupation)
print("\tTribe -",tribe)