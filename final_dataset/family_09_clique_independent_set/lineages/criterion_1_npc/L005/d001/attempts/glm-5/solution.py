Let me analyze this problem.

We have n employees (n ≤ 46), m grievances (edges). A harmonious delegation is an independent set in the underlying undirected graph (since a grievance between u and v means they can't both be in the delegation — the direction doesn't matter for the "no pair" condition, since if u has a grievance against v, they can't both be in).

Wait, let me re-read: "no employee in the delegation has a grievance on record against any other employee in the delegation." So if u has a grievance against v, both u and v can't be in the delegation. So yes, it's an independent set in the undirected graph where edges are grievances (treated as undirected).

We need to decide whether an independent set of exactly size k exists, and report one.

n ≤ 46. This is the classic maximum independent set problem with meet-in-the-middle: split vertices into two halves of ~23 each, compute all independent sets in each half (up to 2^23 each), then combine.

But we need exactly k, not maximum. Hmm. Actually, if there's an independent set of size ≥ k... wait, no. If there's an independent set of size s > k, then any subset of it of size k is also independent. So an independent set of exactly size k exists iff the maximum independent set has size ≥ k. So we just need to find a maximum independent set (or any independent set of size ≥ k), and then output any k vertices from it.

So the problem reduces to: find maximum independent set in a graph with n ≤ 46 vertices. Classic meet-in-the-middle approach:

1. Split vertices into two halves A (first n1 = n/2 vertices) and B (rest).
2. Enumerate all independent sets in A: for each mask, check if independent, record size. Store for each mask... Actually the standard approach: enumerate all independent subsets of A (up to 2^23 ≈ 8.4M), and for each, store the size. Then enumerate all independent subsets of B, and for each independent subset S_B, we need the best independent subset S_A of A that has no edges to S_B. 

Standard technique: For each independent set in B, compute the set of vertices in A that are adjacent to some vertex in S_B (call it forbidden mask F). Then we need max over independent sets S_A of A with S_A ∩ F = ∅. To do this efficiently, we precompute for A: for each mask M ⊆ A, best[M] = max size of independent subset of M (or we can use the trick: f[mask] = max(f[mask with lowest bit removed], f[mask & ~adj[lowest bit]] + 1)... hmm, that's for a different formulation).

Actually the standard approach for max independent set via meet-in-the-middle:

- Enumerate all independent sets in half A. For each subset mask of A that is independent, we have size = popcount. We want, for a given forbidden mask F, the maximum popcount over independent masks that are subsets of complement of F. 

One way: compute g[mask] for mask ⊆ A = maximum size of an independent set contained in mask. This can be computed via DP: g[mask] = 0 if mask == 0; else take lowest bit v: g[mask] = max(g[mask \ {v}], g[mask \ ({v} ∪ adjA[v])] + 1). Wait, that's not quite right either — that's the standard DP for max independent set on small graphs, which works: g[mask] = max(g[mask ^ (1<<v)], 1 + g[mask & ~(1<<v) & ~adj[v]]). This is O(2^(n/2)) which is 8.4M operations for n/2 = 23. That's fine.

But we also need to reconstruct the actual set. Hmm. For reconstruction, we can store the choice (whether the lowest bit is included) in a separate array, or recompute.

Alternative approach: enumerate all independent sets of A explicitly (list of masks with their popcounts), sort... Actually, let me think about the sizes. n ≤ 46, so each half ≤ 23. 2^23 = 8,388,608. 

Approach:
1. Let n1 = n // 2 (or (n+1)//2), A = vertices 0..n1-1, B = vertices n1..n-1.
2. Compute adjacency masks adjA[v] for v in A (restricted to A), adjB[v] for v in B (restricted to B), and cross adjacency.
3. DP over subsets of A: dp[mask] = max independent set size within mask. dp[0] = 0. For mask > 0, v = lowest bit: dp[mask] = max(dp[mask without v], dp[mask & ~(1<<v | adjA[v])] + 1). Also store choice[mask] = whether v is in the optimal set.

Wait, but careful: dp[mask & ~(bit | adjA[v])] — the mask after removing v and its neighbors. This DP is correct for maximum independent set.

Memory: 2^23 ints for dp — in Python, a list of 8.4M ints is ~67MB+ (each Python int in a list is a pointer, 8 bytes, plus small int objects are cached for small values... actually ints 0-256 are cached, so a list of 8.4M pointers = 67MB). Hmm, memory limit is 256MB. We could use array module or bytes to be safe. dp values ≤ 23, so we can use bytearray. choice can be a bytearray too. That's 8.4MB each. 

But wait — in Python, doing 8.4M iterations of DP with bit operations... that might be slow. 5 second time limit. Python does maybe 10-30M simple operations per second in tight loops. 8.4M iterations with several operations each could take ~5-15 seconds. Hmm, risky.

Alternative: use numpy for vectorization? Bit operations over arrays of 2^23 elements... The DP has dependencies (dp[mask] depends on dp of smaller masks), hard to vectorize directly.

Hmm, let me think about alternative approaches.

Alternative: enumerate independent sets of A via recursive enumeration (DFS), which generates only independent sets, not all subsets. The number of independent sets could still be up to 2^23 in the worst case (empty graph). But enumeration via DFS: for each vertex in order, decide include/exclude. Include only if no conflict with already-included. This generates exactly the independent sets. In the worst case (no edges), it's 2^23 sets, and each set requires O(1) amortized work... in Python, recursion with 8.4M leaf nodes would be slow too.

Hmm, but actually, maybe we don't need to enumerate all. Let me think about what we need:

For each independent set S_B in B, we need max over independent S_A ⊆ A \ N(S_B). 

Alternative formulation: For each independent set S_A in A, let U(S_A) = set of vertices in B adjacent to S_A (the "blocked" set in B). Then for a combination S_A ∪ S_B to be independent, we need S_B ∩ U(S_A) = ∅.

Standard meet-in-the-middle for max independent set:
- List all independent sets in B with their sizes: (mask_B, size_B). Sort by size descending.
- For each, compute forbidden mask in A: F = union of adjCross[v] for v in S_B. Then we need the best independent set in A avoiding F.
- Precompute for A: for each mask M ⊆ A, bestA[M] = max size of independent subset of M. Then answer for F is bestA[A_full \ F].

The DP for bestA takes O(2^{n1}) time. With n1 = 23, that's 8.4M steps. In pure Python, each step: extract lowest bit, a few bit ops, list lookups. Maybe 5-10 seconds. Too slow probably.

Can we do it with numpy? The recurrence dp[mask] = max(dp[mask ^ low], dp[mask & ~((1<<v)|adj[v])] + 1) where v = index of lowest bit. 

Hmm, we can process masks in a different way. Alternative: think of it as dp over subsets where we add vertices one at a time. Let's define dp_i[mask] = max independent set size using only vertices 0..i-1 within mask... no wait.

Alternative vectorizable formulation: Let f[i][mask] = max independent set size within mask considering only vertices with index < i... Hmm, that's 2^23 * 23 memory, too much.

Actually, there's a classic way: dp[mask] where we iterate masks in increasing order. The dependency dp[mask] → dp[mask ^ lowbit] and dp[mask & ~(stuff)]. Both targets are strictly smaller than mask (subset). Can we vectorize by processing in order of... hmm.

Alternative: process vertex by vertex. Define D_i[mask] = max independent set size within mask using only vertices 0..i-1 (vertices i and beyond in mask are ignored... no wait).

Hmm, let me think again. Let's define it as: for i from 0 to n1-1, and mask over all 2^{n1} subsets... 

Actually here's a cleaner vectorizable approach: 

g[mask] = max independent set in induced subgraph on mask. 

We can compute: g[mask] = max(g[mask without vertex v], g[mask without N[v]] + 1) where v = lowest bit.

Vectorization idea: process masks grouped by... The issue is dependencies within the same "level".

Alternative approach entirely: since we need max independent set with n ≤ 46, another classic approach is branch and bound (like the "maxclique" algorithm by Tomita et al.). For n=46, branch and bound with good bounding (greedy coloring) is typically very fast, even in Python, for most graphs. But worst cases (e.g., random graphs near threshold, or specially crafted) could be slow. Hmm, but for a problem with n ≤ 46, meet-in-the-middle is the guaranteed approach. The problem setter chose 46 specifically because 2^23 is feasible in C++. In Python, we need to be clever.

Let me think about how to make meet-in-the-middle fast in Python.

Option 1: Use the DP over subsets of A with numpy, processing in a way that vectorizes.

Idea: Split A further? Or use a different decomposition.

Actually, here's a thought: the DP g[mask] = max(g[mask ^ (1<<v)], 1 + g[mask & ~(1<<v) & ~adj[v]]) processes each mask once, with v = lowest set bit. 

We can restructure: Let's compute g via "for each mask, g[mask] = max over v in mask of (1 + g[mask & ~closed_neighborhood(v)])"? No, that's not right either — actually it is right: g[mask] = 0 if mask == 0, else max over v ∈ mask of max(g[mask \ {v}], 1 + g[mask \ N[v]]). But that's O(2^{n1} * n1) which is worse.

Hmm, but with the lowest-bit trick it's O(2^{n1}).

Vectorization by lowest bit: masks where the lowest bit is v are exactly masks of form (odd multiples...) — masks with bits 0..v-1 clear and bit v set. These are {v} ∪ S where S ⊆ {v+1, ..., n1-1}. For all such masks, the recurrence is g[mask] = max(g[mask ^ (1<<v)], 1 + g[mask & ~((1<<v)|adjA[v])]).

Note: mask ^ (1<<v) ranges over all subsets of {v+1,...,n1-1} (i.e., masks < 2^v... no wait, masks with bits > v). And mask & ~((1<<v)|adjA[v]) also ranges over subsets of {v+1,...} minus neighbors of v.

So for fixed v, the set of masks with lowest bit v is: {2^v + s : s ⊆ higher bits}. If we index arrays by mask, then for fixed v, the relevant entries are at positions 2^v + s for s in [0, 2^{n1-v-1}) subsets of the higher part... but the array positions are strided: positions 2^v, 2^v + 1, ..., 2^{v+1} - 1 correspond to s = 0..2^{v-...} hmm wait.

Masks with lowest bit v: mask = 2^v + s where s has bits only in positions > v. So s ∈ {0} ∪ {sums of 2^j for j > v}. The positions in the array are 2^v + s. If we let t = s >> (v+1) (compressing the higher bits), then mask = 2^v + (t << (v+1)). So positions are strided with stride 2^{v+1}, offset 2^v. Number of such masks: 2^{n1 - v - 1}.

For each such mask: 
- g[mask ^ (1<<v)]: position 2^v + (t << (v+1)) - 2^v = t << (v+1). So it's g at positions t * 2^{v+1} for t = 0..2^{n1-v-1}-1. In the array, that's a strided slice: g[0::2^{v+1}] restricted to first 2^{n1-v-1} elements.
- g[mask & ~((1<<v)|adjA[v])]: mask & ~stuff = (2^v + s) with bit v removed and neighbors of v (which are < 2^v possibly, but since mask has no bits below v, the neighbors of v with index < v contribute nothing; neighbors with index > v are removed from s). So it equals s & ~adjHigh where adjHigh = adj[v] >> (v+1) restricted appropriately... Let me define: s = t << (v+1) conceptually where t is over bits 0..n1-v-2 representing original bits v+1..n1-1. Then mask & ~((1<<v)|adj[v]) = (s & ~adj[v]) since bit v removed. s & ~adj[v]: in terms of t: bits of adj[v] above v: adjHigh = adj[v] >> (v+1). Then s & ~adj[v] = ((t & ~adjHigh) << (v+1)). So g at position ((t & ~adjHigh) << (v+1)).

Hmm, so g[mask] = max(g[(t << (v+1))], 1 + g[((t & ~adjHigh) << (v+1))]).

With numpy: for fixed v, we want to compute for all t in [0, 2^{n1-v-1}): out[2^v + (t << (v+1))] = max(g[t << (v+1)], 1 + g[(t & ~adjHigh) << (v+1)]).

The positions t << (v+1) form a strided slice g[::2^{v+1}] of length 2^{n1-v-1}. The positions (t & ~adjHigh) << (v+1) — these are g[(t & ~adjHigh) * 2^{v+1}] — we can compute via fancy indexing: idx = (t_array & ~adjHigh) << (v+1), then g[idx]. Fancy indexing on 8M-element arrays for each v... total work sum over v of 2^{n1-v-1} = 2^{n1} - 1 ≈ 8.4M elements total across all v. That's actually fine for numpy! Each v does O(2^{n1-v-1}) work with numpy vectorized ops. Total ~ 8.4M * constant numpy ops. 

Wait, but there's a subtlety: when we compute g[mask] for masks with lowest bit v, we reference g at positions that are subsets of mask (strictly smaller). Are those positions already computed? g[t << (v+1)]: t << (v+1) has bits only above v, so its lowest bit is > v, meaning it was computed in an earlier iteration (v' > v)? Wait no — we iterate v from... hmm. Let's think: masks with lowest bit v depend on masks with lowest bit > v (i.e., masks that are subsets of {v+1, ...}). Wait: g[t << (v+1)] where t ranges over all values — the mask t << (v+1) has no bits below v+1, so its lowest bit is ≥ v+1. And g[(t & ~adjHigh) << (v+1)] similarly. So if we process v in decreasing order from n1-1 down to 0, then when processing v, all masks with lowest bit > v are already computed. 

For v = n1-1: masks with lowest bit n1-1: just mask = 2^{n1-1}. g[2^{n1-1}] = max(g[0], 1 + g[0]) = 1 (since adjHigh for v=n1-1 is 0, t ranges over {0}).

So the algorithm: 
- g = numpy array of size 2^{n1}, dtype uint8 (values ≤ 23).
- g[0] = 0.
- For v from n1-1 down to 0:
  - stride = 2^{v+1}, count = 2^{n1-v-1}.
  - base = g[0 : count*stride : stride] — wait, positions t << (v+1) = t * stride for t = 0..count-1. So a = g[::stride][:count] — but careful, g[::stride] has length ceil(2^{n1}/stride) = 2^{n1-v-1} = count. Good, a = g[::stride] (a view or copy? we need values before writing — since we write to different positions (offset 2^v), and read positions are multiples of stride which are different from 2^v + t*stride... wait, are they? Write positions: 2^v + t*stride for t=0..count-1. Read positions: t*stride. These sets are disjoint (write positions have bit v set, read positions don't). So no aliasing issue. But numpy fancy indexing with writing... let me just compute:
  - t_arr = np.arange(count, dtype=...). Hmm, but count can be up to 2^{22} for v=0. np.arange(2^22) is fine.
  - Actually for v=0: stride=2, count=2^{n1-1} = 4M for n1=23. t_arr = arange(4M). idx2 = (t_arr & ~adjHigh) << 1. b = g[idx2] (fancy indexing, 4M elements). a = g[::2] (4M elements, strided view — reading it is fine). out = np.maximum(a, b + 1). Then write: g[1::2] = out. Writing to strided view is fine.

  For general v: write positions are g[2^v::stride] which is a strided view of length count. Read a = g[::stride] (length count), read b = g[(t & ~adjHigh) << (v+1)] via fancy indexing.

  Hmm wait, but there's an issue: for the write g[2^v::stride] = out, and read a = g[::stride] — these views overlap in memory? g[::stride] covers positions 0, stride, 2*stride, ...; g[2^v::stride] covers 2^v, 2^v + stride, ... Since stride = 2^{v+1} > 2^v, positions 2^v + t*stride = (2t+1)*2^v, and read positions are (2t)*2^v. Disjoint. But numpy assignment g[2^v::stride] = out where out was already computed as a new array — fine.

  But wait: b = g[idx2] where idx2 = (t & ~adjHigh) << (v+1) — these positions are multiples of stride, i.e., in the "read" region. Already computed? Positions (t & ~adjHigh) << (v+1): these have bit v clear and bits below v clear, so lowest bit > v, computed in earlier iterations (v' > v). Yes.

  Hmm wait, actually I need to double check: is it true that all masks with lowest bit ≥ v+1 are computed before we process v? We process v from high to low. When processing v, we've processed v+1, ..., n1-1. Masks with lowest bit exactly v' for v' in [v+1, n1-1] are computed. Masks with lowest bit ≥ v+1 means lowest bit is some v' ≥ v+1 — yes, all computed. And mask 0 is base case. 

So this gives g[mask] = max independent set size within mask, for all masks ⊆ A, in O(2^{n1}) numpy work. 

But we also need reconstruction: which independent set achieves g[mask]. Hmm. For reconstruction, we could store choices, but with numpy that's another array. Alternatively, reconstruct by walking: given mask, if g[mask] == g[mask without lowest bit v] then... hmm, we need to be careful: we want to find an actual independent set of size g[mask]. Walk: mask_cur = target mask. While mask_cur != 0: v = lowest bit. If g[mask_cur] == g[mask_cur ^ (1<<v)]: then v is not needed; mask_cur ^= (1<<v). Else: v must be in the set (well, at least we can choose it): add v, mask_cur &= ~((1<<v) | adj[v]). Each step is O(1) lookups. Total steps ≤ 2 * n1. That's fine — reconstruction is cheap since we only need it once (or once per query).

Wait, but actually we need g for arbitrary masks (A_full & ~F for various F). The walk works for any mask. 

Now for the B side: we need, for each independent set S_B in B, the best g[A_full & ~F(S_B)] where F(S_B) = neighbors in A of S_B. Then total = size(S_B) + g[...]. We want the maximum over all independent S_B. And we need to reconstruct the actual sets.

Enumerating all independent sets of B: up to 2^{n2} where n2 = n - n1 ≤ 23. Enumerating 8.4M independent sets in Python with a loop is too slow. Need to vectorize this too.

Hmm. Alternative: do the same DP trick symmetrically? Let's think.

Actually, here's a cleaner symmetric approach: 

Compute g_A[mask] for all mask ⊆ A: max independent set size in A within mask. (Via numpy DP as above.)
Compute g_B[mask] for all mask ⊆ B: max independent set size in B within mask. (Same DP on B's adjacency.)

Now we need max over independent sets S_B of (|S_B| + g_A[A \ N_A(S_B)]). 

Hmm, but that requires enumerating independent sets of B. Alternatively:

max over pairs (S_A independent in A, S_B independent in B, no cross edges) of |S_A| + |S_B|.

Standard approach: enumerate independent sets of one side and query the other. To vectorize enumeration of independent sets of B... 

Alternative: Let's define for each subset T ⊆ B: h[T] = max over independent S_B ⊆ T of (|S_B| + g_A[A \ N_A(S_B)]). Can we DP this? h[T] = max(h[T \ {v}], something involving v included)? If v ∈ S_B, then S_B \ {v} ⊆ T \ N_B[v] must be independent, and the g_A term changes: g_A[A \ N_A(S_B)] where N_A(S_B) = N_A(v) ∪ N_A(S_B \ {v}). Hmm, the g_A term depends on the union of neighborhoods, which doesn't decompose nicely. So h[T] = max(h[T\v], max over independent S ⊆ T \ N_B[v] of |S| + 1 + g_A[A \ (N_A(v) ∪ N_A(S))]). The inner max depends on both |S| and N_A(S), so we can't just use h. 

Hmm. So that doesn't directly work. 

Alternative: enumerate independent sets of B, but vectorized. How to enumerate all independent sets of a 23-vertex graph quickly in Python?

Idea: iterative/level-wise construction with numpy. Independent sets of B: we can build them vertex by vertex. Let I_j = array of masks of independent sets using vertices 0..j-1 (within B). Then I_{j+1} = I_j ∪ {mask | (1<<j) : mask ∈ I_j, mask & adjB[j] == 0}. With numpy: sel = I_j[(I_j & adj) == 0] + (1 << j); I_{j+1} = concat(I_j, sel). Total size up to 2^23 at the end. The work at each step is O(|I_j|) vectorized. Total work O(sum |I_j|) ≤ O(23 * 2^23) worst case = 194M element operations... that's too much? Hmm, actually sum over j of |I_j| where |I_j| ≤ 2^j, so sum ≤ 2^{24} = 16.7M. Wait: |I_j| ≤ 2^j (independent sets using first j vertices). Sum over j=0..22 of |I_j| ≤ 2^23. So total numpy element-ops ~ 2^24 including the new masks. That's fine — maybe 16.7M * a few numpy ops. Each step: boolean mask computation (I_j & adj == 0), compression, addition, concatenation. Memory: final array up to 8.4M int32 = 33MB. OK.

But then, for each independent set S_B (up to 8.4M), we need F(S_B) = OR of adjCross[v] for v ∈ S_B, then query g_A[A_full & ~F]. Computing F for each S_B: we can compute alongside enumeration: F_j = array of forbidden masks (in A) for each independent set. F_{j+1} extends similarly: when adding vertex j to set with mask m, new F = F_old | adjCrossA[j]. So maintain parallel arrays. Memory: another 33MB. Then final step: query = g_A[(A_full & ~F)] — fancy indexing 8.4M elements into g_A (8.4M uint8 array). Then total = popcount(S_B) + query. popcount of 8.4M int32s: numpy doesn't have builtin popcount until numpy 2.0 (np.bitwise_count). Hmm, we can maintain sizes alongside too (size array, +1 when adding vertex). Or compute popcount via bit tricks vectorized. Maintaining size array is easiest: another 33MB int8... wait sizes ≤ 23, uint8 fine.

Then answer = max(size_B + g_A[A_full & ~F_B]) over all independent sets S_B. Then find argmax, reconstruct.

Memory total: masks_B (int32, 33MB), F_B (int32, 33MB), size_B (uint8, 8.4MB), g_A (uint8, 8.4MB). Plus intermediate concatenations — numpy concat creates new arrays; peak might be ~2x for one side. Should be OK under 256MB if careful. Actually we can avoid keeping all levels: at each step, we create the new arrays and discard old. Peak: level j arrays (|I_j|) plus level j+1 (≤ 2|I_j|)... peak ~ 3 * final? Hmm, at the last step, |I_22| could be ~2^22 and |I_23| = 2^23, so peak ~ 1.5 * 2^23 elements * (4+4+1 bytes) ≈ 113MB. Plus g_A 8.4MB. Should be OK. Actually wait, we could also split differently: n1 = 23, n2 = 23 for n=46.

Hmm wait, but actually there's a subtlety: we don't need to enumerate ALL independent sets of B and take max with g_A queries. Alternative standard trick: sort independent sets of B by size descending, and for each, query g_A; the first time... no, that doesn't prune anything without extra structure.

Alternatively, symmetric DP approach: compute for A: for each mask M ⊆ A, g_A[M] (max ind set size in M). For B: enumerate independent sets with their cross-neighborhoods. The approach above works.

But hold on — maybe there's an even better approach avoiding enumerating all independent sets of B: 

For each subset F ⊆ A (the forbidden set), define w[F] = max over independent S_B with N_A(S_B) ⊆ F of |S_B|... no wait, we want N_A(S_B) ∩ (chosen S_A) = ∅.

Alternative: define for each mask X ⊆ A: best_B[X] = max over independent S_B with N_A(S_B) ⊆ X of |S_B|. Hmm, then answer = max over S_A independent of (|S_A| + best_B[A \ N_A(S_A)])? No wait: we need S_B's neighborhood in A to avoid S_A: N_A(S_B) ∩ S_A = ∅ ⟺ N_A(S_B) ⊆ A \ S_A. So answer = max over independent S_A of (|S_A| + best_B[A \ S_A]).

Can we compute best_B[X] for all X ⊆ A via DP? best_B[X] = max over independent S_B with N_A(S_B) ⊆ X. Hmm, DP over X: best_B[X] = max(best_B[X \ {v}], ...)? The condition "N_A(S_B) ⊆ X" — adding element v to X: sets S_B that become allowed are those with N_A(S_B) ⊆ X and v ∈ N_A(S_B). Not a nice DP.

Alternatively define via complement: for each S_B, it contributes |S_B| to all X ⊇ N_A(S_B). This is a "subset max" / SOS (sum over subsets) DP but with max instead of sum: best_B[X] = max over S_B with N_A(S_B) ⊆ X of |S_B|. We can compute this if we first compute c[Y] = max |S_B| with N_A(S_B) == Y exactly, then do SOS-style max propagation: best[X] = max(c[Y] for Y ⊆ X). SOS with max: for each bit i, for each X with bit i set: c[X] = max(c[X], c[X ^ (1<<i)]). That's O(2^{n1} * n1) = 8.4M * 23 = 193M numpy element ops... as vectorized numpy: for each of 23 bits, operate on half the array: total 23 passes over 8.4M/2... that's 23 * 4.2M = 97M element ops in 23 numpy calls. Feasible: each pass is c[idx] = maximum(c[idx], c[idx ^ bit]) where idx = positions with bit set. Vectorized: view = c.reshape(-1, 2^{i+1})? Hmm, standard SOS vectorization: for bit i, c[...] — we can do: for each i: strided access. Positions with bit i set: offset 2^i, stride 2^{i+1}. c[2^i::2^{i+1}] = np.maximum(c[2^i::2^{i+1}], c[0::2^{i+1}]). That's a strided in-place maximum — but careful: c[0::stride] and c[2^i::stride] are disjoint views, so in-place is fine. Each such operation touches 2^{n1-i-1} elements. Total ~ 2^{n1} = 8.4M element ops across 23 numpy calls. 

But how do we compute c[Y] = max |S_B| over independent S_B with N_A(S_B) == Y? We'd still need to enumerate all independent sets of B! Unless... hmm.

OK here's another thought: c[Y] = max over independent S_B with N_A(S_B) ⊆ Y of |S_B| — can we compute this with a DP over B's vertices? Define DP over subsets of B? That's 2^{n2} states with... hmm.

Actually, let's reconsider. Maybe combine: 

answer = max over independent S_A, independent S_B, no cross edges of |S_A| + |S_B|.

Alternative formulation via the "forbidden" trick on both sides:

For each independent S_B, contribution: |S_B| + g_A[A \ N_A(S_B)].

We need max over independent S_B. The number of distinct values of N_A(S_B) could be much smaller than the number of independent sets, but worst case still large.

I think enumerating independent sets of B with numpy (vectorized DFS/BFS by levels) is the way. Let me estimate more carefully.

n = 46. Split: n1 = 23 (A), n2 = 23 (B). 

Step 1: g_A DP via numpy: ~2^23 element ops across 23 vectorized steps. Fast (< 1 sec).

Step 2: enumerate independent sets of B, maintaining (mask, size, F_A). Levels j = 0..22. At level j, arrays of length L_j ≤ 2^j. Operations per level: 
- compat = (masks & adjB_j) == 0 → L_j ops.
- new_masks = masks[compat] + (1 << j) → up to L_j.
- new_F = F[compat] | cross_j → up to L_j.
- new_size = size[compat] + 1.
- concat.
Total ~ 2 * 2^23 element ops across levels, in ~23*5 numpy calls. Fast.

Step 3: query = g_A[(A_full & ~F)] — hmm, A_full & ~F: since F ⊆ A_full always (F is union of adjacency masks restricted to A), A_full & ~F = A_full ^ F. So query = g_A[A_full ^ F]. Fancy indexing 8.4M elements. Then totals = size + query; find max and argmax. Fast.

Step 4: reconstruct: take the best S_B (mask), and M_A = A_full ^ F(S_B). Then walk the g_A DP to reconstruct S_A within mask M_A. Also verify... well, trust the algorithm.

Then if max total ≥ k, output any k vertices from S_A ∪ S_B. Wait — but we need exactly k. Since S_A ∪ S_B is independent of size max_total ≥ k, any subset of size k works. If max_total < k, output NO.

Hold on, is it true that "independent set of size exactly k exists iff max independent set ≥ k"? Yes: any subset of an independent set is independent. And conversely if exactly k exists then max ≥ k. 

Edge cases: k could be ≤ max. Also note k ≥ 1 always, and n ≥ 1.

Wait, but also: what if the maximum independent set is ≥ k — we output k vertices from it. Good.

Now, is the meet-in-the-middle correct? The maximum independent set of the whole graph: its intersection with A is an independent set in A, intersection with B independent in B, and no cross edges. Conversely, any pair (independent S_A, independent S_B, no cross edges) forms an independent set. So max over pairs = max independent set. And our enumeration covers all independent S_B, and for each, g_A[A \ N_A(S_B)] = max independent S_A avoiding N_A(S_B), which is exactly the condition "no cross edges between S_A and S_B". 

Now, the g_A DP correctness: g_A[mask] = 0 if mask == 0. For mask ≠ 0, let v = lowest bit of mask. Then max independent set in mask either excludes v: g_A[mask \ {v}], or includes v: 1 + g_A[mask \ N[v]] where N[v] = {v} ∪ neighbors. This is the standard correct recurrence. Note mask \ N[v] = mask & ~((1<<v) | adj[v]) — since v ∈ mask, and we remove v and neighbors.

Wait, in my numpy formulation above, I need to double check the recurrence indexing. For masks with lowest bit v: mask = 2^v + s, s ⊆ {v+1, ..., n1-1}. 
- Exclude v: g[mask ^ (1<<v)] = g[s].
- Include v: 1 + g[mask & ~((1<<v)|adjA[v])] = 1 + g[s & ~adjA[v]] (since s has no bits < v... wait, adjA[v] may have bits < v, but s has no bits below v+1, so s & ~adjA[v] = s & ~(adjA[v] & ~((1<<v) | ((1<<v)-1)))... let me redo: mask & ~((1<<v)|adjA[v]) = (2^v + s) & ~((1<<v)|adjA[v]) = s & ~adjA[v] (the 2^v bit is removed by ~ (1<<v); bits of adjA[v] below v+1 that are in s: s has no bits below v+1, so only bits of adjA[v] above v matter). So = s & ~(adjA[v] >> (v+1) << (v+1))... i.e., s with v's higher neighbors removed.

In terms of t where s = t << (v+1) (t ⊆ {0..n1-v-2} representing bits v+1..n1-1): 
- g[s] = g[t << (v+1)] = g[t * stride] where stride = 2^{v+1}.
- g[s & ~adjA[v]] = g[(t & ~adjHigh) * stride] where adjHigh = adjA[v] >> (v+1).

And write position: mask = 2^v + t*stride.

So: for v from n1-1 downto 0:
  stride = 1 << (v+1)
  count = 1 << (n1 - v - 1)
  t = np.arange(count, dtype=np.int64) — hmm, for v=0, count = 2^{22} = 4M, arange fine.
  a = g[0 : ... : stride] → g[::stride] has length ceil(2^{n1} / stride) = 2^{n1-v-1} = count. Good: a = g[::stride] (view).
  adjHigh = adjA[v] >> (v+1)
  idx = (t & ~adjHigh) * stride — wait, t & ~adjHigh: adjHigh is a Python int; t is numpy array; t & ~adjHigh works (numpy broadcasts). But careful with dtype: for v=0, t up to 2^22 - 1, times stride 2 → up to 2^23 - 2, fits in int64 (or even int32: 2^23 fits in int32). Use int64 to be safe, or int32 to save memory. 2^23 = 8.4M < 2^31, fine for int32.
  b = g[idx] (fancy indexing — creates copy).
  vals = np.maximum(a, b + 1) — hmm, b + 1: b is uint8; b+1 could overflow? Max g value is 23, +1 = 24 < 255, fine. But numpy uint8 + Python int 1 → stays uint8 (in numpy ≥ 1.x, uint8 + int → uint8 with possible overflow warning? Actually numpy: uint8 array + Python scalar int → uint8 array, value-based casting; 24 fits). To be safe, use small ints fine.
  g[1<<v :: stride] = vals.

Wait, g[1<<v::stride] — positions 2^v, 2^v + stride, 2^v + 2*stride, ...: count = number of elements = floor((2^{n1} - 2^v - 1)/stride) + 1 = 2^{n1-v-1} = count. Good.

Hmm, but one concern: a = g[::stride] is a strided view; when we do np.maximum(a, b+1), numpy reads a — fine. Then we write to g[1<<v::stride] — disjoint positions from a's positions? a's positions: 0, stride, 2*stride, ... (even multiples of 2^v). Write positions: 2^v, 2^v+stride, ... (odd multiples of 2^v). Disjoint. But wait — is `vals` computed before the write? Yes, np.maximum returns a new array. Good.

But actually, hmm, wait: there's an aliasing subtlety: b = g[idx] is a copy (fancy indexing always copies). a is a view but np.maximum(a, b+1) produces a new array. So writing afterwards is safe.

Also, for v = n1-1: stride = 2^{n1}, count = 1. t = [0]. a = g[::2^{n1}] = [g[0]] = [0]. adjHigh = adjA[n1-1] >> n1 = 0. idx = [0]. b = [g[0]] = [0]. vals = [max(0, 1)] = [1]. g[2^{n1-1}::2^{n1}] = [1]. Good.

Edge: n1 could be 0? n ≥ 1, and we set n1 = n // 2 or (n+1)//2. Let's set n1 = (n+1)//2 maybe, or n//2. Let's think: A = first n1 vertices, B = rest. If n = 1: n1 = 1, n2 = 0. Then B has no independent sets except empty. Fine. If n1 = 0 (n=... if n//2 = 0 only when n ≤ 1; n=1 → n1 = 0 if n//2). Let's use n1 = n // 2 and B = vertices n1..n-1, so n2 = n - n1 ≥ n1. For n=1: n1=0, n2=1. Then A is empty: g_A has size 2^0 = 1, g_A[0] = 0. B enumeration: independent sets of single vertex: {} and {v}. Works. Alternatively n1 = (n+1)//2. Either fine as long as code handles empty halves. Let me make sure the code handles n1 = 0 (loop doesn't run, g = [0]) and n2 = 0 (enumeration yields just the empty set).

Hmm wait, actually, which half should be bigger? The g_A DP is O(2^{n1}) with small constant (numpy). The B enumeration is O(2^{n2}) with bigger constant (maintaining 3 arrays). Also memory: B arrays are 4+4+1 = 9 bytes per set vs g_A 1 byte. To balance, maybe make A bigger: n1 = (n+1)//2 = 23, n2 = 23 for n=46. For n=45: n1=23, n2=22. Fine either way. Let me just use n1 = n // 2... hmm, for n=46: n1=23, n2=23. Same. For odd n it doesn't matter much. Let me use n1 = (n+1) // 2 so A is the larger or equal half — since g_A DP is cheaper per element. Actually wait, for the B enumeration, the per-element cost is higher, so we want n2 smaller: n2 = n // 2, n1 = n - n2 = ceil(n/2). Yes, n1 = (n+1)//2.

Hmm, wait. Actually, let me reconsider whether we even need the full generality. n ≤ 46, but m can be up to n(n-1)/2 = 1035 — complete graph. In many cases the graph is sparse and simpler algorithms work. But worst case (empty graph, m=0): max independent set = n, trivially. Random dense graphs: max independent set small. The hard cases for meet-in-the-middle are fine; the hard cases for branch-and-bound are adversarial. Meet-in-the-middle is guaranteed O(2^{n/2}) — let's go with it, implemented with numpy.

But wait — what if numpy is not available? The problem says Python 3; typically numpy is available on competitive judges (Codeforces has it). This looks like it might be from a specific judge... "Problem A — Harmonious Delegation". Unknown judge. Risky to rely on numpy? Hmm. Let me think about a pure-Python approach that fits in 5 seconds.

Pure Python: 2^23 = 8.4M iterations of a simple loop — in CPython, roughly 0.5-1 μs per iteration for a loop body with a few operations → 5-10 seconds. Too slow. With PyPy it'd be fine but we must assume CPython.

Alternative pure-Python: use integers as bitsets and process in chunks? Hmm.

Alternative: branch and bound with bitmasks (like maxclique-style). For n=46, a well-implemented B&B with coloring bounds typically explores few nodes for most graphs, but worst case can blow up. Given the problem constraints (n ≤ 46, 5s), the intended solution is meet-in-the-middle in C++. For Python, we need the fastest possible approach. 

Let me think about pure-Python meet-in-the-middle more cleverly.

Actually, here's a classic trick for max independent set meet-in-the-middle that reduces work: 

For the A side, instead of DP over all 2^{n1} masks, enumerate independent sets of A only (could be fewer than 2^{n1} if A has edges, but 2^{n1} worst case).

Hmm, what about using the "profile" approach: for each independent set S_A of A, compute its neighborhood in B: N_B(S_A). Then for the combination, we need S_B ∩ N_B(S_A) = ∅. Sort/list independent sets of B... The standard approach: for each independent S_B, we need max |S_A| over S_A with N_A(S_B) ∩ S_A = ∅. 

Alternative pure-Python trick: represent the DP array g_A as a Python list of ints, and use list comprehensions / slicing to vectorize. Python list operations are ~per-element cost of maybe 30-50ns for simple ops in comprehensions. 8.4M elements * a few ops = maybe 1-2 seconds. Hmm, possible!

Let me think about how to do the g_A DP with list slicing:

for v in range(n1-1, -1, -1):
    stride = 1 << (v+1)
    adjHigh = adjA[v] >> (v+1)  # bits over positions v+1..n1-1, as an int
    # a = g[::stride] — list slicing: g[::stride] gives elements at 0, stride, 2*stride, ...
    # For each t: g[2^v + t*stride] = max(g[t*stride], g[(t & ~adjHigh)*stride] + 1)
    
    # Using map: 
    # idx_list = [ (t & ~adjHigh)*stride for t in range(count) ] — this is a Python loop of 8.4M total... 

Hmm, the total across all v is 2^{n1} = 8.4M iterations of Python-level loop. Each iteration: t & ~adjHigh (int ops), multiply, index. Maybe 0.2-0.4 μs each → 2-3 seconds. Plus the max and assignment. Risky but maybe feasible within 5s? Hmm, hard to say. And the B-side enumeration is another 8.4M with more work per element. Total maybe 8-15 seconds. Too slow for pure Python.

OK here's another thought: maybe use a different algorithm altogether that's fast in Python for n=46.

Branch and bound (Tomita's maxclique-style for maximum independent set via complement graph maximum clique). For n=46, MCR/BBMC-style algorithms are usually very fast. Worst-case instances exist but for a problem like this (probably from a contest where the intended solution is meet-in-the-middle), test data might include adversarial cases for B&B? Unlikely — the problem explicitly has n ≤ 46 which screams meet-in-the-middle; the tests probably include cases designed to defeat... hmm, actually if the intended solution is meet-in-the-middle, tests might include dense random graphs where B&B also does fine, and maybe some structured cases. B&B with good bounds handles most n=46 graphs in well under a second even in Python... but there exist 46-vertex graphs where B&B takes exponential time (e.g., certain Ramsey/C5-like structures, or random graphs at critical density). Actually for n=46, even adversarial cases: the search tree for max clique with coloring bounds on 46 vertices — I believe it's at most a few million nodes for any 46-vertex graph? Hmm, not guaranteed, but practically, 46 is small enough that B&B is nearly always fast. But "nearly always" is risky.

Alternatively: hybrid — use B&B with a node limit; if exceeded, fall back to meet-in-the-middle with numpy? That's complex.

Let me reconsider: is numpy safe to assume? The problem statement format (with "Time limit: 5 s, Memory limit: 256 MB") suggests something like Codeforces or an ICPC-style judge. Codeforces has numpy. Many judges do. But if this is from a custom judge... The instruction says "You write correct, efficient Python 3 solutions." I'll consider including a numpy fast path with a pure-Python fallback? That doubles complexity. Hmm.

Actually, let me think more about pure Python performance with clever tricks.

Key insight for pure Python: we can use Python's big integers as bitsets and bytes/bytearray operations to vectorize some things. 

For the g_A DP: g is an array indexed by mask (0..2^{n1}-1), values 0..23. Use a bytearray. The DP: for v from high to low: for all t: g[2^v + t*stride] = max(g[t*stride], g[(t & ~adjHigh)*stride] + 1).

Hmm, the (t & ~adjHigh)*stride indexing is the problem — it's a gather operation. Pure Python gather of 8.4M elements is slow.

Alternative: reorganize the DP to avoid gathers. 

Different DP formulation: process vertices one at a time, maintaining g over subsets? Let's define D_j[mask] = max independent set size within mask using only vertices 0..j-1 (vertices ≥ j in mask are... hmm).

Let me define: D_j[m] for m ⊆ {0..j-1}: max independent set in induced subgraph on m (using all vertices). Transition from D_j to D_{j+1}: for m ⊆ {0..j}: if bit j not in m: D_{j+1}[m] = D_j[m]. If bit j in m: D_{j+1}[m] = max(D_j[m \ {j}], 1 + D_j[m \ N[j]]) where N[j] ⊆ {0..j-1}... wait no, neighbors of j can be > j. Hmm, but if we restrict m ⊆ {0..j}, then m \ N[j] removes neighbors of j within {0..j}. But D_j is only defined on subsets of {0..j-1}; m \ N[j] ⊆ {0..j-1} after removing j itself. OK so:

D_{j+1}[m] = max(D_j[m ^ (1<<j)], 1 + D_j[m & ~closedN_j]) where closedN_j = (1<<j) | adj[j], for m with bit j set; and D_{j+1}[m] = D_j[m] for m without bit j.

This is exactly the same as before, just organized by vertex. The array size doubles each step: 2^{j+1}. Total work: sum over j of 2^{j+1} = 2^{n1+1}. Same as before. The gather: for each m with bit j set, we need D_j[m & ~closedN_j]. Positions m with bit j set: m = 2^j + s, s ⊆ {0..j-1}. m & ~closedN_j = s & ~adj[j]. So we need, for all s ⊆ {0..j-1}: D_j[s & ~adj_j]. 

Hmm, here's a trick: the map s → s & ~adj_j is a "clear some bits" operation. The values D_j[s & ~adj_j] as s ranges over all subsets: we can compute this as: for each s, D_j[s & ~adj_j]. If adj_j has a bits set, then the map is 2^{|adj_j|}-to-1... We can compute the array E[s] = D_j[s & ~adj_j] for all s ⊆ {0..j-1} efficiently? 

E[s] = D_j[s & ~adj_j]. Note that s & ~adj_j depends only on bits of s not in adj_j. Hmm, we could compute E by "expanding" D_j: E = D_j "spread out". Specifically, let the bits not in adj_j be positions p_1 < p_2 < ... and bits in adj_j be q_1 < q_2 < .... Then E[s] = D_j[s restricted to p bits]. So E is D_j with each entry duplicated 2^{|adj_j|} times in a pattern. Constructing E: interleaving/duplication operations on bytearrays. 

Hmm, this is getting complicated. Let me think about whether there's a slicker way.

Alternative: think of the whole g_A computation differently. 

Actually, you know what — there's a neat alternative: compute for each mask m ⊆ A whether m is independent, and the max independent set within m via a different recurrence that's gather-free?

Hmm, what about: g[m] = max(g[m ^ lowbit], 1 + g[m & ~closedN[lowbit]]) — the gather g[m & ~closedN[v]] where m has lowbit v. As computed: positions (t & ~adjHigh)*stride. The gather indices t & ~adjHigh for t in [0, 2^{n1-v-1}): this is a fixed pattern per v. 

Pure Python trick for gather: if we store g as a list, then [g[(t & mask)*stride] for t in range(count)] — still a Python loop.

What about using dict/array with precomputed index lists? The index list for each v: idx_v = [(t & ~adjHigh) << (v+1) for t in range(2^{n1-v-1})]. Precomputing all these lists takes total 2^{n1} elements across all v — 8.4M list elements, each requiring computation. Then the gather [g[i] for i in idx_v] — list comprehension with indexing: ~50-80ns per element? 8.4M * 2 (precompute + gather) plus max plus store... maybe 3-6 seconds just for A side. Too slow.

Hmm OK. What about structuring the meet-in-the-middle differently to reduce to O(2^{n/2}) simple operations that Python can do fast via built-ins?

Alternative idea: use integers as bitsets for the "independent set enumeration" and process with big-int operations. E.g., enumerate independent sets of B via DP where the collection of masks is packed into a big integer? Not obviously.

Alternative: Reduce to counting/decision via spectral or other methods? No.

Let me reconsider the problem: maybe there's a simpler characterization. We need an independent set of size exactly k. Hmm, k can be anything from 1 to n. The answer is YES iff α(G) ≥ k. So we need α(G) (or just whether α(G) ≥ k) for n ≤ 46.

Hmm wait, actually maybe we don't need the exact maximum — we need to know if there's an independent set of size ≥ k, and find one of size exactly k. If k is small, greedy/other methods might certify quickly. If k is large... Hmm, but worst case k ≈ α(G) requires exact computation.

Complement graph: independent set = clique in complement. Max clique on 46 vertices.

I think the pragmatic approach: implement meet-in-the-middle with numpy, with a pure-Python fallback if numpy is unavailable. Or... just numpy. Actually, let me also consider: maybe implement the whole thing in pure Python but with heavy use of built-in functions that run in C:

Key realization: The B-side enumeration can be done with list comprehensions fairly efficiently. And the A-side DP... let me think about the A-side DP as list operations.

Actually here's a cleaner way to think of the A-side: we want, for every mask m ⊆ A, g[m] = max independent set size in m. 

Alternative: compute ind[m] = 1 if m independent else 0, for all m — via DP: ind[m] = ind[m ^ lowbit] and (adj[lowbit] & m) == 0... that's also per-element Python work.

Hmm, what about computing g via "for each independent set, update"? Like: g[m] = popcount(m) if m independent. And g[m] = max over submasks... The SOS-max approach: g[m] = max over independent s ⊆ m of |s|. If we have the indicator of independent sets with their sizes... 

SOS-max DP: g[m] = max(g[m], g[m ^ (1<<i)]) for each bit i — that's n1 passes over 2^{n1} elements = 23 * 8.4M = 193M element-ops. In pure Python, way too slow. With numpy, 193M element ops in 46 vectorized calls — that's fine actually (~1-2 sec). Hmm wait, but we'd need the base: g0[m] = |m| if m independent else 0. Computing independence for all 2^{n1} masks: vectorized with numpy? ind[m] for all m: DP ind[m] = ind[m ^ lowbit] & ((m & adj[lowbit]) == 0)... also gather-free? ind[m ^ lowbit]: position m ^ lowbit — for m with lowbit v, positions t*stride... same structure as before: ind[2^v + t*stride] = ind[t*stride] & ((t & adjHigh) == 0). Hmm, that's actually simpler: no gather needed! Because the "include v" branch isn't needed for independence testing — independence of m is: v = lowbit; m independent ⟺ (m & adj[v]) == 0... wait no: m independent ⟺ (adj[v] & m) == 0 AND m \ {v} independent. And adj[v] & m = adj[v] & (m ^ (1<<v))... since v ∉ adj[v] (no self loops), adj[v] & m = adj[v] & s where m = 2^v + s. So ind[m] = ind[s] & (s & adjHigh == 0). In numpy: for each v: ind[2^v::stride] = ind[::stride] & (((t & adjHigh) == 0)). Where t = arange... The (t & adjHigh) == 0 computation: t & adjHigh for t in arange — vectorized. 

So with numpy, computing ind[] for all masks: 23 vectorized steps, total 8.4M element ops. Then g0[m] = popcount(m) * ind[m] — popcount vectorized: hmm, np.bitwise_count exists only in numpy ≥ 2.0. Fallback: popcount via lookup table on bytes: split mask into 3 bytes (n1 ≤ 23 → 3 bytes), table lookup: popcount = tbl[(m >> 16) & 255] + tbl[(m >> 8) & 255] + tbl[m & 255]. Vectorized: 3 array ops. Fine.

Then SOS-max: 23 passes, each touching 2^{n1-1}... wait, standard SOS: for i in range(n1): for all m with bit i set: g[m] = max(g[m], g[m ^ (1<<i)]). Vectorized: g[2^i::2^{i+1}] = np.maximum(g[2^i::2^{i+1}], g[0::2^{i+1}]). Each pass touches 2^{n1-i-1} elements... wait: positions with bit i set: 2^{n1-1} of them. Hmm: g[2^i::2^{i+1}] has 2^{n1-i-1} elements. Sum over i: 2^{n1} - 1 ≈ 8.4M. Wait that's not right: for i=0: stride 2, positions 1,3,5,...: 2^{n1-1} = 4.2M elements. For i=1: stride 4, positions 2,6,10,...: 2^{n1-2}. Sum = 2^{n1} - 1. Yes ~8.4M total. 

But wait — is SOS-max correct here? g[m] = max over independent s ⊆ m of |s|. Base: g0[m] = |m| if m independent else 0 (note: empty set is independent, so g0 ≥ 0 always; also if m independent, the max independent subset of m is m itself). SOS-max: g[m] = max over submasks s ⊆ m of g0[s]. The standard SOS DP computes exactly max over subsets. Yes: after processing all bits, g[m] = max_{s ⊆ m} g0[s]. Correct.

Hmm, but actually the direct DP (g[m] = max(g[m ^ lowbit], 1 + g[m & ~closed])) is also fine and I showed it's vectorizable with a gather. The SOS approach avoids gathers entirely — all operations are strided slices! That's cleaner and probably faster. Let me double check the SOS approach's total cost: computing ind: 23 steps, each with a few array ops on ~2^{n1-v-1}... wait, for the ind DP: for v from n1-1 downto 0: operate on positions with lowbit v: count = 2^{n1-v-1}. Sum = 2^{n1}. Each step: t & adjHigh (arange & scalar), ==0, & with ind slice, write. Fine.

Hmm wait, actually for the ind DP I realize we can simplify: we don't even need ind per se... we need g0[m] = popcount(m) if m independent. Alternatively, skip ind and directly do the direct DP with gather. Both fine. Let me compare:

Direct DP with gather: 23 steps, each: arange (or reuse), t & ~adjHigh, << shift or * stride, fancy index gather (b = g[idx]), np.maximum(a, b+1), strided write. Total ~8.4M gathered elements. Fancy indexing gather of 4M elements: fast (~50ms). Total maybe 0.3-0.5s.

SOS approach: ind DP (23 steps, ~8.4M element ops, no gather), popcount (3 byte-table lookups on 8.4M), multiply, SOS-max (23 steps, 8.4M element ops). Total maybe 0.5-1s. Both fine. The direct DP also needs reconstruction which works via walking. The SOS approach reconstruction: walk down from mask m: for i from high to low... hmm, reconstruction for SOS-max: given m, g[m] = max over s ⊆ m of g0[s]. To find the argmax subset: walk bits from high to low: cur = m; for i from n1-1 downto 0: if bit i in cur: if g[cur ^ (1<<i)] == g[cur]: cur ^= (1<<i) (we can drop bit i and still achieve the max). At the end, cur is a submask with g0[cur] = g[m]... wait, need g0[cur] == g[m] and cur independent. Hmm: the walk ensures g[cur] stays = g[m]. At the end (all bits considered), cur is such that removing any bit decreases g... that means g0[cur] = g[cur] = g[m]? Let me think: g[cur] after dropping all droppable bits: for every bit i in cur, g[cur ^ (1<<i)] < g[cur]. Since g[cur] = max(g0[cur], max over bits g[cur ^ (1<<i)]), this means g[cur] = g0[cur], i.e., cur is independent (or empty) with |cur| = g[m]. Yes! Because g[cur] = max over submasks of g0, and if all immediate submasks (cur minus one bit) have smaller g... hmm wait, that's not quite a proof: g[cur] = max(g0[cur], max_i g[cur \ {i}]). If for all i, g[cur\{i}] < g[cur], then g[cur] = g0[cur]. Yes that's right since the max over all submasks is achieved either at cur itself or at some submask cur\{i} (any proper submask is contained in cur\{i} for some i, and g is monotone: s ⊆ m ⟹ g[s] ≤ g[m]). So g[cur \ {i}] ≥ g[s] for any s ⊆ cur\{i}. So max over proper submasks = max_i g[cur\{i}]. Good. So reconstruction: O(n1) lookups. 

Both approaches work. The direct DP is simpler code-wise? Let me flesh out both and pick.

Actually hold on, let me reconsider the overall structure once more, because there's an important alternative that avoids the B-side enumeration being the bottleneck:

Structure choice: 
- Side A: full DP g_A over all 2^{n1} masks (numpy, no gather or with gather).
- Side B: enumerate all independent sets of B (up to 2^{n2}), each with (mask, size, F_A = neighborhood in A). Then best = max over these of size + g_A[A_full ^ F_A].

The B-side enumeration with numpy: levels, each level vectorized. Final arrays: up to 2^{n2} entries. For n2 = 23: 8.4M entries. Arrays: masks (int32: 33MB), F (int32: 33MB), size (uint8: 8.4MB). During construction, we hold level j and build level j+1: peak ~ 1.5x final = ~112MB for the three arrays at the last level plus the previous level... Let me count more carefully:

At the last step (adding vertex 22, 0-indexed): level 22 arrays: L22 ≤ 2^22 entries: masks 16MB, F 16MB, size 4MB = 36MB. Then compute compat mask (bool, 4MB), select subsets: new_masks ≤ 2^22: 16MB, new_F 16MB, new_size 4MB. Then concatenate: level 23 arrays: 2^23: masks 33MB + F 33MB + size 8.4MB = 75MB. Peak during concat: 36 + 36 + 75 = ~147MB. Plus g_A 8.4MB, plus temporaries. Under 256MB, OK but somewhat close. We can reduce: instead of concatenating masks (we don't actually need masks of B sets except for reconstruction of the best one — we need mask for the final best set... we could store parent pointers instead? Or just recompute the best set's mask by walking? Hmm.)

Actually, do we need the B masks at all? At the end, we find the best (size, F) pair — we need to reconstruct which B-set achieves it. Options: (a) keep masks array (33MB); (b) store index/parent info; (c) after finding the best (size_B, F) and knowing its index in the final array, reconstruct the mask from the index: the enumeration order is structured — if we always concatenate [old; new_selected], then the final array index encodes... hmm, the mapping from index to set isn't trivially decodable because selection compresses. Alternative: store for each entry its "parent" — too much memory.

Alternative: avoid storing masks: note that the final array is built as: level arrays where entry i in level j+1 is either entry i of level j (if i < L_j) or a "new" entry derived from some entry of level j. If we store, for the new entries, the source index... that's another 4 bytes each. Same as storing masks. Storing masks directly is simplest: 33MB int32.

Alternatively, reduce memory by processing B in two sub-halves? Overkill.

Alternatively, we can avoid materializing the full B enumeration: process the B enumeration level by level, and at each level... no, we need the final F values to query g_A.

Hmm, actually here's a thought: we could swap roles: do the full DP on B (g_B over all 2^{n2} masks) and enumerate independent sets of A (with F_B = neighborhood in B). Then query g_B[B_full ^ F]. Same memory.

Or: do full DP on both sides and then... we still need to enumerate one side's independent sets. Unless we use the SOS trick on both sides!

Let me think: can we compute max over (S_A, S_B) with no cross edges using only SOS-style DPs?

Define for side A: for each mask m ⊆ A: gA[m] = max independent set in m. (DP as before.)
Define for side B: for each mask m ⊆ B: gB[m] = max independent set in m.

We want max over independent S_A, S_B with N_A(S_B) ∩ S_A = ∅ of |S_A| + |S_B|.

Hmm, define hA[X] for X ⊆ A: max over independent S_A ⊆ X of |S_A| = gA[X]. And we want max over S_B of (|S_B| + gA[A \ N_A(S_B)]).

Define for each Y ⊆ A: c[Y] = max over independent S_B with N_A(S_B) == Y of |S_B| (or -inf if none; note N_A(∅) = ∅ so c[∅] ≥ 0). Then answer = max over Y of (c[Y] + gA[A \ Y]).

Computing c[Y] requires knowing N_A(S_B) for all independent S_B — again enumeration. Unless we can DP it: c as a function over subsets of A, built by adding B vertices one at a time: c_j[Y] = max over independent S ⊆ {B_0..B_{j-1}} of |S| with N_A(S) == Y. Transition adding B vertex j: c_{j+1}[Y] = max(c_j[Y], max over Y' with Y' ∪ adjA(j) == Y... hmm: including vertex j: S = {j} ∪ S', S' independent ⊆ {B_0..B_{j-1}}, N_A(S) = adjA(j) | Y' where Y' = N_A(S'). So c_{j+1}[Y] = max(c_j[Y], 1 + max{c_j[Y'] : Y' | adjA(j) == Y}... this is a "subset convolution"-ish operation — expensive: for each j, for each Y, max over Y' ⊆ Y with Y' ∪ adj = Y... The condition Y' | adjA(j) == Y means Y' ⊆ Y and Y \ adjA(j) ⊆ Y'... i.e., Y' ranges over subsets of Y containing Y \ adjA(j), within bits not in adjA(j)... The number of such Y' is 2^{popcount(Y & adjA(j))}. Total work: sum over Y of 2^{|Y ∩ adj(j)|} = 2^{|adj(j)|} * 2^{n1 - ...} hmm: sum over Y ⊆ A of 2^{|Y ∩ adj|} = (2^{n1 - |adj|}) * (sum over Z ⊆ adj of 2^{|Z|}) = 2^{n1 - a} * 3^a. With n1 = 23 and a up to 23: 3^23 = huge. No good in general. But wait — this is per B-vertex j, so total is even worse. No.

OK so enumeration of one side's independent sets is needed. Fine — numpy level-by-level enumeration is efficient. Let me now also double check the sizes: worst case m = 0 (empty graph): all 2^{23} subsets of B are independent, all 2^{23} of A. The enumeration handles it. But note: if the graph is empty, α = n ≥ k always — we could special-case trivial situations to speed up, but the general code should handle it anyway. Actually, hmm, worst case for the enumeration is empty graph on B — 8.4M sets, each with F = 0. Fine.

But wait, there's a potential optimization: if m = 0, answer is trivially YES with any k vertices. More generally, quick checks: if the greedy finds an independent set of size ≥ k, done. E.g., a maximal independent set via greedy might already have size ≥ k in many cases. But worst case still needs the full computation. Adding a greedy precheck doesn't hurt. Also, a simple bound: α ≥ n^2/(2m+n) (Turán/carousel bound) — if that's ≥ k, answer YES immediately (but we need to output an actual set! So bounds alone don't give the set; greedy gives a set). Caro-Wei bound: α ≥ Σ 1/(d_i + 1) — again no set. Greedy maximal independent set gives an actual set. So: run greedy; if size ≥ k, output. Else fall back to meet-in-the-middle. This handles sparse cases fast. Dense cases: the MITM runs on 46 vertices regardless — the cost doesn't depend on m much (worst when few edges). Hmm, so the fallback cost is the same. The greedy precheck only helps when it succeeds. Fine, cheap to add. Actually, also: if k=1, answer is always YES (single vertex, no self-grievances). Trivial.

Also note: the MITM cost is bounded by 2^{ceil(n/2)} for the DP and 2^{floor(n/2)} for the enumeration — independent of m. So worst-case runtime is fixed ~ a second or two with numpy. The greedy precheck is optional; maybe skip it for simplicity? It's cheap; include a simple version: greedy maximal independent set; if ≥ k, output. This will make many test cases fast, but the worst case is unchanged. I'll include it since it's easy.

Hmm wait, one more consideration: the B-side enumeration produces arrays of size = number of independent sets in B, which is ≤ 2^{n2} but could be 2^{23} = 8.4M. The final query g_A[A_full ^ F] is a gather of 8.4M elements — fine.

Then totals = size_B + query (uint8 + uint8 → careful, max total ≤ 46, fits uint8). argmax over 8.4M — fine. Then reconstruct.

Reconstruction of the best B set: we have its index in the final arrays and its mask (stored). Then F = F_array[idx], M_A = A_full ^ F, and walk g_A to reconstruct S_A. Wait — but actually we don't even need the walk if we use the direct DP with stored choices... no, walking is easy. Let me define the walk for the direct DP:

Given mask m (⊆ A) with g[m] = best size. Reconstruct set S:
- while m: v = lowest bit index of m. If g[m ^ (1<<v)] == g[m]: m ^= (1<<v). Else: S.add(v); m &= ~((1<<v) | adjA[v]).
This works: at each step, if excluding v achieves g[m], drop v; else v must be included (g[m] = 1 + g[m \ N[v]]), include it and recurse on m \ N[v]. Each iteration removes ≥ 1 bit, so ≤ n1 iterations. 

For the SOS-based g_A, the walk is: while True: find any bit v in m with g[m ^ (1<<v)] == g[m]; if found, m ^= (1<<v); else break. Then m is the independent set (g0[m] = g[m], and m independent with |m| = g). Wait, need m independent: g[m] = g0[m] means m is independent (or empty) and popcount(m) = g[m]. Hmm, but is popcount(m) = g[m]? g0[m] = popcount(m) if independent else 0. g[m] = g0[m] means either m independent with popcount = g[m], or g[m] = 0 and g0[m] = 0 (m not independent but max over submasks is 0 → only empty set... if g[m] = 0 then m must be... any single vertex is independent, so g[m] ≥ 1 for m ≠ 0. So g[m] = 0 ⟺ m = 0.) OK so the walk: repeatedly drop bits while g stays the same; end with independent m, |m| = g[original]. But this walk could be O(n1^2) bit tests — trivial.

Both fine. I'll pick the direct DP (with gather) since it's a single DP and the walk is simple. Actually wait, let me re-examine the direct DP vectorization once more, carefully.

Direct DP for g_A (max independent set size within mask), A = vertices 0..n1-1, adjacency adjA[v] = bitmask over A.

g = np.zeros(2^{n1}, dtype=uint8).
For v = n1-1 down to 0:
  stride = 1 << (v+1)
  cnt = 1 << (n1-1-v)
  # positions with lowest bit v: p(t) = (1<<v) + t*stride, t ∈ [0, cnt)
  # a[t] = g[t*stride]  (exclude v)
  # b[t] = g[(t & ~adjHigh) * stride] where adjHigh = adjA[v] >> (v+1)  (include v)
  # g[p(t)] = max(a[t], b[t] + 1)
  
  a = g[::stride]  # length: ceil(2^{n1}/stride) = 2^{n1-v-1} = cnt. ✓.
  
  For b: need idx = (t & ~adjHigh) * stride for t in [0, cnt). 
  t_arr: we can precompute np.arange(2^{n1-1}) once (max size needed is cnt_max = 2^{n1-1} for v=0) and reuse slices: t_arr = AR[:cnt].
  idx = (t_arr & ~adjHigh) << (v+1)  — hmm, (t & ~adjHigh) then shifted. Note ~adjHigh in Python: adjHigh is a Python int; ~adjHigh is negative (infinite two's complement) — but t & ~adjHigh with t ≥ 0 gives correct result (Python handles arbitrary precision two's complement for &). In numpy: t_arr & ~adjHigh — numpy will convert the Python int ~adjHigh to... if it's negative, numpy converts to array dtype; for int64, ~adjHigh as int64 is fine (two's complement), and & works correctly. But careful: adjHigh < 2^{n1} ≤ 2^23, so ~adjHigh = -adjHigh - 1, fits int64. t_arr & (−adjHigh−1): correct bitwise AND on two's complement = clears bits of adjHigh. ✓. Alternatively compute mask_keep = (~adjHigh) & ((1<<(n1-v-1)) - 1) as a positive Python int, then idx = (t_arr & mask_keep) << (v+1). Cleaner. 
  
  b = g[idx]  # fancy indexing gather.
  vals = np.maximum(a, b + 1)  # b+1: uint8 + 1 → uint8 (24 max, fine). Hmm, actually numpy: uint8 array + Python int 1: in newer numpy (NEP 50), result dtype uint8; value 24 fits. In older numpy, also uint8. Fine.
  g[(1<<v)::stride] = vals

Wait, but there's an issue: `a = g[::stride]` is a view of g. `b = g[idx]` is a copy. `vals = np.maximum(a, b+1)` new array. Then writing `g[(1<<v)::stride] = vals` — the write positions are disjoint from a's positions, and vals is already materialized. ✓.

But hmm, wait: is `a = g[::stride]` correct? Positions t*stride for t ∈ [0, cnt): g[::stride] gives g[0], g[stride], g[2*stride], ..., up to < 2^{n1}. Number: ceil(2^{n1}/stride) = 2^{n1}/2^{v+1} = 2^{n1-v-1} = cnt. ✓.

And g[(1<<v)::stride]: positions 2^v, 2^v+stride, ...: count = ceil((2^{n1} - 2^v)/stride) = ceil((2^{n1} - 2^v)/2^{v+1}) = 2^{n1-v-1} - ... let me compute: (2^{n1} - 2^v)/2^{v+1} = 2^{n1-v-1} - 1/2 → ceil = 2^{n1-v-1} = cnt. ✓.

Edge case v = n1-1: stride = 2^{n1}, cnt = 1. a = g[::2^{n1}] = [g[0]] = [0]. mask_keep = (~0) & ((1<<0)-1) = 0. idx = [0]. b = [g[0]] = [0]. vals = [1]. g[2^{n1-1}::2^{n1}] = [1]. ✓ (single vertex, no neighbors within A above it... adjHigh = adjA[n1-1] >> n1 = 0 ✓).

Edge case n1 = 0: 2^{n1} = 1, g = [0], no loop. ✓. Edge n1 = 1: v=0: stride=2, cnt=1: a = g[::2] = [g[0]] = [0]; adjHigh = adjA[0] >> 1 = 0; idx=[0]; b=[0]; vals=[1]; g[1::2] = [1] → g = [0, 1]. ✓.

Now the B-side enumeration. B = vertices n1..n-1, relabeled j = 0..n2-1 (global vertex n1+j). For each j: adjB[j] = bitmask over B (bits 0..n2-1) of neighbors of vertex n1+j within B; cross[j] = bitmask over A of neighbors of vertex n1+j within A.

Enumeration: 
masks = np.array([0], dtype=int32) — hmm, but n2 ≤ 23, masks fit in int32. 
Fs = np.array([0], dtype=int32) — F ⊆ A, A has ≤ 23 bits, fits int32.
sizes = np.array([0], dtype=uint8).

For j in 0..n2-1:
  adj = adjB[j]; bit = 1 << j; crossj = cross[j]
  compat = (masks & adj) == 0
  sub_masks = masks[compat]
  new_masks = sub_masks | bit
  new_F = Fs[compat] | crossj
  new_sizes = sizes[compat] + 1  (uint8 + 1 → fine, ≤ 23)
  masks = np.concatenate([masks, new_masks])
  Fs = np.concatenate([Fs, new_F])
  sizes = np.concatenate([sizes, new_sizes])

At the end: query = g_A[A_full ^ Fs] — wait, A_full ^ Fs: since Fs ⊆ A_full, A_full ^ Fs = A_full & ~Fs. ✓. But hold on — dtype: g_A is indexed by int; Fs is int32 array; A_full ^ Fs is int32 array; g_A[A_full ^ Fs] — fancy indexing with int32 array: fine.

totals = sizes.astype(int8?) + query — sizes uint8 + query uint8: max 23 + 23 = 46 < 255 ✓. totals = sizes + query (uint8). best_idx = argmax(totals). best_total = totals[best_idx].

If best_total ≥ k: reconstruct: S_B mask = masks[best_idx] (bits j → vertex n1+j). M_A = A_full ^ Fs[best_idx] (as Python int). Walk g_A to get S_A. Combine, take any k vertices, output.

Wait, but actually — do we even need to reconstruct via walking g_A? We could also just verify: we know best_total = size_B + g_A[M_A]. We need an actual independent set in A of size g_A[M_A]. The walk gives it. ✓.

Hmm, one more check on the walk with the direct DP: g[m] for m ⊆ A. Walk:
  S = []
  while m:
    v = (m & -m).bit_length() - 1
    if g[m ^ (1<<v)] == g[m]:
      m ^= (1<<v)
    else:
      S.append(v)
      m &= ~((1<<v) | adjA[v])
  Claim: |S| = g[original m]. Proof sketch: invariant g[m] unchanged... when we drop v: g[m^bit] == g[m], so g preserved. When we include v: g[m] = 1 + g[m & ~closed] (since g[m] = max(excl, incl) and excl < g[m]... wait, we know g[m ^ bit] < g[m] (they're not equal), and g[m] = max(g[m^bit], 1 + g[m & ~closed]) — is that right? The DP set g[m] = max(a, b+1) where a = g[m ^ bit] and b = g[m & ~closed]. So if g[m ^ bit] ≠ g[m], then g[m] = 1 + g[m & ~closed]. ✓. So each included vertex adds exactly 1 and g decreases by exactly 1 along the walk; when m = 0, g = 0. So |S| = g[original]. ✓. And S is independent: we only add v when the remaining m excludes N[v]... more precisely, when we add v, we remove all of N[v] from m, so subsequently added vertices are not adjacent to v. And vertices added earlier: when vertex u was added, we removed N[u] from m, so v (∈ N[u]? if adjacent) wouldn't be present... wait, v is added later, so at the time u was added, v might still be in m; but when v gets added, we check... hmm, let me re-verify independence: Suppose u added before v. When u was added, m became m & ~N[u], so v ∉ N[u] at that time — i.e., v is not adjacent to u (v ≠ u obviously). But wait, v was in m at the time u was added? Not necessarily — v could have been dropped... if v was dropped, it's never added later. If v is added later, v remained in m through all earlier steps, in particular v ∈ m when u was added, and after adding u, m excludes N[u], so v ∉ N[u]. ✓ Independent. 

Now, the sizes: is it possible that the walk's g lookups need g at masks we computed? All masks ⊆ A are computed. ✓.

Now let me reconsider performance of the B enumeration in the worst case (empty graph on B): 
- Level j: arrays of size 2^j. Operations: & (with scalar), ==0 (bool array), boolean indexing (3 arrays), | scalar, +1, concatenate (3). Total element-ops across levels: ~ 3 arrays * 2 * 2^{n2} = ~100M element ops? Hmm: sum over j of |level j| = 2^{n2} - 1 ≈ 8.4M; each level does ~10 array operations of size |level j| → ~84M element ops total, but in ~23*10 = 230 numpy calls. numpy does ~100-500M element ops/sec for simple ops. So ~0.3-1s. Plus boolean indexing which is slower (compress) — maybe another factor. Should be OK within 5s.

Memory at final level: masks int32 33.5MB, Fs int32 33.5MB, sizes uint8 8.4MB. During the last concatenate: old (16.8+16.8+4.2=37MB) + new selected (up to 37MB) + concatenated (75MB) → peak ~150MB. Hmm, plus g_A 8.4MB, plus t_arr/idx temporaries in the A DP (already freed). Plus the compat bool arrays (4MB each level). ~160MB peak. Under 256MB. But numpy memory fragmentation might push it. To be safer, we could:

- Use int32 for masks/Fs (already).
- Avoid keeping `sizes` as separate: compute sizes at the end via popcount of masks? popcount without np.bitwise_count: byte-table lookup: sizes = tbl[masks & 255] + tbl[(masks >> 8) & 255] + tbl[(masks >> 16) & 255] (n2 ≤ 23 → 3 bytes). That's computed once at the end on the final array (8.4M * 3 lookups + adds) — saves maintaining sizes through levels (saves 8.4MB final and per-level ops). Actually maintaining sizes per level is cheap; but dropping it saves memory and a few ops. Let me drop sizes and compute at the end via table. Actually, even better: we don't need sizes array separately — we need totals = popcount(masks) + g_A[A_full ^ Fs]. Compute popcount at the end. ✓.

- Also, do we need `masks` at all during enumeration? We need it for (a) the compat check (masks & adj == 0) and (b) final reconstruction of the best set. Both need masks. Keep it.

Alternatively, to halve memory: note that instead of storing F for every independent set, we could store... hmm, F is needed for the g_A query. Keep.

Another memory optimization: process the query incrementally? No — g_A query needs final F. Hmm, actually here's an idea: instead of storing F, store nothing extra and compute F at the end from masks: F = OR of cross[j] for j in mask. Vectorized: F = zeros; for j in 0..n2-1: F[masks & (1<<j) != 0] |= cross[j] — that's n2 passes over 8.4M arrays with boolean indexing — 23 * 8.4M = 193M element ops, slower than maintaining F. Keep F maintenance.

Alternatively reduce peak memory by deleting old arrays before concatenating: 
  new_masks = masks[compat] | bit — this creates selected copy; then masks = np.concatenate([masks, new_masks]); we can del intermediate. Peak at last level: masks_old (16.8MB) + new_masks (16.8MB) + result (33.5MB) = 67MB for masks; same for F: 67MB; total ~134MB + g_A 8.4 + misc. OK ~150MB. Fine.

Hmm, wait — actually, is there a smarter way for the B side that avoids storing all independent sets? Standard MITM for max independent set stores all independent sets of one half (with sizes) and for the other half computes the DP g. We're doing that. The memory is inherent (~2^{23} entries). With int32 masks + int32 F = 67MB final. Fine.

Alternatively, we can flip: enumerate independent sets of A (the bigger half, 23) and DP on B (23). Same.

Hmm, wait, actually, let me reconsider: maybe we can avoid enumerating independent sets entirely by using the SOS trick on BOTH sides with the cross-edge condition handled cleverly. Let me think again...

We want max over independent S_A ⊆ A, independent S_B ⊆ B, no cross edges, of |S_A| + |S_B|.

Consider the combined mask space A × B — 2^{46}, too big. 

Alternative: For each independent S_B, we need g_A[A \ N_A(S_B)]. Define the function φ: {independent sets of B} → subsets of A, φ(S_B) = N_A(S_B). We need max over S_B of |S_B| + g_A[A \ φ(S_B)]. 

If we had, for each Y ⊆ A, the value c[Y] = max{|S_B| : S_B independent, N_A(S_B) ⊆ Y}, then answer = max over independent S_A of (|S_A| + c[A \ S_A]). And c is computed from base values via SOS-max: c[Y] = max over S_B with N_A(S_B) == Y' ⊆ Y. So we need d[Y'] = max |S_B| with N_A(S_B) == Y' exactly, then SOS-max to get c. But computing d requires enumerating independent sets of B (or a DP over subsets of B × subsets of A which is 2^{46}). Hmm, unless... 

Wait, actually here's a thought: d[Y'] = max over independent S_B with N_A(S_B) == Y'. Note N_A(S_B) = OR of cross[j] over j ∈ S_B. Hmm. What if we do a DP over B vertices where the state is (subset of B processed... no. State: (mask of B vertices used must be independent — but we track the neighborhood in A). DP over j = 0..n2-1 with state Y ⊆ A: D_j[Y] = max |S| over independent S ⊆ {0..j-1} with N_A(S) == Y. Transition: D_{j+1}[Y | cross_j] = max(D_{j+1}[Y | cross_j], D_j[Y] + 1) if vertex j compatible (no neighbors in S — but S's B-adjacency isn't tracked!). Problem: independence within B requires knowing S's B-mask. So state would need (S_mask, ...) — no. Unless we process B vertices in order and note that independence only depends on S... yeah we'd need the mask. Dead end. Enumeration it is.

Hmm, alternatively: swap which side gets enumerated vs DP'd based on which has fewer independent sets? The DP side costs 2^{n_side} regardless. The enumeration side costs #independent sets ≤ 2^{n_side}. If one half is dense (few independent sets), enumerate that side and DP the other. But both halves are ~23, cost similar. Fine as is.

Actually — wait. Here's a much better idea for reducing the enumeration side cost, the classic optimization: instead of enumerating all independent sets of B and querying g_A, we can enumerate independent sets of B but merge by "signature": many independent sets share the same F (neighborhood in A). We only need, for each F, the max |S_B|. But dedup costs too. Skip.

Let me also consider: maybe just implement the classic recursive MITM in pure Python but with the A-side DP done via the numpy-free... no. Let me just go with numpy and include a pure-Python fallback? Hmm, how about I write the solution to try importing numpy, and if unavailable, fall back to a pure-Python MITM that might be slow but correct (best effort)? Or fall back to branch and bound? 

Actually, let me reconsider pure Python feasibility more carefully, because if pure Python can do it in ~5s, that's safer.

Pure Python MITM components:
1. g_A DP over 2^{23} masks: 8.4M iterations. With a tight loop:
   for v in reversed(range(n1)):
       stride = 1 << (v+1)
       keep = ~adjHigh & ((1 << (n1-1-v)) - 1)
       # for t in range(cnt): g[(1<<v) + t*stride] = max(g[t*stride], g[(t & keep)*stride] + 1)
   Using list-based operations: 
       a = g[::stride] (list slice — fast, C-level)
       b = [g[(t & keep) * stride] for t in range(cnt)] — Python-level loop, 8.4M total iterations across all v. Each iteration: index into range (t), & keep, * stride, list index. ~0.15-0.25 μs → 1.5-2.5s. Hmm.
       Then vals = list(map(max, a, map(inc, b)))? map with max over two lists — C-level but max is a function call per element... ~0.1μs each → 1s. 
       g[1<<v::stride] = vals — C-level slice assign. 
   Total A side: maybe 3-5s. Too slow already, before B side. 

   Optimization: precompute the index list per v? idx = [(t & keep) * stride for t in range(cnt)] — same cost. Hmm.

   Alternative for the gather: note (t & keep)*stride — the pattern t & keep: if keep has bits set, this is a "folded" pattern. We could compute b via slicing tricks: b[t] = g[(t & keep)*stride]. The map t → t & keep: if keep = 0 (v adjacent to all higher vertices... no wait, keep = complement of adjHigh — keep = 0 means v adjacent to ALL higher vertices), then b = [g[0]] * cnt — trivial. In general, the sequence (t & keep) for t = 0..cnt-1 is a "bit-interleaved" pattern that can be built from slices: hmm, think of it as: for the lowest bit of keep... This is like a Kronecker product structure. We could build the index array via list operations: start with [0], for each bit position i of keep (from high to low): new = old + [x + 2^i for x in old]? That builds t & keep for all t? No wait — (t & keep) for all t in order isn't built that way; the sequence t & keep for t = 0, 1, 2, ... is: it's t with some bits zeroed. As a sequence, it has recursive structure: for t in [0, 2^{w}): split by lowest bit... The sequence S_w (t & keep for t in [0, 2^w)) where keep over w bits: S_w = S_{w-1} followed by S_{w-1} + (keep_bit_0 ? 1 : 0)... no: t & keep for t in [2^{w-1}, 2^w) = (t - 2^{w-1}) & keep + (keep & 2^{w-1} ? 2^{w-1} : 0). Hmm, so S_w = S_{w-1} + [x + b for x in S_{w-1}] where b = keep's bit w-1. So we can build the full index list with doubling list comprehensions: total elements 2^w, built in w steps of C-level-ish comprehensions... each step creates a list of size 2^j via [x + b for x in old] — that's a Python-level comprehension per element: total element ops = 2^{w+1} ≈ same as direct. No win.

   OK pure Python A-side DP ~2-4s. B-side enumeration: 
   Level-by-level with lists: masks list, F list. compat check: [m for m in masks if not (m & adj)] — hmm, or use per-element. 8.4M elements, several ops each: another 3-6s. Total pure Python: 6-12s. Too slow for 5s limit (unless the judge's Python is fast... CPython 3.11+ is ~1.5-2x faster than 3.8 for such loops; still too slow).

So pure Python MITM is too slow. Options: (a) numpy; (b) branch and bound; (c) hybrid.

Let me think about branch and bound viability for n=46 in Python. Max independent set via complement max clique. Tomita's algorithm with greedy coloring bounds. For n=46, the search tree size: for random graphs, tiny. For adversarial graphs (like the 46-vertex instances designed to be hard for MITM — actually MITM has no adversarial cases, it's always 2^{23}; tests for this problem are probably just designed for MITM to pass in C++, meaning any graph). B&B worst case on 46 vertices: could be millions of nodes. In Python, ~50k-200k nodes/sec for a B&B with coloring... could time out.

Hmm. But actually, maybe combine: B&B with a good initial lower bound (from greedy + local search) and good upper bounds. For n=46... I recall that max clique algorithms handle n=46 easily for essentially all instances; the truly hard instances for B&B are structured (e.g., Steiner triple systems, Ramsey instances) at larger n (100+). At n=46, even Ramsey-type instances... Let me think: the hardest known instances around n=45-50 for max clique: e.g., random graphs near density ~0.9? Hmm. Actually for n ≤ 50, modern B&B explores at most maybe 10^5-10^6 nodes typically. In Python at ~10^5 nodes/sec (each node does coloring — expensive), that's 1-10s. Risky.

Alternatively: use MITM but with numpy, and if numpy import fails, fall back to B&B. That's belt and suspenders. But complexity of writing both... The answer must be one code block. I can write both: try numpy; if ImportError, use a pure-Python B&B (which will handle most cases, maybe all). Actually, you know, let me think about whether there's a pure-Python approach that's guaranteed fast enough...

Alternative pure-Python idea: use the MITM but with A-side DP implemented via bytes and translate/int operations? Hmm.

Wait — here's a cute idea for the A-side DP in pure Python using big integers as vectors! Represent the array g (values 0..23, but let's use 1 byte per value... or fixed-width nibbles?) as a big Python int (bit-packed). Operations: gather g[idx] for idx pattern... big-int operations don't support gather. Hmm. But some DP recurrences can be done with shifts/masks on packed representations. The recurrence g[m] = max(g[m ^ lowbit], g[m \ N[lowbit]] + 1) — the "max" and "+1" on packed arrays: max of packed byte arrays isn't a bit operation. Could pack values as unary/bitset columns: represent g as 24 big integers, where bit m of G_i is 1 if g[m] ≥ i... hmm wait, better: G_i[m] = 1 iff g[m] ≥ i? Then max(g1, g2) at each position = OR of... g = max(a, b): the bits: G_i = A_i | B_i. And +1: shift the threshold: (g+1 ≥ i) ⟺ (g ≥ i-1) ⟺ G_{i-1}. So packed column representation: 
- g[m] = max over i of ... g[m] = Σ_i G_i[m] if G is a "threshold" representation (G_i = 1 iff g ≥ i, nested: G_1 ⊇ G_2 ⊇ ...). Then max(a,b) columnwise = A_i | B_i (still nested ✓). a+1 columnwise: C_i = A_{i-1} (with A_0 = all ones). 

So the DP: for each v: for masks with lowbit v: g = max(g_excl, g_incl + 1) where g_excl[m] = g[m ^ 2^v] and g_incl[m] = g[m & ~closed_v]. 

The "gather" g[m ^ 2^v] for all m with lowbit v: this is a permutation of a slice... In packed big-int representation: we need, for positions m = 2^v + t*stride, the value g[t*stride]. If we extract the sub-array of g at positions ≡ 0 mod stride (i.e., g restricted to masks with bits < v+1... hmm wait positions t*stride = t * 2^{v+1}: these are masks whose low v+1 bits are 0). Extracting every (2^{v+1})-th byte from a packed byte array: with big ints, we can mask with a pattern and shift: bytes at positions multiple of stride: mask = repeating pattern (1 byte every stride bytes). Extract: X & M where M has 0xFF at those byte positions → then the extracted bytes are spread out; to compact them, we'd need... compaction of every-stride bytes is not a simple shift. Hmm, but wait — maybe we don't need to compact! Let's see: we want to compute new values at positions 2^v + t*stride from values at positions t*stride and (t&keep)*stride. If we keep everything "in place" (spread), the operations are: 

Let me define the packed int G_i (i = 1..24), each 2^{n1} bytes... wait, positions are masks 0..2^{n1}-1, each position holds a bit in G_i. So G_i is a big int with 2^{n1} bits. Bit m of G_i = [g[m] ≥ i].

Recurrence for masks with lowbit v (call this set P_v = {2^v + t*stride}): 
new_g[m] = max(g[m ^ 2^v], g[m & ~closed_v] + 1) for m ∈ P_v.

In threshold representation: New_i [m] = Old_i[m ^ 2^v] | Old_{i-1}[m & ~closed_v] for m ∈ P_v (with Old_0 ≡ all-ones on valid positions... careful: g_incl + 1 ≥ i ⟺ g_incl ≥ i-1; for i = 1: always true (g ≥ 0), so New_1[m] = 1 for m ∈ P_v — indeed g[m] ≥ 1 for m ≠ 0 ✓).

Now, the operations on big ints: for each i, we need to compute bits at positions P_v from bits at positions Q0 = {t*stride} and Q1 = {(t&keep)*stride}. 

Bit m = 2^v + t*stride needs Old_i[t*stride] and Old_{i-1}[(t&keep)*stride].

Hmm, the position mapping m ↔ t*stride: m = t*stride + 2^v. So bit position m in the big int corresponds to bit position t*stride in the source. If we shift the big int right by 2^v, then bit t*stride + 2^v of Old = bit t*stride of (Old >> 2^v). So: New_i gets, at positions {t*stride} (after shifting back)... let me redo:

Define S_i = big int with bit t (for t ∈ [0, cnt)) = Old_i[t*stride]. I.e., the "compressed" array over t. Then New at position m = 2^v + t*stride should be S_i[t] | S'_{i-1}[t] where S'_{i-1}[t] = Old_{i-1}[(t&keep)*stride].

If I can build the compressed S_i (cnt bits) for each i, then New_i (compressed) = S_i | S'_{i-1}, and then I need to "expand" back: set bits at positions 2^v + t*stride in the full array according to compressed bit t. Expansion: positions 2^v + t*stride — the compressed bit t goes to position 2^v + t*stride = 2^v*(2t+1). Hmm, expansion by interleaving: given compressed bits c_t, place them at positions 2^v*(2t+1). This is a "spread with stride 2^{v+1}, offset 2^v" operation. With big ints: if C = Σ c_t 2^t, then Σ c_t 2^{2t+1}... wait positions in bits: position p = 2^v + t*2^{v+1} = 2^v (1 + 2t). So Expand(C) = Σ c_t 2^{2^v(2t+1)} = 2^{2^v} * Σ c_t 2^{t·2^{v+1}} = 2^{2^v} * "spread C with stride 2^{v+1}". Spreading bits with stride s: Σ c_t 2^{t·s} — this is not a simple shift... but it can be done by interleaving: spread with stride 2^{v+1} means inserting 2^{v+1}-1 zeros between consecutive bits. There's a classic trick: spreading by factor 2 via masks: x = (x | (x << k)) & mask pattern... Spreading by factor s = 2^{v+1}: can be done in v+1 doubling steps: each step doubles the spread: y = x; spread 1→2: y = (y & m1) | ((y & ~m1... hmm, standard bit-interleave via "space insertion": to insert one zero between bits: x = (x | (x << 1)) & 0x5555...? No wait: inserting zeros between bits: given bits at positions 0,1,2,..., produce bits at 0,2,4,...: x_spread = (x | (x << 1))? Let me think: x has bits at positions t. Want bits at 2t. Trick: x = x & 0x5555...? Hmm: Let x = Σ c_t 2^t. Then Σ c_t 2^{2t}: take x, and for each pair of bits... Standard: y = x; y = ((y & 0x...)) — the "Morton number" trick: spreading bits uses masks like 0x5555 for 1→2 spread: x = (x | (x << 1))?? Let me test: x = 0b1011 (bits 0,1,3). Want 0b100101 (bits 0,2,6). Hmm, the standard trick to spread bits by factor 2: 
  x = (x | (x << 1)) & 0x55555555? No — that's for compacting. Let me think: to spread: first, separate even and odd... Actually the classic: "interleave bits by one zero": 
  x = ((x & 0x55555555) ...) hmm I recall: spread: x = (x | (x << 8)) & 0x00FF00FF for 16-bit... The pattern: to spread by 2: 
  Step: x = (x | (x << 1)) — no. Let me just think directly: we want f(x) = Σ c_t 2^{2t}. Write x = Σ c_t 2^t. Consider x * (2^0 + ...)? No. 

  Alternative: binary decomposition: f(x) = Σ_t c_t 4^t. Hmm, this is evaluating the binary digits of x as base-4 digits. There's a doubling algorithm: to convert base-2 digits to base-4: insert a zero bit between every bit. Inserting zeros between bits of a w-bit number: 
  x = (x | (x << 1)) & mask? Test with x = 0b1: want 0b01. x<<1 = 0b10, or → 0b11. Wrong.
  Correct approach: split into halves recursively: spread(x) for 2w bits from w bits: spread(x) = spread(low half) | (spread(high half) << 2w)? That's just the definition — computing it requires per-bit work unless we use the mask trick: 
  The known trick (from "Morton codes"): to interleave/spread, you use: 
  x = (x | (x << 8)) & 0x00FF00FF; — hmm this spreads bytes apart by factor 2? Let's verify: x has bits 0..7 (call them b0..b7 in bytes...). Hmm, the standard sequence for spreading 16 bits to 32 with zeros interleaved:
  x = (x | (x << 8)) & 0x00FF00FF? Hmm wait that's for... Let me look at it differently. Known: "space out bits": 
  x = ((x & 0xFF00) << 8) | (x & 0x00FF) — spreads 16-bit into two bytes at distance 16... 

  Actually the standard Morton trick: to spread bits of x into even positions: 
  x = (x | (x << 16)) & 0x0000FFFF0000FFFF — no...

  OK here's the correct classic (from Hacker's Delight, "spread bits apart" / interleave): To interleave x with zeros (i.e., bits to even positions), for 16-bit x → 32-bit result:
  x = (x | (x << 8)) & 0x00FF00FF? Hmm no. Let me derive: we want each bit at position t to move to 2t. Equivalently insert a 0 after each bit. Doubling approach: given number with bits in the low half positions... 

  Derivation: Let x have bits b_0..b_{w-1}. Want y with bits at 0,2,4,...,2w-2. 
  Step 1: split x into even-indexed bits and odd-indexed bits: E = x & 0x5555..., O = x & 0xAAAA... Then y = spread(E) ... hmm recursive.

  The actual known trick: y = x; then for shifts: y = ((y & m1) | ((y & ~m1) << 1))? Hmm: consider moving odd-indexed bits up by 1: bits at positions 1,3,5,... move to 2,4,6? No wait: we want bit t → 2t. Odd bits: bit 1 → 2: shift by 1. Bit 3 → 6: shift by 3. Not uniform. So single shift doesn't do it; need log steps: 
  Standard: to spread by 2 (insert one zero between bits), for 16 bits:
  x = (x | (x << 8)) & 0x00FF00FF — hmm let me test on small: this operates on bytes: byte0 stays, byte1 moves to byte2. So bits 8-15 → 16-31, bits 0-7 stay at 0-7. That's spreading bytes by factor 2 (with zeros in bytes 1,3). Then next: x = (x | (x << 4)) & 0x0F0F0F0F: spreads nibbles. Then (x | (x << 2)) & 0x33333333: spreads bit-pairs. Then (x | (x << 1)) & 0x55555555: spreads individual bits. Yes! That's the classic. Each step: 3 big-int ops (or, and, shift) on numbers of size up to 2× previous. Total for spreading by 2^{v+1}: v+1 rounds of this (spread by 2 each round), each round 3 ops on ints of size ~2^{n1} bits... wait, the compressed array has cnt = 2^{n1-v-1} bits; after full spread it's 2^{n1} bits. The intermediate sizes double each round. Total work per spread op: sum of sizes ≈ 2 × final size = 2^{n1+1} bit-ops... but Python big-int ops are word-level (30-bit digits), so ~2^{n1+1}/30 word ops ≈ 560k word-ops per spread. Times 24 threshold levels (G_i) times 23 values of v... hmm wait, that's per (i, v) pair: 24 * 23 = 552 spread operations, each ~2^{n1+1} bits of work → 552 * 16.8M bit-ops = 9.3G bit-ops / 30 per word = 300M word ops. Python big-int ops run at maybe 100-500M word-ops/sec... ~1-3s. Hmm, plus the compaction (gather) side which is the reverse (compacting every stride-th bit) — similar cost via the reverse Morton trick. Plus the OR/AND per (i,v): 24*23*3 ops on 2^{n1}-bit ints = 1584 * 8.4M bits = 13G bit ops = 440M word ops. Hmm, total maybe 3-8s. Too slow, and very complicated. Scrap that.

OK, decision: go with numpy as the primary implementation. It's the standard for "efficient Python" on judges. Most judges that accept Python for competitive programming have numpy. Given the problem explicitly asks for Python 3 solution and 5s limit (generous, suggesting they expect slower languages/Python), numpy MITM should be fine.

Hmm, wait, actually — hold on. Let me reconsider the problem source. "Problem A — Harmonious Delegation", n ≤ 46, 5s, 256MB. This smells like a problem designed so that 2^{23} × something fits. The 5s time limit is generous — maybe intended for Python MITM? If the judge intended Python solutions, numpy may or may not be available. A pure-Python solution that runs in, say, 3-4s would be ideal. Let me think harder about pure-Python optimization.

Pure Python MITM, refined plan:

Side A DP (g over 2^{n1} masks): the bottleneck is the gather b[t] = g[(t & keep)*stride]. 

Alternative A-side formulation avoiding gather — the SOS approach:
1. ind[m] for all m: ind[m] = 1 if m independent. Recurrence: for v = lowbit: ind[m] = ind[m ^ 2^v] AND (adj[v] & m == 0). Vectorized over t: ind[2^v + t*stride] = ind[t*stride] & ((t & adjHigh) == 0). The (t & adjHigh) == 0 term: for fixed v, this is a pattern over t. Can we compute the pattern [t & adjHigh == 0 for t in range(cnt)] quickly with slice ops? The indicator of "t & adjHigh == 0" as a list: it's 1 exactly for t ⊆ complement of adjHigh. The sequence over t = 0..cnt-1: recursive structure: for the lowest bit of t: first half (t < cnt/2) is pattern for cnt/2 with adjHigh's higher bits; second half = first half ANDed with [adjHigh's bit (w-1) == 0]... i.e., if bit (w-1) of adjHigh is set, second half is all zeros; else second half = same as first half. So the pattern list P_w can be built by doubling: P = [True]*(2^{z}) where z = number of leading zero bits... Let me define: build the list L = [ (t & adjHigh)==0 for t in range(cnt) ] via: L = [1]; for bit position b from 0 to w-1 (t's bits from low to high): if adjHigh has bit b: L = L + [0]*len(L) else: L = L + L. Each step is a list concatenation (C-level fast!). Total elements built: 2^w = cnt. Across all v: total = 2^{n1} elements built via ~n1 concatenations per v → 23*23 = 529 concatenations, total elements 8.4M... wait, sum over v of cnt_v = 2^{n1}. So total elements copied = 2 * 8.4M = 16.8M via C-level list concat — fast (~0.1-0.2s). 

Then ind update: ind[2^v::stride] = [x & y for x, y in zip(ind[::stride], L)] — zip + comprehension: 8.4M total elements across all v, each ~0.1μs → ~1s. Hmm. Or use map(operator.and_, a, L) — map with operator.and_ is C-level per element but still ~50-80ns/elem → 0.5s. Then slice assignment (C-level). 

Hmm, alternatively, we can compute ind[] differently: ind[m] = 1 iff m & (OR over v∈m of adj[v]) == 0... no. Or: m independent iff for all v ∈ m: adj[v] & m == 0. Hmm.

Actually, wait. Let me reconsider — maybe there's a slicker way to compute g_A (max ind set size per mask) in pure Python using the ind[] array and SOS-max... SOS-max is 23 passes over 8.4M-element lists: g[2^i::2^{i+1}] = [max(x,y) for x,y in zip(g[2^i::2^{i+1}], g[::2^{i+1}])] — hmm wait, that's wrong: SOS needs g[m] = max(g[m], g[m ^ 2^i]) for m with bit i — reading g[::stride] gives g[m ^ 2^i] for m = 2^i + t*stride ✓, and writing to g[2^i::stride] ✓. But the read must be the values BEFORE this pass — since we write only to positions with bit i set and read from positions with bit i clear, no aliasing within the pass ✓. Each pass: slice read (C-level), zip+max comprehension (Python-level per element: ~80-150ns), slice write (C-level). Total elements: 8.4M per full SOS... wait no: pass i touches 2^{n1-i-1} elements; sum over i = 2^{n1} - 1 ≈ 8.4M. So SOS-max total: 8.4M comprehension elements ≈ 0.7-1.2s. Plus ind computation ~0.5-1s. Plus popcount-multiply for base g0: g0 = [popcount(m) if ind[m] else 0] — popcount for all 8.4M masks: hmm, popcount via int.bit_count() (Python 3.10+) per element — 8.4M calls ~1-2s. Or build popcount list via doubling: pc = [0]; for b in range(n1): pc = pc + [x+1 for x in pc] — C-ish comprehension, 8.4M elements total, ~0.5s. Then g0 = [p if i else 0 for p, i in zip(pc, ind)] — another 8.4M comprehension ~0.8s. Hmm, adding up: ind ~0.7s + pc ~0.5s + g0 ~0.8s + SOS ~1s = ~3s. And that's just side A. Side B enumeration in pure Python: 

Level-by-level: masks list, F list. Per level: 
  sel = [i for i, m in enumerate(masks) if not m & adj] — hmm, or build new lists directly: 
  nm = [m | bit for m in masks if not m & adj] — comprehension with condition: per element ~100-150ns. 
  nf = [f | crossj for f, m in zip(F, masks) if not m & adj] — hmm, zip with condition — need paired comprehension: [(m|bit, f|crossj) for m, f in zip(masks, F) if not m & adj] then unzip — or two passes. 
  masks = masks + nm; F = F + nf. 
Total elements across levels: 2 * 2 * 8.4M = 33M comprehension element-ops ≈ 3-5s. 

Then final: query = [g[A_full ^ f] for f in F] — 8.4M gather + xor ~1.5-2s; totals & argmax: totals = [q + popcount... wait we need sizes: sizes via popcount of masks: another 8.4M ~1.5s; argmax via max(range(...), key=...) — slow. Better: best = max(zip(query, sizes))? Hmm, or compute totals list then max(totals) then .index — a few more 8.4M passes ~1s each.

Total pure Python: ~10-15s. Too slow for 5s. Unless the judge uses PyPy... The problem says Python 3; if it's PyPy, pure Python MITM would run in ~1s. But we can't count on PyPy.

Hmm, so pure CPython without numpy seems infeasible for the worst case (n=46, near-empty graph). With numpy: ~1-2s total. 

Let me now also double-check: is the worst case really 2^{23} independent sets? If the graph has no edges, greedy immediately finds an independent set of size n ≥ k → output immediately. So the MITM only runs when greedy fails to find size ≥ k. When does greedy fail? Greedy maximal independent set has size ≥ n/(Δ+1) ≥ n^2/(2m+n). For greedy to fail to reach k, we need the graph fairly dense: n^2/(2m+n) < k → m > (n^2 - kn)/(2k)... For k large and n=46: e.g., k = 23: m > (2116 - 1058)/46 = 23. Hmm, so even moderately dense graphs force the MITM. But dense graphs have FEW independent sets! The number of independent sets in the B-half is at most... for a graph on 23 vertices with edge density p, the expected number of independent sets is Σ C(23,s) (1-p)^{s(s-1)/2}. For the enumeration to have 8.4M sets, B must be very sparse (like < a handful of edges). But if B is sparse, then... hmm, but the graph could be structured: B sparse (many independent sets) but A dense such that the max independent set is small and k is just above what greedy finds. E.g., adversarial: B = empty graph on 23 vertices (8.4M independent sets), A = complete graph (α(A) = 1), cross edges arranged so that... max independent set = max over S_B of |S_B| + g_A[A \ N(S_B)]. With A complete: g_A[nonempty] = 1, g_A[0] = 0. If some B vertex has no neighbors in A: then taking that vertex alone... hmm, the max would be |S_B| + (1 if A \ N(S_B) nonempty). With B empty and cross edges: every S_B allowed; N(S_B) = union of cross neighborhoods. Max = max(|S_B| + [A \ N(S_B) ≠ ∅]). If all B vertices have full cross neighborhoods... then any nonempty S_B blocks all of A: max = max(23 + 0, 0 + 1) = 23. And greedy on the whole graph: greedy picks vertices... might find 23 easily (pick all of B — but greedy might pick A vertices first). Hmm, greedy order matters. Anyway, such adversarial cases make the enumeration 8.4M — the numpy path handles it in ~1s. Pure Python would take 10s+. So numpy it is.

But hmm, wait: maybe I should ALSO add the greedy precheck + a simple B&B to catch most cases, and use numpy MITM as the workhorse. If numpy is missing, fall back to pure-Python MITM (slow but correct — might TLE on worst cases, but at least correct). Or fall back to B&B. I think: primary = numpy MITM; fallback (no numpy) = pure-Python MITM optimized as much as possible (with greedy precheck to skip easy cases). Actually, for the fallback, maybe B&B is better than pure-Python MITM? B&B in pure Python for n=46: for the adversarial case above (B empty, A complete, cross full): B&B would... max independent set = 23 (all of B). B&B with coloring bounds would find it fast? The complement graph: B is a clique of 23 in complement... max clique in complement = 23 (B) — B&B on complement: greedy coloring gives B as a clique immediately → found in first descent. Probably fast. Hard instances for B&B at n=46 exist but are exotic. Honestly, for a fallback, B&B is likely faster in practice than pure-Python MITM, but MITM is guaranteed-ish. Ugh.

Let me just decide: I'll write the numpy MITM as the main solution, and wrap it: if numpy import fails, run a pure-Python MITM (best-effort, with the greedy shortcut first). Actually, you know what? Let me simplify: I'll write the solution with numpy, and if numpy is unavailable, use a carefully optimized pure-Python MITM. The code will be long but fine.

Hmm, actually, wait. Let me reconsider the pure-Python MITM cost once more, with tighter engineering, because if I can get it under ~4s, I could skip numpy entirely and be judge-agnostic.

Pure-Python MITM, refined:

Side A: compute g_A via the direct DP but restructure to minimize Python-level per-element work.

Actually — alternative side-A approach: enumerate independent sets of A directly (not all masks), and build g_A via... no, g_A needs all masks.

Hmm, what about flipping the roles to make BOTH sides enumerations with a hash-join? Classic alternative MITM for max independent set: enumerate independent sets of A (list1: (F_B = neighborhood in B, size)) and independent sets of B (list2: (mask_B, size)), then for the join we need max over pairs with compatible... that's the "for each S_A, need max |S_B| over S_B ⊆ B \ N_B(S_A)" — which is g_B[B \ N_B(S_A)] — again a DP over B masks. Symmetric. No.

What about the sorting trick: enumerate independent sets of A with (N_B(S_A), |S_A|) — sort by |S_A| desc; enumerate independent sets of B... for each S_B, find the first S_A in sorted order with N_B(S_A) ∩ S_B = ∅ — no index structure helps; worst case O(|list1| * |list2|). No.

OK so side A must be the full-mask DP (2^{n1} entries). The DP with gather: per element: compute (t & keep)*stride (2 int ops) + list index + max + ... Let me think about how to do the whole per-v update with minimal Python-level ops using map and list builtins:

for v in reversed(range(n1)):
    stride = 1 << (v+1)
    base = 1 << v
    keep = (~adjA[v]) & ((1 << (n1-1-v)) - 1)   # over t-bits
    cnt = 1 << (n1-1-v)
    a = g[::stride]                      # C-level slice
    if keep == 0:
        b = [g[0]] * cnt                 # C-level! (v adjacent to all higher)
    else:
        # b[t] = g[(t & keep) * stride]
        b = list(map(g.__getitem__, map(keep.__and__, range(cnt))))  # hmm: (t & keep) * stride — need the *stride too.
        
Hmm, the multiply by stride: (t & keep) * stride. Can I avoid it? Alternative: precompute a "strided getitem": define getter = lambda i: g[i * stride]... Or: note that g[::stride] is a list `a_full` where a_full[t] = g[t*stride]. Then b[t] = a_full[t & keep]! Because g[(t&keep)*stride] = a_full[t & keep]. So b = list(map(a_full.__getitem__, map(keep.__and__, range(cnt)))). Two chained maps + list() — all C-level dispatch, per element: range iteration, int & int (small ints), list getitem, append. Maybe ~60-100ns per element. Total 8.4M → 0.5-0.8s. 

Then vals = list(map(max, a, b_adjusted)) where b_adjusted = [x+1 for x in b] — hmm, +1 per element: map((1).__add__, b)? That's C-level: ~40-60ns/elem. Then vals = list(map(max, a, map((1).__add__, b))) — max via map: max is a builtin taking two args — map(max, a, binc) calls max per element: ~80-120ns/elem. Then g[base::stride] = vals — C-level.

Total side A: ~8.4M * (0.08 + 0.06 + 0.1) μs ≈ 8.4M * 0.25μs ≈ 2s. Hmm. Still 2s. Plus side B ~3-4s. Total ~6s. Over budget for CPython, OK for PyPy. 

Can we shave side A more? Idea: combine ops: vals = list(map(max, a, map((1).__add__, map(a_full.__getitem__, map(keep.__and__, range(cnt)))))) — the maps chain lazily; list() drives everything. Per element: ~4 C-function calls + int ops. CPython function call overhead ~50-80ns each → ~250-350ns/elem. Hmm, similar.

Alternative: avoid the +1 by pre-incrementing? Note the recurrence: g[m] = max(g_excl, g_incl + 1). What if we store h[m] = g[m] and compute differently... no.

Alternative: process side A with the ind/SOS approach where the per-element op is simpler? SOS-max pass: g[bit::stride] = list(map(max, g[bit::stride], g[::stride])) — per element: 2 slice reads (C), map(max) (~100ns), slice write (C). Total SOS: 8.4M * ~0.15μs = 1.2s. ind DP: ind[bit::stride] = list(map(int.__and__... hmm, we need ind_new[t] = a[t] & pattern[t] where pattern = [t & adjHigh == 0]. Building pattern via doubling concatenations (C-level, fast). Then map(operator.and_, a, pattern) ~80ns/elem → 0.7s. popcount list via doubling: pc = pc + [x+1 for x in pc] — comprehension per element ~40-60ns → 0.5s. g0 = [p if i else 0 ...]: hmm — alternative: g0 = list(map(operator.mul, pc, ind)) — since ind is 0/1: mul gives p*ind ✓. ~60ns/elem → 0.5s. Total side A (SOS variant): 0.7 + 0.5 + 0.5 + 1.2 ≈ 3s. Worse than direct DP (~2s). 

Hmm what about a completely different side-A approach: note that we don't need g_A for ALL masks — we only need it queried at masks A_full ^ F for F values that arise. But F values arise from all independent S_B — could be all sorts. No.

Alternatively — reduce n1! The split doesn't have to be 23/23. The cost: side A DP = 2^{n1}, side B enumeration = (#independent sets in B) ≤ 2^{n2}. If we split 20/26: side A = 1M (fast even in pure Python: ~0.25s), side B ≤ 2^{26} = 67M — way too many. 23/23 is the balance point: 8.4M each. Total pure-Python ~5-7s. Borderline. With CPython 3.11+ (faster), maybe 4-5s. Risky.

Alternatively, hybrid split: side A = 23 with numpy... no wait, if numpy is available everything is numpy.

Let me step back. Decision: 
- Primary: numpy MITM. Fast (~1-2s worst case), safe.
- Fallback without numpy: pure-Python MITM with all the C-level tricks (map/slices), plus greedy precheck. Might pass in ~4-6s on CPython worst case; likely passes on PyPy instantly. It's a fallback anyway.

Actually, hmm, wait. Let me reconsider the fallback: maybe make the fallback smarter: greedy precheck + local search (e.g., a quick heuristic like simulated annealing or iterated greedy) to often find size ≥ k quickly, then MITM only when needed. But when MITM is needed, it's the worst case anyway. The fallback is best-effort. Fine.

Actually, let me reconsider whether to even include a fallback. The instructions: "You write correct, efficient Python 3 solutions." Judges running Python almost certainly have numpy (Codeforces, AtCoder, CSES... CSES has numpy? CSES supports Python but I'm not sure about numpy — I believe CSES does NOT have numpy! Hmm. CSES's Python is plain. But this problem doesn't look like CSES (CSES problems have specific format). The format with "Problem A", examples with **Input**/**Output** — could be from a university contest (e.g., SWERC, or an ICPC regional). ICPC judges (Kattis) — Kattis has numpy for Python 3. Yes, Kattis Python 3 includes numpy. Time limit 5s and n ≤ 46 — hmm.

Given uncertainty, including a pure-Python fallback is prudent. But it doubles the code. Let me think about whether the pure-Python fallback can be made fast enough to just be THE solution (no numpy at all), simplifying to one path... From estimates: side A ~2s, side B ~3-4s, final join ~2s → 7-8s. Too slow. With numpy: everything comfortable. So: numpy primary + python fallback. OR: numpy primary + B&B fallback. 

Hmm, let me estimate the B&B fallback quality. A decent MIS via complement max-clique B&B with bit masks: for n=46, using the standard "expand with coloring bound" (Tomita/MCS): each node: greedy coloring of the candidate set (O(n^2/64) with bitsets or O(n^2) with masks — in Python with ints as bitsets, coloring ~ n iterations each with bit ops — ~46*46 = 2100 int-ops per coloring, ~50-100μs per node?). Nodes: typically hundreds to thousands for n=46; worst case maybe 10^5-10^6 → 5-100s. Risky but it's a fallback. Alternatively the fallback could be MITM-pure-python. I'll go with pure-Python MITM as fallback since it has guaranteed bounds (2^{23} * small constant), and just accept it might be ~6-8s on CPython worst case (but such worst case requires the adversary to defeat greedy AND have huge independent-set counts in B... note: if greedy fails, the graph is somewhat dense overall, but B could still be sparse as shown). Hmm.

Hmm, hold on, wait. Let me reconsider the problem constraints once more: m ≤ n(n-1)/2, and the interesting observation: the answer is NO only when α < k. Let me think about when MITM is truly needed with all optimizations:

1. If k == 1: YES always (any single vertex). 
2. Greedy maximal independent set: if size ≥ k → YES.
3. Also quick upper bound check: if a cheap upper bound on α < k → NO fast? Upper bounds: α ≤ n - matching... hmm, α ≤ n - ν (max matching size)? No: α ≤ n - ν where ν = max matching (each matching edge kills at least one endpoint... actually α ≤ n - ν since independent set contains ≤ 1 endpoint per matching edge). Computing max matching (blossom) is heavy. Simpler: α ≤ min over... eh. Skip.

These shortcuts handle easy cases; hard cases go to MITM. Fine.

Now, let me also reconsider: maybe there's an entirely different guaranteed-fast-in-Python algorithm for "does α ≥ k" with n=46... 

Hmm, what about a randomized approach: e.g., for the decision "α ≥ k", use Karp's / color-coding? No. 

What about the "exactly k" structure: we need an independent set of size exactly k. Meet in the middle over... hmm, alternative MITM for exact-size independent set: split A/B; enumerate independent sets of A of size ≤ k... no, sizes up to 23 each, same thing.

OK let me also sanity-check the numpy approach's total runtime budget:

Side A DP (n1 = 23, 2^23 = 8.4M uint8 array):
- 23 iterations; iteration v: arange reuse (precomputed AR = np.arange(2^{n1-1}, dtype=int64) — 4M * 8 bytes = 33MB, hmm, or int32: 16MB. idx values up to 2^{23} — fits int32 ✓. Precompute AR32 = np.arange(2^{22}, dtype=np.int32) = 16MB. For v=0, cnt = 2^{22} = 4.2M ✓ (n1-1-v = 22 → cnt = 2^{22}). Wait: cnt = 1 << (n1-1-v); for v=0: 1 << 22 = 4.19M ✓ = len(AR32) ✓.
- per iteration: t = AR32[:cnt]; idx = (t & keep) << (v+1) — hmm, (v+1) up to 23: t & keep < 2^{22}, << 23 → up to 2^{23}*... wait: (t & keep) << (v+1): t & keep < 2^{n1-1-v} = cnt; shifted by v+1 → < 2^{n1} ✓ fits int32 (2^{23}) ✓. But careful: numpy int32 << 23: values < 2^{22} << 23 = 2^{45}?? NO WAIT. t & keep: t ranges over [0, cnt) = [0, 2^{n1-1-v}), representing bits v+1..n1-1 of the mask. The actual mask bits: (t & keep) << (v+1) < 2^{n1} ✓. E.g., v=0: t < 2^{22}, t & keep < 2^{22}, << 1 → < 2^{23} ✓. v=22: t < 1, << 23 → 0 ✓. OK so idx < 2^{n1} = 8.4M ✓ int32 fine.
- b = g[idx]: fancy indexing with int32 indices — numpy handles. 4.2M elements max per call.
- vals = np.maximum(a, b); b+1: b+1 as uint8. Hmm: np.maximum(a, b+1): b+1 creates temp uint8 array. Fine.
- write g[1<<v::stride] = vals.
Total per-element work: ~8.4M * ~6 ops = 50M element-ops in ~100 numpy calls → well under 1s. 

Side B enumeration (n2 = 23):
- levels j=0..22; level sizes up to 2^22 before final concat to 2^23.
- per level: compat = (masks & adjB_j) == 0 → int32 & scalar → bool; sel = masks[compat] (compress); new = sel | bit; Fs_sel = Fs[compat]; newF = Fs_sel | cross; concat.
- element-ops: ~10 * 8.4M = 84M → ~0.5-1s (compress is slower-ish). OK.
- final: q = g[A_full ^ Fs] — wait, A_full ^ Fs: Fs int32, A_full Python int → array int32 ✓; fancy gather 8.4M → ~0.1s. sizes: popcount of masks: 3 byte-table lookups: t8 = np.array([bin(i).count('1') for i in range(256)], uint8); sizes = t8[masks & 255] + t8[(masks >> 8) & 255] + t8[(masks >> 16) & 255] — masks is int32; masks & 255 → int32; indexing t8 (len 256) with int32 array ✓ result uint8; sum: uint8 + uint8 → careful overflow: max 23 ✓ fine. 
- totals = sizes + q (uint8, ≤ 46 ✓). best = totals.argmax(); bestval = totals[best].

Then reconstruct & output.

Total numpy runtime: ~1-2s worst case. Memory: ~150-170MB peak. Hmm, memory is a bit concerning. Let me recount side B peak more carefully:

Final level construction (j = 22, the last): before: masks (2^{22} int32 = 16