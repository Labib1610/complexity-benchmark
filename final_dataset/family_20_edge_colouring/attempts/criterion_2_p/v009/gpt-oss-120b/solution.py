import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    nL = int(next(it)); nR = int(next(it)); m = int(next(it))
    edges = []
    degL = [0]*(nL+1)
    degR = [0]*(nR+1)
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        edges.append((u, v))
        degL[u] += 1
        degR[v] += 1

    Δ = 0
    for d in degL[1:]:
        if d > Δ: Δ = d
    for d in degR[1:]:
        if d > Δ: Δ = d

    # structures
    usedL = [set() for _ in range(nL+1)]
    usedR = [set() for _ in range(nR+1)]
    # colour -> edge id for each vertex
    col_edgeL = [{} for _ in range(nL+1)]
    col_edgeR = [{} for _ in range(nR+1)]

    ans = [0]*m

    for idx, (u, v) in enumerate(edges):
        # try greedy colour
        cu = usedL[u]
        cv = usedR[v]
        c = 1
        while c in cu or c in cv:
            c += 1
        if c <= Δ:
            ans[idx] = c
            cu.add(c); cv.add(c)
            col_edgeL[u][c] = idx
            col_edgeR[v][c] = idx
            continue

        # need recolouring
        # find a not in usedL[u], b not in usedR[v]
        a = next(c for c in range(1, Δ+1) if c not in cu)
        b = next(c for c in range(1, Δ+1) if c not in cv)

        # BFS for alternating a/b path starting from u
        # we store (vertex, side) where side 0 = left, 1 = right
        # and the colour we expect on the outgoing edge from this vertex
        q = deque()
        visitedL = {}
        visitedR = {}
        q.append( (u, 0, a) )          # at left u, want colour a
        visitedL[u] = (None, None)    # (prev vertex, colour used to come)

        end_vertex = None
        end_side = None

        while q:
            x, side, want = q.popleft()
            if side == 0:   # left side, look at edge of colour want incident to x
                if want in col_edgeL[x]:
                    e_id = col_edgeL[x][want]
                    _, y = edges[e_id]
                    # move to right vertex y, next wanted colour is the other one
                    nxt = b if want == a else a
                    if y not in visitedR:
                        visitedR[y] = (x, want)
                        if nxt not in usedR[y]:
                            end_vertex = y
                            end_side = 1
                            break
                        q.append( (y, 1, nxt) )
                else:
                    # colour want is free at x -> we have found endpoint
                    end_vertex = x
                    end_side = 0
                    break
            else:           # right side
                if want in col_edgeR[x]:
                    e_id = col_edgeR[x][want]
                    y, _ = edges[e_id]
                    nxt = b if want == a else a
                    if y not in visitedL:
                        visitedL[y] = (x, want)
                        if nxt not in usedL[y]:
                            end_vertex = y
                            end_side = 0
                            break
                        q.append( (y, 0, nxt) )
                else:
                    end_vertex = x
                    end_side = 1
                    break

        # reconstruct path and flip colours
        # start from end_vertex back to u
        cur = end_vertex
        cur_side = end_side
        while True:
            if cur_side == 0:   # left
                prev, col = visitedL[cur]
            else:
                prev, col = visitedR[cur]
            if prev is None:
                break
            # edge between prev and cur has colour col, flip it
            e_id = col_edgeL[prev][col] if cur_side == 1 else col_edgeR[prev][col]
            # swap colour
            new_col = b if col == a else a
            # update structures
            # remove old
            if cur_side == 1:
                # edge stored in left prev, right cur
                del col_edgeL[prev][col]
                del col_edgeR[cur][col]
                usedL[prev].remove(col)
                usedR[cur].remove(col)
                # add new
                col_edgeL[prev][new_col] = e_id
                col_edgeR[cur][new_col] = e_id
                usedL[prev].add(new_col)
                usedR[cur].add(new_col)
            else:
                # cur_side == 0, edge stored left cur, right prev
                del col_edgeL[cur][col]
                del col_edgeR[prev][col]
                usedL[cur].remove(col)
                usedR[prev].remove(col)
                col_edgeL[cur][new_col] = e_id
                col_edgeR[prev][new_col] = e_id
                usedL[cur].add(new_col)
                usedR[prev].add(new_col)

            # move one step back
            cur = prev
            cur_side ^= 1

        # now colour a is free at u and at v
        ans[idx] = a
        usedL[u].add(a); usedR[v].add(a)
        col_edgeL[u][a] = idx
        col_edgeR[v][a] = idx

    out = ['YES', ' '.join(map(str, ans))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()