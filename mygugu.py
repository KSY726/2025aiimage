# 숫자 두개를 입력 받고 
#연산을 출력하는 프로그램
from colorama import Fore, Style, init

# Windows에서도 색상이 적용되도록 설정
init(autoreset=True)

# 사용자 입력 받기
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 연산 수행
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num2 and (num1 / num2)  # 0으로 나누는 오류 방지

# 결과 출력 (무지개 색상 적용)
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN]

print(colors[0] + f"{num1} + {num2} = {add}")
print(colors[1] + f"{num1} - {num2} = {sub}")
print(colors[2] + f"{num1} × {num2} = {mul}")

if num2 != 0:
    print(colors[3] + f"{num1} ÷ {num2} = {div}")
else:
    print(Fore.RED + "0으로 나눌 수 없습니다!")