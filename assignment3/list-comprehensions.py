import csv

with open("../csv/employees.csv", newline="") as f:
    reader = csv.reader(f)
    rows = list(reader)

names = [row[0] + " " + row[1] for row in rows[1:]]
print(names)

names_with_e = [name for name in names if "e" in name]
print(names_with_e)
