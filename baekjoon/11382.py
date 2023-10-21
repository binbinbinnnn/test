from sys import stdin
# stdin = open("baekjoon/input.txt", "r") # 테스트 파일을 읽을 때 사용합니다.

line = stdin.readline() # 한 줄을 읽습니다.
[nbr1, nbr2, nbr3] = map(int, line.split(' '))

print(nbr1 + nbr2 + nbr3)