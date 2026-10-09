import sys
sys.setrecursionlimit(300000)

)



def solve():
    input = sys.stdin.readline
    n, m, B = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -=  ​1
        adj[u].append(v)
        adj[v].append(u)

    # Try preorder and postorder
    orders = []

    # Preorder
    parent = [-1] * n
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            stack.append(v)
    orders.append(order[:])

    # Postorder
    parent = [-1] * n
    order = []
    stack = [(0, 0)]
    parent[0] = 0
    while stack:
        u, state = stack.pop()
        if state == 0:
            stack.append((u, 1))
            for v in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                stack.append((v, 0))
        else:
            order.append(u)
    orders.append(order[:])

    best_pos = None
    best_cost = None

    for order in orders:
        pos = [0] * n
        for idx, u in enumerate(order, 1):
            pos[u] = idx
        cost = 0
        for u in range(n):
            for v in adj[u]:
                if u < v:
                    cost += abs(pos[u] - pos[v])
        if best_cost is None or cost < best_cost:
            best_cost = cost
            best_pos = pos[:]

    if best_cost <= B:
        print("YES")
        print(" ".join(map(str, best_pos)))
    else:
        print("NO")



if __name__ == "__main__":
    solve()