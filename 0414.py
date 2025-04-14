from rich.console import Console
from rich.text import Text
import time

console = Console()

nyan_cat = [
    "░░░░░░░░░░░░░░░░▄▄▄▄▄▄▄▄░░░░░░░░░░░░░░░",
    "░░░░░░░░░░▄▀▀▀▀▀░░░░░░░░▀▀▀▀▀▄░░░░░░░░░",
    "░░░░░░░░▄▀░░░░░░░░░░░░░░░░░░░▀▄░░░░░░░░",
    "░░░░░░░█░░░░▄▄▄▄▄░░░░░░▄▄▄▄▄░░░█░░░░░░░",
    "░░░░░░░█░░░▀█████▀░░░░▀█████▀░░░█░░░░░░",
    "░░░░░░░█░░░░▀▀▀▀░░░▄░░░░▀▀▀▀░░░░█░░░░░░",
    "░░░░░░░░█░░░░░░░░▄▀░▀▄░░░░░░░░░█░░░░░░░",
    "░░░░░░░░░▀▄░░░░░░▀▄▄▄▀░░░░░░░▄▀░░░░░░░░",
    "░░░░░░░░░░▀▄▄░░░░░░░░░░░░░▄▄▀░░░░░░░░░░",
    "░░░░░░░░░░░░▀▀▄▄▄▄▄▄▄▄▄▄▄▀▀░░░░░░░░░░░░",
    "░░░░░░░░░░░░░░░░▀▀▀▀▀▀▀░░░░░░░░░░░░░░░░",
]

rainbow_colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]

# 🌈 무지개 꼬리 애니메이션 효과!
for frame in range(20):
    console.clear()

    for i, line in enumerate(nyan_cat):
        color = rainbow_colors[(i + frame) % len(rainbow_colors)]
        text = Text(line, style=color)
        console.print(text)

    time.sleep(0.1)
