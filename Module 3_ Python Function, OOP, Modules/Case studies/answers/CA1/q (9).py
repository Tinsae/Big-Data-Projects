#9
rows, cols = input().split(",")
rows = int(rows)
cols = int(cols)
table = [[x * y for y in range(cols)] for x in range(rows)]
print(table)