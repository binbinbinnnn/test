from sys import stdin
stdin = open("baekjoon/input.txt", "r")\

lines = []

for _ in range(1):
	lines.append(stdin.readline().rstrip())

tmp = lines[0]

[nbr1, nbr2] = map(int, tmp.split(' '))

if nbr1 > nbr2:
	print('>')
elif nbr1 < nbr2:
	print('<')
elif nbr1 == nbr2:
	print('==')