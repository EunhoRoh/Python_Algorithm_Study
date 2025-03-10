N, K =map(int,input().split())
coins = []
for _ in range(N):
    coins.append(int(input))
coins.sort(reverse=True)
cnt =0
for coin in coins:
    cnt += K//coin
    K %=coin
print(cnt)
# #N개의 동전을 가지고 K원을 만들기 위해 필요한 동전의 최소 개수를 구하는 문제이다.