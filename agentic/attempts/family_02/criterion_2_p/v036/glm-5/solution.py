import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    # 2*n nodes: node 2*i is literal (i+1)=False, node 2*i+1 is literal (i+1)=True
    # literal x>0 -> node 2*(x-1)+1, negation 2*(x-1)
    # literal x<0 -> node 2*(-x-1), negation 2*(-x-1)+1
    
    size = 2 * n
    graph = [[] for _ in range(size)]
    rev_graph = [[] for _ in range(size)]
    
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        if a > 0:
            la = 2 * (a - 1) + 1
            na = 2 * (a - 1)
        else:
            la = 2 * (-a - 1)
            na = 2 * (-a - 1) + 1
        if b > 0:
            lb = 2 * (b - 1) + 1
            nb = 2 * (b - 1)
        else:
            lb = 2 * (-b - 1)
            nb = 2 * (-b - 1) + 1
        # clause (a or b): ~a -> b, ~b -> a
        graph[na].append(lb)
        graph[nb].append(la)
        rev_graph[lb].append(na)
        rev_graph[la].append(nb)
    
    # Kosaraju
    order = []
    visited = bytearray(size)
    
    for i in range(size):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                node, idx = stack.pop()
                if idx == 0:
                    if visited[node]:
                        continue
                    visited[node] = 1
                pushed = False
                adj = graph[node]
                while idx < len(adj):
                    nxt = adj[idx]
                    idx += 1
                    if not visited[nxt]:
                        stack.append((node, idx))
                        stack.append((nxt, 0))
                        pushed = True
                        break
                if not pushed:
                    order.append(node)
    
    visited = bytearray(size)
    comp = [-1] * size
    
    for node in reversed(order):
        if not visited[node]:
            stack = [node]
            visited[node] = 1
            cid = []
            while stack:
                cur = stack.pop()
                cid.append(cur)
                for nxt in rev_graph[cur]:
                    if not visited[nxt]:
                        visited[nxt] = 1
                        stack.append(nxt)
            for c in cid:
                comp[c] = node
    
    assignment = [0] * n
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            print("NO")
            return
        assignment[i] = 1 if comp[2*i+1] > comp[2*i] else 0
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()