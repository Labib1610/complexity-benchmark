import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    color = [0] * n
    queue = []
    
    for i in range(n):
        if color[i] == 0:
            color[i] = 1
            queue.append(i)
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        sys.stdout.write("NO\n")
                        return
                        
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color)) + "\n")

if __name__ == '__main__':
    solve()