import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])

    idx = 3
    req = [int(x) for x in input_data[idx:idx + t]]
    idx += t

    if t <= 1:
        print(0)
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        w = int(input_data[idx + 2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        idx += 3

    req_count = [0] * (n + 1)
    for r in req:
        req_count[r] = 1

    root = req[0]
    parent = [0] * (n + 1)
    weight_to_parent = [0] * (n + 1)
    order = []
    order.append(root)

    visited = [False] * (n + 1)
    visited[root] = True

    head = 0
    while head < len(order):
        u = order[head]
        head += 1
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                weight_to_parent[v] = w
                order.append(v)

    ans = 0
    for u in reversed(order):
        if u == root:
            continue
        if req_count[u] > 0:
            ans += weight_to_parent[u]
            req_count[parent[u]] += req_count[u]

    print(ans)

if __name__ == '__main__':
    main()