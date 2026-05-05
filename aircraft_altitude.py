from aircraft import Aircraft

model = input("Enter aircraft model:\n")
aircraft = Aircraft(model)

while True:
    command = input("Enter command (A for ascent, D for descent, X to exit):\n")

    parts = command.split()

    if parts[0] == "X":
        break

    feet = int(parts[1])

    if parts[0] == "A":
        aircraft.ascent(feet)
    elif parts[0] == "D":
        aircraft.descent(feet)

print(aircraft)