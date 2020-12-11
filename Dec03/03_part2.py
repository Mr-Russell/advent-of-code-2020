reference = open("slopes.txt", "r")

mountain = []

for line in reference:
    new_line = []
    for i in line:
        if i != "\n":
            new_line.append(i)
    mountain.append(new_line)

slopes = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
]

tree_totals = []

for i in slopes:
    trees = 0
    x = 0
    y = 0

    right = i[0]
    down = i[1]

    while y < len(mountain):
        if mountain[y][x] == "#":
            trees += 1

        if x + right >= len(mountain[y]):
            remaining = (len(mountain[y]) - 1) - x
            x = (right - 1) - remaining
        else:
            x += right
        
        y += down
    
    tree_totals.append(trees)

answer = 1
for total in tree_totals:
    answer *= total
print(f"\nANSWER: {answer}\n")