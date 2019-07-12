n = int(input("Enter n: "))
sum = 0
for i in range(1, n+1):
    sum += (i / (i + 1))
print(round(sum, 2))