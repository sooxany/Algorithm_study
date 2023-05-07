num = int(input())

a = []

for i in range(num):
    a.append(int(input()))

for i in range(num-1):
    if a[i] < a[i+1]:
        a[i], a[i+1] = a[i+1], a[i]

print(a)

