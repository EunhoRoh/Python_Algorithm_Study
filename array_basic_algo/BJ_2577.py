# 문제 설명
#세 개의 자연수 A, B, C가 주어질 때 
# A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# import sys
# A=int(sys.stdin.readline().strip())
# B=int(sys.stdin.readline().strip())
# C=int(sys.stdin.readline().strip())
# result=A*B*C

# for i in range(10):
#     print(str(result).count(str(i)))   
    
def main():
    # A = int(input())
    # B = int(input())
    # C = int(input())
    
    A, B, C = map(int, input().split())

    t = A * B * C  # A * B * C의 곱셈 결과 저장
    d = [0] * 10   # 0~9까지의 숫자 개수를 저장할 리스트

    # 각 자릿수 카운트
    while t > 0:
        d[t % 10] += 1  # t의 마지막 자리 숫자를 증가
        t //= 10        # 마지막 자리 숫자 제거

    # 0부터 9까지 각 숫자가 몇 번 등장했는지 출력
    for count in d:
        print(count)

if __name__ == "__main__":
    main()