from sys import stdin
stdin = open("baekjoon/input.txt", "r")\

lines = []

for _ in range(1):
	lines.append(stdin.readline().rstrip())
	
tmp = lines[0].split(' ')

array = []

for _ in range(len(tmp)):
	array.append(tmp.pop())

print(' '.join(array))