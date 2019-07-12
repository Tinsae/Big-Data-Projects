# 2
def binary_search(listt, key):
    lower = 0
    upper = len(listt)
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = listt[x]
        if key == val:
            return x
        elif key > val:
            if lower == x:   # these two are the actual lines
                break        # you're looking for
            lower = x
        elif key < val:
            upper = x
            
    # go back to match
xyz_data = sorted([1, 2, 3,11, 5.5, 3.5, 9, 8, 4])
print(xyz_data)
# search 3
binary_search(xyz_data, 3)