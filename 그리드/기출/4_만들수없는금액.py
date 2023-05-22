N = int(input())
list = list(map(int, input().split()))
list.sort()

target = 1
for x in list:
    if target < x:
        break
    else:
        target += x

print(target)


