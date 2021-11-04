0, 100

[2, 4, 15, 20]



[0, 1]3

3 - 4 - 1 = [3, 3]5

14- 5 16


start, end = 0, 100

badnum.sort()

currentLenght = 0
lastgood = lower
for num in badnum:
    if num < lower:
        continue
    if num > upper:
        break
    
    if lastGood > upper:
        break

    # construct interval here
    currentLenght = max(currentLenght, (num - 1) - lastGood)
    lastGood = num + 1

upper - lastGood
- 
return currentLenght