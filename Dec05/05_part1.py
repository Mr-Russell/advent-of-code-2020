tickets = open("tickets.txt", "r")

largest = 0

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
    if seat > largest:
        largest = seat

print(f"LARGEST SEAT ID: {largest}")