import sys

def main():
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
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    def propagate(dom):
        dom = list(dom)
        q = [u for u in range(n) if (dom[u] & (dom[u] - 1)) == 0]
        propagated = [False] * n
        for u in q:
            propagated[u] = True
        
        head = 0
        while head < len(q):
            u = q[head]
            head += 1
            d = dom[u]
            if d == 0:
                return False, None
            for v in adj[u]:
                if dom[v] & d:
                    dom[v] &= ~d
                    if dom[v] == 0:
                        return False, None
                    if not propagated[v] and (dom[v] & (dom[v] - 1)) == 0:
                        propagated[v] = True
                        q.append(v)
        return True, dom

    def can_color(dom):
        ok, dom = propagate(dom)
        if not ok:
            return False
        
        best_u = -1
        min_size = 4
        for u in range(n):
            d = dom[u]
            sz = (d & 1) + ((d >> 1) & 1) + ((d >> 2) & 1)
            if sz > 1 and sz < min_size:
                min_size = sz
                best_u = u
                if min_size == 2:
                    break
                    
        if best_u == -1:
            return True
        
        d = dom[best_u]
        for c in (1, 2, 4):
            if d & c:
                dom_copy = list(dom)
                dom_copy[best_u] = c
                if can_color(dom_copy):
                    return True
        return False

    dom = [7] * n
    if not can_color(dom):
        print("NO")
        return

    ans = [0] * n
    current_dom = [7] * n

    for i in range(n):
        for c_val in (1, 2, 3):
            mask = 1 << (c_val - 1)
            if current_dom[i] & mask:
                test_dom = list(current_dom)
                test_dom[i] = mask
                if can_color(test_dom):
                    ans[i] = c_val
                    current_dom[i] = mask
                    break

    print("YES")
    print(*(ans[i] for i in range(n)))

if __name__ == '__main__':
    main()