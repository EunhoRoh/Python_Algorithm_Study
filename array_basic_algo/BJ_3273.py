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