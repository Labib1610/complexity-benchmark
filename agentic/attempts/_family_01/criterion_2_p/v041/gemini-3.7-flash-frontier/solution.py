import sys

# Increase recursion depth just in case, though BFS is iterative
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    color = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            queue = [i]
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                c_next = 2 if color[u] == 1 else 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = c_next
                        queue.append(v)
                    elif color[v] != c_next:
                        print("NO")
                        return

    print("YES")
    print(*(color[1:]))

if __name__ == '__main__':
    solve()