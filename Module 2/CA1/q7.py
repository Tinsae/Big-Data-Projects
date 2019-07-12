text = input("Enter a string: ")
# use dictionary
counter = {}
# for each letter
for letter in text:
    # if it doesn't exist in dictionary
    if(not (letter in counter)):
        counter[letter] = 1
    # add count by one
    else:
        counter[letter] += 1
sorted_items = sorted(counter.items(), key=lambda kv: kv[1], reverse=True)

print("Frequency Table\n")
for letter, count in sorted_items:
    print(letter, ",", count)