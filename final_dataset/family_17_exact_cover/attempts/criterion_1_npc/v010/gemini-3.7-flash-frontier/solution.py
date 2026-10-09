import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    t = int(input_data[1])
    
    n = 3 * q
    idx = 2
    triples = []
    seen = set()
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        triple = (a, b, c)
        if triple not in seen:
            seen.add(triple)
            triples.append(triple)
    
    num_triples = len(triples)
    elem_to_triples = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(triples):
        elem_to_triples[a].append(i)
        elem_to_triples[b].append(i)
        elem_to_triples[c].append(i)

    # Check for elements with 0 triples
    for i in range(1, n + 1):
        if not elem_to_triples[i]:
            print("NO")
            return

    covered = [False] * (n + 1)
    ans = []

    # Dancing Links / Backtracking with MRV heuristic
    # To be fast, let's keep track of remaining elements.
    remaining_elements = set(range(1, n + 1))

    # Pre-sort triples for each element or keep as is
    def search(rem_count):
        if rem_count == 0:
            return True

        # Find element with minimum available triples
        best_elem = -1
        best_count = 10**9
        best_cand = None

        for u in remaining_elements:
            # Count how many valid triples cover u
            valid = []
            for tr_idx in elem_to_triples[u]:
                a, b, c = triples[tr_idx]
                if not covered[a] and not covered[b] and not covered[c]:
                    valid.append(tr_idx)
            cnt = len(valid)
            if cnt < best_count:
                best_count = cnt
                best_elem = u
                best_cand = valid
                if cnt <= 1:
                    break

        if best_count == 0:
            return False

        u = best_elem
        for tr_idx in best_cand:
            a, b, c = triples[tr_idx]
            # Extra check in case state changed
            if covered[a] or covered[b] or covered[c]:
                continue
            
            covered[a] = covered[b] = covered[c] = True
            remaining_elements.remove(a)
            remaining_elements.remove(b)
            remaining_elements.remove(c)
            ans.append(tr_idx)

            if search(rem_count - 3):
                return True

            ans.pop()
            remaining_elements.add(a)
            remaining_elements.add(b)
            remaining_elements.add(c)
            covered[a] = covered[b] = covered[c] = False

        return False

    sys.setrecursionlimit(2000)
    if search(n):
        print("YES")
        for tr_idx in ans:
            a, b, c = triples[tr_idx]
            print(f"{a} {b} {c}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()