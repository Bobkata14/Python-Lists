#Restaurant Menu Manager
restaurant_name = "Food Palace Menu".upper().center(23)

menu = ["Pizza", "Pasta", "Burger", "Salad", "Cola"]

print(restaurant_name)
print(" ")

for i, item in enumerate(menu, start=1):
    print(f"{i}. {item}")
print(" ")


menu.append("Apple Juice")

for i, item in enumerate(menu, start=1):
    print(f"{i}. {item}")
print(" ")


menu.remove("Cola")

for i, item in enumerate(menu, start=1):
    print(f"{i}. {item}")
print(" ")


if "Pizza" in menu:
    print("Pizza is in the menu.")
else:
    print("Pizza is not in the menu.")
print(" ")


print(len(menu))
print(menu[0])
print(menu[-1])

#Overall - 6.00