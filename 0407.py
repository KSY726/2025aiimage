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

# my_if 함수처럼 처리하는 동물 출력 프로그램

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

def my_if(choice):
    if choice == '1':
        print(rabbit)
    elif choice == '2':
        print(dog)
    elif choice == '3':
        print(cat)
    else:
        print("잘못된 입력입니다.")

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
    else:
        my_if(choice)

print("프로그램이 끝났습니다.")
