import sys

data = list(map(int, sys.stdin.readline().split()))
result = 0

for num in data:
    result += num
sys.stdout.write(str(result))