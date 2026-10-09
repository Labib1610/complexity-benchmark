import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    t = int(input_data[1])
    
    if q == 0:
        print("YES")
        return

    n = 3 * q
    triples = []
    triples_of = [[] for _ in range(n + 1)]
    
    idx = 2
    for i in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        triples.append((a, b, c))
        triples_of[a].append(i)
        triples_of[b].append(i)
        triples_of[c].append(i)
        
    covered = [False] * (n + 1)
    uncovered_elements = set(range(1, n + 1))
    solution = []

    def get_valid_triples(u):
        valid = []
        for tr_idx in triples_of[u]:
            a, b, c = triples[tr_idx]
            if not covered[a] and not covered[b] and not covered[c]:
                valid.append(tr_idx)
        return valid

    def search():
        if not uncovered_elements:
            return True
        
        # Unit propagation & find best element to branch on
        applied_forced = []
        
        while True:
            best_u = -1
            best_triples = None
            min_count = float('inf')
            
            for u in uncovered_elements:
                v_triples = get_valid_triples(u)
                c = len(v_triples)
                if c == 0:
                    # Conflict: an uncovered element has 0 valid triples
                    for forced_tr in reversed(applied_forced):
                        a, b, c_node = triples[forced_tr]
                        covered[a] = covered[b] = covered[c_node] = False
                        uncovered_elements.add(a)
                        uncovered_elements.add(b)
                        uncovered_elements.add(c_node)
                        solution.pop()
                    return False
                
                if c < min_count:
                    min_count = c
                    best_u = u
                    best_triples = v_triples
                    if c == 1:
                        break
            
            if min_count == 1:
                forced_tr = best_triples[0]
                a, b, c_node = triples[forced_tr]
                solution.append(forced_tr)
                covered[a] = covered[b] = covered[c_node] = True
                uncovered_elements.remove(a)
                uncovered_elements.remove(b)
                uncovered_elements.remove(c_node)
                applied_forced.append(forced_tr)
                if not uncovered_elements:
                    return True
            else:
                break
        
        # Branching on best_u
        for tr_idx in best_triples:
            a, b, c = triples[tr_idx]
            if covered[a] or covered[b] or covered[c]:
                continue
            
            solution.append(tr_idx)
            covered[a] = covered[b] = covered[c] = True
            uncovered_elements.remove(a)
            uncovered_elements.remove(b)
            uncovered_elements.remove(c)
            
            if search():
                return True
            
            covered[a] = covered[b] = covered[c] = False
            uncovered_elements.add(a)
            uncovered_elements.add(b)
            uncovered_elements.add(c)
            solution.pop()
            
        # Undo forced moves made in this frame
        for forced_tr in reversed(applied_forced):
            a, b, c_node = triples[forced_tr]
            covered[a] = covered[b] = covered[c_node] = False
            uncovered_elements.add(a)
            uncovered_elements.add(b)
            uncovered_elements.add(c_node)
            solution.pop()
            
        return False

    if search():
        print("YES")
        out = []
        for tr_idx in solution:
            a, b, c = triples[tr_idx]
            out.append(f"{a} {b} {c}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == '__main__':
    solve()