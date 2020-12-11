policies = open("passwords.txt", "r")

valid = 0

for line in policies:
    arr = line.replace(":", "").split()
    requirements = arr[0].split("-")

    first = int(requirements[0])
    second = int(requirements[1])
    character = arr[1]
    password = arr[2]

    if (password[first - 1] == character) != (password[second - 1] == character):
        valid += 1

print(f"\nVALID: {valid}\n")