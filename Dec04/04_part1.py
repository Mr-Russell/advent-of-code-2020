reference = open("passports.txt", "r")

passports = []

for line in reference:
    passports.append(line.split())



# for i in range(len(passports)-1):
#     if len(passports[i+1]) != 0:
#         passports[i].extend(passports[i+1])




# for i in passports:
#     print(i)