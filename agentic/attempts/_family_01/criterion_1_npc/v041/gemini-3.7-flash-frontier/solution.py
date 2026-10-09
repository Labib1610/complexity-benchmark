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
        idx += 2
        if u != v:
            adj[u].append(v)
            adj[v].append(u)

    # Remove duplicate edges
    for i in range(n):
        adj[i] = list(set(adj[i]))

    # Domain for each vertex: bitmask of available colors (1: bit 0, 2: bit 1, 3: bit 2)
    # Mask = 7 means {1, 2, 3} are available
    domains = [7] * n
    degree = [len(adj[i]) for i in range(n)]

    def popcount(x):
        return (x & 1) + ((x >> 1) & 1) + ((x >> 2) & 1)

    def backtrack(doms):
        # Find the unassigned vertex with minimum domain size
        best_u = -1
        min_size = 4
        max_deg = -1

        for i in range(n):
            cnt = popcount(doms[i])
            if cnt == 0:
                return None
            if cnt > 1:
                if cnt < min_size or (cnt == min_size and degree[i] > max_deg):
                    min_size = cnt
                    best_u = i
                    max_deg = degree[i]

        if best_u == -1:
            # All vertices have domain size 1
            res = []
            for i in range(n):
                if doms[i] == 1:
                    res.append(1)
                elif doms[i] == 2:
                    res.append(2)
                elif doms[i] == 4:
                    res.append(3)
            return res

        u = best_u
        u_dom = doms[u]

        # Try each available color for u
        for color_bit in (1, 2, 4):
            if u_dom & color_bit:
                new_doms = list(doms)
                new_doms[u] = color_bit
                valid = True
                for v in adj[u]:
                    if new_doms[v] & color_bit:
                        new_doms[v] &= ~color_bit
                        if new_doms[v] == 0:
                            valid = False
                            break
                if valid:
                    ans = backtrack(new_doms)
                    if ans is not None:
                        return ans

        return None

    ans = backtrack(domains)
    if ans is not None:
        print("YES")
        print(*(ans))
    else:
        print("NO")

if __name__ == '__main__':
    solve()