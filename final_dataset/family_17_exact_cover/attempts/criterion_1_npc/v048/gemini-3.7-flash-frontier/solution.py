import sys

# Increase recursion depth just in case
sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    q = int(input_data[0])
    t = int(input_data[1])
    n = 3 * q

    triples = []
    idx = 2
    seen = set()
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        # Ensure canonical order
        trip = tuple(sorted((a, b, c)))
        if trip not in seen:
            seen.add(trip)
            triples.append(trip)

    # triples_of[x] contains indices of triples containing element x
    triples_of = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(triples):
        triples_of[a].append(i)
        triples_of[b].append(i)
        triples_of[c].append(i)

    # Check if any element is not covered at all
    for x in range(1, n + 1):
        if not triples_of[x]:
            print("NO")
            return

    # DLX / Backtracking with MRV
    # State tracking:
    # disabled_triple[i] > 0 means triple i shares an element with an already chosen triple
    disabled_triple = [0] * len(triples)
    covered_elem = [False] * (n + 1)
    
    # Active triple count for each element
    active_count = [len(triples_of[x]) for x in range(n + 1)]

    selected_triples = []

    def search(remaining_q):
        if remaining_q == 0:
            return True

        # Find uncovered element with minimum active triples (MRV)
        best_x = -1
        best_val = float('inf')

        for x in range(1, n + 1):
            if not covered_elem[x]:
                cnt = active_count[x]
                if cnt == 0:
                    return False
                if cnt < best_val:
                    best_val = cnt
                    best_x = x
                    if cnt == 1:
                        break

        # Try all active triples covering best_x
        # We make a static copy of candidate triples to iterate over
        candidates = [t_idx for t_idx in triples_of[best_x] if disabled_triple[t_idx] == 0]

        for t_idx in candidates:
            if disabled_triple[t_idx] > 0:
                continue

            a, b, c = triples[t_idx]
            selected_triples.append(t_idx)

            # Mark elements as covered
            covered_elem[a] = True
            covered_elem[b] = True
            covered_elem[c] = True

            # Disable all conflicting triples
            affected_triples = []
            for elem in (a, b, c):
                for other_t in triples_of[elem]:
                    if disabled_triple[other_t] == 0:
                        disabled_triple[other_t] = 1
                        affected_triples.append(other_t)
                        # Decrement active_count for all elements in other_t
                        oa, ob, oc = triples[other_t]
                        active_count[oa] -= 1
                        active_count[ob] -= 1
                        active_count[oc] -= 1
                    else:
                        disabled_triple[other_t] += 1

            if search(remaining_q - 1):
                return True

            # Backtrack
            selected_triples.pop()
            covered_elem[a] = False
            covered_elem[b] = False
            covered_elem[c] = False

            for elem in (a, b, c):
                for other_t in triples_of[elem]:
                    disabled_triple[other_t] -= 1

            for other_t in affected_triples:
                oa, ob, oc = triples[other_t]
                active_count[oa] += 1
                active_count[ob] += 1
                active_count[oc] += 1

        return False

    if search(q):
        print("YES")
        for t_idx in selected_triples:
            a, b, c = triples[t_idx]
            print(f"{a} {b} {c}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()