from sys import stdin
stdin = open("baekjoon/input.txt", "r")\

lines = []

for _ in range(1):
	lines.append(stdin.readline().rstrip())

count = int(lines[0])

for nbr in range(1,count+1):
	print('*' * nbr)