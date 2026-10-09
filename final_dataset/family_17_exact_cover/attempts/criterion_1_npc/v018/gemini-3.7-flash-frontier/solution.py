import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    q = int(input_data[0])
    t = int(input_data[1])
    n = 3 * q

    trios = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        idx += 3
        trios.append((a, b, c))

    # Remove duplicates
    trios = list(set(trios))
    m = len(trios)

    # Precompute masks and elements for each trio
    trio_elems = trios
    elem_to_trios = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(trio_elems):
        elem_to_trios[a].append(i)
        elem_to_trios[b].append(i)
        elem_to_trios[c].append(i)

    # Check if any element has 0 trios
    for i in range(1, n + 1):
        if not elem_to_trios[i]:
            print("NO")
            return

    # DLX / Backtracking with MRV heuristic
    # State tracking:
    # covered[x] = True/False for elements 1..n
    # used_trios = list of selected trio indices
    covered = [False] * (n + 1)
    solution = []
    
    # Track remaining elements
    uncovered_elements = set(range(1, n + 1))

    def search():
        if not uncovered_elements:
            return True

        # Find uncovered element with minimum available trios (MRV)
        best_elem = -1
        best_trios = None
        min_count = 1000000

        for elem in uncovered_elements:
            # Count valid trios containing elem
            valid_trios = []
            for tr_idx in elem_to_trios[elem]:
                a, b, c = trio_elems[tr_idx]
                if not covered[a] and not covered[b] and not covered[c]:
                    valid_trios.append(tr_idx)
            
            cnt = len(valid_trios)
            if cnt == 0:
                return False
            if cnt < min_count:
                min_count = cnt
                best_elem = elem
                best_trios = valid_trios
                if cnt == 1:
                    break  # Forced move

        # Branch on valid trios for best_elem
        for tr_idx in best_trios:
            a, b, c = trio_elems[tr_idx]
            if covered[a] or covered[b] or covered[c]:
                continue
            
            # Apply
            covered[a] = covered[b] = covered[c] = True
            uncovered_elements.remove(a)
            uncovered_elements.remove(b)
            uncovered_elements.remove(c)
            solution.append(tr_idx)

            if search():
                return True

            # Undo
            solution.pop()
            covered[a] = covered[b] = covered[c] = False
            uncovered_elements.add(a)
            uncovered_elements.add(b)
            uncovered_elements.add(c)

        return False

    if search():
        print("YES")
        for tr_idx in solution:
            a, b, c = trio_elems[tr_idx]
            print(f"{a} {b} {c}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()