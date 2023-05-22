N = int(input())
loc = list(map(int, input().split()))
loc.sort()

print(loc[(N-1)//2])