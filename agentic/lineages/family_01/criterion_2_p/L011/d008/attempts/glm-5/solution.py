import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n)]
    for i in range(m):
        u = int(data[2 + 2 * i]) - 1
        v = int(data[3 + 2 * i]) - 1
        adj[u].append(v)
        adj[v].append(u)
        
    color = [-1] * n
    queue = []
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            queue.append(i)
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
                        
    print("YES")
    print(*(c + 1 for c in color))

if __name__ == '__main__':
    solve()