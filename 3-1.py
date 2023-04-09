#그리디
#가장 큰 순서대로 , 가장 작은 순서대로
# --> 당장 좋은 것만을 선택하는 것

N = 1260
count = 0

coin_types =[500,100,50,10]

for coin in coin_types: # 여기서 코인은 코인타입들의 종류를 나타낸다
    count += N // coin #거스릅돈을 코인들로 나눴을 때의 몫이 그 개수가 된다
    N %= coin #이제 N은 해당 코인을 나눈 나머지가 된다 -> 그리고 for문 반복

print(count)