loc = input()
row = int(loc[1])

col = int(ord(loc[0]))-int(ord('a'))+1

cnt = 0

steps = [(2,-1),(1,2),(-2,1),(-1,-2),(2,1),(-1,2),(-2,-1),(1,-2)]

for step in steps:
    for i in range(len(steps)):
        new_row = row + step[0]
        new_col = col + step[1]

    if new_row > 0 and new_col > 0:
        cnt += 1

print(cnt)


