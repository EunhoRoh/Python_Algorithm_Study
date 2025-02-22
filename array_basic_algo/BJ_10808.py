# 알파벳 각각의 갯수를 어떻게 알까?
#65는 알파벳 a이다.
# a b c d e f g h i j k l m n o p q r s t u v w x y z
#총 26개
# 65부터 90까지인가..?
S= input("알파벳을 입력하시오.").lower()

alpha=[0] *26
for c in S:
    alpha[ord(c)-97] +=1
    
print(alpha)
