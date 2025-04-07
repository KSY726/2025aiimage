# 총 5번 반복, 0 입력시 종료하는 동물 출력 프로그램

rabbit = r"""
 (\_/)
 ( •_•)
 />🍎
"""

dog = r"""
 /^ ^\
 / 0 0 \
 V\ Y /V
  / - \
 |    \
 || (__\
"""

cat = r"""
 /\_/\  
( o.o ) 
 > ^ <
"""

print("동물 그림 출력 프로그램 (최대 5번 실행 가능)")

for i in range(5):
    print(f"\n{i+1}번째 실행")
    print("1. 토끼")
    print("2. 강아지")
    print("3. 고양이")
    print("0. 종료")

    choice = input("번호 입력 : ")

    if choice == '0':
        print("프로그램을 종료합니다.")
        break
    elif choice == '1':
        print(rabbit)
    elif choice == '2':
        print(dog)
    elif choice == '3':
        print(cat)
    else:
        print("잘못된 입력입니다.")

print("프로그램이 끝났습니다.")

# 함수 만들기
def hello():
    print("hello world!")

# 함수 호출(실행)
hello()

def hello_name(name):
    print(f"안녕 {name}야~")

# 함수 호출(실행)
name = input("이름을 입력: ")
hello_name(name)

# 연산을 하는 함수
def cal(n1, n2, op): # 1, 2, + (이렇게 입력)
    r = 0 # 결과값
    if op == "+":
        r = n1 + n2
    elif op == "-":
        r = n1 - n2
    else:
        print("잘못입력")
    return r # 결과값을 전달

r = cal(2, 1, "+")
print(f"두수를 더한값{r}")
r = cal(2, 1, "-")
print(f"두수를 뺀값{r}")