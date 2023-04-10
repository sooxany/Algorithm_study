loc = input()
row = int(loc[1])
# 문자를 숫자로 바꾸기 ord를 이용해서
col = int(ord(loc[0])) - int(ord('a')) +1

cnt = 0

# 나이트의 경로
steps = [(2,-1),(1,2),(-2,1),(-1,-2),(2,1),(-1,2),(-2,-1),(1,-2)]


# 이동 계획을 하나씩 확인
for step in steps:
    for i in range(len(steps)):
        new_col = step[0] + col
        new_row = step[1] + row
    if new_col > 0 and new_row > 0:
        cnt += 1

print(cnt)