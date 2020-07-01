numbers = [1, 4, 64, 25, 19, 42]
highest_number = numbers[0]

for item in numbers:
    if item > highest_number:
        highest_number = item
print(highest_number)

duplicates = [1, 2, 2, 3, 6, 6, 7, 9]
singles = []

for number in duplicates:
    if number not in singles:
        singles.append(number)
print(singles)