We need to find an independent set of exactly size k in a graph with n ≤ 46. This is the classic maximum independent set problem for n up to ~40-46, solvable with meet-in-the-middle (the standard technique for n up to ~40-45).

The standard approach: split vertices into two halves L (first n1 vertices) and R (remaining n2 vertices). For each half, enumerate all independent subsets. Then for each independent subset S of L, compute the set of vertices in R that are NOT adjacent to any vertex in S (i.e., allowed). Then we want to find an independent subset of R of size k - |S| that is contained in the allowed set. To do this efficiently, precompute for each subset mask of R... wait, but the allowed set is arbitrary, so we need "for each subset T of R, the maximum independent set size within T" — that's 2^n2 entries which for n2=23 is 8 million entries. That's feasible in terms of memory (8M bytes or ints). Actually with n=46, split into 23 and 23. 2^23 = 8,388,608. Storing best[T] = max independent set size within T, as a byte array of 8M entries — fine. But computing it takes 2^23 iterations, each doing a small computation: best[T] = best[T without lowest bit] ... hmm, standard recurrence: for each T, pick lowest vertex v in T; either v is in the independent set (then size = 1 + best[T & ~N[v] restricted...]) or not (best[T \ {v}]). So best[T] = max(best[T ^ (1<<v)], 1 + best[T & ~adj[v]]). That's 8M iterations with a few operations each — in Python that's too slow probably (8M iterations of Python loop ~ maybe 10-30 seconds). Time limit is 5 seconds. Hmm.

Alternative: we don't need max independent set for all subsets; we need, for each independent set S of L, whether there's an independent set of size exactly k-|S| within allowed set A(S) ⊆ R. 

Alternative approach: enumerate independent sets of R with their sizes, and for each, we need max independent set in L within the allowed set from R. Symmetric problem.

Better approach for Python: use the "meet in the middle with sorted lists" approach. Enumerate all independent subsets of L (there could be up to 2^23 but typically far fewer since independent sets only). For each independent subset S of L, record (mask_in_R_blocked? no...). Hmm.

Standard MITM for max independent set: 
- Enumerate all independent sets in L: list of (maskL, sizeL, maskR_allowed) where maskR_allowed = R vertices not adjacent to S.
- Enumerate all independent sets in R: list of (maskR, sizeR, maskL_allowed).
- Sort R list by maskR. For each entry in L list, we need max sizeR among R-independent sets whose maskR ⊆ allowedR. That's a subset-max query which is hard in general.

The standard technique uses the DP over all subsets of R: f[T] = max size of independent set contained in T. Then answer = max over S in L of sizeL(S) + f[allowedR(S)]. This requires the 2^23 DP.

Can we do the DP efficiently in Python? 2^23 = 8.4M. A pure Python loop of 8.4M iterations with array indexing... roughly 8.4M * maybe 0.5-1 μs per simple operation, but each iteration has several operations (find lowest bit, two array lookups, max, store). Probably ~5-15 seconds. Risky but time limit is 5s. Hmm.

Alternative: reduce the problem. Note we need independent set of size exactly k, but if there's an independent set of size > k, we can... no wait, we need exactly k, but any subset of an independent set is independent, so if max independent set ≥ k, then answer exists (take any k of them). So the problem reduces to: find max independent set; if ≥ k, output any k vertices from it. 

So we need maximum independent set with n ≤ 46.

Alternative algorithms: branch and bound with bitsets. For n=46, a well-implemented branch-and-bound (like a simple branching on max-degree vertex with coloring bound) can be fast in practice, but worst case could be bad. However, with n=46, even a decent branch and bound should work. Actually, a common approach: recursive MIS with memoization on the "remaining graph" — but the state space could be large.

Let me think about the meet-in-the-middle more carefully with Python performance in mind.

n ≤ 46. Split: L = vertices 0..h-1, R = vertices h..n-1, with h = n//2 (so h ≤ 23, n-h ≤ 23).

Step 1: Enumerate all independent subsets of L. We can do this with DP: for each mask of L... that's 2^23 again. Hmm, but we can enumerate independent sets more cleverly: recursive enumeration. The number of independent sets could be up to 2^23 in the worst case (empty graph on 23 vertices has 2^23 independent sets). Enumerating 8M independent sets in Python recursion is also slow.

Hmm, but wait — in the empty graph case, the answer is trivially yes (k ≤ n). Maybe we can add shortcuts: if the graph has few edges, greedy works. Actually a simple observation: if m = 0, answer is any k vertices. More generally, if the graph is sparse, greedy/other heuristics find large independent sets quickly.

Let me think about a robust approach: branch and bound for maximum independent set with n=46. 

Standard approach (like in "maximum clique" solvers): 
- MIS(G) = max(1 + MIS(G \ N[v] \ {v}), MIS(G \ {v})) branching on a vertex v.
- Bound: use greedy coloring of the complement... For MIS, bound via greedy coloring on the complement graph is awkward. Alternative bound: the number of remaining vertices (trivial), or a greedy "partition into independent... " hmm. For MIS, an upper bound is the number of vertices in the remaining set (trivial) or better: partition remaining vertices into cliques? No — MIS upper bound = minimum number of cliques covering the remaining vertices (clique cover of G = coloring of complement). Computing a greedy clique cover: repeatedly extract... hmm, greedy coloring of complement graph.

Actually, a simpler and quite effective bound for MIS: since each vertex in remaining set R, MIS(R) ≤ |R|. Also we can use the bound MIS(R) ≤ max over... Let me think of a simpler approach: 

For n=46, a simple branch and bound with the trivial bound |R| might blow up in the worst case (e.g., empty graph — but there branching picks v, includes it, removes nothing... actually in empty graph, including v removes only v, so recursion depth 46 with branching factor 2 → 2^46 nodes without pruning. Bad). But with the bound: once current + |R| ≤ best, prune. In empty graph, first path includes vertices greedily and gets best=46 immediately, then all other branches pruned immediately since current + |R| ≤ 46 = best. Actually the pruning works well there.

Worst cases for MIS branch and bound with trivial bound: graphs where max independent set is small relative to n, e.g., complete graph (trivial), or random dense graphs. Hmm, consider a graph that is a disjoint union of many triangles: n=46, ~15 triangles, MIS = 15. Branch and bound: each triangle branches... With trivial bound, could be 3^15 ≈ 14M nodes. Too slow in Python.

Better: use a good upper bound. Clique cover bound: MIS(R) ≤ number of cliques in a clique cover of R. Greedy clique cover: process vertices, assign each to first clique where it's adjacent to all... Actually simpler: greedy coloring of complement graph gives an upper bound on MIS? Wait: MIS(G) = ω(complement(G))... no! MIS(G) = maximum clique in complement(G). And clique number ≤ chromatic number. So MIS(G) = ω(Ḡ) ≤ χ(Ḡ) = clique cover number of G. So greedy coloring of the complement graph gives an upper bound on MIS. 

So branch and bound: at each node, take remaining vertex set R (as bitmask). Compute greedy coloring of complement restricted to R: number of colors c is an upper bound on MIS(R). If current_size + c ≤ best, prune. Branch on a chosen vertex (e.g., one with max degree in R, or the vertex with highest color, etc.).

This is essentially the classic MaxCLQ algorithm applied to the complement. For n=46, this should be very fast in practice. But implementing greedy coloring per node in Python adds overhead per node.

Alternatively, meet-in-the-middle with numpy vectorization could handle the 2^23 DP.

Let me think about how to do the MITM with numpy:

1. Compute adjacency bitmasks adj[i] for each vertex i (as Python ints, n ≤ 46 bits).

2. Split: h = n // 2. L = [0, h), R = [h, n). Let nL = h, nR = n - h. Both ≤ 23.

3. For the R side, we need f[T] for all T ⊆ R: max independent set size within induced subgraph on T. DP over 2^nR subsets:
   f[0] = 0.
   For T ≠ 0: let v = lowest set bit of T. f[T] = max(f[T \ {v}], 1 + f[T & ~adjR[v]]).
   
   With numpy, this DP is sequential (each f[T] depends on f of smaller subsets), hard to vectorize directly. Hmm. But there's a trick: process subsets in order... The dependency f[T] depends on f[T ^ lowbit] and f[T & ~adj[v]] — both are subsets of T with fewer elements, but arbitrary masks. Vectorizing arbitrary subset DP is hard.

   Alternative: enumerate independent sets of R directly via recursion/iteration, and for each independent set mask, we want to store, for every superset... no.

Alternative formulation avoiding the full-subset DP:

For each independent set S ⊆ L, define A(S) = vertices in R not adjacent to S. We need max over independent sets T ⊆ A(S) of |S| + |T|.

Equivalently: enumerate all independent sets of R as (maskR, sizeR, allowedL) where allowedL = L-vertices not adjacent to maskR. Then for each independent set S of L, we need max sizeR over enumerated R-sets with maskR ⊆ A(S). 

Hmm, still subset queries.

Another classic approach: since we just need to know whether size k is achievable, and k ≤ 46... 

Alternative: DP over subsets of R but only for masks that arise as A(S)? The number of distinct A(S) values is at most number of independent sets of L, which could be 2^23. Not helpful.

Hmm, what about a different split of work: 

Meet in the middle where we enumerate independent sets in each half and then combine with sorting + subset-max queries via... The combination step: we have list PairsL = [(allowedR, sizeL)] and we want max over pairs of sizeL + sizeR where maskR ⊆ allowedR. 

Trick: Instead of arbitrary subset queries, we can use the following: for each independent set T of R with size s, and each independent set S of L with S ⊆ allowedL(T), combine. If we sort... no.

OK here's another thought: the DP f[T] over all 2^23 subsets — can we compute it with numpy in a vectorized way? 

Observation: f[T] = max independent set in induced subgraph T. There's a recurrence by lowest bit which is sequential. But we could compute it via a different decomposition: f[T] = max(f[T without vertex v], f[...]) — inherently sequential.

Alternative: compute g[T] = max size of independent set that is a subset of T, using the "for each independent set I, for each superset T of I, g[T] = max(g[T], |I|)" — that's sum over independent sets of 2^(nR - |I|) operations. In empty graph, that's 3^23 — way too much.

Hmm. Let's think about the sizes more carefully. n ≤ 46, so nR ≤ 23, 2^23 = 8.4M. A pure Python loop doing:

f = bytearray(1 << nR)
for T in range(1, 1 << nR):
    v = (T & -T).bit_length() - 1
    ...

Each iteration: compute lowbit index, two array reads, a max, a store. In CPython, that's maybe 0.5-1 μs per iteration optimistically... realistically ~1.5-2 μs → 12-17 seconds for 8.4M. Too slow for 5s limit. Unless... we can use PyPy-style optimizations — no, we must assume CPython.

Can we vectorize the DP with numpy? Let's think. 

Idea: process the DP in blocks. Note the recurrence: f[T] depends on f[T ^ (1<<v)] where v = lowest bit of T, and f[T & ~adj[v]]. 

Alternative recurrence that's more vectorizable: f[T] = max over v ∈ T of (1 + f[T & ~adj[v] & ~{v}])? No wait, that's not right either — f[T] = max(f[T\{v}], 1 + f[T ∩ allowed(v)]) where allowed(v) = complement of closed neighborhood. Actually f[T] = max over v ∈ T of (1 + f[T ∩ allowed(v)]) where allowed(v) = vertices not adjacent to v (excluding v itself). Is that correct? f[T] = max independent set in T. If the max independent set is nonempty, pick any vertex v in it: then f[T] ≥ 1 + f[T ∩ allowed(v)]. And conversely. So f[T] = max(0, max over v∈T of 1 + f[T ∩ allowed(v)]). Hmm, this is a max over nR choices, each requiring f at a subset. Still sequential.

Vectorization idea: compute f layer by layer by popcount? f[T] for |T| = t depends on f at subsets with popcount... T ∩ allowed(v) can have any popcount < |T|... no, T ∩ allowed(v) ⊆ T \ {v}, so popcount ≤ t-1. And T ^ (1<<v) has popcount t-1. So we can compute f in order of popcount! For each popcount level t, all f[T] with |T| = t depend only on f values with popcount < t. 

So: group subsets by popcount. For level t, for each T with |T|=t, f[T] = max over v ∈ T of (1 + f[T & allowed_mask[v]]). With numpy: for each v (nR ≤ 23 values), and for each T in level-t list: compute T & allowed[v], then look up f at that index. Lookup at arbitrary indices — we can do f_array[indices] with numpy fancy indexing, where indices = T_list & allowed[v]. That's vectorized! 

Total work: sum over levels t of (number of subsets with popcount t) × nR. Sum over all t of C(23, t) × 23 = 23 × 2^23 ≈ 193M numpy element-operations, but done in 23 × 23 = 529 vectorized calls (each on arrays of size C(23,t) ≤ ~1.35M for t=11,12). Each level: for each v in 0..22, compute (T_arr & allowed_v) → array op, then f[those] → gather, then +1, then max-accumulate into current level's f values. 

Memory: f as numpy array of size 2^23, dtype uint8 (max value 23 fits). The gather operations: 193M gathered elements total across all calls — numpy fancy indexing throughput maybe 100-500M elements/sec... could be ~1-2 seconds. Plus the & operations similar. Hmm, total maybe 2-4 seconds. Risky but maybe OK. Actually wait, we can reduce: for level t, for vertex v, we only need to consider T that contain v. We could pre-partition each level's subsets by... that complicates. Alternatively, note f[T] = max(f[T without v], 1 + f[T & allowed(v)]) — using the lowest-bit recurrence reduces to 1 gather per T instead of nR gathers per T. But lowest-bit recurrence is sequential within... no wait! With popcount layering: f[T] for |T| = t: take v = lowest bit of T. f[T] = max(f[T ^ (1<<v)], 1 + f[T & allowed(v)]). T ^ (1<<v) has popcount t-1 ✓. T & allowed(v) has popcount ≤ t-1 ✓. So both lookups are at lower levels. And we only need ONE v per T (the lowest bit). So total gathers = 2^23 × 2 ≈ 16.7M gathers. 

But computing "lowest bit of T" vectorized: v = T & (-T) as numpy int32/int64, then index = trailing zeros. We can precompute a lookup table lz[lowbit] → but lowbit values up to 2^22, table of size 2^23 (uint8) — 8MB, fine. Or use bit tricks: v = T & -T; idx = log2(v) via multiplication trick, or precomputed table of size 2^23 (8MB uint8). Table lookup vectorized: lz_table[v_array] — gather of 8.4M elements. Fine.

So the plan for the R-side DP:
- Precompute lists of subsets grouped by popcount? Actually we can just iterate T from 1 to 2^nR - 1 in order... no, we need level-by-level processing for vectorization. Grouping 8.4M subsets by popcount: we can generate combinations per level using itertools.combinations — total 8.4M combinations generated, each producing an int. Generating 8.4M ints via combinations and packing bits... that's expensive in pure Python (~8.4M × maybe 0.5μs = 4s+). Hmm.

