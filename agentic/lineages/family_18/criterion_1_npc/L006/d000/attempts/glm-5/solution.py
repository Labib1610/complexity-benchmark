import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it))
        m = int(next(it))
        B = int(next(it))
    except StopIteration:
        return

    adj = defaultdict(list)
    degrees = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
        degrees[u] += 1
        degrees[v] += 1

    # Sort variables by degree in descending order
    # variables are 1-indexed
    variables = list(range(1, n + 1))
    variables.sort(key=lambda x: degrees[x], reverse=True)

    # Assign sectors 1 to n to variables in order of sorted degree
    assignment = [0] * (n + 1)
    for i, var in enumerate(variables):
        assignment[var] = i + 1

    # Calculate total routing overhead
    total_cost = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if u < v: # count each edge once
                total_cost += abs(assignment[u] - assignment[v])

    if total_cost <= B:
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()