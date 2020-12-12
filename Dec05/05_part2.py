tickets = open("tickets.txt", "r")

ids = []

for string in tickets:
    rows = [x for x in range(128)]
    columns = [x for x in range(8)]

    my_row = None
    my_column = None
    for letter in string[:7]:
        mid = len(rows) // 2
        if letter == "F":
            rows = rows[:mid]
        elif letter == "B":
            rows = rows[mid:]

        my_row = rows[0]

    for letter in string[7:]:
        mid = len(columns) // 2
        if letter == "L":
            columns = columns[:mid]
        elif letter == "R":
            columns = columns[mid:]
        
        my_column = columns[0]

    seat = my_row * 8 + my_column
    ids.append(seat)

ids.sort()
for i in range(1, len(ids) - 1):
    if ids[i] == ids[i-1] + 1 and ids[i] == ids[i+1] - 1:
        continue
    else:
        my_seat = ids[i]+1
        print(f"MY SEAT ID: {my_seat}")
        break