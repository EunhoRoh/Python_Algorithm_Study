# 한줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.
# 이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽),           또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다.       
# 즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.
# 이 편집기가 지원하는 명령어는 다음과 같다.        
# L - 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D - 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B - 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# P $ - $라는 문자를 커서 왼쪽에 추가함
# 이 편집기가 지원하는 명령어를 모두 수행하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다. 이 문자열은 길이가 N이고, 길이는 100,000을 넘지 않는다.




import sys
from collections import deque
input = sys.stdin.readline
left = deque(list(input().strip()))
right = deque()
n = int(input())
for _ in range(n):
    cmd = input().strip()
    if cmd[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif cmd[0] == 'D':
        if right:
            left.append(right.popleft())
    elif cmd[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(cmd[2])
print(''.join(left + right))

# import sys
