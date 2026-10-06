status_codes = [201, 200, 500, 400]
print(status_codes)

# mixed types are allowed
mixed_list = [1, "two", True]
print(mixed_list)

# for qa it is better to avoid mixed types
usernames = ["admin", "guest", "tester"]
print("\n Usernames list:", usernames)

# Access elements by index
print("First username:", usernames[0])
print("Second username:", usernames[1])
print("Last username:", usernames[-1])

# Get the length of a list
print("Length:", len(usernames))

# Slicing (sublists)
print("First two usernames:", usernames[0:2])
print("Last two usernames:", usernames[-2:])
print("All except the first:", usernames[1:])

# remove items from a list using pop()
removed_value = usernames.pop()
print("Removed value:", removed_value)
print("List after removing:", usernames)

# remove items using del
del usernames[-1]
print("List after removing:", usernames)

# remove vales from a list using value itself remove()
usernames.remove("admin")
print("List after removing:", usernames)

# check if a value exists in a list
if 500 in status_codes:
    print("500 status code found!")

# sort values in a list, the list itself is modified
status_codes.sort()
print("Sorted status codes list:", status_codes)

# select values in the list based on conditions
error_codes = []

for code in status_codes:
    if code >= 400:
        error_codes.append(code)

print("Error codes:", error_codes)