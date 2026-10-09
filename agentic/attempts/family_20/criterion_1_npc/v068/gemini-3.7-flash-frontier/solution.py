import sys

# Increase recursion depth just in case
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj_v = [[] for _ in range(n + 1)]
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj_v[u].append(i)
        adj_v[v].append(i)
    
    # Precompute for each vertex its 3 incident edges
    # Each vertex has exactly 3 incident edges in a 3-regular graph
    color = [0] * m
    used_mask = [0] * (n + 1)
    cnt = [0] * (n + 1)
    
    history = []
    
    def get_missing_color(mask):
        # mask has 2 bits set among 1, 2, 3 (values 2, 4, 8)
        # 1 << 1 = 2, 1 << 2 = 4, 1 << 3 = 8. Sum = 14.
        rem = 14 - mask
        if rem == 2: return 1
        if rem == 4: return 2
        return 3

    def propagate(initial_e, initial_c):
        queue = [(initial_e, initial_c)]
        head = 0
        while head < len(queue):
            e, c = queue[head]
            head += 1
            
            if color[e] == c:
                continue
            if color[e] != 0:
                return False
            
            u, v = edges[e]
            c_bit = 1 << c
            if (used_mask[u] & c_bit) or (used_mask[v] & c_bit):
                return False
            
            # Apply assignment
            color[e] = c
            history.append(e)
            
            for x in (u, v):
                used_mask[x] |= c_bit
                cnt[x] += 1
                if cnt[x] == 2:
                    missing_c = get_missing_color(used_mask[x])
                    # Find the uncolored edge at x
                    for ne in adj_v[x]:
                        if color[ne] == 0:
                            queue.append((ne, missing_c))
                            break
        return True

    def rollback(checkpoint):
        while len(history) > checkpoint:
            e = history.pop()
            c = color[e]
            c_bit = 1 << c
            u, v = edges[e]
            used_mask[u] ^= c_bit
            cnt[u] -= 1
            used_mask[v] ^= c_bit
            cnt[v] -= 1
            color[e] = 0

    def backtrack():
        # Find next uncolored edge
        # Prefer edges incident to vertices with cnt == 1
        best_e = -1
        for v in range(1, n + 1):
            if cnt[v] == 1:
                for e in adj_v[v]:
                    if color[e] == 0:
                        best_e = e
                        break
                if best_e != -1:
                    break
        
        if best_e == -1:
            # Find any uncolored edge
            for e in range(m):
                if color[e] == 0:
                    best_e = e
                    break
        
        if best_e == -1:
            return True # All colored
        
        u, v = edges[best_e]
        avail = ~(used_mask[u] | used_mask[v])
        
        # If this is a completely isolated decision (both endpoints have cnt == 0),
        # by symmetry we only need to try color 1
        if cnt[u] == 0 and cnt[v] == 0:
            colors_to_try = [1]
        else:
            colors_to_try = []
            for c in (1, 2, 3):
                if avail & (1 << c):
                    colors_to_try.append(c)
        
        for c in colors_to_try:
            checkpoint = len(history)
            if propagate(best_e, c):
                if backtrack():
                    return True
            rollback(checkpoint)
            
        return False

    if backtrack():
        print("YES")
        print(*(color[i] for i in range(m)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()