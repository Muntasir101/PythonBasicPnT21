age = 36.55
txt = f"My name is John, I am {age}"
print(txt)

first_name = "Mr.Alice"
last_name = "Smith"

full_name = first_name +" "+ last_name
print(full_name)

print(first_name , 30)

"""
username: Alice
Success Message: user Alice added successfully. 
"""
product_name = "MacBook"
Success_Message = "Success: You have added MacBook to your shopping cart!"

word_list = Success_Message.split()
print(word_list)
actual_product_name_success = word_list[4]

"""
if product_name == actual_product_name_success:
    print(f"{product_name} added successfully")
else:
    print(f"{product_name} did not add successfully")
"""
if product_name in word_list:
    print(f"{product_name} added successfully")
else:
    print(f"{product_name} did not add successfully")

