reference = open("answers.txt", "r")

all_groups = []

group = []
for line in reference:
    if line == "\n":
        all_groups.append(group)
        group = []
    else:
        group.append(line.strip())
all_groups.append(group)

count = 0

for group in all_groups:
    cache = {}
    for person in group:
        for letter in person:
            if letter not in cache:
                cache[letter] = 1
            else:
                cache[letter] += 1

    for i in cache:
        if cache[i] == len(group):
            count += 1

print(f"TOTAL: {count}")