Alternative: generate all masks 0..2^nR-1 as numpy array (np.arange — fast). Compute popcounts vectorized (via bit tricks: popcount of 23-bit numbers — can do with shifts and adds, ~5 vector ops on 8.4M elements, fast). Then argsort by popcount or use np.bincount + sorting. Sorting 8.4M elements with numpy: ~1-2 seconds maybe. Hmm, or: process levels via a different trick.

Actually, do we even need level ordering? Let's reconsider: we could process T in increasing numeric order — but then vectorization by blocks doesn't respect dependencies (T and T+1 can be in the same level). The dependency f[T] ← f[T ^ lowbit] and f[T & allowed(v)]: both are numerically smaller than T. If we process in blocks of... hmm, T ^ lowbit < T and T & anything ≤ T (strictly less since v removed). So dependencies are always on strictly smaller indices. If we process in increasing index order in blocks [B, 2B), dependencies are in [0, B) ∪ [B, T) — within-block dependencies break vectorization. Unless block size = 1, which is the pure loop.

But with popcount levels: within a level, no dependencies (all deps are lower popcount). 

So we need subsets grouped by popcount. Options:
1. np.arange(2^nR), compute popcount vectorized, then np.argsort (stable) by popcount → order array. argsort on 8.4M int32: numpy sort is ~O(N log N) with decent constant; maybe 1-1.5s. Then levels via np.searchsorted or bincount cumsum.

Actually simpler: we don't need a full sort. We can iterate levels t = 0..nR, and select masks with popcount == t via boolean indexing: masks_t = all_masks[pc == t]. That's nR+1 = 24 passes over 8.4M boolean arrays — each pass ~ a few vector ops on 8.4M elements → 24 × ~30ms = 0.7s. Acceptable. Or use np.argsort once. Either fine.

Hmm wait, actually there's an even better idea. Let me reconsider the whole problem: maybe branch and bound is simpler and fast enough, avoiding all this heavy machinery. Let me think about worst cases for B&B with coloring bound on complement.

Actually, let me reconsider: maybe there's a smarter formulation. We need MIS on n ≤ 46 vertices. Known: MITM handles n ≤ ~40 comfortably in C. In Python, we need vectorization.

Alternatively — think about the problem differently. Since we need "exactly k" and any superset works, we need max independent set ≥ k. 

Hmm, what about a randomized/greedy + local search? Not guaranteed.

What about a different exact approach: Since n ≤ 46, and we need to check if MIS ≥ k. If k is small, we could use a different algorithm (e.g., k ≤ some threshold → branching with depth k). If k is large, then the complement... MIS ≥ k means the complement graph has a clique of size ≥ k. If k > n/2, hmm, clique of size > 23 in a 46-vertex graph — dense complement. Not obviously easier.

I think MITM with numpy is the way, but let me carefully design it to be fast. Alternatively, B&B with good bounds might just be much simpler and fast enough. Let me estimate B&B more carefully.

Branch and bound for MIS:
- Represent remaining candidate set as a bitmask (Python big ints, fast bitwise ops).
- Upper bound: greedy clique cover (equivalently greedy coloring of complement). Computing this per node costs O(n × something) in Python — maybe 20-100 μs per node with bit tricks. If the search tree has ≤ ~100k nodes, that's ≤ 10s. Hmm, risky.

Actually, there's a classic simpler bound for MIS branch and bound that's very effective: process vertices in a fixed order and use the coloring bound only... Let me think about the standard "MCS/MCR" algorithms. Those are complex.

Alternatively, a cleaner exact approach: **Iterative deepening / branch on vertices in order with memo**? 

Hmm, let me think again about MITM but with a twist to reduce the 2^23 DP: 

We need f[T] only for T values that arise as A(S) = allowed set in R for some independent set S ⊆ L. The number of independent sets of L is at most 2^23 but typically much less. But worst case (empty L) it's 2^23 with all A(S) = full R. Hmm, but in the empty-graph case we can shortcut: if the graph has ≤ ... hmm.

Wait, actually here's a thought: we can handle it as max independent set = max over independent sets S of L of |S| + MIS(R restricted to A(S)). Instead of computing f for all subsets, we can compute, for each independent set S of L, MIS(A(S)) via... recursion? No.

Alternative: swap roles. Enumerate independent sets of R (list with masks), and for each, allowedL. Then we want max over pairs. Hmm.

Alternative known technique for MITM MIS: 
- List all independent sets of L as (sizeL, maskR_blocked) — i.e., for each independent set S of L, the set B(S) ⊆ R of vertices blocked (adjacent to S).
- List all independent sets of R as (sizeR, maskR).
- For each independent set T of R, we need max sizeL over independent sets S of L with S ∩ ... no: S and T compatible iff no edges between S and T iff T ⊆ R \ B(S) iff B(S) ∩ T = ∅.
- So: for each independent T of R, answer candidate = sizeR + max{ sizeL : B(S) ∩ T = ∅ }.
- Define G[M] for M ⊆ R: max sizeL over independent S of L with B(S) ∩ M = ∅, i.e., B(S) ⊆ R \ M. Hmm, that's again a subset DP over R: G[M] = max over S with B(S) ⊆ complement(M)... 

Define H[U] = max{ sizeL : S independent in L, B(S) ⊆ U } for U ⊆ R. Then answer = max over independent T of R of sizeR + H[R \ T]. And H can be computed: H[U] = max(H[U without lowest bit], max{ sizeL(S) : B(S) = ... }) hmm, H is a "zeta-like" DP: H[U] = max over S with B(S) ⊆ U of sizeL(S). This is a max-subset-sum (superset) DP: H[U] = max(base[U], max over v ∈ U of H[U \ {v}]) where base[U] = max sizeL among S with B(S) exactly... no, B(S) ⊆ U. Hmm, we'd initialize H[U] = w(U) where w(U) = max{sizeL(S) : B(S) = U} (or -inf), then H[U] = max(w[U], max_{v∈U} H[U\{v}]). This is the standard "subset max" DP, computable in nR × 2^nR operations — and THIS one is vectorizable! 

The subset-max DP: for each bit v (nR bits), for all U containing v: H[U] = max(H[U], H[U ^ (1<<v)]). This is the classic SOS (sum over subsets) DP, which vectorizes beautifully with numpy:

for v in range(nR):
    # for all U with bit v set: H[U] = max(H[U], H[U without v])
    # vectorized: reshape trick

The standard numpy vectorization of SOS DP: view the array of size 2^nR as shape (2^v, 2, 2^(nR-v-1)) and do H[:, 1, :] = maximum(H[:, 1, :], H[:, 0, :]). That's nR vectorized passes over 2^nR elements: 23 × 8.4M = 193M element-ops but as 23 numpy calls each on 4.2M elements — very fast (~0.1-0.3s total).

So the plan:
1. Enumerate all independent sets S of L, with sizeL(S) and B(S) ⊆ R (blocked mask). For each, update w[B(S)] = max(w[B(S)], sizeL(S)). Number of independent sets of L ≤ 2^23 = 8.4M. Enumerating them in Python... this is the bottleneck now. Hmm.

Wait, but actually we don't need to enumerate independent sets of L explicitly if we do the symmetric DP! Let's define things symmetrically:

