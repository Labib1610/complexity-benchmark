import sys
sys.setrecursionlimit(1 << 20)

def solve():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    R = int(next(it))
    S = int(next(it))
    P = int(next(it))
    
    compromised = set()
    for _ in range(P):
        compromised.add(int(next(it)))
    
    tree = [[] for _ in range(R + 1)]
    for _ in range(S):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        tree[u].append((v, w))
        tree[v].append((u, w))
    
    # If P == 1, no edges needed
    if P == 1:
        print(0)
        return
    
    parent = [0] * (R + 1)
    parent_cost = [0] * (R + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in tree[u]:
            if v != parent[u]:
                parent[v] = u
                parent_cost[v] = w
                stack.append(v)
    
    sub_count = [0] * (R + 1)
    for u in order:
        if u in compromised:
            sub_count[u] = 1
    
    total_cost = 0
    for u in reversed(order):
        if u == 1:
            continue
        if sub_count[u] > 0 and sub_count[u] < P:
            total_cost += parent_cost[u]
        p = parent[u]
        sub_count[p] += sub_count[u]
    
    print(total_cost)

if __name__ == "__main__":
    solve()