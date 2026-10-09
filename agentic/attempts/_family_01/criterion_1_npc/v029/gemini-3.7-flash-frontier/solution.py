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
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    domain = [7] * n
    color = [0] * n

    for i in range(n):
        if (adj[i] >> i) & 1:
            print("NO")
            return

    def backtrack(colored_count):
        if colored_count == n:
            return True

        best_v = -1
        best_size = 4
        best_deg = -1

        for i in range(n):
            if color[i] == 0:
                mask = domain[i]
                sz = bin(mask).count("1")
                if sz == 0:
                    return False
                if sz < best_size:
                    best_size = sz
                    best_v = i
                    best_deg = bin(adj[i]).count("1")
                elif sz == best_size:
                    deg = bin(adj[i]).count("1")
                    if deg > best_deg:
                        best_deg = deg
                        best_v = i

        v = best_v
        for c_idx in range(3):
            c_mask = 1 << c_idx
            if domain[v] & c_mask:
                color[v] = c_idx + 1

                affected = []
                valid = True
                neigh = adj[v]
                while neigh:
                    u = (neigh & -neigh).bit_length() - 1
                    neigh &= neigh - 1
                    if color[u] == 0:
                        if domain[u] & c_mask:
                            domain[u] ^= c_mask
                            affected.append(u)
                            if domain[u] == 0:
                                valid = False
                                break

                if valid and backtrack(colored_count + 1):
                    return True

                for u in affected:
                    domain[u] |= c_mask
                color[v] = 0

        return False

    if backtrack(0):
        print("YES")
        print(*(color[i] for i in range(n)))
    else:
        print("NO")


if __name__ == "__main__":
    solve()