For side L: for each subset U ⊆ L, define e[U] = max size of independent set within U (that's the f DP again — sequential). Hmm no.

Let me re-derive. We want max over independent sets I of the whole graph of |I|. Split I = S ∪ T, S ⊆ L independent, T ⊆ R independent, no cross edges.

Approach A: 
- Compute for side R: for each subset U ⊆ R, fR[U] = max independent set size within U. (Sequential DP, 2^nR states.)
- Enumerate independent sets S of L; for each, candidate = sizeL + fR[R \ B(S)].
- Bottleneck: sequential DP 2^23 + enumerating independent sets of L.

Approach B (SOS-based):
- For side L: enumerate all independent sets S of L; for each, set w[B(S)] = max(w[B(S)], |S|) where B(S) ⊆ R is the blocked-in-R mask. Then H[U] = max over subsets... compute H via SOS: H[U] = max{w[V] : V ⊆ U}. Then for each independent set T of R: candidate = |T| + H[R \ T]... wait let me double check: we need B(S) ∩ T = ∅, i.e., B(S) ⊆ R \ T. So candidate = |T| + H[R\T] where H[U] = max{ |S| : S independent in L, B(S) ⊆ U }. ✓.
- Bottleneck: enumerating all independent sets of L (up to 2^23) and all independent sets of R (up to 2^23), plus two SOS DPs (vectorizable) — but the enumeration of independent sets is the problem.

Hmm, enumerating up to 8.4M independent sets in pure Python is too slow (~10+ s). 

But wait — can we vectorize the enumeration of independent sets too? Or avoid it?

Alternative: compute w[B(S)] for all independent S of L via a DP over subsets of L? The issue: B(S) depends on the whole set S, not just... Hmm, but here's a trick: 

Actually, here's a cleaner idea. Let's define the DP over subsets of L differently. For the combination, what we ultimately need is: for each U ⊆ R, H[U] = max{ |S| : S ⊆ L independent, N(S) ∩ (R\U)... } hmm.

Alternative approach C (fully vectorizable, "DP over subsets with cross constraints"):

Let me think of it as: for each subset X ⊆ L, define gL[X] = (max size of independent set S ⊆ X... ) — no, the cross-blocking is the issue.

Hmm, here's another angle. Classic MITM for MIS (à la Kojevnikov et al. or the standard "split and list"): 

For each vertex subset... Let me think about the standard split & list for MIS: variables x_i ∈ {0,1} for i in L. For each vertex j ∈ R, constraint: if any neighbor of j in L is chosen, j can't be chosen. Hmm.

Standard split & list for max independent set (from "Exact Maximum Independent Set in O(1.19^n)" or the meet-in-the-middle for MIS): 

Actually the well-known approach: MIS(G) = max over subsets S of L that are independent of (|S| + MIS(G[R \ N(S)])). To make the second part table-lookup, precompute MIS for all 2^(n/2) subsets of R — the sequential DP. So Approach A is standard.

The sequential DP f over 2^23 subsets: can we vectorize it with the popcount-level trick? Let me flesh that out:

f: numpy uint8 array of size 2^nR. f[0] = 0.
Group all masks by popcount. For level t ≥ 1, for each mask T in level t:
  v = lowest set bit of T
  f[T] = max(f[T ^ (1<<v)], 1 + f[T & allowedR[v]])
where allowedR[v] = R-vertices not adjacent to v (within R), as a bitmask (excluding v itself).

Vectorized per level:
  Ts = array of masks with popcount t (int32)
  low = Ts & (-Ts)  (careful with numpy int32 negative — use int64 or compute via unsigned: low = Ts & (~Ts + 1)? In numpy, for signed ints, -Ts works as two's complement, and Ts & -Ts gives the lowest set bit correctly for signed types as long as Ts ≥ 0... Actually for signed int32, -Ts is computed as two's complement, and Ts & -Ts = lowest set bit. Yes that works. But safer: use int64 or uint32 with np.uint32 arithmetic: low = Ts & (-Ts) with uint32: numpy will complain about negative... Use int64: fine for values < 2^23.)
  v_idx = lz_table[low] — precomputed table mapping 2^v → v, size 2^23 uint8 (8MB). Gather: 8.4M total gathers across all levels.
  without_v = Ts ^ low
  a = f[without_v]  (gather)
  b = f[Ts & allowed_arr[v_idx]] — hmm, allowed_arr[v_idx] is a gather of size |level| from a small array (23 entries) — fast; then Ts & that — vector op; then f[...] — gather.
  f[Ts] = maximum(a, b + 1) — scatter.

Total numpy ops across all levels: ~8-10 ops per element × 8.4M elements ≈ 70-84M element-ops, in ~24 × 10 = 240 numpy calls. Gathers (fancy indexing) are the slow ones: 3 gathers + 1 scatter per element = 4 × 8.4M = 33.6M random accesses. numpy fancy indexing throughput: roughly 50-200M elements/s for gather (depends on cache — f is 8MB, exceeds L2 but fits L3 on many machines). Estimate ~0.5-1.5s. Plus the & ops etc. Probably total ~1-2s. Feasible!

But wait — there's a subtlety: within a level, f[Ts] = ... reads f[without_v] and f[Ts & allowed] — both have popcount < t, so they're already computed. ✓. And writes to f[Ts] within the level don't affect reads within the level (reads are lower levels). ✓.

Then, the L side: enumerate all independent sets S of L with their sizes and blocked masks B(S), and compute candidate = |S| + f[R_full \ B(S)] where R_full = (1<<nR) - 1. The number of independent sets of L can be up to 2^23 (empty graph on L). Enumerating them in pure Python: too slow if 8.4M.

Hmm! But wait — we can apply the same trick symmetrically? We need max over independent S of L of (|S| + f[allowedR(S)]). Define for each subset X ⊆ L: hL[X] = max size of independent set within X (the same sequential DP, on the L side). Then... no, that doesn't directly give the combination because allowedR(S) depends on S itself, not just its size.

Hmm. Let me think differently. 

Alternative: do the combination DP over subsets of L! Define, for each subset X ⊆ L: 
  best[X] = max over independent S ⊆ X of (|S| + f[allowedR(S)])? 
That's not decomposable simply because allowedR(S) isn't additive... Actually wait: allowedR(S) = R \ N(S), and N(S) = union of N(v) for v ∈ S. Hmm, f[allowedR(S)] — we're taking f of an intersection-ish... f[R \ N(S)] where N(S) is a union. Not decomposable per-element.

But here's a trick: reverse the roles. Define the combination as a DP over subsets of R instead:

We want max over independent T ⊆ R of (|T| + H[R \ T]) where H[U] = max{ |S| : S independent ⊆ L, N(S) ⊆ R \ U }... wait I had it before: H[U] = max{ |S| : S independent in L, B(S) ⊆ U } where B(S) = N(S) ∩ R. Then answer = max over independent T ⊆ R of (|T| + H[R \ T]).

To compute H: first w[U] = max{ |S| : S independent in L, B(S) = U } (exactly U), then SOS-max: H[U] = max_{V ⊆ U} w[V]. The SOS is vectorizable. The problem is computing w, which requires enumerating independent sets of L.

Alternatively compute w via a sequential DP over subsets of L? w[U] for U ⊆ R — indexed by R-subsets, but the DP would be over L-subsets... The mapping S ↦ B(S) is many-to-one. Hmm.

Hmm, what about computing H[U] for all U ⊆ R directly via a different DP: 

H[U] = max{ |S| : S ⊆ L, S independent, N(S) ∩ (R \ U) = ∅ }.

Consider DP over subsets of L: define for each subset X ⊆ L: 
  D[X] = max{ |S| : S ⊆ X, S independent, N(S) ∩ M = ∅ } — depends on M too. Two-dimensional. No.

OK here's another classic idea: **make the cross-constraint part of the per-side DP by folding**. 

Actually, you know what? Let's just think about whether we can enumerate independent sets of L efficiently enough, or find shortcuts.

Key insight: the number of independent sets of L is 2^23 only when L has no edges. If L has no internal edges, then... the problem is easier? Not necessarily (cross edges matter). Hmm, but wait: if L is an independent set (no internal edges), then every subset S of L is independent, and B(S) = union of neighborhoods. Then H[U] = max{ |S| : S ⊆ L, N(S) ∩ (R\U) = ∅ } = max number of L-vertices whose neighborhoods avoid R\U. This is itself computable... for each vertex v ∈ L, it's usable iff N(v) ∩ (R\U) = ∅, and since L is independent, we can take ALL usable vertices: H[U] = |{v ∈ L : N(v) ∩ (R\U) = ∅}| = count of v with N_R(v) ⊆ U. That's computable for all U via... for each v, mark. Hmm, this is a special case.

General case: we need max over independent S ⊆ L. This is like a "weighted independent set with forbidden-usage penalties" — actually here's a cleaner way to think:

H[U] = max{ |S| : S independent in L, B(S) ⊆ U }.

Equivalently: assign each vertex v ∈ L a "cost" mask N_R(v); we want max independent set in L using only vertices whose combined N_R stays within U. 

DP over subsets of L with the R-constraint folded in? The state would need to track which R-vertices are blocked — that's the 2-dimensional issue again.

Hmm OK, but wait. Let's reconsider. Maybe we don't need H for all U ⊆ R — we need H[R \ T] only for T that are independent sets of R. And symmetrically... circular.

Let me reconsider Approach A with both parts vectorized:

Part 1 (R side): f[U] = MIS size within U, for all U ⊆ R — via popcount-level vectorized DP. ✓ (described above).

Part 2 (L side + combination): max over independent S ⊆ L of |S| + f[R \ B(S)].

For part 2, define a DP over subsets of L: 
  g[X] = max over independent S ⊆ X of (|S| + f[R \ B(S)])? 
Can we compute g with a recurrence? g[X]: consider lowest vertex v ∈ X. Either S doesn't contain v: g[X \ {v}]. Or S contains v: then S \ {v} ⊆ X \ ({v} ∪ N_L(v)) independent, and B(S) = B(S\{v}) ∪ N_R(v). So the value = 1 + (|S\{v}| + f[R \ B(S\{v}) \ N_R(v)]) — but f[R \ B(S\{v}) \ N_R(v)] ≠ f[R \ B(S\{v})] minus something... we'd need f at "R \ B(S') \ N_R(v)" for arbitrary S' — i.e., we'd need to track B(S') in the state. 2-dimensional again. 

Unless... we define the DP state as (X, blocked mask in R)? That's 2^23 × 2^23. No.

Hmm, alternatively: swap which side gets the "f" treatment and which gets enumerated, and pick the side with FEWER independent sets to enumerate? Both could be 2^23 in the worst case (whole graph empty — but then answer trivially yes... but we still need to detect that; well, if the whole graph is empty, MIS = n ≥ k always, answer YES immediately. Actually more generally, if m = 0, answer YES with any k vertices).

Hmm, wait. Let's think about when the number of independent sets is huge: sparse graphs. For sparse graphs, MIS is large, and greedy finds large independent sets quickly. Could we use a hybrid: run a fast heuristic first; if it finds an independent set of size ≥ k, done. Otherwise (heuristic MIS < k), the graph must be reasonably dense, and then the number of independent sets is small?

Let's quantify: if the graph on L (23 vertices) has e edges, the number of independent sets is at most... For a graph with independence number α, the number of independent sets is at most sum_{i≤α} C(23, i). If heuristic gives MIS(G) < k, then α(G) < k, so α(L) < k, so independent sets of L number ≤ sum_{i=0}^{k-1} C(23, i). If k is small, this is small. If k is large (say k = 30), then sum_{i≤29} C(23,i) = 2^23 — no constraint. But if k is large, then... hmm, we need MIS ≥ 30 out of 46 — that means the graph is quite sparse (complement is dense). For the enumeration to be big, L must be sparse; L sparse → α(L) large → likely MIS overall is large → heuristic likely finds it. But "likely" isn't a guarantee.

Hmm, let me think about whether there's a cleverer exact algorithm. 

Actually — wait. Let me revisit: maybe pure branch-and-bound with a good bound is fine. n=46 is small. Let me think about the worst-case for a well-bounded B&B. Known results: exact MIS solvers handle random graphs with n in the hundreds or thousands. Hard instances are structured (e.g., Ramsey-type, combinatorial designs). For a problem with n ≤ 46 (this looks like a "problem A" from some contest — probably intended solution is MITM in C++), test cases are probably not adversarial against B&B... but I shouldn't rely on that. Actually, since this is likely from a contest where the intended solution is meet-in-the-middle (n ≤ 46 is the classic MITM MIS threshold — e.g., from "Nordic Collegiate Programming Contest" or some Russian contest), tests might include hard instances like Ramsey graphs where MIS is small and hard to find. Hmm, but with n=46, even a decent B&B should handle it. Let me think about known hard instances: the smallest hard instances for modern MIS solvers have n ≥ 100+ (e.g., DIMACS instances). For n=46, even mediocre B&B should finish quickly. But Python is slow...

Let me estimate a simple B&B in Python: nodes with bitmask ops. A typical search tree for n=46 with coloring bound: maybe 10^3–10^5 nodes for typical instances, up to maybe 10^6 for nasty ones. At ~10-50 μs per node in Python → 0.01–50 s. Risky in the worst case but probably fine typically. Hmm.

Alternatively, implement MITM fully vectorized with numpy. Let me think harder about how to make BOTH sides vectorized, because I think it's possible with the popcount-level trick on both sides plus a vectorized combination.

Full plan (Approach A, vectorized):

Side R: compute f[U] for all U ⊆ R (MIS within U) — vectorized popcount-level DP. ✓

Side L + combination: we need max over independent S ⊆ L of (|S| + f[R \ B(S)]).

Idea: compute this via a DP over subsets of L where the state is just X ⊆ L, using a DIFFERENT decomposition. Hmm, the problem is f[R \ B(S)] couples everything.

Alternative idea: **fold the R-side into the L-side DP via "profile"**? No.

Alternative: **Use the SOS trick on the L side instead, and enumerate R's independent sets** — symmetric problem. One of the two sides must be enumerated. 

Hmm, wait, actually — can we enumerate independent sets of a 23-vertex graph efficiently in a vectorized way? 

Independent set enumeration via DP: the number of independent sets can be 8.4M. Even just writing out 8.4M entries (mask, size, blocked) in Python is too slow. But numpy could do it if we can vectorize...

Hmm, think: all subsets of L = np.arange(2^23). Independent subsets = those with no edge inside. Checking independence for all subsets vectorized: for each edge (u,v) in L: eliminate masks containing both u and v: masks[(masks has bit u) & (has bit v)] — we can do this with a boolean array: keep = np.ones(2^23, bool); for each edge: keep &= ~((M >> u & 1) & (M >> v & 1))... that's per-edge vector ops over 8.4M — with up to 253 edges in L, that's 253 × 8.4M = 2.1G element-ops. Too slow. 

Better: compute independence via the sequential DP anyway... 

Hmm wait, actually here's a much better idea for the L side. Let me define the L-side DP as follows:

For each subset X ⊆ L, define:
  F[X] = max over independent S ⊆ X of ( |S| + f[ R \ B(S) ] )   ... (the quantity we want, with X = L)

Recurrence on the highest vertex? F[X] = max(F[X \ {v}], ...) — the "contains v" branch needs f at modified masks. Doesn't work as noted.

BUT: what if we make the R-side DP f richer? Define instead of f[U] (max size), define f2[U] = ... we need to handle "B(S) ∪ N_R(v)". Note R \ (B(S) ∪ N_R(v)) = (R \ B(S)) ∩ allowedR(v). So if in the L-side DP we track the "currently allowed R-set" A = R \ B(S), then adding vertex v updates A ← A ∩ allowedR(v). The value we want at the end is |S| + f[A]. So define the L-side DP with state (X ⊆ L, A ⊆ R)? Too big. 

BUT here's the trick: we can do the L-side DP where we process vertices of L one at a time, and the state is (X, A)... no. 

Alternative trick — "shift the f lookup into the DP": Define G[X][A]? No.

Hmm, what about a completely different combination method: **weighted SOS on both sides**. Let me look at this from the "split and list" SAT-ish perspective:

We want max Σ over chosen vertices, subject to: for each edge (u,v), not both chosen. Split edges into three classes: LL edges, RR edges, LR edges.

- Enumerate independent sets of L: list of (S, |S|, B(S)) — the LL constraints handled.
- Enumerate independent sets of R: list of (T, |T|, A(T)) where A(T) = allowed L-vertices.
- Combine: need max |S| + |T| s.t. S ⊆ A(T) (equivalently T ⊆ R \ B(S)).

For the combination, sort/organize one side by mask and do subset-max queries — the standard way is the SOS DP over one side's masks. So: 

Side L: build array w over subsets of R: w[U] = max{ |S| : S independent in L, B(S) = U } (or -1 if none). Then H = SOS-max: H[U] = max_{V ⊆ U} w[V]. Then answer = max over independent T of R of (|T| + H[R \ T]).

To build w without enumerating independent sets of L one by one in Python: hmm, we need, for each independent S, w[B(S)] = max(w[B(S)], |S|). 

Vectorized idea: iterate over all subsets X of L in popcount-level order, computing two arrays over subsets of L: 
  - ind[X] = (is X independent) — computable via: ind[X] = ind[X \ lowbit] and (lowbit-vertex has no neighbors in X \ lowbit)... i.e., ind[X] = ind[X ^ low] and ((X ^ low) & adjL[v] == 0). Vectorizable per popcount level! ✓
  - For independent X: we want to record |X| at index B(X) in w. B(X) = OR of N_R(v) for v ∈ X. Computing B(X) for all X: B[X] = B[X ^ low] | N_R(v). Vectorizable per level: B is an array over 2^nL subsets (int32), B[X] = B[without_v] | NR[v_idx]. ✓ (gather + or + scatter).

So: compute arrays over all 2^nL subsets of L: ind (bool), B (int32), and then for independent X: w[B[X]] = max(w[B[X]], popcount(X)). The last step is a scatter-max: np.maximum.at(w, B[ind_masks], sizes) — np.maximum.at is notoriously slow (~10M/s?). Hmm, 8.4M scatter-max operations via np.maximum.at could take ~5-10s. Too slow. 

Alternative: sort by B value and use np.maximum.reduceat, or use the fact that... hmm. Alternatively: since we ultimately apply SOS-max over w anyway, note that H[U] = max over independent S with B(S) ⊆ U of |S|. 

Alternative: skip w; directly compute H via a different route: H[U] = max over independent S ⊆ L with B(S) ⊆ U of |S|. 

Hmm, what if we do the SOS on the L side instead: define over subsets of L... no, H is indexed by R-subsets.

Wait, actually, maybe reverse: let's do the SOS-max over subsets of L instead, and enumerate R's independent sets. Symmetric — same problem.

Hmm, but here's a cleaner idea: **do the scatter-max smartly**. We have up to 8.4M (B(X), |X|) pairs (only for independent X). We want w[U] = max |X| over pairs with B(X) = U, then SOS. 

Instead of scatter-max into w (size 2^23) and then SOS over R-subsets, we can:
1. Sort pairs by B (numpy argsort on ≤8.4M int32: ~1s, hmm).
2. ... still messy.

Alternative: use np.maximum.at but reduce the number of items: note that for the SOS-max H[U] = max_{V ⊆ U} w[V], we can instead compute directly: H[U] = max over independent S with B(S) ⊆ U of |S|. 

Flip it around: H[U] = max{ |S| : S independent in L, N_R(S) ∩ (R\U) = ∅ }. 

Define M = R \ U (the "forbidden" R-vertices). H[R \ M] = max{ |S| : S independent in L, no vertex of S adjacent to M }. Call this Q[M]: max independent set in L avoiding neighborhoods of M. Q[M] = MIS of the graph L restricted to vertices with N_R(v) ∩ M = ∅. 

So Q[M] = fL[ L \ N_L(M) ] where fL is the L-side "MIS within subset" DP! Oh nice!! Let me double check: Q[M] = max independent set among L-vertices v with N_R(v) ∩ M = ∅. The set of allowed L-vertices is X(M) = {v ∈ L : N_R(v) ∩ M = ∅}. Then Q[M] = fL[X(M)] where fL[Y] = MIS within Y ⊆ L. ✓✓

So: answer = max over independent T ⊆ R of (|T| + fL[X(R \ T)]) where X(U) = {v ∈ L : N_R(v) ⊆ U}.

Hmm wait, let me recompute: we need S and T with no cross edges: S ⊆ {v : N(v) ∩ T = ∅} = X' where X'(T) = L-vertices not adjacent to T. And S must be independent in L. So the best S given T is MIS_L within X'(T), which is fL[X'(T)]. So:

answer = max over independent T ⊆ R of ( |T| + fL[ X'(T) ] ), where X'(T) = {v ∈ L : N_R(v) ∩ T = ∅} = {v : N_R(v) ⊆ R \ T}.

So we need: (a) fL over all subsets of L (vectorized popcount-level DP — same as before, on the L side), and (b) enumerate independent sets T of R with |T| and X'(T). 

Damn, (b) still requires enumerating independent sets of R. BUT — here's the key realization — we can compute max over independent T of (|T| + fL[X'(T)]) via a DP over subsets of R! Define:

g[T] = max over independent T' ⊆ T of ( |T'| + fL[X'(T')] )? 

Hmm, recurrence: g[T] with lowest vertex v ∈ T: either T' doesn't contain v: g[T \ {v}]; or T' contains v: then T' \ {v} ⊆ T \ ({v} ∪ N_R(v)) must be independent, and X'(T') = X'(T' \ {v}) ∩ allowedL(v)... so fL[X'(T' \ {v}) ∩ allowedL(v)] — again the f-lookup at a modified set. Same issue as before. Argh. The fundamental issue: the combination couples the two sides.

OK so at least ONE side must be enumerated as independent sets (with their properties), OR we need the scatter-max approach. Let me reconsider the scatter-max approach's cost, or find a way to avoid enumerating.

Hmm wait, actually, let's reconsider. What about doing the whole thing as a DP over subsets of ONE side, where the other side's contribution is folded via the f-array, using this identity:

