import sys

def find_smallest_feedback_loop():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    edges = []
    index = 2
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        if u > v:
            u, v = v, u
        edges.append((u, v))
        index += 2
        
    adj_list = [[] for _ in range(n + 1)]
    
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    for a in range(1, n + 1):
        adj_a = sorted(adj_list[a])
        for i, b in enumerate(adj_a):
            if b > a:
                break
            for c in adj_a[i+1:]:
                if c > b and (b in adj_list[c] or (c in adj_list[b])):
                    print(a, b, c)
                    return

if __name__ == "__main__":
    find_smallest_feedback_loop()