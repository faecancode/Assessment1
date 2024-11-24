#use input statement so the user can enter the values for name, hometown and age
name = input("Enter Name: ") #string value can carry multipe words 
hometown = input("Enter Hometown: ") 

while True:
    age = input("Enter age: ")
    if age.isdigit() and int(age) > 0:  # using the .isdigit() function to Check if the value input is a number and >0 is a positive number
        break  #using the break function to exit the loop if the age is valid
    else:
        print("Invalid input, Please enter a number for ag: ") #the user can re enter the age 

user_info = {"Name": name, "Hometown": hometown, "Age": age} #dictionary with the key

print ("Name:", user_info["Name"] )
print("Hometown:", user_info["Hometown"])
print("Age:", user_info["Age"])

