import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    t = int(data[2])
    
    idx = 3
    terminals = [int(x) for x in data[idx:idx+t]]
    idx += t
    
    if t <= 1:
        print(0)
        return
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        w = int(data[idx+2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    is_terminal = [False] * (n + 1)
    for term in terminals:
        is_terminal[term] = True
        
    root = terminals[0]
    parent = [0] * (n + 1)
    edge_weight_to_parent = [0] * (n + 1)
    order = []
    
    stack = [root]
    parent[root] = -1
    
    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if v != parent[u]:
                parent[v] = u
                edge_weight_to_parent[v] = w
                stack.append(v)
                
    has_terminal = [False] * (n + 1)
    for term in terminals:
        has_terminal[term] = True
        
    total_cost = 0
    for u in reversed(order):
        if u == root:
            continue
        if has_terminal[u]:
            total_cost += edge_weight_to_parent[u]
            has_terminal[parent[u]] = True
            
    print(total_cost)

if __name__ == '__main__':
    main()