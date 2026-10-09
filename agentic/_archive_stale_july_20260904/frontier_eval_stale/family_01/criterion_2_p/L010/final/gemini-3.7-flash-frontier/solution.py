import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    head = [-1] * (n + 1)
    to = [0] * (2 * m)
    nxt = [0] * (2 * m)
    
    edge_idx = 0
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        
        to[edge_idx] = v
        nxt[edge_idx] = head[u]
        head[u] = edge_idx
        edge_idx += 1
        
        to[edge_idx] = u
        nxt[edge_idx] = head[v]
        head[v] = edge_idx
        edge_idx += 1

    color = [0] * (n + 1)
    queue = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] != 0:
            continue
        
        color[i] = 1
        head_q = 0
        tail_q = 0
        queue[tail_q] = i
        tail_q += 1
        
        while head_q < tail_q:
            u = queue[head_q]
            head_q += 1
            c_u = color[u]
            c_v = 3 - c_u
            
            e = head[u]
            while e != -1:
                v = to[e]
                if color[v] == 0:
                    color[v] = c_v
                    queue[tail_q] = v
                    tail_q += 1
                elif color[v] != c_v:
                    print("NO")
                    return
                e = nxt[e]
                
    print("YES")
    print(*(color[1:]))

if __name__ == '__main__':
    solve()