# 14
sentence = input()
upper = 0
lower = 0

for s in sentence:
    if(s.islower()):
        lower += 1
    elif(s.isupper()):
        upper += 1
    else:
        pass
print("UPPER CASE ", upper)
print("LOWER CASE ", lower)