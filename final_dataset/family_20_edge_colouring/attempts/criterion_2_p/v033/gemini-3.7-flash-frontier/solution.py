import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    nP = int(input_data[0])
    nS = int(input_data[1])
    m = int(input_data[2])
    
    if m == 0:
        print("YES")
        print()
        return

    L = [{} for _ in range(nP + 1)]
    R = [{} for _ in range(nS + 1)]
    ans = [0] * m

    idx = 3
    for e_idx in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2

        Lu = L[u]
        Rv = R[v]

        c1 = 0
        while c1 in Lu:
            c1 += 1

        if c1 not in Rv:
            Lu[c1] = (v, e_idx)
            Rv[c1] = (u, e_idx)
            ans[e_idx] = c1
        else:
            c2 = 0
            while c2 in Rv:
                c2 += 1

            cur_v = v
            cur_u, e_id1 = Rv[c1]

            while True:
                nxt = L[cur_u].get(c2)

                del R[cur_v][c1]
                R[cur_v][c2] = (cur_u, e_id1)
                ans[e_id1] = c2

                L[cur_u][c2] = (cur_v, e_id1)

                if nxt is not None:
                    nxt_v, e_id2 = nxt
                    nxt_u_pair = R[nxt_v].get(c1)

                    del R[nxt_v][c2]
                    R[nxt_v][c1] = (cur_u, e_id2)
                    ans[e_id2] = c1

                    L[cur_u][c1] = (nxt_v, e_id2)

                    if nxt_u_pair is not None:
                        cur_v = nxt_v
                        cur_u, e_id1 = nxt_u_pair
                    else:
                        break
                else:
                    del L[cur_u][c1]
                    break

            Lu[c1] = (v, e_idx)
            Rv[c1] = (u, e_idx)
            ans[e_idx] = c1

    print("YES")
    print(*(c + 1 for c in ans))

if __name__ == '__main__':
    solve()