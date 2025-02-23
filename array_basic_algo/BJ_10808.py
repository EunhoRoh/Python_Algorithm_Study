# 알파벳 각각의 갯수를 어떻게 알까?
#65는 알파벳 a이다.
# a b c d e f g h i j k l m n o p q r s t u v w x y z
#총 26개
# 65부터 90까지인가..?

1. sys.stdin.readline()을 써야 하는 이유
(1) sys.stdin.readline() vs input() 차이점
python
복사
편집
s = input().strip()  # 일반적인 입력 방식
대신, 내가 사용한 코드:

python
복사
편집
import sys
s = sys.stdin.readline().strip()
를 쓴 이유는 속도 차이 때문이야.

(2) input()과 sys.stdin.readline() 속도 비교
입력 방식	속도	특징
input()	느림	한 줄을 읽을 때마다 내부적으로 여러 처리가 추가됨
sys.stdin.readline()	빠름	한 번에 입력을 받아서 속도가 더 빠름
보통 input()은 한 줄을 읽을 때도 내부적으로 여러 과정을 거치기 때문에 느려.
하지만, sys.stdin.readline()은 입력을 한 번에 가져오므로 더 빠름.

(3) 그럼 sys.stdin.readline()을 언제 써야 할까?
코딩 테스트에서 많은 입력을 받을 때
백준 같은 온라인 저지에서 실행 속도를 줄이고 싶을 때
반복문으로 여러 줄 입력을 받을 때

2. print(*freq)에서 *freq의 의미
print(*freq)에서 *는 언패킹(Unpacking) 연산자야.
C++의 포인터와 비슷한 느낌이지만, 역할이 다름.

(1) 언패킹(Unpacking) 개념
python
복사
편집
arr = [1, 2, 3, 4, 5]
print(*arr)
출력 결과:

복사
편집
1 2 3 4 5
*arr은 리스트 arr의 각 요소를 풀어서 전달하는 역할을 해.
즉, print(*arr)는 print(1, 2, 3, 4, 5)처럼 동작해.

3. ord(c) - ord('a')의 의미
이 부분:

python
복사
편집
freq[ord(c) - ord('a')] += 1
이게 C++ 코드의 freq[c - 'a']++ 부분을 변환한 거야.

(1) 왜 ord(c) - ord('a')를 쓰는 거야?
ord()는 문자를 아스키 코드 값으로 변환해.
'a'의 아스키 코드 값은 97이고, 'b'는 98, 'c'는 99 ...
만약 c = 'b'라면?
python
복사
편집
ord('b') - ord('a')  # 98 - 97 = 1
→ 즉, 'b'는 배열의 1번 인덱스에 해당.

1. sys.stdin.readline()은 무엇을 기준으로 입력을 받나?
네, sys.stdin.readline()은 개행 문자(\n) 를 기준으로 입력을 받아!
즉, 한 줄을 입력받고, 그 끝에는 자동으로 개행 문자 \n이 포함됨.

예제: sys.stdin.readline() 사용
python
복사
편집
import sys

s = sys.stdin.readline()
print(f"입력된 문자열: '{s}'")  # 개행 문자 포함 여부 확인
입력
nginx
복사
편집
hello world
출력
bash
복사
편집
입력된 문자열: 'hello world\n'

2. strip()의 역할
(1) strip()이란?
strip()은 문자열 양쪽 끝의 공백 문자(띄어쓰기, 개행 문자 \n, 탭 \t 등)를 제거하는 함수야.

python
복사
편집
s = "  hello world  \n"
print(f"원본: '{s}'")
print(f"strip 사용: '{s.strip()}'")
출력
bash
복사
편집
원본: '  hello world  \n'
strip 사용: 'hello world'
→ 앞뒤에 있는 공백과 \n이 사라졌어!

(2) 특정 문자만 제거하려면?
.strip() → 앞뒤 모든 공백, 개행 문자 제거
.lstrip() → 왼쪽(앞) 공백만 제거
.rstrip() → 오른쪽(뒤) 공백만 제거
.strip('xyz') → 'x', 'y', 'z'만 제거
python
복사
편집
s = "xxxyhelloxyx"
print(s.strip("xy"))  # 'hello'
→ 'x', 'y'가 제거됨!



# Version 1.
# S= input("알파벳을 입력하시오.").lower()

# alpha=[0] *26
# for c in S:
#     alpha[ord(c)-97] +=1
# alpha = int(''.join(map(str,alpha)))  
# print(alpha)

import sys

def main():
    s = sys.stdin.readline().strip()
    freq = [0] * 26  # 알파벳 개수만큼 리스트 초기화

    for c in s:
        freq[ord(c) - ord('a')] += 1  # 'a'를 기준으로 인덱스 계산

    print(*freq)  # 리스트를 공백으로 구분하여 출력

if __name__ == "__main__":
    main()