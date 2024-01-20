import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a_upsort = sorted(a)
b_downsort = sorted(b, reverse=True)
mul_list = [a_item * b_item for a_item, b_item in zip(a_upsort, b_downsort)]
result = sum(mul_list)
sys.stdout.write(str(result))