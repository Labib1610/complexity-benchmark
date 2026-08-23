import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    edges = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        edges[u].append(v)
        edges[v].append(u)

    color = [0] * n
    used_colors = [set() for _ in range(n)]  # colors already used by neighbors

    def backtrack(i):
        if i == n:
            return True
        # Try colors 1, 2, 3 in order
        for c in (1, 2, 3):
            if c not in used_colors[i]:
                color[i] = c
                # Update neighbor restrictions
                added = []
                possible = True
                for v in edges[i]:
                    if color[v] == 0:
                        used_colors[v].add(c)
                        added.append(v)
                        if len(used_colors[v]) == 3:
                            possible = False
                            break
                if possible and backtrack(i + 1):
                    return True
                # rollback
                for v in added:
                    used_colors[v].remove(c)
                color[i] = 0
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()