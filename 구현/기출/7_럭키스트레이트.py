# 123402
# len(num) => 6
# num[0]=1, num[1]=2, num[2]=3, num[3]=4, num[4]=0, num[5]=2

num = input()

result1 = 0
result2 = 0

for i in range((len(num)//2)):
    result1 += int(num[i])

for j in range(len(num)//2, len(num)):
    result2 += int(num[j])

if result1 == result2:
    print("LUCKY")
else:
    print("READY")
