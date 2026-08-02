import sys
from collections import defaultdict

def read_input():
    return map(int, sys.stdin.read().split())

input = read_input()
n, m = next(input), next(input)

edges = [tuple(sorted((next(input)-1, next(input)-1))) for _ in range(m)]
G = defaultdict(set)
for x, y in edges:
    G[x].add(y)
    G[y].add(x)

def solve():
    if n == 1 or m == 0:
        print("YES")
        print('1 ' * n)
        return

    degree = [len(G[i]) for i in range(n)]
    zero_degree = set(i for i, d in enumerate(degree) if d == 0)

    if len(zero_degree) not in (0, n):
        s = {i: 0 for i in zero_degree}
        for x in zero_degree:
            for y in G[x]:
                degree[y] -= 1
                if degree[y] == 0:
                    s[y] = 0

    elif len(zero_degree) == n:
        return "NO",

    else:
        s = {}
        one_degree = {i: d for i, d in enumerate(degree) if d == 1}
        while True:
            one = set(one_degree.keys())
            two_or_more = [i for i in range(n) if degree[i] >= 2]
            if len(one) == 0 and len(two_or_more) == 0:
                break

            if len(one) == 0 or (len(one) == 1 and one_degree[list(one)[0]] != 1):
                return "NO",

            for x in one:
                s[x] = 1
                for y in G[x]:
                    degree[y] -= 1
                    if degree[y] == 1:
                        one_degree[y] = 1

    blocks = [2, 1]
    while len(s) < n:
        smallest_unassigned = min(set(range(n)) - set(s.keys()))
        s[smallest_unassigned] = blocks[min(degree[smallest_unassigned], 1)]

    result = ['YES'] + [str(s[i]) for i in range(n)]
    return '\n'.join(result)

print(solve())