import sys
sys.setrecursionlimit(300000)

def main():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    keys = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    parent = [0]*(n+1)
    parent_w = [0]*(n+1)
    order = [1]
    parent[1] = -1
    for node in order:
        for nei, w in adj[node]:
            if nei == parent[node]:
                continue
            parent[nei] = node
            parent_w[nei] = w
            order.append(nei)
    
    sub_count = [0]*(n+1)
    for node in reversed(order):
        if node in keys:
            sub_count[node] += 1
        if parent[node] > 0:
            sub_count[parent[node]] += sub_count[node]
    
    total = 0
    for node in range(2, n+1):
        cnt = sub_count[node]
        if 0 < cnt < t:
            total += parent_w[node]
    
    print(total)

if __name__ == "__main__":
    main()