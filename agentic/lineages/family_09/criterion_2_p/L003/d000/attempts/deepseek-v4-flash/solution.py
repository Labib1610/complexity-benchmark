import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    comps = []
    
    for i in range(n):
        if color[i] == -1:
            # BFS to color component
            q = deque([i])
            color[i] = 0
            cnt0 = 0
            cnt1 = 0
            verts = []
            while q:
                u = q.popleft()
                verts.append(u)
                if color[u] == 0:
                    cnt0 += 1
                else:
                    cnt1 += 1
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
            comps.append((cnt0, cnt1, verts))
    
    # DP bitset
    possible = 1  # bit 0 set
    for cnt0, cnt1, verts in comps:
        if cnt0 + cnt1 == 1:
            # isolated vertex: can pick 0 or 1
            possible = (possible << 1) | possible
        else:
            # can pick any from 0..cnt0 or 0..cnt1
            mask1 = (1 << (cnt0 + 1)) - 1
            mask2 = (1 << (cnt1 + 1)) - 1
            new_possible = 0
            # shift by each possible pick size
            for s in range(cnt0 + 1):
                new_possible |= (possible << s)
            for s in range(cnt1 + 1):
                new_possible |= (possible << s)
            possible = new_possible
    
    if k > n or not (possible >> k) & 1:
        print("NO")
        return
    
    # Reconstruct
    chosen = []
    # We'll go backwards
    # We need to know which component contributed what
    # So we store the possible states after each component
    dp_states = []
    possible = 1
    for cnt0, cnt1, verts in comps:
        dp_states.append(possible)
        if cnt0 + cnt1 == 1:
            possible = (possible << 1) | possible
        else:
            new_possible = 0
            for s in range(cnt0 + 1):
                new_possible |= (possible << s)
            for s in range(cnt1 + 1):
                new_possible |= (possible << s)
            possible = new_possible
    
    target = k
    for idx in range(len(comps) - 1, -1, -1):
        cnt0, cnt1, verts = comps[idx]
        prev_possible = dp_states[idx]
        if cnt0 + cnt1 == 1:
            # can take 0 or 1
            if target >= 1 and (prev_possible >> (target - 1)) & 1:
                chosen.append(verts[0])
                target -= 1
            # else take 0
        else:
            # try to find s such that prev_possible has bit (target - s)
            found = False
            # try from cnt0 side
            for s in range(cnt0, -1, -1):
                if target >= s and (prev_possible >> (target - s)) & 1:
                    # take s vertices from color 0
                    cnt_taken = 0
                    for v in verts:
                        if color[v] == 0 and cnt_taken < s:
                            chosen.append(v)
                            cnt_taken += 1
                    target -= s
                    found = True
                    break
            if not found:
                for s in range(cnt1, -1, -1):
                    if target >= s and (prev_possible >> (target - s)) & 1:
                        cnt_taken = 0
                        for v in verts:
                            if color[v] == 1 and cnt_taken < s:
                                chosen.append(v)
                                cnt_taken += 1
                        target -= s
                        break
    
    print("YES")
    print(" ".join(str(x + 1) for x in chosen))

if __name__ == "__main__":
    solve()