items=[21,34,63,91,100,112,220,910,2,63]
target = 910

for i in range(len(items)):
    if items[i] == target:
        print("Found at",i)
        break

