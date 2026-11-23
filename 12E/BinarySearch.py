items=[102,118,125,139,147,156,163,178,184,199]
target = 163
lowindex = 0
highindex=len(items)-1
count = 0
while lowindex <= highindex:
    midindex = (lowindex+highindex)//2

    if items[midindex]==target:
        count=count+1
        print("Found after",count,"actions")
        break
    elif items[midindex] > target:
        highindex = midindex - 1
        count = count+1
    else:
        lowindex = midindex + 1
        count=count+1