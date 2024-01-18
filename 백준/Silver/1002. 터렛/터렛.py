import sys
import math

n = int(sys.stdin.readline())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance == 0 and r1 == r2:
        sys.stdout.write(str(-1) + '\n')
    elif distance == r1 + r2 or distance == abs(r1 - r2):
        sys.stdout.write(str(1) + '\n')
    elif abs(r1 - r2) < distance < r1 + r2:
        sys.stdout.write(str(2) + '\n')
    else:
        sys.stdout.write(str(0) + '\n')