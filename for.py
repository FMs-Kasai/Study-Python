for i in range(7):
    print(i)

for i in range(7):
    if i == 5:
        break
    print(i)

for i in range(7):
    if i == 3:
        continue
    print(i)

for i in range(10):
    for j in  range(10):
        print(i,j, sep='*')

arr = [2,4,6,8,10]
for i in arr:
    print(i)

arr = [2,4,6,8,10]
sum = 0
for i in arr:
    sum += i
    print(sum)