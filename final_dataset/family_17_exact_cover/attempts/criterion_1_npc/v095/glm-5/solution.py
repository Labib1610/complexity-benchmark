import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    
    adj = [[] for _ in range(3 * q + 1)]
    for i in range(t):
        a = int(input_data[2 + 3 * i])
        b = int(input_data[3 + 3 * i])
        c = int(input_data[4 + 3 * i])
        adj[a].append((b, c))
        adj[b].append((a, c))
        adj[c].append((a, b))
        
    match = [0] * (3 * q + 1)
    visited = [False] * (3 * q + 1)
    result = []
    
    for u in range(1, 3 * q + 1):
        if match[u] == 0:
            stack = [u]
            while stack:
                v = stack[-1]
                if not visited[v]:
                    visited[v] = True
                    for w1, w2 in adj[v]:
                        if match[w1] == 0 and match[w2] == 0:
                            match[v] = w1
                            match[w1] = v
                            result.append((v, w1, w2))
                            stack.pop()
                            break
                    else:
                        for w1, w2 in adj[v]:
                            if match[w1] != 0 and match[w2] == 0:
                                u1 = match[w1]
                                match[v] = w1
                                match[w1] = v
                                match[u1] = 0
                                stack.append(u1)
                                break
                            elif match[w1] == 0 and match[w2] != 0:
                                u2 = match[w2]
                                match[v] = w2
                                match[w2] = v
                                match[u2] = 0
                                stack.append(u2)
                                break
                else:
                    stack.pop()
                    
    if len(result) == q:
        print("YES")
        for a, b, c in result:
            print(a, b, c)
    else:
        print("NO")

if __name__ == '__main__':
    solve()