items = []

for i in range(3):
    item = input(f"Enter item {i+1}: ")
    items.append(item)

# Save to file
with open("shopping.txt", "w") as file:
    for item in items:
        file.write(item + "\n")

print("Shopping list saved to shopping.txt!")