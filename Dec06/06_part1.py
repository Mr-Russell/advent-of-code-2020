reference = open("answers.txt", "r")

groups = []

string = ''
for line in reference:
    if line == "\n":
        groups.append(string)
        string = ''
    else:
        string += line.strip()
groups.append(string)

count = 0

for string in groups:
    cache = set()
    for letter in string:
        if letter not in cache:
            cache.add(letter)
            count += 1

print(f"TOTAL: {count}")