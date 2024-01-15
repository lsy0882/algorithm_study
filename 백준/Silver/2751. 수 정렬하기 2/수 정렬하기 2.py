import sys
from collections import deque

n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))
numbers = deque(sorted(numbers))
for _ in range(n):
    sys.stdout.write(str(numbers.popleft()) + "\n")