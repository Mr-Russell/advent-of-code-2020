reference = open("slopes.txt", "r")

mountain = []

for line in reference:
    new_line = []
    for i in line:
        if i != "\n":
            new_line.append(i)
    mountain.append(new_line)


trees = 0

x = 0
y = 0

while y < len(mountain):
    if mountain[y][x] == "#":
        trees += 1

    if x + 3 >= len(mountain[y]):
        right = (len(mountain[y]) - 1) - x
        x = 2 - right
    else:
        x += 3
    
    y += 1

print(f"\nTREES: {trees}\n")