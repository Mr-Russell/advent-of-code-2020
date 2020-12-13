reference = open("rules.txt", "r")

rules = []

bags = {}

for line in reference:
    rules.append(line.replace(",", "").replace(".", "").split())

for rule in rules:
    bag = f"{rule[0]} {rule[1]}"
    if bag not in bags:
        bags[bag] = set()
    
    new_bag = ''
    for i in rule[4:]:
        if i == "no":
            break
        elif i == "bag" or i == "bags":
            if len(new_bag) > 0:
                bags[bag].add(new_bag)
                new_bag = ''
        elif i.isdigit():
            continue
        elif len(new_bag) == 0:
            new_bag += i
        else:
            new_bag = f"{new_bag} {i}"

def bag_contents(name):
    count = 0
    if "shiny gold" in bags[name]:
        count += 1
    else:
        for i in bags[name]:
            if bag_contents(i) > 0:
                count += bag_contents(i)
                break
        
    return count

total = 0
for i in bags:
    total += bag_contents(i)

print(f"COUNT: {total}")