#10234

data = input()

res = int(data[0]) # 1

for i in range(1, len(data)):
    num = int(data[i])

    if num <= 1 or res <= 1:
        res += num
    else:
        res *= num

print(res)





