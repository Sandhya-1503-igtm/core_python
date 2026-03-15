# Program to calculate minimum number of notes for a given amount

amount = int(input("Enter the amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
note_count = {}

for note in notes:
    count = amount // note        # Number of notes of this denomination
    if count > 0:
        note_count[note] = count
        amount = amount % note    # Remaining amount

print("Minimum number of notes needed:")
for note, count in note_count.items():
    print(f"{note} : {count}")