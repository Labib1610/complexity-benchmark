import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        triples.append((a-1, b-1, c-1))  # 0-based

    n = 3 * q
    # For each operator, list of triple indices containing it
    op_to_triples = [[] for _ in range(n)]
    for i, (a,b,c) in enumerate(triples):
        op_to_triples[a].append(i)
        op_to_triples[b].append(i)
        op_to_triples[c].append(i)

    used_triple = [False] * t
    used_op = [False] * n
    chosen = []

    # Precompute triple members for quick access
    triple_members = triples

    def backtrack():
        if len(chosen) == q:
            return True
        # Find unused operator with fewest candidate triples
        best_op = -1
        best_list = None
        for op in range(n):
            if not used_op[op]:
                cand = [i for i in op_to_triples[op] if not used_triple[i]]
                if best_op == -1 or len(cand) < len(best_list):
                    best_op = op
                    best_list = cand
                    if len(cand) == 0:
                        return False
        # Try each candidate triple
        for ti in best_list:
            a,b,c = triple_members[ti]
            if used_op[a] or used_op[b] or used_op[c]:
                continue
            # Use it
            used_triple[ti] = True
            used_op[a] = used_op[b] = used_op[c] = True
            chosen.append(ti)
            if backtrack():
                return True
            # Undo
            chosen.pop()
            used_triple[ti] = False
            used_op[a] = used_op[b] = used_op[c] = False
        return False

    if backtrack():
        print("YES")
        for ti in chosen:
            a,b,c = triple_members[ti]
            print(a+1, b+1, c+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()