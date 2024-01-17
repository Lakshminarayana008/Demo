def fullname(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
result = fullname(first_name, last_name)
print("Full Name:", result)