import re

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

ecl = { "amb", "blu", "brn", "gry", "grn", "hzl", "oth" }

for i in passports:
    required = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" }
    for j in passports[i]:
        pair = j.split(":")
        field = pair[0]
        value = pair[1]
        if field in required:
            if field == "byr":
                if len(value) != 4 or (1920 > int(value) > 2002):
                    continue
            
            elif field == "iyr":
                if len(value) != 4 or (2010 > int(value) > 2020):
                    continue
            
            elif field == "eyr":
                if len(value) != 4 or (2020 > int(value) > 2030):
                    continue
            
            elif field == "hgt":
                unit = value[-2:]
                if (unit != "cm") == (unit !="in"):
                    continue
                elif unit == "cm" and (150 > int(value[:-2]) > 193):
                    continue
                elif unit == "in" and (59 > int(value[:-2]) > 76):
                    continue
            
            elif field == "hcl" and re.match(r"#[\da-f]{6}", value) == None:
                continue
            
            elif field == "ecl" and value not in ecl:
                continue

            elif field == "pid" and len(value) != 9:
                continue


            required.remove(field)
    
    if len(required) == 0:
        valid += 1

print(f"\nTOTAL: {len(passports)}")
print(f"VALID: {valid}\n")
