for a = 1 … n:
        for b in adj_list[a] with b > a (list already sorted):
                # a < b is guaranteed
                common = adj_mask[a] & adj_mask[b]          # vertices adjacent to both
                # we need a vertex c > b
                mask = common >> b                          # drop bits ≤ b
                if mask != 0:
                        # lowest set bit of mask = the smallest possible c
                        low = mask & -mask
                        pos = low.bit_length() - 1          # 0‑based position inside mask
                        c = b + 1 + pos
                        output a b c and finish