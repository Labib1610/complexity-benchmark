#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    neighbors = [[] for _ in range(n+1)]
    adj_mask = [0]*(n+1)
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        if v not in neighbors[u]:
            neighbors[u].append(v)
            neighbors[v].append(u)
            adj_mask[u] |= 1<<(v-1)
            adj_mask[v] |= 1<<(u-1)
    color = [0]*(n+1)
    color_mask = [0,0,0,0]  # index 1..3
    avail_mask = [0b111]*(n+1)  # 3 bits for colors 1,2,3

    def dfs(idx):
        if idx > n:
            return True
        if avail_mask[idx] == 0:
            return False
        for c in (1,2,3):
            if (adj_mask[idx] & color_mask[c]) == 0:
                # forward checking
                changes = []
                ok = True
                for j in neighbors[idx]:
                    if color[j] == 0:
                        prev = avail_mask[j]
                        new = prev & ~(1<<(c-1))
                        if new == 0:
                            ok = False
                            break
                        avail_mask[j] = new
                        changes.append((j, prev))
                if not ok:
                    for j, prev in changes:
                        avail_mask[j] = prev
                    continue
                # assign
                color[idx] = c
                color_mask[c] |= 1<<(idx-1)
                if dfs(idx+1):
                    return True
                # revert
                color[idx] = 0
                color_mask[c] ^= 1<<(idx-1)
                for j, prev in changes:
                    avail_mask[j] = prev
        return False

    if dfs(1):
        out = ['YES']
        out.append(' '.join(str(color[i]) for i in range(1, n+1)))
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

if __name__ == "__main__":
    main()