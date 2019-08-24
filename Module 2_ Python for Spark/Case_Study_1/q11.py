mylist = [12, 24, 35, 70, 88, 120, 155]
length = len(mylist)
print([mylist[i] for i in range(length)
       if i not in [0, 4, 5]])
