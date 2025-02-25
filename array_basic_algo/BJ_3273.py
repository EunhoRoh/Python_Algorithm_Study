# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다.
# ai의 값이 양의 정수인 이유는 두 가지 이유가 있다. 첫째는 ai의 값이 음수인 경우에는 두 수의 합이 양수가 될 수 없기 때문이다.   둘째는 ai의 값이 0인 경우에는 두 수의 곱이 0이 되기 때문이다.
# 이 수열의 두 수를 합쳐서 x가 되는 서로 다른 쌍의 개수를 구하여라.
n = int(input().strip())
arr = list(map(int, input().split()))
x=int(input().strip())
arr.sort()
cnt=0
start=0
end=n-1 # 0 1 2 3 4 5 6 7 8 9
while start<end:
    if arr[start]+arr[end]==x:
        cnt+=1
        start+=1
        end-=1
    elif arr[start]+arr[end]>x:
        end-=1
    else:
        start+=1
print(cnt)
# 9

import sys

def main():
    # 입력 받기
    n = int(sys.stdin.readline().strip())  # 수열의 크기 n
    a = list(map(int, sys.stdin.readline().split()))  # 수열 a
    x = int(sys.stdin.readline().strip())  # 목표값 x

    occur = [False] * 2000001  # 각 숫자의 존재 여부를 저장할 배열
    ans = 0  # 쌍의 개수

    # a[i]를 하나씩 확인하며 (x - a[i])가 존재하는지 확인
    for num in a:
        if x - num > 0 and occur[x - num]:  # (x - num)이 존재하면 정답 증가
            ans += 1
        occur[num] = True  # 현재 숫자를 존재하는 것으로 표시

    print(ans)

if __name__ == "__main__":
    main()