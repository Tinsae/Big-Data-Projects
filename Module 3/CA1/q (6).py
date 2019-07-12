#6 
result = []
for num in range(2000, 3201):
    not_5 = num % 5 != 0
    div_7 = num % 7 == 0
    if(not_5 and div_7):
        result.append(str(num))
print(",".join(result))