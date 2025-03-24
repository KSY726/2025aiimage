from colorama import Fore, Style, init

# Windows에서도 색상이 적용되도록 설정
init(autoreset=True)

# 무지개 색 리스트
rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

# 사용자 입력 받기
dan = int(input("출력할 단을 입력하세요 (2~9): "))

if 2 <= dan <= 9:
    for i in range(1, 10):
        color = rainbow_colors[i % len(rainbow_colors)]  # 색상을 순환하도록 설정
        print(color + f"{dan} x {i} = {dan * i}")
else:
    print(Fore.RED + "2에서 9 사이의 숫자를 입력해주세요!")
