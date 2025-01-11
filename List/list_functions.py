products = ['Mobile', 'watch', 'Tab','Mobile']
products.append("Laptop")
print(products)

print("Tab Count is: ",products.count("Tab"))
print("Mobile Count is: ",products.count("Mobile"))
print("Mobile index is: ",products.index("Mobile"))

products.insert(0,"Router")
print(products)

popped_item = products.pop(0)
print('Popped Item: ',popped_item)
print(products)

products.remove("Mobile")
products.remove("Mobile")
print(products)

numbers = [1,2,43,33,54,34,67,75,6,7,8,9]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

marks = [20,25,54,67,80,90]
marks.sort(reverse=False)
print(marks)

print('Length is: ',len(marks))