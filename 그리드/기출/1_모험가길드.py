# 5
# 2 3 1 2 2

N = int(input())
member = list(map(int, input().split()))
teams = 0 # 만들 수 있는 팀의 수
i = 0 # 모험가 리스트의 인덱스

# 우선 데이터를 정렬가기
member.sort(reverse=True)
# --> 3 2 2 2 1

# 공포도가 낮은 사람은 최대한 혼자 팀을 이룰 수 있도록 냅두기
while i < N:
    if i+member[i] <= N:
        teams += 1
        i += member[i]
    else:
        break
print(teams)
