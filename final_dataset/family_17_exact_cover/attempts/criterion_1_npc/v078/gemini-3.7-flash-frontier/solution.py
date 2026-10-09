import sys

# Increase recursion depth for deep search trees up to q = 200
sys.setrecursionlimit(5000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    q = int(input_data[0])
    t = int(input_data[1])
    n = 3 * q

    triplets = []
    seen = set()
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        idx += 3
        trip = (a, b, c)
        if trip not in seen:
            seen.add(trip)
            triplets.append(trip)

    masks = []
    adj = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(triplets):
        m = (1 << a) | (1 << b) | (1 << c)
        masks.append(m)
        adj[a].append(i)
        adj[b].append(i)
        adj[c].append(i)

    for i in range(1, n + 1):
        if not adj[i]:
            print("NO")
            return

    target_mask = (1 << (n + 1)) - 2
    solution = []

    def search(cur_mask):
        if cur_mask == target_mask:
            return True

        min_len = 999999
        min_options = None

        for i in range(1, n + 1):
            if not (cur_mask & (1 << i)):
                opts = [j for j in adj[i] if not (masks[j] & cur_mask)]
                l = len(opts)
                if l == 0:
                    return False
                if l < min_len:
                    min_len = l
                    min_options = opts
                    if l == 1:
                        break

        for j in min_options:
            solution.append(j)
            if search(cur_mask | masks[j]):
                return True
            solution.pop()

        return False

    if search(0):
        print("YES")
        out = [f"{triplets[j][0]} {triplets[j][1]} {triplets[j][2]}" for j in solution]
        print("\n".join(out))
    else:
        print("NO")


if __name__ == "__main__":
    solve()