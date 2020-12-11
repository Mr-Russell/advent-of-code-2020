policies = open("passwords.txt", "r")

valid = 0

for line in policies:
    arr = line.replace(":", "").split()
    requirements = arr[0].split("-")
    
    minimum = requirements[0]
    maximum = requirements[1]
    character = arr[1]
    password = arr[2]
    count = password.count(character)

    if int(minimum) <= count <= int(maximum):
        valid += 1

print(f"\nVALID: {valid}\n")