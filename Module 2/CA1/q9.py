mylist = [12,24,35,24,88,120,155,88,120,155]
unique = []
for item in mylist:
    if item not in unique:
        unique.append(item)
print(unique)