max over independent T ⊆ R of (|T| + fL[X'(T)]) — let me define per R-vertex... 

Alternative: think of it as a maximum-weight independent set problem on R where the weight of T is |T| + fL[X'(T)] — but weights aren't additive. However! We can use the following trick: fL[X'(T)] = fL[ L \ N_L^{cross}(T) ] where N_L^{cross}(T) = L-vertices adjacent to T. Hmm.

What if we enumerate over subsets M = N_L^{cross}(T)? For each M ⊆ L, define bestR[M] = max |T| over independent T ⊆ R with N_L^{cross}(T) = M... then answer = max over M of bestR[M] + fL[L \ M]. And bestR over all M: scatter-max again, but now we can compute bestR[M] via SOS-style DP? bestR[M] = max{|T| : T independent in R, N_L^{cross}(T) ⊆ M}? No wait, we need exact M for the formula fL[L\M]... hmm, actually if N(T) ⊆ M then L \ M ⊆ L \ N(T) = X'(T), so fL[L \ M] ≤ fL[X'(T)]... that gives a lower bound, not exact. But for maximization: answer = max over independent T of (|T| + fL[X'(T)]) = max over T of (|T| + max over M ⊇ N(T) of ... no. Hmm: fL[X'(T)] where X'(T) = L \ N(T). If we define for each M: h[M] = max{|T| : T independent, N(T) ⊆ M}, then answer = max over M of (h[M] + fL[L \ M])? Let's verify: for a given T, taking M = N(T): h[N(T)] ≥ |T| and fL[L \ N(T)] = fL[X'(T)] — so max over M ≥ max over T. Conversely, for any M and any T counted in h[M] (N(T) ⊆ M): |T| + fL[L\M] ≤ |T| + fL[L\N(T)] ≤ answer. ✓ So answer = max over M ⊆ L of (h[M] + fL[L \ M]). 

And h[M] = max{|T| : T independent in R, N_L^{cross}(T) ⊆ M} — this is a "max independent set in R with all cross-neighbors inside M". Can we compute h via a DP over subsets of R with... h depends on M ⊆ L. Two-dimensional again (2^23 × 2^23). BUT: h[M] can be computed via SOS-style if we first compute h0[P] = max{|T| : T independent, N(T) = P} (scatter-max over 2^nL indices) then SOS-max over L-subsets: h[M] = max_{P ⊆ M} h0[P]. The scatter-max is the issue again. Hmm, but wait — maybe we can compute h0/P-to-M more cleverly.

Hmm hold on. Let me step back and think about the sizes: is the scatter-max really that bad? We need, for all subsets X of L (2^23 = 8.4M), if X is independent: w[B(X)] = max(w[B(X)], |X|) where B(X) ⊆ R... wait no, I flipped sides. Let me redo consistently.

Let me now fix the design: 
- L side: compute fL[Y] for all Y ⊆ L via vectorized popcount DP. (fL[Y] = MIS within Y.)
- R side: enumerate independent sets T ⊆ R; answer = max(|T| + fL[X'(T)]).
- To enumerate R's independent sets T and compute X'(T) = L \ N_L(T) vectorized: over all subsets of R (2^nR masks), compute ind[T] (independent?) and NL[T] = N_L^{cross}(T) (int over L bits) via popcount-level DP: NL[T] = NL[T \ low] | NLcross[v]. Then for independent T: candidate = |T| + fL[fullL & ~NL[T]]. Then answer = max over independent T of candidate. This is a masked gather + max — vectorizable! For all T (or just independent ones): vals = fL[(fullL & ~NL_arr)[ind_mask]]... 

Wait, but this requires computing NL[T] for ALL 2^nR subsets T (not just independent ones) — that's fine, it's a vectorized DP over 8.4M entries: NL[T] = NL[T ^ low] | NLc[v]. And ind[T] similarly. Then final: for independent T: val = pc(T) + fL[fullL & ~NL[T]]; take max. All vectorized!

But hold on — this is asymmetric: we're enumerating ALL subsets of R (not just independent ones) and using fL lookups. The cost: DP arrays over 2^nR subsets for NL (int32: 8.4M × 4B = 33MB) and ind (bool: 8.4MB), plus fL array over 2^nL subsets (uint8: 8.4MB). Plus per-level gathers. Totally feasible!

Wait, but there's still an issue: we're iterating over ALL subsets T of R and checking independence — that's fine, 8.4M subsets, vectorized. And for each independent T, we compute the candidate. The max over all gives the answer. And we don't need any scatter-max! 

Let me double-check correctness: MIS(G) = max over T ⊆ R independent of (|T| + MIS(L restricted to X'(T))) where X'(T) = L-vertices with no neighbor in T. Yes: any independent set I of G splits into T = I ∩ R (independent in R) and S = I ∩ L (independent in L, and no cross edges so S ⊆ X'(T)). Conversely any such pair gives an independent set. ✓.

So the algorithm:
1. nL = n // 2 (or split to balance memory: both sides ≤ 23). Let nL = n - n//2? Let's just say L = first nL vertices, R = rest. To minimize max(2^nL, 2^nR), set nL = n//2, nR = n - nL. For n=46: nL=23, nR=23. For n=45: 22, 23. Fine.

2. Compute fL[Y] for all Y ⊆ L: fL[Y] = max independent set size within Y. Vectorized popcount-level DP:
   - fL = np.zeros(2^nL, uint8); fL[0] = 0.
   - For levels t = 1..nL: Ts = masks with popcount t (precomputed grouping).
     low = Ts & (-Ts); v = lz[low] (or via table); 
     fL[Ts] = max(fL[Ts ^ low], fL[Ts & allowedL[v]] + 1)
     where allowedL[v] = (bits of L) & ~adj[v] (adj within whole graph, restricted to L, excluding v itself — note v ∉ allowedL[v] anyway since we take Ts & allowed and Ts contains v... wait, Ts & allowedL[v]: allowedL[v] should exclude v; since adj[v] doesn't include v itself, ~adj[v] includes v. So define allowedL[v] = fullL & ~adj[v] & ~(1<<v). Or just note Ts & ~adj[v] still contains v — that would give fL[Ts & ~adj[v]] which includes v — wrong (would allow reusing v). So must exclude v: allowedL[v] = fullL & ~(adj[v] | (1<<v)). ✓

3. Compute over all T ⊆ R: 
   - ind[T]: whether T is independent in R.
   - NL[T]: bitmask over L of vertices adjacent to some vertex of T.
   DP by popcount levels:
     ind[T] = ind[T ^ low] and ((T ^ low) & adjR[v] == 0)
     NL[T] = NL[T ^ low] | NLcross[v]
   where v = lowest bit.
   Base: level 0: T=0: ind=True, NL=0.
   
4. answer = max over T with ind[T] of (popcount(T) + fL[fullL & ~NL[T]]).

   Vectorized: pc = popcount array over all subsets of R (precomputed vectorized). vals = pc + fL[(fullL & ~NL)] — but only for independent T; for non-independent T, fL lookup is still valid (just ignore). We can compute vals for all T and then mask: vals[~ind] = -1 or use np.where. Actually simpler: compute cand = pc + fL[fullL & ~NL_arr] for all T, then set cand[~ind] = 0 (or -inf), then answer = cand.max(). Since for non-independent T we must exclude. Note: T=0 gives cand = 0 + fL[fullL] = MIS(L) ≥ 0, fine.

   Wait, but actually we could skip the ind array: for non-independent T, cand might exceed the true MIS? E.g., T contains an edge, |T| + fL[...] could exceed MIS(G)? Yes it could (e.g., complete graph on R with 2 vertices, L empty: T = both vertices: cand = 2 + 0 = 2 > MIS = 1). So we do need ind. ✓

5. If answer ≥ k: reconstruct. Reconstruction: we need an actual independent set of size ≥ k. 

Reconstruction plan: 
   - Find the T achieving the max (or any T with ind[T] and pc(T) + fL[fullL & ~NL[T]] ≥ k). We can find argmax of cand (with ind mask). Then S-side: need an independent set within Y* = fullL & ~NL[T*] of size fL[Y*] — reconstruct from fL DP: standard: start with Y = Y*; while Y: v = lowest bit; if fL[Y] == fL[Y ^ low]: Y ← Y ^ low (v not used); else: v is used: record v; Y ← Y & allowedL[v]. This works because fL[Y] = max(fL[Y^low], 1 + fL[Y & allowedL[v]]). ✓
   - But careful: we need total size ≥ k, and then output exactly k vertices from the union (any subset of an independent set of size ≥ k... wait, we need exactly k, and any k-subset of an independent set is independent ✓).
   - Also T* itself: T* is independent by ind[T*] ✓, and S* from reconstruction is independent in L ✓, and S* ⊆ X'(T*) so no cross edges ✓. Total = |T*| + |S*| = cand value ≥ k. Output any k of them. ✓

   Hmm wait, one subtlety: cand[T*] = pc(T*) + fL[Y*], and reconstruction of S* gives exactly fL[Y*] vertices. ✓.

6. Edge cases: n=1: nL = 0, nR = 1. Then L is empty: fL array over 2^0 = 1 subset: fL[0] = 0. fullL = 0. R = {vertex 0}. Subsets of R: T=0: cand = 0 + fL[0 & ~0] = fL[0] = 0. T={0}: ind = true, NL = N_L(0) = 0, cand = 1 + fL[0] = 1. So MIS = 1. If k=1: YES, output vertex. ✓.

   Also m=0: fine. k ≤ n always ≥ 1.

Now, the heavy part: step 3 requires arrays over 2^nR subsets: NL (int32 or int64 — L has ≤ 23 bits, so int32 suffices... but careful: numpy int32 bitwise ops fine). ind (bool). pc (uint8). And grouping subsets by popcount.

Memory: 2^23 × (4 + 1 + 1) = 50MB for the R side, plus fL 8.4MB, plus per-level temporary arrays (level sizes up to C(23,11) ≈ 1.35M × 8 bytes × few = fine), plus the initial np.arange(2^23) as int64 = 67MB — hmm, that's big; use int32 (33MB). Total maybe ~120MB peak. Memory limit 256MB. Should be OK if careful. Let me plan memory carefully:

- all_masks = np.arange(2^nR, dtype=np.int32): 33.5MB (for nR=23).
- popcount: compute pc8 = uint8 array 8.4MB. Computing popcount vectorized: 
  pc = all_masks; then for each bit: pc = pc - ((pc >> 1) & 0x5555...); standard SWAR on int32. Or simpler: pc = np.zeros(uint8); for b in range(nR): pc += (all_masks >> b) & 1 — that's 23 passes over 8.4M int32 → 23 × 33MB reads... ~2-3 GB of memory traffic, maybe 1-2s. Hmm. SWAR: ~6 vector ops on int32 (33MB each) → faster. Or: pc via np.bitwise_count if numpy ≥ 2.0 (np.bitwise_count exists in numpy 2.0!). Not guaranteed available. Let me do SWAR:
    x = all_masks.copy() (int32)
    x = x - ((x >> 1) & 0x55555555)
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    x = (x + (x >> 4)) & 0x0F0F0F0F
    pc = (x * 0x01010101) >> 24 — hmm, multiplication overflow in int32? x ≤ 0x0F0F0F0F-ish per byte... (x + (x>>4)) & 0x0F0F0F0F gives per-byte counts ≤ 8 (since ≤ 23 < 32, per byte ≤ 8 fits). x * 0x01010101 in int32: 0x0F0F0F0F * 0x01010101 overflows int32 → use int64 or just extract byte: since nR ≤ 23, the top byte of x is 0 (bits 24-31 zero since x < 2^23 → after masking, bytes: b0 = count of bits 0-3, b1 = bits 4-7, b2 = bits 8-11, b3 = bits 12-15, b4 = bits 16-19, b5 = bits 20-22 → x after & 0x0F0F0F0F: hmm bits 16+ are in byte positions 2 (bits 16-23)... let me redo: after (x + (x>>4)) & 0x0F0F0F0F, each byte i of x holds popcount of bits [4i, 4i+3]. For 23-bit numbers, bytes 0..5 relevant (byte 5 = bits 20-23). Then total = b0+b1+b2+b3+b4+b5. Multiply trick: x * 0x01010101 >> 24 gives b0+b1+b2+b3 (bytes 0-3 summed into byte 3)... For 23 bits we need bytes 0-5. Simpler: cast to int64 then multiply: y = x.astype(np.int64); pc = (y * 0x0101010101010101) >> 56 as uint8. Or even simpler: pc = x.astype(uint8) style sums... Alternatively compute pc via np.add.reduce over bytes? Simplest robust: 
    x = all_masks.astype(np.int64) — 67MB, hmm.
    
    Alternative approach: compute pc incrementally during the level DP! Actually, we need pc for the final candidate computation (|T| = pc(T)), and for grouping subsets by popcount. Hmm, grouping: we need, for each level t, the array of masks with popcount t. 

    Alternative grouping method without popcount computation: generate combinations! For level t, masks = [sum(1<<i for i in comb) for comb in combinations(range(nR), t)] — pure Python, 8.4M total combinations → too slow (~5-10s). No.

    Better: compute popcount via SWAR into uint8, then group. Let me just do SWAR carefully with int32 and extract:
      x = masks (int32, values < 2^23)
      x -= (x >> 1) & 0x55555555  — wait, standard: x = x - ((x >> 1) & 0x55555555). In int32 arithmetic, fine.
      x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
      x = (x + (x >> 4)) & 0x0F0F0F0F
      Now bytes 0..5 hold nibble-pair counts (each ≤ 8... actually each byte holds count of 8 bits ≤ 8 ✓).
      pc = (x & 0xFF) + ((x >> 8) & 0xFF) + ((x >> 16) & 0xFF) + ((x >> 24) & 0xFF) — but as int32 arithmetic then cast to uint8. That's 3 shifts + 3 ands + 3 adds on int32 arrays (33MB each pass, ~10 passes ≈ 330MB traffic, fast ~0.3s). Or use the multiply trick on int64. Either fine. Actually simpler: 
      pc32 = x with bytes summed. Let me do: 
        y = x.astype(np.uint8).view? Hmm, viewing int32 array as uint8 gives 4× length; then reshape (N,4) and sum axis 1: pc = arr.view(np.uint8).reshape(-1,4).sum(axis=1) — that's neat: view as uint8 (33.5M elements), reshape to (8.4M, 4), sum along axis 1 (uint8 sum → need dtype: .sum(axis=1, dtype=np.uint8)? sums ≤ 23 fit uint8 ✓). This is one pass, fast. 

    Then grouping by popcount: 
      order = np.argsort(pc, kind='stable')? Sorting 8.4M uint8 — numpy sort of uint8 is fast (radix-ish? it's quicksort by default; for uint8, np.sort is quite fast). Then masks_by_level via np.searchsorted on sorted pc. Alternatively: counts = np.bincount(pc, minlength=nR+1); offsets = cumsum; then order = np.argsort(pc, kind='stable') gives masks grouped by popcount, and within level we don't care about order. argsort of 8.4M elements: ~0.5-1.5s? Hmm. For uint8, numpy uses... I believe np.argsort on 8.4M uint8 takes maybe 0.5s. Acceptable but let me think of something faster.

      Faster grouping: for each level t, masks_t = masks[pc == t] — 24 boolean-mask passes, each pass reads pc (8.4M) + writes selected (avg 350k) → 24 × ~10ms = 0.25s. And computing pc==t is 24 passes... total fine. Actually even better: use np.argwhere? Similar cost. Or: sort once. Either is fine; boolean selection is simple and predictable: total extra memory = sum of level arrays = 8.4M int32 = 33.5MB (if we keep them all) — or we can keep them as a list of arrays; total 33.5MB. OK.

      Hmm wait, actually we could avoid materializing per-level mask arrays: we need, per level, to process Ts. We need the masks grouped. Materializing is fine.

Actually hold on. Let me reconsider whether we need popcount-level processing at all for the R-side DP (ind, NL). The recurrence ind[T] = ind[T^low] and ((T^low) & adjR[v])==0; NL[T] = NL[T^low] | NLc[v]. Dependencies: T^low < T numerically. If we process T in increasing numeric order 1..2^nR-1 sequentially, dependencies are satisfied — but that's a pure Python loop (8.4M iterations — too slow). With level processing, within-level independence of reads/writes ✓ (reads at level t-1 or lower... wait: T^low has popcount t-1 ✓; and that's the only read. ✓).

Alternatively — process in blocks with numpy where dependencies... no, level processing is clean.

Hmm, wait, actually, there's an even simpler alternative for ind and NL that avoids per-level gathers: 

ind[T]: T is independent iff for every edge... Alternative: compute via "for each vertex v, mark masks where v is the lowest bit and check..." — that's what we're doing.

Alternatively, compute NL[T] for all T via SOS-style?? NL[T] = OR of NLc[v] for v ∈ T. This is an OR-subset DP: NL[T] = NL[T ^ low] | NLc[v] — sequential-ish, but OR-SOS can be done as: NL[T] = OR over v ∈ T of NLc[v]. The standard SOS for OR: for each bit b: for all T with bit b set: NL[T] |= NL[T ^ (1<<b)]. That's nR passes over the full 2^nR array, each pass vectorizable via the reshape trick! 

for b in range(nR):
    NL = NL.reshape(-1, 2, 1 << b)?? Let me get the reshape right: we want, for all T with bit b set: NL[T] = NL[T] | NL[T ^ (1<<b)]. View array as shape (2^(nR-b-1), 2, 2^b) where the middle axis is bit b: index T = i * 2^(b+1) + m * 2^b + j. Then NL[:, 1, :] |= NL[:, 0, :]. ✓ This is exactly the SOS DP, fully vectorized, no popcount grouping needed!! Each pass: read 2^(nR-1) elements, OR, write 2^(nR-1) — 23 passes × 4.2M = ~97M element-ops but as 23 numpy calls. FAST (~0.1-0.3s). 

Similarly, ind[T] (independence): T independent iff no edge within T. Hmm, can we compute ind via SOS-style passes? ind is not additive like that. But: T independent iff for the lowest... hmm. Alternative: T independent iff T ∩ (anything)... Let me think: define for each T, bad[T] = 1 if T contains both endpoints of some edge. Hmm. 

Alternative: T independent iff for every v ∈ T, N(v) ∩ (T \ {v}) = ∅. 

Trick: compute cnt[T] = number of edges (u,w) with u,w ∈ T? That's a sum over subsets — SOS-able! For each edge e = (u,w) with mask e_m = (1<<u)|(1<<w): base[e_m] = 1; then cnt[T] = sum over subsets — SOS-sum: for each bit b: for T with bit b: cnt[T] += cnt[T ^ (1<<b)]. Then ind[T] = (cnt[T] == 0). ✓ Fully vectorizable with the same reshape trick, using int8 or int16 (max edges within R: C(23,2) = 253 > 255? 253 < 256, fits uint8 barely; use int16 to be safe — 16.8MB). 

So R-side: 
- cnt: int16 array 2^nR, SOS-add over edges within R (each edge: base cnt[(1<<u)|(1<<w)] += 1 — scatter, few ops), then 23 SOS passes. ind = cnt == 0.
- NL: int32 array 2^nR, initialized NL[T] = NLc[lowest bit]? Hmm — the SOS-OR DP: initialize NL[T] = 0 for all T, then... wait, SOS-OR computes NL[T] = OR of base over subsets: NL[T] = OR_{V ⊆ T} base[V]. If we set base[{v}] = NLc[v] for each v (scatter: NL[1<<v] = NLc[v] — but careful: base[0] = 0 ✓), then after SOS-OR passes, NL[T] = OR of NLc[v] over v ∈ T ✓. 

Similarly pc[T] = popcount: SOS-add with base[{v}] = 1: pc[T] = number of v ∈ T ✓. Or just compute pc via SWAR (probably faster than 23 SOS passes? Both fine). Actually we can compute pc from... hmm, SWAR is fine and independent.

And fL on the L side: fL[Y] = MIS within Y. Is there an SOS-style computation for fL? fL is a max over independent subsets — not additive. Hmm. The recurrence fL[T] = max(fL[T^low], 1 + fL[T & allowed(v)]) needs level processing. 

Hmm wait — alternative for fL: fL[Y] = max{ |S| : S ⊆ Y, S independent }. We could compute it as: for all independent S ⊆ L (which we'd enumerate... no). OR: use the cnt trick: fL[Y] = max{ t : ∃ S ⊆ Y, |S| = t, cnt[S] = 0 }. Hmm, that's a max over subsets with a constraint — the popcount-level DP seems needed. 

Alternatively, compute fL via a different vectorized scheme: process vertices one at a time with DP over subsets? fL as function of Y... Let me think: is there a way to compute "max independent subset size within Y" for all Y via SOS-like passes? 

Hmm: define g[Y] = max{ |S| : S ⊆ Y, S independent }. Consider the "weighted subset max" formulation: g[Y] = max over independent S ⊆ Y of |S|. If we had w[S] = |S| for independent S, -inf otherwise, then g = SOS-max of w: g[Y] = max_{S ⊆ Y} w[S]. SOS-max is vectorizable (23 passes with np.maximum on reshaped views)! And w[S] = |S| if cnt[S] == 0 else -inf — computable via cnt (SOS-add) and pc (SWAR)! 

So: 
- pcL: popcount over subsets of L (SWAR) — uint8, 2^nL.
- cntL: edges-within count (SOS-add, int16) — 2^nL.
- w = where(cntL == 0, pcL, -1) (int8).
- fL = SOS-max of w: for b in range(nL): view reshape, fL[:,1,:] = maximum(fL[:,1,:], fL[:,0,:]). Result: fL[Y] = max_{S ⊆ Y} w[S] = MIS within Y ✓ (note S=∅ always gives w=0, so fL ≥ 0 ✓).

This avoids the popcount-level gather DP entirely! All SOS passes with reshape views — very numpy-friendly.

Similarly, the R side: we need for each T ⊆ R: ind[T] (via cnt SOS-add), NL[T] (SOS-OR), pc[T] (SWAR or SOS-add). Then cand[T] = pc[T] + fL[fullL & ~NL[T]] for ind[T], and answer = max.

Wait, but actually — hmm, hold on. If we're doing SOS-max on the L side anyway, do we even need the R-side enumeration over ALL subsets? We need max over independent T of (|T| + fL[X'(T)]). We're iterating all T ⊆ R (8.4M), computing NL[T] via SOS-OR, checking ind[T], gathering fL. The gather fL[fullL & ~NL[T]] is a random gather over 8.4M elements — that's the main cost (~0.3-1s). Fine.

Actually wait, can we simplify further: note X'(T) = fullL & ~NL[T], and fL[X'(T)] = max_{S ⊆ X'(T)} w[S] = max_{S: S ⊆ L, S ∩ NL[T] = ∅} w[S] = max_{S independent in L, NL[T] ∩ ... } hmm — S ⊆ X'(T) iff S ∩ NL[T] = ∅ iff NL[T] ⊆ L \ S iff (N_R(S) ∩ T = ∅). So cand[T] = pc[T] + max{w[S] : N_R(S) ∩ T = ∅}. 

Alternative symmetric formulation: answer = max over (S independent in L, T independent in R, N_R(S) ∩ T = ∅) of |S| + |T|. 

Could we do a "double SOS"? Define over subsets of... hmm, the pair (S,T) constraint is N_R(S) ∩ T = ∅. 

Alternative: for each independent S, allowed T's are those ⊆ R \ N_R(S). So answer = max over independent S of (w[S] + fR[R \ N_R(S)]) where fR[U] = max_{T ⊆ U independent} |T| — same structure mirrored. Either way, one side gets full-subset iteration with a gather into the other side's SOS-max array. Current plan: iterate all T ⊆ R, gather fL. Good.

Hmm, but wait: actually we can even avoid the gather! Define the combined quantity via SOS over R: 

answer = max over T independent of (pc[T] + max{w[S] : NL[T] ∩ S = ∅}).

Define for each S independent in L: mask M(S) = N_R(S) ⊆ R (the blocked R-vertices). Then condition: T ∩ M(S) = ∅. So answer = max over independent S, T with T ∩ M(S) = ∅ of |S| + |T| = max over M ⊆ R of ( h[M] + gR[R \ M] )? where h[M] = max{w[S] : M(S) ⊆ M} (SOS-max over L-indexed... no wait, M(S) is a subset of R, so h is indexed by subsets of R: h[M] = max{|S| : S ind in L, N_R(S) ⊆ M}) and gR[U] = max{|T| : T ind in R, T ⊆ U} (SOS-max over R subsets). Then answer = max over M of h[M] + gR[R\M]... but h requires scatter-max of w[S] into index N_R(S) over subsets of R — scatter-max over up to 8.4M items — np.maximum.at slow. Unless we compute h via SOS over... hmm, h[M] = max over S with N_R(S) ⊆ M. 

Alternatively compute h via a clever SOS: h[M] = max{ |S| : S independent in L, ∀v ∈ S: N_R(v) ⊆ M } = max{ |S| : S independent, S ⊆ A(M) } where A(M) = {v ∈ L : N_R(v) ⊆ M} = fL-ish... circular again (h[M] = fL[A(M)] — and A(M) requires per-M computation — that's the gather approach again, fine).

OK so the gather approach it is: iterate all T ⊆ R, compute cand[T] = pc[T] + fL[fullL & ~NL[T]], mask by ind[T], take max. 

Let me now also double check: is iterating over all 2^nR subsets with gathers OK cost-wise? 8.4M gathers from an 8.4MB array (fL, uint8) — random access pattern (NL[T] varies) — cache misses. numpy fancy indexing: maybe 50-150M/s → 0.06-0.17s... realistically ~0.5s. Fine.

Now, total memory: 
R-side arrays (nR = 23): 
- masks int32: 33.5MB (needed? for SWAR pc and for... we need NL as int32: 33.5MB; cnt as int16: 16.8MB; pc as uint8: 8.4MB; ind as bool: 8.4MB (can reuse cnt==0 on the fly); cand computation temporaries: fullL & ~NL → int32 temp 33.5MB; gather result uint8 8.4MB; cand int16 or so.)
L-side arrays (nL = 23): fL uint8 8.4MB; w int8 8.4MB; cntL int16 16.8MB; pcL uint8 8.4MB; SOS temporaries in-place.

Peak: maybe ~150MB. Under 256MB, but let's be careful and free arrays (del) when possible. Also note: for n < 46, sizes shrink (2^22 = half etc.). Worst case n=46: nL=23, nR=23.

Hmm wait, actually, we can reduce: choose the split so that the R side (the one we iterate fully with NL array int32) is the SMALLER half? Both are 23 at n=46. nL = 23, nR = 23. Fine.

Alternatively, we can avoid storing NL for all T: we need NL[T] only to compute the gather index. We could process the SOS-OR in place and then compute cand in one pass: idx = fullL & ~NL (temp int32 33.5MB), then fL[idx] (uint8 8.4MB), then cand = pc + that (int16 16.8MB or compute max directly with masking). Then we need argmax for reconstruction — but careful: for reconstruction we need a specific T with cand[T] ≥ k and ind[T]. We can find T* = index of max cand (with ind enforced). Then reconstruct.

Let me now think about reconstruction in detail:

Given T* (subset of R, independent, with pc[T*] + fL[Y*] ≥ k where Y* = fullL & ~NL[T*]):
- The R part: T* itself, size pc[T*].
- The L part: need independent S* ⊆ Y* with |S*| = fL[Y*]. Reconstruct via the fL recurrence... but fL was computed via SOS-max, not the lowbit recurrence! Reconstruction from SOS-max: fL[Y] = max_{S ⊆ Y} w[S]. To find the argmax S: standard technique: iterate bits... Hmm, reconstruction from a SOS-max array: we want S ⊆ Y with w[S] = fL[Y] and S independent. 

  Method: greedily peel: we want to find S ⊆ Y with w[S] = fL[Y]. Note fL[Y] = max(fL[Y without bit b], ...) hmm, from SOS structure: fL[Y] = max over S ⊆ Y. Consider lowest bit... Actually here's a clean way: fL[Y] = max(fL[Y ^ (1<<b)], fL[Y]) for any b ∈ Y — that tells us whether we can drop bit b: if fL[Y ^ (1<<b)] == fL[Y], then there's an optimal S not using b → drop it. Otherwise every optimal S uses b... hmm, not exactly — fL[Y ^ (1<<b)] == fL[Y] means ∃ optimal S ⊆ Y \ {b}. If fL[Y ^ (1<<b)] < fL[Y], then all optimal S use b? No! Optimal S ⊆ Y with |S| = fL[Y]; if some optimal S doesn't use b then fL[Y\{b}] = fL[Y]. So if fL[Y\{b}] < fL[Y], all optimal S contain b → S must contain b. So reconstruction: 
  S = 0; Y_cur = Y*; 
  for b in bits of Y* (say from high to low or any order): if fL[Y_cur ^ (1<<b)] == fL[Y_cur]: Y_cur ^= (1<<b) (b not needed); else: b must be in every optimal subset of Y_cur → add b to S, Y_cur ← Y_cur & ~adjL_closed... wait no. Hmm, if b ∈ every optimal S ⊆ Y_cur, then S ∋ b, and the rest S \ {b} ⊆ Y_cur \ ({b} ∪ N(b)) with w = fL[Y_cur] - 1... but is fL[Y_cur \ ({b} ∪ N(b))] == fL[Y_cur] - 1? Yes: S optimal in Y_cur, b ∈ S → S\{b} independent ⊆ Y_cur \ N[b], so fL[Y_cur \ N[b]] ≥ fL[Y_cur] - 1. And fL[Y_cur \ N[b]] ≤ fL[Y_cur] - 1? If there were independent S' ⊆ Y_cur \ N[b] with |S'| > fL[Y_cur] - 1, then S' ∪ {b} independent ⊆ Y_cur with size > fL[Y_cur] — contradiction. ✓ So: add b, Y_cur ← Y_cur & ~N_closed[b] (N_closed[b] = adj[b] | (1<<b) restricted to L).
  
  But wait — the "else" branch requires that b is in EVERY optimal S — which we get from fL[Y\{b}] < fL[Y]. But then after adding b and restricting, we continue. At the end S has size fL[Y*]? Let's verify: invariant: fL[Y_cur] = (number of bits added so far) + (max achievable in Y_cur). Initially 0 + fL[Y*]. When we drop b (fL unchanged): invariant holds. When we add b: fL[Y_cur \ N[b]] = fL[Y_cur] - 1 ✓, so new (added+1) + fL[new Y_cur] = old. At the end Y_cur = 0 → fL[0] = 0 → added = fL[Y*]. ✓ And S is independent: each added b has no neighbors in Y_cur at the time... hmm wait, need: S independent. When we add b, we remove N[b] from Y_cur, so future additions are not adjacent to b ✓. And S ⊆ Y* ✓. 

  But hold on — is the "drop" test valid? fL[Y_cur ^ (1<<b)] == fL[Y_cur] → ∃ optimal S ⊆ Y_cur avoiding b → drop b and continue with Y_cur ^ (1<<b): invariant maintained ✓. If fL[Y_cur ^ (1<<b)] < fL[Y_cur] → every optimal S ⊆ Y_cur contains b → add b ✓. But what if fL[Y_cur ^ (1<<b)] > fL[Y_cur]? Impossible (subset). ✓. 

  Edge: what if fL[Y_cur] == 0? Then all remaining can be dropped: fL[Y\{b}] = 0 = fL[Y] ✓ drops everything. ✓.

  This reconstruction is O(nL) lookups — trivial.

  Hmm wait, but there's a subtle issue: the "add b" branch: we claimed fL[Y_cur \ N[b]] = fL[Y_cur] - 1 using the fact that every optimal S contains b. ✓ proven above. Good.

- Then total independent set = T* ∪ S*, size = pc[T*] + fL[Y*] = cand[T*] ≥ k. Output any k of them. But wait — we need to double check T* is independent: we enforce ind[T*] ✓. And S* ⊆ Y* = X'(T*) → no cross edges ✓. S* independent in L ✓. 

Also, we should double check the claim "if MIS ≥ k then answer YES with any k vertices of the MIS" — yes, subsets of independent sets are independent. And conversely if MIS < k → NO. So decision = (MIS ≥ k). ✓

Now, one more consideration: we could also just directly search for any T with cand[T] ≥ k (not necessarily max) — but computing max is the same cost. For reconstruction, take argmax.

Wait, actually — hmm, one concern: cand[T] for T with ind[T]: cand = pc[T] + fL[fullL & ~NL[T]]. The argmax over ind[T] gives MIS(G) ✓. 

Now let me also double check the SOS-max on the L side gives fL correctly:
- w[S] = pc[S] if S independent in L else -1 (or any negative). 
- fL = SOS-max: fL[Y] = max_{S ⊆ Y} w[S]. Since w[∅] = 0 (pc=0, cnt=0 → independent ✓), fL[Y] ≥ 0 ✓. And max over independent S ⊆ Y of |S| ✓. 

SOS-max implementation: 
w = w.reshape? For bit b: we want for all Y with bit b set: w[Y] = max(w[Y], w[Y ^ (1<<b)]). Reshape: A = w.reshape(-1, 2, 1<<b) — wait, need to be careful: with C-order, index = i * 2^(b+1) + m * 2^b + j where j ∈ [0, 2^b). So A[:, 1, :] corresponds to masks with bit b set, and A[:, 1, j] ↔ A[:, 0, j] differ by bit b ✓. So: np.maximum(A[:, 0, :], A[:, 1, :], out=A[:, 1, :])? Careful: A[:, 1, :] is a view (strided) — np.maximum with out=view works ✓. But is A[:, 1, :] a contiguous view? No, but numpy handles strided ops fine (slightly slower). Alternatively do it as: w_view = w.reshape(-1, 2, 1<<b); np.maximum(w_view[:, 0, :], w_view[:, 1, :], out=w_view[:, 1, :]). ✓ In-place on a view — allowed since maximum reads both inputs before writing? np.maximum(a, b, out=b) — elementwise, safe ✓.

For SOS-add (cnt): cnt_view[:, 1, :] += cnt_view[:, 0, :] ✓.
For SOS-OR (NL): NL_view[:, 1, :] |= NL_view[:, 0, :] ✓.

These passes: for b from 0 to nR-1: the reshape (2^(nR-b-1), 2, 2^b) — total elements touched per pass: 2^(nR-1) × 2 (read+write) — fine.

Wait, important: the SOS DP requires processing bits in any order but each bit once — standard SOS: for b in bits: for all masks with bit b: f[mask] = combine(f[mask], f[mask ^ (1<<b)]). After processing all bits, f[Y] = combine over all subsets ✓. Yes, standard.

Now, the R side details:
- cntR[T] = number of R-internal edges within T. Initialize cntR = 0; for each edge (u,v) both in R: cntR[(1<<u')|(1<<v')] += 1 where u' = u - nL (local index). Then SOS-add over nR bits. ind[T] = cntR[T] == 0.
- NL[T] = OR of NLc[v] for v ∈ T, where NLc[v] = bitmask over L of L-neighbors of v. Initialize NL[1<<v'] = NLc[v] for each R-vertex (note: NL[0] = 0 ✓; but careful — if we scatter NL[1<<v'] = NLc[v], and two different v have same... no, 1<<v' distinct per v ✓). Then SOS-OR. ✓
- pcR[T]: popcount — SWAR or SOS-add with base[1<<v'] = 1 (int8/uint8). SOS-add for pc: pc = zeros(uint8); pc[1<<v'] = 1 for each v; SOS-add. That's 23 passes over 8.4MB — fine, ~0.2s. Or SWAR — also fine. I'll use SOS-add for uniformity? SWAR is fewer passes (6 ops over int32 33MB = 200MB traffic vs SOS 23 passes × 8.4M × 2 = 390M element-ops on uint8 = 390MB traffic). Similar. Let me just use SWAR on an int32 copy... but that needs masks array (33.5MB) — we need masks anyway? Hmm, do we need the masks array for the R side? For SWAR pc we need masks = np.arange(2^nR). We don't otherwise need masks... except for finding T* at the end: argmax gives an index which IS the mask ✓ (index = mask). So masks array only needed for SWAR pc. Alternatively SOS-add pc avoids the 33.5MB arange. Let me use SOS-add for pc to save memory. Actually hmm, wait: we can also compute pc from... we need pc[T] for cand. Alternatively note: cand[T] = pc[T] + fL[...]. Hmm, we could avoid pc array: pc[T] = SOS-add... we need it stored (8.4MB uint8) — fine, cheap.

Actually, hmm, wait: can we avoid the cntR array (int16, 16.8MB)? ind[T] = cntR[T] == 0. Alternative: compute ind via... we could compute "min edge count" — same thing. Or use uint8 with saturation? Max edges within a 23-vertex subset: C(23,2) = 253 ≤ 255 ✓ fits uint8! But SOS-add could overflow uint8 during intermediate steps? cnt values only increase toward final value; intermediate SOS partial sums are ≤ final ✓ (all non-negative additions). Max final = 253 < 255 ✓. So uint8 works: 8.4MB. But wait — is it exactly true that partial sums ≤ final? SOS-add: cnt[T] accumulates subsets' base values; at any point, cnt[T] = sum over some family of subsets of T — always ≤ sum over all subsets of T = final ✓. Great, uint8 safe. (Edge case: m ≤ n(n-1)/2 = 1035 for n=46; within R: ≤ C(23,2) = 253 ✓.)

Hmm, but actually — do we even need cntR/ind as a separate array? We need ind only to mask cand. We could compute bad[T] differently: T non-independent. Alternative: compute cand only for independent... we compute cand for all T then mask. We need the ind array (bool 8.4MB) or use cntR directly: cand_masked = np.where(cntR == 0, cand, 0). Fine — compute on the fly, maybe keep cntR (uint8 8.4MB) and do the where at the end.

Let me now also reconsider: maybe there's an even simpler approach — since we need fL (SOS-max over L) and full iteration over R subsets with NL (SOS-OR) — total numpy work: 
L side: pcL (SWAR or SOS), cntL (SOS-add), w, fL (SOS-max). 
R side: cntR (SOS-add), NL (SOS-OR), pcR (SOS-add), final: idx = fullL & ~NL (int32 op), gather fL[idx], cand = pcR + gathered, mask by cntR==0, max & argmax.

All are ~23-pass SOS DPs over ≤ 8.4M-element arrays. Each pass ~10-30ms → each DP ~0.3-0.7s → total maybe 2-3s. Hmm, cutting close with 5s limit but probably OK. Let me count passes: L: cntL (23), fL (23), pcL (23 or SWAR ~6 heavy int32 passes). R: cntR (23), NL (23), pcR (23), final ops (~5 passes incl. gather). Total ~120 passes over ~8.4M arrays. At ~15ms per pass (8.4M uint8 elements, strided views might be slower — the strided maximum on views: A[:, 1, :] has stride pattern... for small b, the inner dimension 2^b is contiguous-ish; for large b, outer stride. numpy handles it; maybe 20-40ms per pass) → 120 × 25ms = 3s. Hmm. Plus Python overhead negligible. Risky but let's optimize:

Optimizations:
1. Balance the split: the cost is dominated by 2^max(nL,nR)... total ≈ (passes_L × 2^nL + passes_R × 2^nR). With nL = nR = 23 both 8.4M. If we make one side smaller, e.g., nL = 20, nR = 26 — no, 2^26 = 67M × several arrays — memory blows up. Keep 23/23.

2. Reduce passes: 
   - pcL: instead of SOS-add (23 passes), use SWAR on int32 arange (needs 33.5MB temp) — 6 passes over int32 = 24 passes-equivalent of uint8 traffic... hmm similar. OR: compute pcL from cntL? No. Alternative: note w[S] = pc[S] for independent S — and fL = SOS-max of w. Could we fold pc into the SOS differently? Hmm: fL[Y] = max over independent S ⊆ Y of |S|. 
   
   Alternative idea: compute fL via the "level" DP with gathers (as originally planned) — that's ~10 ops × 8.4M with 4 gathers... probably slower than 23 simple passes. Keep SOS.
   
   - Actually, here's a cute trick to compute fL with FEWER passes: fL[Y] = max over independent S ⊆ Y of |S|. Equivalently: fL[Y] = max t such that ∃ independent S ⊆ Y with |S| = t. Hmm.
   
   Alternative: skip pcL array: w[S] = pc[S]·ind[S]. We need pcL anyway for w. SWAR popcount: x = arange(2^nL, dtype=int32) (33.5MB); 6 int32 ops; then view as uint8 pairs... Actually here's a cheaper SWAR: since nL ≤ 23, pc = sum of bits. Use np.bitwise_count if available (numpy ≥ 2.0): try: pc = np.bitwise_count(masks) — I'll feature-detect. Fallback SWAR. Actually, simpler robust approach: pc via SOS-add is only 23 cheap passes on uint8 (8.4MB each, read+write 4.2M+4.2M... each pass touches 2^(nL-1) elements twice = 8.4M element-ops) — total 23 × 8.4M = 193M uint8 ops ≈ 200MB traffic ≈ 0.2-0.4s. That's fine, honestly. Let me not over-optimize; use SOS-add for pc on both sides. Actually wait — even better: pcL can be computed via... hmm, np.add? Let me think of the cleanest: 

   pc = np.zeros(1<<nL, uint8); pc[1<<v] = 1 for v in range(nL); then SOS-add. Clean. ~0.3s.

   Hmm, actually, alternative for pcL: we don't need pcL for all S — we need w[S] = pc[S] if independent. What if instead we define w differently: run a "max independent set size" DP... no, keep it simple.

3. Reduce the L-side passes: cntL (SOS-add, 23) + fL (SOS-max, 23) + pcL (23) = 69 passes over 2^23. R-side: cntR (23) + NL (23) + pcR (23) + final (~4-5) = ~74 passes. Total ~143 passes ≈ 143 × 8.4M × 2 element-ops ≈ 2.4G element-ops... hmm, that might be 2-4 seconds. Tight. Let me think about reducing.

Reduction ideas:

A. Combine cntL and pcL: note that for the L side, we need w[S] = pc[S] if cntL[S] == 0 else -1. What if instead of pc, we use a different weight that's SOS-addable... Hmm. 

   Alternative: compute fL directly with a smarter DP: fL[Y] = max(fL[Y \ {b}], fL[Y ∩ allowed(b)] + 1) for b = lowest bit — the gather DP. Cost: per element ~2 gathers + 1 scatter + few ops. Gathers are ~4-8 bytes random access into 8.4MB array — L2/L3-ish. 8.4M × 3 random accesses ≈ 25M random accesses ≈ maybe 0.3-0.8s. Plus we need popcount-level grouping (argsort or boolean selection: +0.3-1s). Hmm, comparable. 

B. Reduce R-side: do we need cntR AND NL AND pcR? 
   - NL: needed for the gather index. Could we avoid NL by restructuring? The gather fL[fullL & ~NL[T]] — alternative: iterate over L-side subsets instead and gather into an R-side SOS-max array fR: cand[S] = pc[S] + fR[fullR & ~NR[S]] for independent S ⊆ L, where NR[S] = R-neighbors of S. Symmetric — same cost. 
   - pcR: needed for cand. 
   - cntR: needed for ind. 
   
   Hmm, what about combining pcR and cntR into one array? E.g., pack into int16: high byte = pc, low byte = cnt? SOS-add would add both simultaneously (with carry issues — pc ≤ 23 < 256, cnt ≤ 253; packed as pc*256 + cnt: adding two packed values: cnt parts sum ≤ 253+253 = 506 > 255 → carry into pc — corrupts. Use int32 with pc << 16, cnt << 0: sums: cnt ≤ 253 fine no overflow into byte 1? cnt sums ≤ 253 < 256 ✓ no carry; pc ≤ 23 ✓. So packed = (pc << 8) | cnt in int16? cnt ≤ 253 fits in byte 0; pc in byte 1; additions never carry across ✓. So one SOS-add pass array (int16, 16.8MB) computes both pcR and cntR simultaneously! Initialize: for each R-vertex v: packed[1<<v'] = (1 << 8) | 0; for each R-edge: packed[emask] += 1 (cnt part). Wait — but a mask could be both a single vertex and... no: single-vertex masks get (1<<8); edge masks (2 bits) get +1 each. A 2-bit mask is not a 1-bit mask ✓. But multiple edges share... each edge has distinct mask (no duplicate edges) ✓. So init: packed[1<<v] = 256 for all v; packed[edgemask] += 1 for all R-edges. Then SOS-add. Then pcR = packed >> 8, cntR = packed & 255. Saves 23 passes (one SOS-add instead of two). ✓ Nice.
   
   Similarly L side: pcL and cntL packed → one SOS-add (23 passes saved). Then w = where(cnt==0, pc, -1) as int8, then fL SOS-max (23 passes). L total: 23 (packed SOS-add) + 23 (SOS-max) = 46 passes + small extras.
   
   R total: 23 (packed SOS-add) + 23 (NL SOS-OR) + final (~5) = ~51 passes.
   
   Total ~97 passes ≈ 97 × 8.4M × ~2 = 1.6G element-ops. At ~1-2 GB/s effective for strided numpy... hmm, numpy strided ops on uint8/int16: memory bandwidth ~5-20 GB/s for simple ops. 1.6G element-ops × 1-2 bytes ≈ 2-3 GB traffic → ~0.3-1s. Plus gather ~0.5s. Plus overhead. Should fit in 5s. 

   Wait, actually the strided views: A[:, 1, :] where A = arr.reshape(-1, 2, 2^b): for b=0: shape (2^22, 2, 1) — A[:, 1, :] is every other element — strided access, numpy handles with stride 2 — bandwidth halves-ish. For b=22: shape (1, 2, 2^22): A[:, 1, :] is contiguous half ✓. Mixed. Fine.

C. Another optimization: note fL SOS-max processes int8 (w as int8, -1 for non-independent). ✓ 8.4MB.

D. NL as int32 (33.5MB) — SOS-OR passes over int32 = 4× traffic of uint8. Hmm, 23 passes × 4.2M elements × 4 bytes × 2 (r+w) = 780MB traffic. OK. Could we use int32 but... L has ≤ 23 bits so int32 needed (23 bits). Unless nL ≤ 23 — yes int32 minimum (or uint32). Fine.

Actually — wait. Let me reconsider the split sizes to reduce total cost. Total cost ≈ α·2^nL + β·2^nR where α ≈ 46 passes (L), β ≈ 51 passes (R) — roughly equal, so nL = nR = 23 optimal for n=46. ✓.

Hmm, but hold on — maybe we can cut the L-side cost significantly with a different fL computation. Let me reconsider... 

Actually, here's a thought: we don't need fL[Y] for ALL Y — only for Y values of the form fullL & ~NL[T] for T ⊆ R. But that's up to 2^23 distinct values anyway. No.

Alternatively, flip: compute fR (SOS-max over R subsets: fR[U] = max independent T ⊆ U) — needs cntR (have it), pcR (have it), wR, SOS-max (23 passes) — and then iterate over ALL S ⊆ L with NR[S] (SOS-OR over L, 23 passes) and ind... wait, that's exactly symmetric — same total. No gain.

OK here's another BIG optimization idea: prune the R-side iteration using ind early? The final pass computes cand for all T and masks. The gather is over all 8.4M T. Could restrict to independent T only (via boolean indexing) — but selecting independent T's requires a pass anyway; the gather count is the same (all independent T's could be ~all of them in sparse graphs). No gain.

Alternatively: note that we don't need per-T cand for ALL T — we need the MAX. Could we compute max over T of (pc[T] + fL[fullL & ~NL[T]]) more cleverly? Hmm... 

max over T independent of (pc[T] + fL[L \ NRc... ]). Define over subsets of R: hmm, what if we do SOS on the R side to compute: for each U ⊆ R: gR[U] = max{|T| : T ⊆ U, T independent} — that's fR (SOS-max, 23 passes). And then answer = max over S ⊆ L independent of (|S| + fR[R \ NR(S)]) — iterate all S ⊆ L with NR(S) via SOS-OR over L... symmetric, same cost. The gather-based combination is unavoidable ~one full-side iteration + one SOS-max per side + SOS-add per side + SOS-OR per side. 

Actually wait — can we avoid the SOS-OR (NL) pass?! Alternative: iterate over T ⊆ R, and instead of gathering fL[fullL & ~NL[T]], note fullL & ~NL[T] = X'(T). Hmm what if we flip the gather: precompute for the L side an array over L-subsets... we need fL at X'(T) — X'(T) is determined by NL[T]. The map T ↦ X'(T) is exactly what SOS-OR computes. Alternatively compute the gather indices differently: idx[T] = fullL & ~NL[T] — could compute idx directly via SOS-AND?! Define idx[T] = AND over v ∈ T of allowedL(v) where allowedL(v) = fullL & ~NLc(v). Then idx[T] = X'(T) ✓ (intersection of allowed sets). SOS-AND: initialize idx[1<<v] = allowedL(v), idx[0] = fullL, idx[T] for |T|≥2 init to fullL? Hmm — SOS-AND computes idx[T] = AND_{V ⊆ T} base[V]. Set base[0] = fullL, base[{v}] = allowedL(v), base[other] = all-ones (fullL). Then idx[T] = fullL & AND_{v∈T} allowedL(v) = X'(T) ✓. Same cost as SOS-OR. No gain, but equivalent. Fine — either way, 23 passes over int32.

Hmm OK, what about reducing passes via processing 2 bits at a time? SOS with combined transforms: for bits b1, b2: the standard SOS does 2 passes; combining into one pass over a reshape (-1, 4, 2^b) with 3 updates (masks with bit patterns 01, 10, 11 relative)... The updates for a 2-bit group: f[01] = combine(f[01], f[00]); f[10] = combine(f[10], f[00]); f[11] = combine(f[11], f[10]) then f[11] = combine(f[11], f[01])... order matters: standard SOS for two bits: after bit b1 pass and bit b2 pass. Combined: for the group of 4: f[11] needs f[01] and f[10] updated first. Do: t0 = f[00]; f[01] ⊙= t0; f[10] ⊙= t0; f[11] ⊙= f[10]; f[11] ⊙= f[01]... wait f[11] ⊙= f[10] where f[10] already updated with f[00] ✓, and f[11] ⊙= f[01] (updated) ✓. That covers subsets {00,01,10,11}... f[11] gets f[01], f[10] (which got f[00]), and f[11] itself — but does f[11] get f[00] directly? Via f[10] and f[01] ✓ (combine is idempotent for max/or/and/add? For max: f[11] = max(f[11], f[10], f[01]) where f[10] ≥ f[00] ✓ — since max is idempotent and monotone, transitive ✓. For add: f[11] += f[10] + f[01] would double-count f[00]! ✗). So 2-bit combining works for max/or/and but NOT add. Our SOS-adds (packed pc/cnt) can't combine bits. Hmm. But SOS-max (fL) and SOS-OR/AND (NL) can! That saves ~11 passes each (23 → 12 passes). Meh, marginal gains, added complexity. Let me first estimate more carefully whether the simple version fits in 5s.

Rough cost estimate (n=46, arrays of 8.4M):
- L-side packed SOS-add (int16, 16.8MB array): 23 passes, each pass: read 4.2M int16 (8.4MB) + write 4.2M (8.4MB) → 16.8MB traffic per pass → 386MB total. At ~5GB/s → 0.08s. 
- L-side w computation: a few full passes (where, shifts) → ~0.05s.
- L-side fL SOS-max (int8, 8.4MB): 23 passes × 8.4MB traffic = 193MB → 0.04s + numpy overhead per call (~23 calls × 2 ops... trivial). 
- R-side packed SOS-add: 0.08s.
- R-side NL SOS-OR (int32, 33.5MB): 23 passes × 33.5MB = 770MB → 0.15s.
- Final: idx = fullL & ~NL (int32, read 33.5 write 33.5 = 67MB → 0.02s); gather fL[idx]: 8.4M random gathers → hmm, 8.4M × ~50-100ns = 0.4-0.8s (this is the slowest part); cand = pc + gathered (uint8 ops, but need int16 for safety? pc ≤ 23, fL ≤ 23, sum ≤ 46 — fits uint8 ✓ (≤ 255)); masking & max: ~0.05s.
- Total: well under 1s + gather ~0.5s + Python/numpy call overhead. 

Oh wait, but I should double check the strided-view performance concern: A[:, 1, :] operations on reshaped views — for b small, stride 2^(b+1) elements, inner length 2^b — numpy's inner loop handles contiguous runs of 2^b; for b=0: runs of length 1, stride 2 — inefficient-ish but the total elements are 4.2M per pass — numpy does this at maybe 1-2 GB/s → fine.

Also the initializations: packed arrays via np.zeros + scatter of ≤ 253+23 values — trivial.

And popcount grouping — NOT NEEDED anymore! Great, the SOS approach avoids popcount-level processing entirely.

Wait, wait. Let me re-verify the whole approach once more, carefully, because the SOS-max for fL is crucial:

fL[Y] = max_{S ⊆ Y} w[S], where w[S] = |S| if S independent in L else -1. 

Claim: fL[Y] = MIS(L[Y]) (max independent set in induced subgraph on Y). ✓ (max over independent subsets S of Y of |S|; w = -1 for non-independent excludes them; ∅ gives 0.)

SOS-max computation: start with w (indexed by S), after processing all bits: fL[Y] = max over all S ⊆ Y of w[S] ✓ — standard subset-max zeta transform. ✓

R side: for each T ⊆ R: 
- pcR[T] = |T| ✓ (SOS-add of base[1<<v]=1).
- cntR[T] = # edges inside T ✓ (SOS-add of base[edgemask]=1).
- NL[T] = ∪_{v∈T} NLc(v) ✓ (SOS-OR of base[1<<v]=NLc(v), base[0]=0).
- cand[T] = pcR[T] + fL[fullL & ~NL[T]].
- MIS(G) = max over T with cntR[T]==0 of cand[T]. 

Proof of correctness: 
(≤) For T independent in R: let S* = MIS of L restricted to X'(T) where X'(T) = fullL & ~NL[T] (L-vertices with no R-neighbor in T). Then T ∪ S* is independent in G: T independent ✓, S* independent ✓, no cross edges since S* ⊆ X'(T) ✓. So MIS ≥ |T| + fL[X'(T)] = cand[T]. Taking max over such T: MIS ≥ max cand. 
(≥) Let I be a maximum independent set; T = I ∩ R, S = I ∩ L. T independent → cntR[T] = 0. S ⊆ X'(T) (no cross edges) and S independent → fL[X'(T)] ≥ |S|. So cand[T] ≥ |T| + |S| = |I| = MIS. ✓
So MIS = max over independent T of cand[T] ✓.

Reconstruction: T* = argmax (over cntR==0) of cand. Then S* ⊆ X'(T*) with |S*| = fL[X'(T*)] via the peeling reconstruction described. Output min(k, ...) — well, output exactly k vertices from T* ∪ S* (size = MIS ≥ k). ✓

Edge cases and details:
- nL could be 0 (n=1): then L empty: 2^0 = 1 arrays; fullL = 0; fL[0] = 0; w[0] = 0. R side: nR = 1. cand[0] = 0 + fL[0 & ~0] = fL[0] = 0; cand[1] = 1 + fL[0] = 1 (if vertex 0 has no self-loop — cntR[1] = 0 ✓). MIS = 1. ✓
- k could equal n: need MIS = n → graph empty. Works: cand[fullR] = nR + fL[fullL] = nR + nL = n iff cntR[fullR] == 0 and fL[fullL] = nL (iff L independent). ✓
- m = 0: MIS = n ≥ k → YES. ✓ (cand[fullR] = n.)
- Duplicate edges: problem says no link listed twice ✓. Self-loops: u ≠ v ✓.
- Input parsing: possibly multiple links per line / whitespace — read all tokens.

Now, sizes when n < 46: nL = n // 2, nR = n - nL. For n=45: 22/23 → arrays 4M/8.4M. Fine.

Hmm wait, actually let me reconsider which side should be bigger. The R side has: packed SOS-add (int16) + NL SOS-OR (int32) + final gather. The L side has: packed SOS-add (int16) + SOS-max (int8) + gather target. The R side is heavier (int32 NL passes + gather over 2^nR). So maybe make R the SMALLER half: nR = n // 2, nL = n - n // 2 (bigger L). For n=46: nR = 23, nL = 23 — same. For odd n: nR = 22, nL = 23 → R arrays 4.2M, L 8.4M. The gather is over 2^nR = 4.2M (cheaper) and fL table is 8.4MB. Good: set nR = n // 2, nL = n - nR. For n=46 both 23. OK.

Hmm, one more consideration: the final gather fL[idx] where idx = fullL & ~NL — idx values are int32; numpy fancy indexing with int32 index array into uint8 fL — fine.

Then cand = pcR + fL_gathered (uint8 + uint8 → numpy will upcast to... uint8+uint8 = uint8 (wraps at 256; max 46 ✓ no wrap)). Then apply mask: cand[cntR != 0] = 0 — hmm, careful: cntR is packed inside the int16 packed array: packed & 255. Let me extract: pcR = (packed >> 8) — as uint8: (packed >> 8).astype(uint8); cntR = (packed & 255). Then valid = cntR == 0; cand_valid = np.where(valid, cand, 0); best = cand_valid.max(); T* = argmax.

Wait — potential issue: packed is int16; packed >> 8 — for non-negative values fine (values ≤ (23<<8)|253 < 32767 ✓ no sign issues). ✓

Memory tally (n=46, nL=23, nR=23):
L side: packedL int16 2^23 × 2 = 16.8MB; wL int8 8.4MB; fL int8 8.4MB (can reuse w in place! SOS-max in place on w → fL. ✓ saves 8.4MB).
R side: packedR int16 16.8MB; NL int32 33.5MB; idx temp int32 33.5MB (can compute in place: NL ^= ... hmm: idx = fullL & ~NL → in-place: np.bitwise_and(NL, ~fullL, out=NL)? fullL & ~NL = ~(~fullL | NL) = ... simpler: NL &= ~fullL gives ~fullL & NL — no. We want fullL & ~NL. In-place: np.bitwise_not(NL, out=NL); NL &= fullL → NL = fullL & ~NL ✓ in place, no extra 33.5MB.) Then gathered = fL[NL] (uint8 8.4MB); cand = pcR + gathered (uint8 8.4MB — or compute in place into gathered: gathered += pcR ✓); valid mask (bool 8.4MB); then max with masking: best = gathered[valid].max() — boolean indexing creates temp; or use np.where(valid, gathered, 0) (temp 8.4MB) then .max() and .argmax(). Fine.

Total peak: ~16.8 + 8.4 (L) + 16.8 + 33.5 + 8.4 + 8.4 + 8.4 ≈ 100MB + temporaries. OK under 256MB. 

Hmm, also: do we need pcR separately? packedR holds (pc<<8)|cnt. pcR = packedR >> 8 (int16 temp 16.8MB or astype uint8 8.4MB). Fine.

Also for the L side: wL = where(cntL == 0, pcL, -1): pcL = packedL >> 8, cntL = packedL & 255 — temps. Then wL int8. Then SOS-max in place. ✓

Wait, actually — for the L side, do we need cntL at all?? wL[S] = pcL[S] if S independent. Hmm yes we need independence of S ⊆ L. ✓ needed.

Alternatively — hmm, here's a thought — could we skip computing fL via wL and instead compute fL via... no, current plan is fine.

Let me now also double-check the SOS-add packed trick once more: base values: for each vertex v (local index): packed[1 << v] += (1 << 8) — wait, should it be = or +=? A mask 1<<v is a single vertex — it can't also be an edge mask (2 bits) ✓, so = or += both fine (use += for safety). For each edge (a,b): packed[(1<<a)|(1<<b)] += 1. Then SOS-add over all nR bits: packed[T] = sum over subsets V ⊆ T of base[V] = sum_{v ∈ T} 256 + sum_{edges ⊆ T} 1 = (|T| << 8) + cnt(T) ✓. Carry from cnt byte into pc byte: cnt(T) ≤ 253 ✓ never carries. But WAIT — intermediate SOS steps: packed[T] after some passes = sum over a subfamily — still ≤ final ✓. And the pc byte: |T| ≤ 23 ✓. But could the cnt byte of an intermediate exceed 255? Intermediate ≤ final ≤ 253 ✓. ✓ Safe.

Hmm, one more check: edges within R: at most C(23,2) = 253 ✓. Edges within L: at most C(23,2) = 253 ✓ (for the L-side packed). ✓.

Now the reconstruction of S* from fL (peeling): 
Y = X'(T*) = fullL & ~NL[T*] — but we destroyed NL (turned it into idx = X' values in place). That's fine: idx[T*] IS X'(T*) ✓. 
S = []; 
while Y: pick any set bit b of Y (say lowest): 
  if fL[Y ^ (1<<b)] == fL[Y]: Y ^= (1<<b) 
  else: S.append(b); Y &= ~closedN[b] (closedN[b] = (adjL[b] | (1<<b)) — neighbors within L plus itself).
Loop terminates: each step removes ≥ 1 bit. Final |S| = fL[X'(T*)] ✓ (proved invariant). 

Hmm wait, let me re-verify the invariant proof once more, since it's crucial: 
Invariant: |S_so_far| + fL[Y] = fL[Y_original]... let me define Φ = |S| + fL[Y]; claim Φ stays = fL[Y0] throughout. 
- Drop: fL[Y ^ bit] == fL[Y] → Φ unchanged ✓.
- Add b: requires fL[Y ^ bit] < fL[Y] (i.e., fL[Y ^ (1<<b)] != fL[Y]; since ≤ always, it's <). Then every max independent S' ⊆ Y contains b. New Y' = Y & ~closedN[b]. Claim fL[Y'] = fL[Y] - 1: 
  ≥: take max independent S' ⊆ Y, b ∈ S' → S' \ {b} ⊆ Y' (since S' independent, no neighbors of b in S') → fL[Y'] ≥ |S'| - 1 = fL[Y] - 1. 
  ≤: if fL[Y'] ≥ fL[Y], then ∃ independent S'' ⊆ Y' with |S''| ≥ fL[Y]; but then S'' ∪ {b} ⊆ Y independent (b has no neighbors in Y' ⊇ S'') with size ≥ fL[Y] + 1 > fL[Y] — contradiction. So fL[Y'] ≤ fL[Y] - 1. ✓ 
  So Φ' = |S| + 1 + fL[Y'] = |S| + fL[Y] ✓.
- Termination: Y = 0 → fL[0] = 0 → |S| = fL[Y0]. ✓
Also S independent: each added b has all its L-neighbors removed from Y at add time, and subsequent additions come from reduced Y ✓; also earlier additions: when b1 added, Y reduced by closedN[b1]; b2 added later from Y' — b2 not adjacent to b1 ✓. And drops don't affect. ✓

But hmm — one subtlety in the drop branch: we pick the lowest set bit each iteration; after dropping, the next lowest bit is considered. Fine — order arbitrary. ✓

Also, potential subtlety: fL[Y ^ (1<<b)] — Y ^ (1<<b) removes bit b ✓ (b ∈ Y).

Now, T* selection: T* = argmax of cand over valid T. But note: multiple T may achieve max; any works. Also — IMPORTANT: we need cand[T*] = pc[T*] + fL[X'(T*)] and then S* of size fL[X'(T*)] — total = MIS ≥ k ✓.

Then final answer set = T* (as global vertex indices nL + local) ∪ S* (global indices = local). Take first k. Print YES and them.

If MIS < k: print NO.

Let me now also handle potential numpy pitfalls:
1. Reshape views for SOS: arr must be a contiguous numpy array; arr.reshape(-1, 2, 1<<b) returns a view ✓ (contiguous). Then A[:, 1, :] and A[:, 0, :] are views with strides. np.maximum(A0, A1, out=A1) — A0 and A1 are different memory regions (different slices along axis 1) — no aliasing ✓. For in-place add: A1 += A0 ✓. For OR: A1 |= A0 ✓.

2. For b from 0..nR-1: A = arr.reshape(-1, 2, 1 << b)? Wait — I need to double check the bit ordering. With C-contiguous layout, linear index = ((i * 2) + m) * 2^b + j. So bit b corresponds to m (the middle axis) ✓: masks with bit b set are m=1 slices ✓, and A[i, 0, j] = mask i*2^(b+1) + j, A[i, 1, j] = that + 2^b ✓ — differ exactly in bit b ✓. 

3. SOS correctness: after processing bits 0..nR-1 (each once), arr[T] = combine over all subsets of T ✓ — standard (the order of bits doesn't matter; each subset V ⊆ T differs from T in some set of bits; the SOS accumulates along each bit dimension — yes, this is the standard multidimensional prefix... it's the standard "subset sum DP" — correct ✓).

4. dtypes: NL as int32 — L-bit masks ≤ 2^23 - 1 fit ✓. But careful: np.bitwise_not on int32: ~NL gives negative values; then NL &= fullL → non-negative ✓. Actually let me just do: idx = fullL & ~NL — with int32, ~NL = -(NL+1) — bitwise AND with fullL (positive < 2^23) gives correct result ✓ (two's complement: ~NL has all high bits set; AND with fullL < 2^23 keeps only low bits = fullL & ~NL ✓).

5. Fancy indexing fL[idx] where idx is int32 array of shape (2^nR,) — returns uint8 array ✓.

6. np.argmax on masked cand: I'll compute cand = gathered + pcR (uint8), then set cand[~valid] = 0 — hmm, but MIS could be 0? No — n ≥ 1, k ≥ 1, and MIS ≥ 1 always (single vertex) — actually MIS ≥ 1 since n ≥ 1 and no self-loops... wait, is a single vertex always independent? Yes (no self-loops since u ≠ v). So MIS ≥ 1. But cand[T] for valid T: T=∅ is valid (cnt=0) with cand = 0 + fL[fullL] ≥ 0. Max over valid ≥ MIS ≥ 1 ✓. Setting invalid to 0 is safe since true max ≥ 1 > 0 ✓. Hmm, unless MIS = 0 — impossible for n ≥ 1 ✓.

   Implementation: cand[invalid] = 0 via cand[~valid] = 0 (boolean mask assignment — fine) or np.where. Then best_idx = int(cand.argmax()); best = int(cand[best_idx]).

7. For nL = 0: L-side arrays size 1: packedL = zeros(1, int16); wL = [0]; fL = [0]; SOS loops over 0 bits — skip. fullL = 0. X'(T) = 0 for all T; fL[0] = 0 ✓. Reconstruction: Y = 0 → S empty ✓.

8. For nR = 0? nR = n // 2 and n ≥ 1 → nR ≥ 0. n=1: nR = 0, nL = 1. Then R side: arrays size 1: T=∅ only: cand = 0 + fL[fullL] = fL[fullL] = MIS(L) = MIS(G) ✓ (all vertices in L). NL array size 1: NL[0] = 0 → idx[0] = fullL & ~0 = fullL ✓. Works ✓. Reconstruction: T* = 0, S* from fL[fullL] ✓.

9. Reading input: first line n, m, k; then m lines of pairs. Use sys.stdin.buffer.read().split().

10. Output: "YES\n" + " ".join of k vertex numbers (1-based). Or "NO".

Now — performance of the gather: fL[idx] with idx int32 8.4M elements. numpy fancy indexing with int32 indices: it may internally cast to intp (int64) — creating a 67MB temp?! Hmm, that could be a memory + time issue. To avoid, make idx int64 directly? NL as int64 = 67MB — heavy for SOS passes (23 passes × 67MB × 2 = 3GB traffic — ~0.6s, acceptable?). Alternatively keep NL int32 and let numpy cast (temp 67MB during gather — memory spike to ~67+33 = 100MB extra — total maybe 200MB — risky but probably OK?). Hmm. Alternatively use np.take(fL, idx) — same casting behavior. 

Let me think: numpy fancy indexing with int32 index array: NumPy will convert to intp (int64 on 64-bit) — yes, it typically makes a copy of the index array as int64. 8.4M × 8 = 67MB temp. Plus NL 33.5MB + packed 16.8 + others ~50MB → peak ~180MB. Under 256MB but uncomfortable. 

Alternative: avoid the big gather by processing in CHUNKS: iterate over T in blocks of, say, 1M, casting per block — keeps temp at 8MB. The gather itself: 8.4M random lookups into 8.4MB table — mostly L3/resident — fine. Chunking adds Python loop overhead (9 chunks × few ops — negligible). Let me do chunked processing for the final combination to control memory:

for chunk over range(0, 2^nR, CH):
    idx_c = idx[chunk:chunk+CH] (view, int32)
    g = fL[idx_c] — numpy casts idx_c to int64 (CH×8 bytes temp, e.g., 8MB for CH=1M) ✓
    c = g + pcR[chunk:...]; c[invalid...] = 0; track max & argmax.

Actually simpler: convert idx to int64 in place chunk-wise... or just make the whole idx array int64 from the start? NL int64 = 67MB; SOS-OR passes over int64: 23 × (33.5 read + 33.5 write) = 1.5GB traffic ~0.3s. Memory: 67MB for NL + rest ~60MB = ~130MB peak. Hmm, that's actually fine and simpler! But the int32 version with chunked gather is also fine. Let me weigh: 

Option 1: NL int32 (33.5MB), chunked final gather (temp small). Peak memory ~33.5+16.8+16.8+8.4×3 ≈ 110MB. 
Option 2: NL int64 (67MB), direct gather (temp 67MB during cast — actually if idx is already int64, no cast needed! fancy indexing with int64 = intp on 64-bit systems → no copy ✓). Peak ~67+16.8+16.8+8.4×3+gathered 8.4 ≈ 135MB. 

Hmm, both OK. But wait — is intp guaranteed int64? On typical 64-bit platforms yes (Windows: intp is int64 too... on Windows, C long is 32-bit but intp is ssize_t = 64-bit ✓). OK.

Actually, let me reconsider: maybe avoid the idx array materialization altogether: we need, for each T: fL[fullL & ~NL[T]]. What if we instead iterate over chunks of T and compute everything per chunk? The SOS-OR for NL must be global though (it's a DP). So NL array must exist fully. OK.

Alternatively — reduce NL to int32 and do the gather with np.take with mode='clip'? np.take also casts indices I believe. Hmm. Let me just do chunked fancy indexing with int32 → per-chunk cast. Actually you know what, let me simply test-think: numpy's fancy indexing: arr[idx] where idx.dtype == np.intp → no copy. Else it copies idx to intp. With chunk size 2^20 (1M): temp 8MB — trivial. I'll do that. Actually, even simpler: I can pre-convert idx per chunk: idx64 = idx_chunk.astype(np.int64) then fL[idx64] — same thing. Or just let numpy do it. Fine.

Hmm, actually — wait. Let me reconsider using int64 for NL from the start but with fewer bytes... no, 23 bits need ≥ 3 bytes → int32 minimum. OK: NL int32, chunked gather. 

Actually, hold on, let me reconsider the whole memory: is 2^23 really needed for both sides? n=46 → yes worst case. Fine.

Let me also double check the SOS-OR init for NL: NL[0] = 0 ✓ (np.zeros). For each R-vertex v (local idx j, global nL+j): NL[1<<j] = NLc[v] where NLc[v] = bitmask over L of L-neighbors. But note: base for SOS-OR should be: NL[T] = OR of base[V] for V ⊆ T. base[0] = 0, base[{j}] = NLc[j], base[|T|≥2] = 0 (empty OR = 0 ✓). So init NL[1<<j] = NLc[j] ✓ and everything else 0 ✓. After SOS: NL[T] = OR_{j∈T} NLc[j] ✓.

Edge case: what if some NLc[j] = 0 (vertex j has no L-neighbors)? NL[1<<j] = 0 ✓ fine.

Now, the L-side packed init: packedL[1<<i] += 256 for each L-vertex i; packedL[edgemask] += 1 for each L-edge. ✓

R-side packed init similarly. ✓

Then SOS-add for packed arrays: A[:, 1, :] += A[:, 0, :] — int16 adds. ✓

Then L: pcL = (packedL >> 8).astype(np.int8)? Values ≤ 23 ✓ int8 fine. cntL = (packedL & 255). wL = np.where(cntL == 0, pcL, -1).astype(np.int8) — hmm, np.where returns int16 maybe; cast to int8. Then SOS-max in place on wL (int8) → fL. 

Wait — SOS-max on int8 with -1 values: fine ✓.

Then R: pcR = (packedR >> 8).astype(np.uint8); cntR = (packedR & 255) — keep as int16 or uint8: valid = (packedR & 255) == 0 — compute as bool array (8.4MB) ✓.

Then NL: int32 zeros; init; SOS-OR; then in-place: np.bitwise_not(NL, out=NL); np.bitwise_and(NL, fullL, out=NL) → NL now holds X'(T) for each T ✓.

Then chunked: for each chunk: g = fL[NL_chunk] (uint8); c = g + pcR_chunk (uint8); c[~valid_chunk] = 0 — hmm, boolean-mask assignment per chunk: c[valid_chunk == False] = 0... or c = np.where(valid_chunk, c, 0). Then chunk max & argmax; track global best.

Actually — simpler: since invalid T's must be excluded, and valid = cntR==0: note we could ALSO just not worry: compute c for all, then c