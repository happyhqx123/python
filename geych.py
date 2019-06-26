import sys, termios

fd = sys.stdin.fileno()
old = termios.tcgetattr(fd)
new = termios.tcgetattr(fd)
# turn off echo and press-enter
new[3] = new[3] & ~termios.ECHO & ~termios.ICANON


def getch():
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        while True:
            char = sys.stdin.read(1)
            print("输入内容是：", char)
            if char == "q":
                break
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


getch()
