# Lab 03
# Course: COMP2152
# Name: Emir Sadi
# Student ID: 101470121
# Description: Working with Lists, Tuples, Sets, and Dictionaries

print("Lab 03 – COMP2152")
print()

# --------------------------------------------------
# Question 1: Student Grades List
# --------------------------------------------------
grades = [85, 92, 78, 95, 88]

grades.append(90)
grades.sort()

print("Sorted grades:", grades)
print("Highest grade:", grades[-1])
print("Lowest grade:", grades[0])
print("Total number of grades:", len(grades))
print()

# --------------------------------------------------
# Question 2: Shopping Cart
# --------------------------------------------------
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

apple_count = cart.count("apple")
milk_position = cart.index("milk")

cart.remove("apple")
removed_item = cart.pop()

banana_exists = "banana" in cart

print("Number of apples:", apple_count)
print("Position of milk:", milk_position)
print("Removed item using pop:", removed_item)
print("Is banana in cart?", banana_exists)
print("Final cart:", cart)
print()

# --------------------------------------------------
# Question 3: Coordinate System
# --------------------------------------------------
point1 = (3, 5)
point2 = (7, 2)

x1, y1 = point1
x2, y2 = point2

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

char_tuple = tuple("PYTHON")

print("Point 1:", point1)
print("Point 2:", point2)
print(f"x1 = {x1}, y1 = {y1}")
print(f"x2 = {x2}, y2 = {y2}")
print("Distance between points:", distance)
print("Characters tuple:", char_tuple)

for char in char_tuple:
    print(char)

print()

# --------------------------------------------------
# Question 4: Class Attendance
# --------------------------------------------------
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}

monday_class.add("Grace")

both_classes = monday_class & wednesday_class
either_class = monday_class | wednesday_class
only_monday = monday_class - wednesday_class
only_one_class = monday_class ^ wednesday_class
is_subset = monday_class <= either_class

print("Monday class:", monday_class)
print("Wednesday class:", wednesday_class)
print("Attended both classes:", both_classes)
print("Attended either class:", either_class)
print("Only Monday:", only_monday)
print("Only one class (not both):", only_one_class)
print("Is Monday subset of all students?", is_subset)
print()

# --------------------------------------------------
# Question 5: Contact Book
# --------------------------------------------------
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

print("Alice's number:", contacts["Alice"])

contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)

contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)

del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)

print("All names:", contacts.keys())
print("All numbers:", contacts.values())
print("Total contacts:", len(contacts))
print()

# --------------------------------------------------
# Question 6: Inventory Management System
# --------------------------------------------------
inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}

print("=== Current Inventory ===")
for product, (price, quantity) in inventory.items():
    print(f"{product} - Price: ${price}, Quantity: {quantity}")

electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}

all_products = electronics | accessories
print()
print("All product categories:", all_products)

price_list = []
for item in inventory.values():
    price_list.append(item[0])

price_list.sort()

print()
print("Price list:", price_list)
print("Sorted prices:", price_list)
print(f"Lowest price: ${price_list[0]}")
print(f"Highest price: ${price_list[-1]}")

inventory["Headphones"] = (49.99, 20)
inventory["Mouse"] = (inventory["Mouse"][0], 12)
del inventory["Monitor"]

print()
print("=== Final Inventory ===")
for product, (price, quantity) in inventory.items():
    print(f"{product} - Price: ${price}, Quantity: {quantity}")
