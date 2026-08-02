import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_set = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        adj_set[u].add(v)
        adj_set[v].add(u)

    # Sorted adjacency lists for iteration
    adj_list = [sorted(lst) for lst in adj_set]

    for a in range(1, n + 1):
        for b in adj_list[a]:
            if b <= a:
                continue  # ensure a < b
            # choose smaller degree list for iteration
            if len(adj_set[a]) < len(adj_set[b]):
                small_list = adj_list[a]
                other_set = adj_set[b]
            else:
                small_list = adj_list[b]
                other_set = adj_set[a]

            for c in small_list:
                if c <= b:
                    continue
                if c in other_set:
                    # triangle found in lexicographically smallest order
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()