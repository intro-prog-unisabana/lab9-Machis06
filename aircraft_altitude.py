from aircraft import Aircraft


model = input("Enter aircraft model:\n")
aircraft = Aircraft(model)

altitude = 0

while True:
    command = input("Enter command (A for ascent, D for descent, X to exit):\n")
    parts = command.split()

    if parts[0] == "X":
        break

    feet = int(parts[1])

    if parts[0] == "A":
        altitude += feet

    elif parts[0] == "D":
        altitude -= feet

print(f"Final altitude: {altitude} feet")