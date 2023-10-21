from sys import stdin
stdin = open("baekjoon/input.txt", "r")

lines = []

for _ in range(2):
	lines.append(stdin.readline().rstrip())

word = lines[0]
# print(lines)
print(word[int(lines[1]) - 1])