import sys


def solve():
    sys.setrecursionlimit(3000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    n = 3 * q

    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx]) - 1
        b = int(input_data[idx + 1]) - 1
        c = int(input_data[idx + 2]) - 1
        idx += 3
        triples.append((a, b, c))

    item_to_triples = [[] for _ in range(n)]
    for i, (a, b, c) in enumerate(triples):
        item_to_triples[a].append(i)
        item_to_triples[b].append(i)
        item_to_triples[c].append(i)

    item_deg = [len(item_to_triples[i]) for i in range(n)]
    triple_active = [True] * len(triples)
    item_active = [True] * n
    active_items = set(range(n))

    if any(item_deg[i] == 0 for i in range(n)):
        print("NO")
        return

    solution = []

    def search():
        if not active_items:
            return True

        best_item = -1
        min_deg = 1000000
        for item in active_items:
            d = item_deg[item]
            if d < min_deg:
                min_deg = d
                best_item = item
                if min_deg == 0:
                    return False

        cand_triples = [
            tr for tr in item_to_triples[best_item] if triple_active[tr]
        ]

        for tr_idx in cand_triples:
            a, b, c = triples[tr_idx]

            deactivated = []
            for u in (a, b, c):
                active_items.remove(u)
                item_active[u] = False

            for u in (a, b, c):
                for other_tr in item_to_triples[u]:
                    if triple_active[other_tr]:
                        triple_active[other_tr] = False
                        deactivated.append(other_tr)
                        oa, ob, oc = triples[other_tr]
                        item_deg[oa] -= 1
                        item_deg[ob] -= 1
                        item_deg[oc] -= 1

            solution.append(tr_idx)

            if search():
                return True

            solution.pop()

            for other_tr in reversed(deactivated):
                triple_active[other_tr] = True
                oa, ob, oc = triples[other_tr]
                item_deg[oa] += 1
                item_deg[ob] += 1
                item_deg[oc] += 1

            for u in (a, b, c):
                active_items.add(u)
                item_active[u] = True

        return False

    if search():
        print("YES")
        out = []
        for tr_idx in solution:
            a, b, c = triples[tr_idx]
            out.append(f"{a+1} {b+1} {c+1}")
        print("\n".join(out))
    else:
        print("NO")


if __name__ == "__main__":
    solve()