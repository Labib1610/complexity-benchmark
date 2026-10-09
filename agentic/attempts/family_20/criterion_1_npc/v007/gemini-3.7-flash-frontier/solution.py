import sys
from collections import deque

sys.setrecursionlimit(200000)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edge_u = [0] * m
    edge_v = [0] * m
    adj_edges = [[] for _ in range(n + 1)]
    
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        edge_u[i] = u
        edge_v[i] = v
        adj_edges[u].append(i)
        adj_edges[v].append(i)
        
    mask = [7] * m
    trail = []
    queue = deque()
    
    def set_mask(e, new_mask):
        cur = mask[e]
        target = cur & new_mask
        if target == cur:
            return True
        if target == 0:
            return False
        trail.append((e, cur))
        mask[e] = target
        queue.append(e)
        return True

    def propagate():
        while queue:
            e = queue.popleft()
            m_e = mask[e]
            if m_e == 0:
                return False
            
            if (m_e & (m_e - 1)) == 0:
                u = edge_u[e]
                v = edge_v[e]
                for adj_e in adj_edges[u]:
                    if adj_e != e:
                        if not set_mask(adj_e, ~m_e):
                            return False
                for adj_e in adj_edges[v]:
                    if adj_e != e:
                        if not set_mask(adj_e, ~m_e):
                            return False
            
            for vert in (edge_u[e], edge_v[e]):
                e0, e1, e2 = adj_edges[vert]
                m0, m1, m2 = mask[e0], mask[e1], mask[e2]
                for bit in (1, 2, 4):
                    c0 = 1 if (m0 & bit) else 0
                    c1 = 1 if (m1 & bit) else 0
                    c2 = 1 if (m2 & bit) else 0
                    total = c0 + c1 + c2
                    if total == 0:
                        return False
                    elif total == 1:
                        target_e = e0 if c0 else (e1 if c1 else e2)
                        if not set_mask(target_e, bit):
                            return False
        return True

    def undo(checkpoint):
        queue.clear()
        while len(trail) > checkpoint:
            e, old_mask = trail.pop()
            mask[e] = old_mask

    def solve():
        best_e = -1
        min_size = 4
        for e in range(m):
            m_e = mask[e]
            if m_e in (3, 5, 6):
                best_e = e
                min_size = 2
                break
            elif m_e == 7:
                if min_size > 3:
                    min_size = 3
                    best_e = e
        
        if best_e == -1:
            return True
        
        m_e = mask[best_e]
        for bit in (1, 2, 4):
            if m_e & bit:
                checkpoint = len(trail)
                if set_mask(best_e, bit) and propagate():
                    if solve():
                        return True
                undo(checkpoint)
        return False

    if n > 0 and len(adj_edges[1]) == 3:
        e0, e1, e2 = adj_edges[1]
        set_mask(e0, 1)
        set_mask(e1, 2)
        set_mask(e2, 4)
        if not propagate():
            print("NO")
            return

    if solve():
        bit_to_color = {1: '1', 2: '2', 4: '3'}
        res = [bit_to_color[mask[i]] for i in range(m)]
        print("YES")
        print(" ".join(res))
    else:
        print("NO")

if __name__ == '__main__':
    main()