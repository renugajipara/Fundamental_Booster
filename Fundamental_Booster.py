from datetime import datetime

print("Welcome to the Interactive Personal Data Collector!!")
print("\nThis program takes input from the user and display it.")
print("This program also shows us datatype of the variables.")

#User Inputs
name = input("\nEnter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
num = int(input("Enter your favourite number: "))

#Displaying Information
print("All informayion is collected...")
print("\nCollected Information:")
print(f"Name : {name} (Type : {type(name)} , Memory Address : {id(name)})")
print(f"Age : {age} (Type : {type(age)} , Memory Address : {id(age)})")
print(f"Height : {height} (Type : {type(height)} , Memory Address : {id(height)})")
print(f"Favourite Number : {num} (Type : {type(num)} , Memory Address : {id(num)})")

#Birthyear Calculation
current_year = datetime.now().year
birth_year = current_year - age
print(f"\nYour Birthyear as given age is approximately: {birth_year}")

print("\nThank you for using Personal Data collector. GoodBye!!")