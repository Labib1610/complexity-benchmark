import sys

# Set recursion depth just in case
sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])

    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        if u != v:
            adj[u] |= 1 << v
            adj[v] |= 1 << u

    domains = [7] * n
    colors = [0] * n
    assigned = [False] * n

    popcnt = [bin(i).count("1") for i in range(8)]
    deg = [bin(adj[i]).count("1") for i in range(n)]

    def backtrack(count):
        if count == n:
            return True

        best_v = -1
        best_size = 4
        best_deg = -1

        for i in range(n):
            if not assigned[i]:
                sz = popcnt[domains[i]]
                if sz < best_size:
                    best_size = sz
                    best_v = i
                    best_deg = deg[i]
                elif sz == best_size and deg[i] > best_deg:
                    best_v = i
                    best_deg = deg[i]

        if best_size == 0:
            return False

        v = best_v
        v_mask = domains[v]
        assigned[v] = True

        for c in range(3):
            if (v_mask >> c) & 1:
                colors[v] = c + 1
                c_bit = 1 << c
                changed = []
                valid = True
                temp = adj[v]
                while temp:
                    u = (temp & -temp).bit_length() - 1
                    temp &= temp - 1
                    if not assigned[u] and (domains[u] & c_bit):
                        domains[u] ^= c_bit
                        changed.append(u)
                        if domains[u] == 0:
                            valid = False
                            break

                if valid and backtrack(count + 1):
                    return True

                for u in changed:
                    domains[u] |= c_bit

        assigned[v] = False
        return False

    if backtrack(0):
        print("YES")
        print(*(colors[i] for i in range(n)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()