reference = open("passports.txt", "r")

imported = []

passports = {}

for line in reference:
    imported.append(line.split())

person_id = 0

for i in imported:
    if person_id not in passports:
        passports[person_id] = []

    if len(i) > 0:
        passports[person_id].extend(i)
    else:
        person_id += 1


valid = 0

for i in passports:
    required = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" }
    for j in passports[i]:
        if j[:3] in required:
            required.remove(j[:3])
    
    if len(required) == 0:
        valid += 1

print(f"\nTOTAL: {len(passports)}")
print(f"VALID: {valid}\n")
