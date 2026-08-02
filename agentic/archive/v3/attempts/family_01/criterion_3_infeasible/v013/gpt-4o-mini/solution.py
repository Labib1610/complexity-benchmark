def find_non_cooperative_team(n, m, prohibited_pairs):
    # Create a set to store prohibited pairings for fast lookup
    prohibited = set()
    for u, v in prohibited_pairs:
        if u > v:
            u, v = v, u
        prohibited.add((u, v))
    
    # Iterate through all combinations of a, b, c
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if (a, b) not in prohibited:
                continue
            for c in range(b + 1, n + 1):
                if (a, c) in prohibited and (b, c) in prohibited:
                    return a, b, c

import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
prohibited_pairs = [tuple(map(int, line.split())) for line in data[1:m + 1]]

a, b, c = find_non_cooperative_team(n, m, prohibited_pairs)
print(a, b, c)