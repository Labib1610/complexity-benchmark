cur = h[S_arr]              # gather
   cand = f[T_arr]             # gather
   h[S_arr] = np.minimum(cur, cand)   # scatter to distinct positions — OK!