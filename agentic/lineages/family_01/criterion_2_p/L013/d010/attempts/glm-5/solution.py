import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    color = [-1] * n
    parent = [-1] * n
    
    for i in range(n):
        if color[i] == -1:
            queue = [i]
            color[i] = 0
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        parent[v] = u
                        queue.append(v)
                    else:
                        if color[v] == color[u]:
                            print("NO")
                            return
                            
    # To get the lexicographically smallest valid assignment,
    # we can just assign 1 to all nodes that were colored 0 in the BFS.
    # This works because:
    # 1. The BFS processes nodes in increasing order of index.
    # 2. The root of each component is the smallest uncolored index, and it gets color 0.
    # 3. Any valid assignment must be exactly this assignment or its complement (flipping 1 and 2).
    # 4. The complement would assign 2 to the root, making it lexicographically larger.
    # Thus, assigning 1 to color 0 and 2 to color 1 yields the lexicographically smallest sequence.
    ans = [1 if c == 0 else 2 for c in color]
    
    print("YES")
    print(*ans)

if __name__ == '__main__':
    solve()