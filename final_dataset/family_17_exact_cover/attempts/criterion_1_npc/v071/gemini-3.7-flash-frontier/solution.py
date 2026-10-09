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
    triples = []
    pos = [[] for _ in range(n + 1)]
    
    idx = 2
    for i in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        triples.append((a, b, c))
        pos[a].append(i)
        pos[b].append(i)
        pos[c].append(i)
        
    deleted = [False] * t
    covered = [False] * (n + 1)
    degree = [len(pos[u]) for u in range(n + 1)]
    
    # Doubly linked list for uncovered elements to quickly iterate and remove
    prev_el = list(range(-1, n + 1))
    next_el = list(range(1, n + 3))
    # Head of uncovered list is 0, elements are 1..n
    # 0 -> 1 -> 2 -> ... -> n -> n+1
    next_el[0] = 1
    prev_el[1] = 0
    next_el[n] = n + 1
    prev_el[n + 1] = n

    def remove_element(u):
        p = prev_el[u]
        nx = next_el[u]
        next_el[p] = nx
        prev_el[nx] = p

    def restore_element(u):
        p = prev_el[u]
        nx = next_el[u]
        next_el[p] = u
        prev_el[nx] = u

    solution = []

    def search(rem_q):
        if rem_q == 0:
            return True
        
        # Find uncovered element with minimum degree (MRV)
        best_u = -1
        min_deg = 1000000000
        
        curr = next_el[0]
        while curr <= n:
            d = degree[curr]
            if d < min_deg:
                min_deg = d
                best_u = curr
                if min_deg <= 1:
                    break
            curr = next_el[curr]
            
        if min_deg == 0 or best_u == -1:
            return False
            
        # Try all candidate triples containing best_u
        cand_triples = [tr for tr in pos[best_u] if not deleted[tr]]
        
        for tr_idx in cand_triples:
            a, b, c = triples[tr_idx]
            solution.append(tr_idx)
            
            # Apply choice: cover a, b, c and delete conflicting triples
            to_restore = []
            for u in (a, b, c):
                covered[u] = True
                remove_element(u)
                for other_tr in pos[u]:
                    if not deleted[other_tr]:
                        deleted[other_tr] = True
                        oa, ob, oc = triples[other_tr]
                        degree[oa] -= 1
                        degree[ob] -= 1
                        degree[oc] -= 1
                        to_restore.append(other_tr)
                        
            if search(rem_q - 1):
                return True
                
            # Backtrack
            for other_tr in reversed(to_restore):
                deleted[other_tr] = False
                oa, ob, oc = triples[other_tr]
                degree[oa] += 1
                degree[ob] += 1
                degree[oc] += 1
                
            for u in (c, b, a):
                restore_element(u)
                covered[u] = False
                
            solution.pop()
            
        return False

    if search(q):
        out = ["YES"]
        for tr_idx in solution:
            a, b, c = triples[tr_idx]
            out.append(f"{a} {b} {c}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()