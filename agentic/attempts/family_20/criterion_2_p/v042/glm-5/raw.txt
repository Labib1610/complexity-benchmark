This is the classic edge coloring of bipartite multigraphs problem. By König's theorem, the edge chromatic number of a bipartite multigraph equals the maximum degree Δ. We need to produce an edge coloring with Δ colors.

Constraints: nL, nR up to 100000, m up to 400000. Time limit 2 seconds. Need an efficient algorithm.

Standard approaches:

1. **König's edge coloring via repeated bipartite matching / augmenting paths**: The classic algorithm colors edges one at a time. For each edge (u, v), if there's a free color at both u and v, use it. Otherwise, do an "augmenting path" (Kempe chain) recoloring. This can be O(m Δ) worst case which could be 400000 * 400000... too slow in worst case? Actually Δ ≤ m, but also Δ ≤ nL + ... hmm, Δ ≤ min(nL, nR)? No, Δ is max degree, which can be up to min(nL, nR) if multigraph... wait, is it a multigraph? The problem says "tests" — could there be duplicate edges? The problem statement doesn't say edges are distinct. Hmm. "Next m lines: two integers u v: a test between transmitter u and receiver v." It doesn't say the tests are distinct. So it could be a multigraph. Δ could be up to m = 400000 in theory (if all tests are between the same pair... then Δ = 400000, and each edge gets a distinct color — trivial).

Actually with multigraph, Δ ≤ m. The augmenting path algorithm: for each edge, we do at most one Kempe chain traversal, which is O(Δ) per edge... Actually the standard algorithm: process edges one by one. For edge e = (u,v), find a color free at u (say color a) and a color free at v (say color b). If a == b, assign a. Otherwise, find the maximal alternating path (Kempe chain) starting at v using colors a and b, and swap colors along it. The chain traversal is O(length of chain) which can be O(m) in worst case... but amortized analysis shows total O(m log m)? Hmm, actually the standard complexity is O(m Δ) or with better implementations O(m log m)? Let me think.

Actually, there's a well-known approach: the Kempe chain argument. When we process edge (u, v), color a free at u, color b free at v, a ≠ b. Consider the maximal path starting at v alternating colors b, a, b, a, ... (each vertex has at most one edge of each color, so the path is unique). This path cannot end at u (because bipartite + parity argument: the path starting at v with color b... if it reaches u, then u would have an edge of color a or b, but a is free at u — contradiction... let me recall). Actually the standard argument: the alternating path starting at v with colors a,b: if it ends at u, then since a is free at u, the path must end with an edge of color a at u — but that contradicts a being free at u. Wait, the path could end at u with color b edge? Let me think: path alternates b, a, b, a... starting at v. If the path reaches u, the last edge into u has some color. If it's color a, contradiction (a free at u). If it's color b, then... hmm, actually in a bipartite graph, the parity works out: v is on the right side, u on the left. Path of length 1: v - (left vertex). Length 2: ends at right vertex. So paths starting at v (right side) end at left side on odd lengths and right side on even lengths. u is on the left side, so the path reaching u has odd length, meaning the last edge has color... path edges alternate starting with b: edge 1 = b, edge 2 = a, edge 3 = b, ... odd edges are b. So the last edge into u would be color b. Hmm, that's not immediately a contradiction. Wait, but then u has an edge of color b, and v has... hmm.

Let me redo: we want to swap colors a and b along the maximal alternating path starting at v. After swapping, b becomes free at v (so edge (u,v) can take color b), and we need a to remain free at u, or the path ends before reaching u so nothing changes at u. The standard argument: the maximal alternating path starting at v (with respect to colors a, b) either ends at some vertex other than u, or ends at u. If it ends at u, it must end with an edge of color a (since a is free at u, the path can't continue through u, and if it arrived via color b edge then u would have a b-edge, and then the path would continue? no...). Hmm, let me think again carefully.

Alternating path from v: v = x0, x1, x2, ... where edge (x0, x1) has color b, edge (x1, x2) has color a, edge (x2, x3) has color b, etc. Since each vertex has at most one edge of each color, the path is uniquely determined and simple. The path ends when the next edge doesn't exist.

Claim: the path cannot end at u. Suppose it ends at u = x_k. Since a is free at u, u has no edge of color a. The path ends at u means the edge (x_{k-1}, u) exists with some color c ∈ {a, b}, and u has no edge of the other color... wait no, the path ends at u means after arriving at u, there's no edge of the "next" color to continue. The next color after arriving at u: if edge (x_{k-1}, u) has color b, next needed is a — but a is free at u, so path ends. If edge (x_{k-1}, u) has color a — impossible since a free at u. So the path arrives at u via a b-colored edge. But x_{k-1} is on the left side (u is on right? wait).

Hold on: v is a receiver (right side), u is a transmitter (left side). Path: x0 = v (right), x1 (left), x2 (right), ... So x_k is on right for even k, left for odd k. u is on left, so k is odd, and edge (x_{k-1}, x_k) is edge k, which has color b if k odd (edges: 1=b, 2=a, 3=b, ...). So the path arrives at u via color b. Then u has an edge of color b. Hmm, so it's possible for the path to end at u? Then swapping would give u an edge of color a... wait no. Swapping colors a↔b along the path: edge colors b→a and a→b. The edge (x_{k-1}, u) with color b becomes color a. Then u has an edge of color a — but we wanted to color edge (u,v) with... hmm wait.

Let me restate the standard algorithm properly. Edge (u, v) uncolored. Let a = a color free at u, b = a color free at v. If a == b, color edge with a. Else, consider the maximal alternating path P starting at v with colors a and b (first edge color b... or a?). We swap a and b on P. After the swap, b is free at v (the first edge of P had color b, becomes a; wait, if the first edge from v has color b, after swap it's a, so v loses its b-edge and gains an a-edge; but b was free at v, meaning v had no b-edge... contradiction!).

Hmm, I mixed up. Let me redo: b is free at v. So v has no edge of color b. The alternating path from v must start with an edge of color a (v may have an a-edge). Path: x0 = v, edge (v, x1) color a, edge (x1, x2) color b, edge (x2, x3) color a, etc. After swapping a↔b on this path: v's a-edge becomes b-edge, so a becomes free at v. Hmm, but we want to free up... we want to color (u, v). We need a color free at both u and v. Currently a free at u, b free at v. If we swap along the path from v, then a becomes free at v (if v had an a-edge) — but wait, we need the color to also be free at u after the swap. If the path doesn't reach u, then u's colors unchanged, and a is still free at u, and now a is free at v → color (u,v) with a. If the path reaches u: u is on left, path position k odd, edge k color: 1=a, 2=b, 3=a,... odd = a. But a is free at u — contradiction. So the path can never reach u. 

So the algorithm: for each edge (u,v): find a color free at u and a color free at v. If same, assign. Else, find maximal alternating path from v starting with color a (the color free at u), swap a↔b along it, then color (u,v) with a.

Wait, but I need to double check the direction: we start from v with color a (free at u, possibly used at v). The path alternates a, b, a, b... After swap, a is free at v. And the path can't reach u (as shown). Also need: after swap, coloring is still proper (each vertex still has at most one edge of each color) — yes, because along the path each vertex's a-edge and b-edge get swapped; internal vertices of the path have both an a-edge and a b-edge on the path (or the path passes through them once with two edges). Actually a vertex could appear... the path is simple (alternating path in a proper coloring is simple: if a vertex repeated, it would have two edges of the same color). Endpoints: v loses its a-edge (gains nothing on path except being endpoint), the other endpoint either loses its b-edge or gains... hmm, the other endpoint x_k: if k even, edge k has color b (edges 1=a, 2=b, ..., even = b), and the path ends at x_k because x_k has no a-edge (k even means x_k on right side... wait x_k right for even k). Hmm, x_k ends the path because it has no edge of the next color. If k is even, next color is a, so x_k has no a-edge; after swap, its b-edge becomes a-edge — fine, still proper. If k is odd, next color is b, x_k has no b-edge; its a-edge becomes b-edge — fine.

OK so this is the standard Vizing-like/König edge coloring algorithm. Complexity: each edge insertion does one path traversal, path length can be O(m). Worst case O(m^2) = 1.6e11 — too slow. But in practice, paths are usually short. Hmm, but worst case matters.

Actually, there's a classical result: this algorithm (with appropriate choices) runs in O(m Δ)? Or there's a smarter approach.

Alternative approach: **Reduction to bipartite matching / flow**: Edge coloring bipartite graph with Δ colors = decomposing into Δ matchings. There's a classical divide-and-conquer: split colors into two halves, for each vertex, split its incident edges into two groups of sizes ⌈d/2⌉ and ⌊d/2⌋, and recursively... This is the "balanced edge coloring" approach. Actually there's a neat trick: 

**Approach via Euler splits / binary decomposition**: For bipartite multigraphs, we can find an edge coloring with Δ colors in O(m log Δ) using the following: recursively, given a graph with max degree Δ, split the edge set into two subgraphs with max degrees ⌈Δ/2⌉ and ⌊Δ/2⌋ (this can be done by Euler tours on each connected component after adding dummy edges to make degrees even — the classical technique). Recurse until Δ = 1. Then each edge gets a color determined by the binary representation of its path in the recursion tree. Total O(m log Δ).

The Euler split: to split a graph (multigraph) with max degree Δ into two graphs with max degrees ⌈Δ/2⌉ and ⌊Δ/2⌋: add a dummy vertex... hmm, the standard technique: pair up edges at each vertex. At each vertex v with degree d(v), if d(v) is odd, add a dummy edge (to a new vertex or pair with another odd-degree vertex). Then each vertex has even degree, and each connected component has an Euler tour. Alternately assign edges of the Euler tour to two sets. Then each vertex has at most ⌈d(v)/2⌉ edges in each set... Let me recall precisely.

Actually the standard technique for bipartite edge coloring in O(m log Δ): 

Function color(G, k) where max degree of G ≤ k... Hmm, let me think of the recursive halving:

Given bipartite multigraph G with max degree Δ. If Δ == 1, all edges get the current color base. Otherwise, we want to split E into E1, E2 such that max degree of G[E1] ≤ ⌈Δ/2⌉ and max degree of G[E2] ≤ ⌊Δ/2⌋. Then recurse on each with the corresponding number of colors.

How to split: For each vertex, its incident edges number d(v) ≤ Δ. We want each part to get at most ⌈Δ/2⌉ (resp ⌊Δ/2⌋) at each vertex. Hmm, but actually a cleaner way: we want to 2-color the edges (red/blue) such that at each vertex, the numbers of red and blue edges are as balanced as possible: |red(v) - blue(v)| ≤ 1. This is achievable via Euler tour technique: 

Add dummy edges to make all degrees even: for each vertex with odd degree, we need to pair them up. In a bipartite graph, we can add dummy edges between odd-degree vertices... but odd-degree vertices might be all on one side. Hmm, add a dummy vertex connected to all odd-degree vertices? That changes things. Alternative: add dummy edges between pairs of odd-degree vertices on the same side — but that breaks bipartiteness for the Euler tour? Euler tour doesn't need bipartiteness. The Euler tour technique: make all degrees even by adding dummy edges (dummy edges are marked and later ignored). Then each connected component has an Euler circuit. Traverse the Euler circuit, alternately coloring edges red, blue, red, blue... Since the circuit is closed and even length, each vertex on the circuit gets equal red/blue counts among its circuit-edge incidences. Each visit to a vertex contributes 2 edges (in and out), one red one blue. So each vertex gets exactly d'(v)/2 red and d'(v)/2 blue where d'(v) is the degree including dummy edges. If d(v) is even, d'(v) = d(v), so red = blue = d(v)/2. If d(v) odd, d'(v) = d(v)+1, so red = blue = (d(v)+1)/2, meaning one of red/blue has (d(v)+1)/2 and the other (d(v)-1)/2 — but which one gets the extra depends on... hmm, actually red = blue = (d(v)+1)/2 exactly, but one of those counts includes a dummy edge. So the real edges: either ⌈d/2⌉ red and ⌊d/2⌋ blue or vice versa. Either way, both ≤ ⌈d(v)/2⌉ ≤ ⌈Δ/2⌉. 

So after the split, max degree of each part ≤ ⌈Δ/2⌉. Then recurse: part with... hmm wait, but both parts have max degree ≤ ⌈Δ/2⌉, and we have Δ colors total. If Δ is even, Δ = 2k, each part gets k colors, and max degree ≤ k = ⌈Δ/2⌉ — fine. If Δ odd, Δ = 2k+1, parts have max degree ≤ k+1 = ⌈Δ/2⌉. We give k+1 colors to one part and k colors to the other. But the part with k colors might have max degree k+1 > k. Problem!

Fix: standard trick — when Δ is odd, first remove a matching covering all vertices of degree Δ (a maximum... actually a matching that covers all maximum-degree vertices exists in bipartite graphs — by taking a matching in the subgraph... hmm). Alternatively: peel off one matching first: In a bipartite graph, there's a matching covering all vertices of max degree Δ (this is a classical result — the "balanced" ... hmm). Then color that matching with color Δ, and recurse on the rest with Δ-1 colors.

Alternatively, simpler fix for the halving: when Δ is odd, Δ = 2k+1: split into two parts each with max degree ≤ k+1. Give part1 colors {1..k+1} and part2 colors {k+2..2k+1} — that's k colors for part2 but part2 might have degree k+1. Doesn't work directly.

Hmm, but there's a cleaner way to think: the recursion is on "color sets". Let me think of it as: color(G, color_list) where |color_list| = Δ ≥ maxdeg(G). Split color_list into two halves L1, L2 with sizes ⌈Δ/2⌉, ⌊Δ/2⌋. Split G into G1, G2 with maxdeg(G1) ≤ ⌈Δ/2⌉, maxdeg(G2) ≤ ⌊Δ/2⌋. For the split to give G2 the smaller bound, we need control over which part is "smaller" at each vertex... 

Alternative known approach: the split where at each vertex, red count ≤ ⌈d(v)/2⌉ and blue count ≤ ⌈d(v)/2⌉, and additionally we can orient the imbalance: we want maxdeg(G1) ≤ ⌈Δ/2⌉ and maxdeg(G2) ≤ ⌊Δ/2⌋. At a vertex with d(v) = Δ (odd), we need blue(v) ≤ (Δ-1)/2, i.e., the extra edge goes red. At vertices with d(v) < Δ, both ⌈d/2⌉ ≤ ⌊Δ/2⌋? If d ≤ Δ-1, then ⌈d/2⌉ ≤ ⌈(Δ-1)/2⌉ = ⌊Δ/2⌋ (for odd Δ). Yes! So for odd Δ: vertices with d(v) = Δ need red = ⌈Δ/2⌉, blue = ⌊Δ/2⌋; all other vertices are fine either way. So we need an Euler-split where at each max-degree vertex, the dummy edge (if any) is blue... Hmm, at a max-degree vertex (d = Δ odd), d' = Δ+1 even, red + blue = Δ+1 with red = blue = (Δ+1)/2 among all edges including dummy. Real red + real blue = Δ. If dummy is blue: real red = (Δ+1)/2, real blue = (Δ-1)/2. Good. If dummy is red: real red = (Δ-1)/2, real blue = (Δ+1)/2. Bad.

So we need to control dummy edge colors. Hmm, this is getting complicated. 

Alternative: handle odd Δ by first extracting a matching covering all Δ-degree vertices. Classical theorem: In a bipartite graph, there is a matching that covers all vertices of maximum degree. Proof: Take the subgraph... hmm, actually the theorem is that there's a matching saturating all max-degree vertices (this follows from Hall's theorem: for any set S of vertices, ... hmm). Actually the standard proof for König's theorem via induction: Let G bipartite with max degree Δ. There exists a matching M covering all vertices of degree Δ. Remove M, max degree becomes ≤ Δ-1, recurse.

Existence of such matching: Consider the bipartite graph G. We want a matching saturating X' = {v : d(v) = Δ}. By Hall's theorem, need: for all S ⊆ X', |N(S)| ≥ |S|. Suppose |N(S)| < |S|. The edges incident to S all go to N(S). Total edges from S: Δ|S|... each vertex in S has degree Δ. Edges into N(S): at most Δ|N(S)| < Δ|S|. But edges from S = Δ|S| ≤ edges into N(S) ≤ Δ|N(S)| < Δ|S|. Contradiction. Wait, but S ⊆ X (left side) only. What about max-degree vertices on the right side? Hmm, the matching needs to cover max-degree vertices on both sides. A matching edge covers one left and one right vertex. So we need a matching covering X' ∪ Y' where X' ⊆ X, Y' ⊆ Y. Hmm, Hall's condition on the combined set... A matching saturating X' ∪ Y': this is like a matching in a graph that must cover specified vertices on both sides. 

Trick: A matching saturating all of X' (max-degree left vertices) — exists by Hall as shown. After removing it, do max-degree left vertices still... hmm, we need to cover both sides' max-degree vertices with matching edges. 

Alternative: find a matching saturating X' (left max-degree vertices). Remove it. Now right vertices that had degree Δ: if such a right vertex y was matched, its degree drops to Δ-1. If not matched, its degree is still Δ. Hmm. So then find a matching saturating the remaining Δ-degree vertices... but removing edges changed degrees. This could iterate. Hmm, actually there's a cleaner statement: In a bipartite graph, there's a matching that covers all vertices of maximum degree. Let me verify with Hall: We want matching M such that every vertex with d(v) = Δ is matched. 

Standard proof: Consider any set S of vertices... Let me think of it via the following: a matching in bipartite graph G=(X∪Y, E) saturating a set Z ⊆ X∪Y exists iff for all A ⊆ Z∩X, |N(A)| ≥ |A| and for all B ⊆ Z∩Y, |N(B)| ≥ |B|? No, that's not sufficient in general (need simultaneous). Hmm, actually for bipartite matching saturating specified vertices on both sides, the condition is more complex. But for this specific case (max-degree vertices), I recall the result holds. Let me verify: Suppose we find a maximum matching M. Suppose some vertex v with d(v) = Δ is unmatched. WLOG v ∈ X. By König's theorem / Gallai–Edmonds... Let's use the vertex cover characterization: min vertex cover = max matching. If M is maximum and v unmatched, there's a vertex cover C of size |M| not containing... hmm.

Alternative cleaner approach: use the min vertex cover. Let C be a minimum vertex cover, |C| = max matching ν. Every edge touches C. If v ∉ C and d(v) = Δ: all Δ edges from v go to C ∩ Y. Hmm.

Let me just trust the classical result: In a bipartite multigraph with max degree Δ, there is a matching covering all vertices of degree Δ. Actually here's a proof: Take a maximum matching M. Suppose v is a max-degree vertex not covered by M. Consider alternating paths from v. Standard argument: Let Z = set of vertices reachable from v by M-alternating paths (starting with non-matching edge). Since M is maximum, Z contains no unmatched vertex other than v (else augmenting path). Also, no edge from Z∩X to Y∖Z (else extend alternating path... wait need care with matched/unmatched). Standard: Z∩Y vertices are all matched (else augmenting path increases matching). Each vertex in Z∩Y is matched to a vertex in Z∩X. So |Z∩X| ≥ |Z∩Y| + 1 (v ∈ Z∩X unmatched). Edges from Z∩X to Z∩Y: hmm. Every edge from v: v has Δ edges, all to Z∩Y (by closure of Z). Each y ∈ Z∩Y has degree ≤ Δ. Edges incident to Z∩Y from outside: from X∖Z? If there's an edge from x ∉ Z to y ∈ Z∩Y, then x would be reachable via alternating path (y is reachable, edge (x,y) unmatched? if (x,y) is a matching edge then y matched to x, but y is matched to someone in Z∩X — contradiction since matching is a function; so (x,y) is non-matching, so x reachable — contradiction). So all edges incident to Z∩Y come from Z∩X. Total edges incident to Z∩Y ≥ edges from v (Δ) + edges from other Z∩X... hmm, let me count: edges incident to Z∩Y = edges from Z∩X to Z∩Y (all of them, as shown). Each y ∈ Z∩Y has degree ≤ Δ, so total ≤ Δ|Z∩Y|. Each x ∈ Z∩X has degree ≤ Δ, and v has degree exactly Δ. Total edges from Z∩X to Z∩Y ≥ Δ (from v) + (Z∩X minus v each have at least 1 edge to Z∩Y? hmm, each x ∈ Z∩X \ {v} is matched, so has a matching edge to Z∩Y). So total ≥ Δ + (|Z∩X| - 1). And total ≤ Δ|Z∩Y| ≤ Δ(|Z∩X| - 1). So Δ + |Z∩X| - 1 ≤ Δ|Z∩X| - Δ. Hmm, that gives Δ + |Z∩X| - 1 ≤ Δ(|Z∩X|-1), i.e., Δ + 1 ≤ (Δ-1)|Z∩X| + ... let me just: Δ|Z∩Y| ≥ Δ + |Z∩X| - 1 ≥ Δ + |Z∩Y| (since |Z∩X| ≥ |Z∩Y|+1). So Δ|Z∩Y| ≥ Δ + |Z∩Y|, so (Δ-1)|Z∩Y| ≥ Δ, so |Z∩Y| ≥ Δ/(Δ-1) > 1, so |Z∩Y| ≥ 2. Hmm, that's not a contradiction yet. Let me recount more carefully.

Edges incident to Z∩Y: all from Z∩X (shown above). Sum over y ∈ Z∩Y of d(y) ≤ Δ|Z∩Y|. Sum over x ∈ Z∩X of (edges from x to Z∩Y) = same total. Each x ∈ Z∩X: v contributes Δ. Each other x ∈ Z∩X is matched to some y ∈ Z∩Y (matching partner is reachable), so contributes ≥ 1. So total ≥ Δ + |Z∩X| - 1. Also |Z∩X| ≥ |Z∩Y| + 1. So Δ|Z∩Y| ≥ Δ + |Z∩Y|, giving (Δ-1)|Z∩Y| ≥ Δ. For Δ ≥ 2: |Z∩Y| ≥ Δ/(Δ-1). Since Δ/(Δ-1) ≤ 2 for Δ ≥ 2, we get |Z∩Y| ≥ 2 — no contradiction. Hmm, so this argument doesn't immediately work. Let me think differently.

Hmm wait, I think the correct classical statement is: there's a matching covering all max-degree vertices, proven via Hall's theorem on a modified graph. Let me look at it via the "split off one color class" induction differently.

Actually, the classical proof of König's edge coloring theorem: induction on Δ. Given bipartite G with max degree Δ. Claim: E can be partitioned into Δ matchings. Proof: It suffices to show there's a matching M covering all vertices of degree Δ; then G - M has max degree ≤ Δ-1... wait no, G - M has max degree ≤ Δ - 1 only at vertices covered by M; vertices not covered by M have degree < Δ, so after removing M, degree ≤ Δ - 1? No! If d(v) < Δ, removing M (which doesn't touch v) leaves d(v) < Δ, i.e., ≤ Δ-1. If d(v) = Δ, v is covered by M, so d_{G-M}(v) = Δ - 1. So yes, if M covers all degree-Δ vertices, G-M has max degree ≤ Δ-1. 

So the key lemma: every bipartite multigraph has a matching covering all max-degree vertices. Proof via Hall: Let X' = max-degree vertices in X, Y' = max-degree vertices in Y. We want a matching saturating X' ∪ Y'. Hmm, but as noted, Hall-type conditions for saturating both sides simultaneously... 

Actually here's a cleaner way: we want a matching saturating X' ∪ Y'. Equivalently, a matching in the graph where... Consider adding a new vertex structure: For saturating specified vertices on both sides, we can use the following: a matching saturating X' ∪ Y' exists iff ... Let me think about whether it's always true here.

Counter-consideration: X' = {x1}, Y' = {y1}, and the only edge is x1-y1? Then matching {(x1,y1)} saturates both. Fine. What if x1 and y1 have no common... x1 has degree Δ so it has Δ edges; y1 has degree Δ. Suppose X = {x1, x2}, Y = {y1, y2}, edges: x1-y2 (Δ parallel edges? multigraph). Then d(x1) = Δ, d(y2) = Δ, X' = {x1}, Y' = {y2}, matching (x1,y2) covers both. Hmm. Suppose edges: x1-y2 and x2-y1, each vertex degree Δ... then X' = {x1, x2}, Y' = {y1, y2}, matching {(x1,y2), (x2,y1)} covers all. 

General proof attempt via Hall for saturating X' ∪ Y': This is equivalent to a perfect matching in a modified graph? Saturating specified vertices on both sides — we can reduce to perfect matching: add dummy vertices to make it a perfect matching problem: For each x ∈ X ∖ X', add a dummy... hmm, standard reduction: to find matching saturating X' ⊆ X and Y' ⊆ Y: create graph where X-side = X ∪ (dummy for Y'), Y-side = Y ∪ (dummy for X')... Let me think: we want every vertex in X' matched and every vertex in Y' matched. Equivalently perfect matching in bipartite graph H with left side = X ∪ D_Y (dummies corresponding to Y'... no wait.

Hmm, simpler: matching saturating X' ∪ Y' in G. Consider G' where we add, for each y ∈ Y', a new left vertex y* connected only to y; and for each x ∈ X', a new right vertex x* connected only to x. Then a matching saturating X' ∪ Y' in G... hmm, not quite — the new vertices also need matching which conflicts.

OK here's the thing — I recall that the lemma "bipartite graph has a matching covering all max-degree vertices" is TRUE and standard. Let me find the proof. 

Proof: Let M be a maximum matching. Suppose v is a max-degree vertex not covered by M. WLOG v ∈ X. Let Z = set of vertices reachable from v by alternating paths (odd length: start with unmatched edge from v). As argued: (1) all vertices in Z∩Y are matched (else augment), and their partners are in Z∩X. (2) No edges between Z∩X and Y∖Z... wait is that right? If x ∈ Z∩X and edge (x, y) with y ∉ Z: if (x,y) ∉ M, then y is reachable (path to x, then edge (x,y)) — wait, is x reachable via an alternating path ending with a matched edge? Alternating paths from v: v →(unmatched) y →(matched) x →(unmatched) y' ... So vertices in Z∩X are reached via matched edges (except v). From x ∈ Z∩X, any unmatched edge (x,y) makes y ∈ Z. If (x,y) ∈ M, then y is the partner of x, which is in Z. So actually all neighbors of Z∩X are in Z. Hence N(Z∩X) ⊆ Z∩Y. (3) Similarly, edges from X∖Z to Z∩Y: if (x, y) with x ∉ Z, y ∈ Z∩Y: if (x,y) ∈ M then y's partner is x, but y's partner is in Z∩X — contradiction. If (x,y) ∉ M, then x is reachable via y — contradiction. So no edges between X∖Z and Z∩Y. 

So the edge set incident to Z∩Y is exactly edges from Z∩X to Z∩Y. Now count: sum of degrees of Z∩Y = e(Z∩X, Z∩Y) ≤ Δ|Z∩Y|. Also e(Z∩X, Z∩Y) ≥ d(v) + (number of matched edges from Z∩X∖{v} to Z∩Y) = Δ + (|Z∩X| - 1) since each x ∈ Z∩X∖{v} is matched (else augmenting path — wait, could there be an unmatched x ∈ Z∩X other than v? If x ∈ Z∩X unmatched and x ≠ v, then the alternating path from v to x is an augmenting path (starts unmatched, alternates, ends at unmatched vertex) — yes that would augment, contradiction. So all Z∩X∖{v} are matched, to partners in Z∩Y.) So e ≥ Δ + |Z∩X| - 1 ≥ Δ + |Z∩Y| (since |Z∩X| ≥ |Z∩Y| + 1: partners of Z∩Y are distinct in Z∩X, plus v). So Δ|Z∩Y| ≥ Δ + |Z∩Y| ⟹ (Δ-1)|Z∩Y| ≥ Δ.

Hmm, and also each y ∈ Z∩Y: d(y) ≤ Δ. And e(Z∩X, Z∩Y) = sum over Z∩X of edges to Z∩Y. Each x ∈ Z∩X has d(x) ≤ Δ. So e ≤ Δ|Z∩X| too. Not obviously contradictory. Hmm, so where's the contradiction? Let me reconsider — maybe I need to also use that vertices in Z∩Y have degree... Hmm.

Wait, maybe the lemma is about "all vertices of degree Δ" but the matching covers them — let me test a potential counterexample. Δ = 2. Path x1 - y1 - x2? That's bipartite: X = {x1, x2}, Y = {y1}, edges x1-y1, x2-y1. Max degree: d(y1) = 2 = Δ. X' = {} (d(x1)=d(x2)=1), Y' = {y1}. Matching covering y1: {(x1, y1)}. Fine.

Δ = 2, star: x1-y1, x1-y2. X' = {x1}, Y' = {}. Matching covers x1: fine.

Hmm, when could it fail? Consider: X = {a, b}, Y = {c, d}. Edges: a-c, a-d, b-c, b-d (K2,2), Δ = 2, all vertices max degree. Perfect matching exists. 

Consider a weird multigraph: X = {a}, Y = {c, d}, edges: a-c ×2, a-d ×2? Δ = 4? d(a) = 4, d(c) = 2, d(d) = 2. X' = {a}. Matching covers a: pick any edge. Fine.

I believe the lemma is true. Let me recall the actual proof. König's edge coloring theorem proof (from e.g. West's textbook): "Proof by induction on m (number of edges). If some vertex has degree less than Δ... " Hmm, one standard proof: induction on number of edges. If every vertex of degree Δ... Let me recall: 

Theorem (König): every bipartite multigraph has an edge coloring with Δ colors, and moreover there's a proof by induction: if G has a vertex v with d(v) < Δ... hmm.

Alternative standard proof: Let e = (u, v) be any edge. By induction, G - e has a Δ-edge-coloring (max degree of G-e is ≤ Δ; if max degree of G-e is Δ, induct; if max degree drops to Δ-1... then we need to color G-e with Δ colors which is fine by induction with Δ-1 colors plus... hmm, induction on Δ: G - e has max degree ≤ Δ. If max degree ≤ Δ-1, color with Δ-1 colors by induction, then e gets color Δ. If max degree = Δ, color G-e with Δ colors by induction on m, then extend: u has a free color a, v has a free color b; if a = b done; else Kempe chain argument as I described — the alternating path from v starting with color a cannot reach u (parity/bipartiteness argument), swap, done. This is the O(m·chain) algorithm.

OK so back to algorithms. Given constraints (m ≤ 4·10^5, 2s), what's practical in Python?

Option A: Kempe chain algorithm with adjacency structures. Worst case path lengths could be long, but is there a known bad case? The Kempe chain algorithm's worst case is O(m·Δ) I think, but in practice it's near O(m α)? Hmm. Actually, I recall that this algorithm (color edges one by one with Kempe chain fixes) can be O(m^2) in the worst case for general graphs, but for bipartite... Let me think about whether long chains happen often. Each chain traversal is O(chain length). Total = sum of chain lengths over all insertions. Adversarially, this could be Θ(m·Δ)? Hmm, hard to construct but possible. With m = 4·10^5 and Δ up to 4·10^5... but note Δ ≤ max(nL, nR)? No — multigraph: Δ ≤ m. But also Δ ≤ nL·(multiplicity)... Δ can be up to m. Hmm, but if Δ is huge, chains... 

Hmm, wait. Actually, let me reconsider. There's a classical result that the Kempe-chain edge coloring algorithm for bipartite graphs runs in O(m log m) or O(m Δ)? Let me think... I don't remember a strong bound. Let me think about the structure: when we insert edge (u,v) and do a chain swap, the chain has length L. The swap changes colors of L edges. Hmm.

Option B: The binary splitting (Euler split) approach — O(m log Δ) guaranteed. This is elegant: 

color(G, k): colors 1..k, maxdeg(G) ≤ k. If k == 1: all edges color 1. Else: split G into G1, G2 with maxdeg(G1) ≤ ⌈k/2⌉, maxdeg(G2) ≤ ⌈k/2⌉ (both halves bounded by ⌈k/2⌉). Then recurse color(G1, ⌈k/2⌉) with colors 1..⌈k/2⌉ and color(G2, k - ⌈k/2⌉) with colors ⌈k/2⌉+1..k. But maxdeg(G2) ≤ ⌈k/2⌉ might exceed k - ⌈k/2⌉ = ⌊k/2⌋ when k is odd. Problem again.

Hmm right, so the issue is odd k. Let me reconsider: we need split with maxdeg(G1) ≤ ⌈k/2⌉ and maxdeg(G2) ≤ ⌊k/2⌋. As computed: for odd k, at vertices with d(v) = k we need the split to be exactly ⌈k/2⌉ / ⌊k/2⌋ with the larger part in G1; at vertices with d(v) ≤ k-1, ⌈d/2⌉ ≤ ⌊k/2⌋ so any split works. So we need an Euler split where at each max-degree vertex, the dummy edge goes to G2 (the "blue" side)... wait let me redo: at max-degree vertex v (d(v) = k odd), we add one dummy edge, making d' = k+1. Euler tour alternation gives red(v) = blue(v) = (k+1)/2 counting dummy. If dummy is blue: real red = (k+1)/2 = ⌈k/2⌉, real blue = (k-1)/2 = ⌊k/2⌋. So we need dummy edges at max-degree vertices to be blue (in G2). Can we arrange that? 

Hmm, the dummy edges: we add them to make degrees even. The set of odd-degree vertices: we pair them up with dummy edges (any pairing, e.g., consecutive). Then Euler tour on each component, alternate colors. The color a dummy edge gets depends on the tour. We can't easily control it per-vertex.

Alternative fix: instead of pairing odd-degree vertices with each other, pair each odd-degree vertex with a new dummy "partner" — i.e., for each odd-degree vertex v, create a dummy vertex v' and dummy edge (v, v'). Then v' has degree 1. Now the graph has all even degrees except the dummy leaves... no wait, v' has degree 1, odd. Hmm, that doesn't fix parity.

Alternative: handle it differently — allow the split to be "off by one" and fix up. Actually, here's a cleaner classical approach: **the "peel matching" + halving** combined:

Actually, you know what — there's a much simpler classical approach for this exact problem. This problem is from some contest (looks like it could be from Codeforces problem about edge coloring bipartite graph, m up to 4·10^5... hmm, "nL, nR up to 1e5, m up to 4e5"). Hmm, this smells like a specific competitive programming problem. Possibly from a recent contest where the intended solution is the Kempe chain / "Vizing-style" algorithm, or the divide and conquer.

Let me think about what's implementable efficiently in Python within 2 seconds for m = 4·10^5.

Hmm, 2 seconds in Python (probably CPython) with m = 4·10^5... We need roughly O(m log m) with small constants, or O(m √m)? Python does maybe 10^7-5·10^7 simple operations per second. m log m ≈ 4e5 * 19 ≈ 7.6e6 basic steps — but each "step" in the Euler-split recursion involves adjacency traversal which is heavy. Hmm, this is challenging but let's think.

Actually wait — maybe there's a much simpler observation for this specific problem. Let me re-read the problem statement.

"A testing facility... assign a channel to each test such that no device experiences channel interference, ensuring the total number of distinct channels used is exactly Δ."

Hmm, "exactly Δ" — but also "no more than this unavoidable minimum". So we need exactly Δ distinct channels used (which is automatic if Δ ≥ 1 and... well if m ≥ 1, using at most Δ and we need exactly Δ distinct values in output; if the coloring uses fewer distinct colors we'd need to bump some edges up — but a proper edge coloring where some color class is empty... can that happen with max degree Δ? If we produce a coloring with ≤ Δ colors that's proper, the number of distinct colors used could be less than Δ in theory (e.g., a single edge: Δ = 1, one color — fine; a path of length 2: Δ = 2, colors 1,2 — we could also color both edges 1? No! They share the middle vertex, so they must differ. Hmm, a matching of 3 edges: Δ = 1, all color 1. Fine.). Actually, if the coloring is proper and uses k colors, then... can k < Δ? Yes: e.g., a star with 3 edges: Δ = 3, needs 3 colors. Hmm, proper coloring with fewer than Δ colors is impossible? No wait — edge chromatic number of bipartite = Δ, so any proper coloring uses ≥ Δ colors... no! Edge chromatic number = Δ means the minimum number of colors for a proper coloring is Δ. So any proper coloring uses ≥ Δ colors. And we use ≤ Δ. So exactly Δ. Good — as long as our coloring is proper and uses ≤ Δ colors, it automatically uses exactly Δ (when m ≥ 1; if m = 0, Δ = 0 and output... hmm, m = 0: "Print YES, then a line with m integers" — empty line. Δ = 0. Edge case.)

Wait, but actually is it true that any proper edge coloring uses ≥ Δ colors? Yes: at a vertex of degree Δ, all Δ incident edges have distinct colors. So ≥ Δ distinct colors. 

So the task: proper edge coloring of bipartite multigraph with exactly Δ colors (Δ = max degree). 

Now, algorithms:

**Option 1: Greedy + Kempe chains (the "Vizing fan"-free bipartite version).** 

Implementation sketch:
- Maintain for each vertex a "color → edge" map or "used colors" bitset, and "free color" pointer.
- Process edges in some order. For edge (u, v): find smallest color free at u (a) and at v (b). If a == b: assign. Else: walk the Kempe chain from v: current vertex x = v, looking for edge of color a at x; if found, move to its other endpoint y, then look for color b at y, etc. Swap colors along the chain. Then assign color a to (u,v).

Wait, I need to re-derive the direction. Edge (u, v) to color. a = free at u, b = free at v, a ≠ b. Chain from v: does v have an edge of color a? If yes, follow it: v —e1(color a)— x1; at x1, look for color b edge: x1 —e2(color b)— x2; at x2 look for color a; etc. The chain ends when the next color's edge doesn't exist. Swap a↔b on all chain edges. After swap: v no longer has color a (its a-edge became b). Wait — v's a-edge e1 becomes color b. So now a is free at v. And u: chain never reaches u (proven via parity). So a is free at u still. Assign color a to (u, v). 

But wait — I should double check the parity argument once more. Chain: v (right) —a— x1 (left) —b— x2 (right) —a— x3 (left)... Edges at odd positions (1st, 3rd, ...) have color a; even positions color b. The chain reaches u (left) at odd position k (k odd), via an edge of color a. But a is free at u — u has no a-edge. Contradiction. So chain never reaches u. ✓.

Also, the chain is simple (no repeated vertices): if a vertex repeated, it would have two incident edges of the same color among {a, b} — impossible in a proper coloring. ✓. And the swap keeps properness: each internal chain vertex x_i has exactly one a-edge and one b-edge (both on the chain — wait, is that true? x1 has the a-edge e1 on the chain; does x1 have another a-edge? No, proper coloring: at most one edge of each color per vertex. Does x1 have a b-edge? Yes — e2, since the chain continued via color b from x1. So x1's a-edge and b-edge are both on the chain, and they swap — still one a and one b. Endpoints: v: had a-edge e1 (on chain), no b-edge (b free at v). After swap: v has b-edge e1, no a-edge. Other endpoint x_k: has one chain edge of color a or b, and no edge of the other color (that's why the chain stopped). After swap: has the other color, still no duplicate. ✓.

Complexity concern: chain lengths. Each insertion triggers one chain walk of length L_i. Total time O(Σ L_i). Worst case? I recall for this algorithm (sometimes called the "König algorithm" or greedy with recoloring), the total is O(m Δ) worst case but typically much better. Hmm. Actually hold on — is there a smarter order/choice that bounds it? 

There's a classical result: if you always pick a and b as the *smallest free colors*, the total chain work is O(m log m)? I'm not sure. Let me think about potential bad cases. 

Hmm, actually, I recall a Codeforces problem: "CF 1462?" no... There's a known hard problem on edge coloring bipartite graphs online: e.g., "https://codeforces.com/problemset/problem/1462/F"? no. There's "Problem: D. Edge Coloring"? Hmm, there's CF Round problem "1738...". Actually I remember: **Codeforces 1619 F?** no. There's the problem "Kattis??" Hmm.

I definitely recall a recent Codeforces problem (maybe 2023) requiring bipartite edge coloring with n up to 2·10^5? Hmm, "Codeforces Round 906"? Or maybe it's from a CodeChef contest. The constraints nL, nR ≤ 1e5, m ≤ 4e5 with 2s — this looks like it could be from a recent contest where intended solution is O(m √m) or O(m log). 

Hmm wait, actually I think I remember now: this is from **Codeforces problem 1949? ICPC-style? "Mirror" contest?** The phrase "Problem B" and the story... It resembles problems from "The 2nd Universal Cup" or similar. The statement "Because the array is strictly two-sided, this optimal configuration is always achievable" confirms König's theorem.

Let me just design a robust solution. Given Python's speed, I want the simplest algorithm that's fast enough. Let me consider the options more concretely:

**Option 1: Kempe chains.** Per edge: find free colors at u and v (need efficient "find a free color at vertex" — maintain per-vertex pointer/heap? Since colors only get added per vertex over time (colors are never removed from a vertex... wait, in a chain swap, a vertex can lose a color and gain another. E.g., v loses a, gains b. So the set of used colors at a vertex changes. Hmm, but note: in a swap at vertex x, x loses one color and gains the other — the count stays the same. And when we assign a new edge, the count increases by 1. So the number of used colors at vertex x after processing prefix = ... hmm, not exactly d(x) because chain swaps exchange colors but keep counts. Actually at any time, the number of used colors at x equals the number of colored edges at x (each edge contributes a distinct color at x). So "find smallest free color at x" — we can maintain a pointer "next possibly-free color" per vertex: since used-color count only increases (by 1 per incident edge colored), the smallest free color is ≤ (count of colored incident edges) + 1... hmm, actually the smallest free color at x: if x has c colored incident edges, they occupy c distinct colors, so among colors 1..c+1 at least one is free at x. So the smallest free color is ≤ c+1. Maintain per-vertex a "candidate pointer" starting at 1; when we need a free color, scan from the pointer upward until we find a color not used at x; after using it, set pointer appropriately. But chain swaps can free up smaller colors at a vertex (v loses color a which might be small, gains b). Hmm, then the pointer should decrease? The smallest free color at v after the swap is min(a, previous smallest free). Since a < ... hmm, a was the smallest free at u, not necessarily related to v's colors. Hmm.

Wait, actually, let's reconsider: we don't need the *smallest* free color; any free color works for correctness. But for efficiency of "find free color", pointers that only move forward are nice. Chain swaps might invalidate "pointer" invariants (a color below the pointer becomes free). But that's fine for correctness — we just need SOME free color; if we maintain "all colors < pointer are used at x" as invariant, chain swaps break it. Alternative: maintain per-vertex a set of used colors as a bitmask (Python big ints!) and find free color via bit tricks: used_mask[x]; free = lowest zero bit above... We can compute smallest free color as (used_mask[x] + 1) & ~used_mask[x]? Hmm: let m = used_mask. The lowest free color c satisfies: bit c of m is 0. (m+1) flips trailing ones and the lowest zero: m+1 = m with trailing 1s cleared and the lowest 0 set. So lowest zero bit of m = (m+1) & ~m? Let's see: m = 0b0111 (colors 1,2,3 used, using bit i for color i). m+1 = 0b1000. (m+1) & ~m = 0b1000 → color 4. ✓. m = 0b1011 (colors 1,2,4): m+1 = 0b1100, & ~m = 0b0100 → color 3. ✓. So smallest free color = ((m+1) & ~m).bit_length()... wait, (m+1)&~m gives the lowest zero bit as a bitmask; its bit_length gives position+1. If we use bit (c-1) for color c: mask bit c-1 set iff color c used. Then lowest free color = ((m+1) & ~m).bit_length(). Since m+1 = -~m, and (m+1)&~m = (m+1) & (-m-1)... hmm, simpler: lowest zero bit of m = ~m & (m+1). Yes.

But careful: we need free color at u (a) and at v (b) — but also we need them to be ≤ Δ. Since degree of u ≤ Δ, the number of used colors at u ≤ Δ, so among colors 1..Δ+1... hmm, smallest free could be Δ+1 if colors 1..Δ all used — but that means u already has Δ colored edges, so the new edge would make degree Δ+1 > Δ — impossible. So when we color the k-th incident edge at u (k ≤ Δ), smallest free color ≤ Δ. ✓ (since k-1 colors used among 1..Δ, smallest free ≤ Δ).

Big-int bitmasks per vertex: operations are O(Δ/64) word ops each — with Δ up to 4·10^5, that's 6250 words per operation — too slow if done per edge (4·10^5 edges × ... no wait, Δ is the max degree; a vertex with degree d has mask with ~d bits, operations O(d/64). Sum over edges of (d(u)/64 + d(v)/64) = O(m·Δ/64) worst case — too slow for large Δ. Hmm, but wait: Σ_edges (d(u) + d(v)) = Σ_v d(v)^2. Worst case: one vertex with degree 4·10^5 → Σ d^2 = 1.6·10^11. Way too slow.

Better: maintain per-vertex pointer + a "used" structure allowing O(1) checks. Since we just need *a* free color (not smallest), and we know count of colored incident edges c(x), we know a free color exists among 1..c(x)+1. Maintain per vertex: array-free approach: "color_used[x][c]" — but that's per-vertex dict — heavy.

Alternative: maintain per vertex a pointer p(x) such that all colors < p(x) are... hmm, the issue is chain swaps freeing small colors. Let me think about whether we can avoid maintaining exact "smallest free" and instead maintain a valid pointer with amortized O(1) advancement:

Idea: maintain per vertex x a pointer p(x) = a color that is free at x (or scan to find one). When we color an edge at x with color c, if c == p(x), we need to advance p(x) to the next free color: scan upward from p(x)+1 until finding a free color at x. "Free at x" check: need per-vertex color usage. Chain swaps: at vertex x on the chain, x's colors a and b swap — the set of used colors at x is unchanged! Wait: x had both a and b (internal chain vertices), so the set is unchanged. Endpoints: v loses a gains b — set changes: a becomes free, b becomes used. Other endpoint x_k: loses one gains other — set changes. Hmm so sets do change at chain endpoints.

Hmm OK. Let me think about the total work differently. 

Alternative clean approach: **process edges grouped by left vertex**? Or use the classical O(m log m) D&C with Euler splits. Let me flesh that out since it has guaranteed complexity.

**Option 2: Divide & conquer on colors with Euler splits.**

The recursion: solve(G, colors 1..k) where maxdeg(G) ≤ k. If k == 1: assign color 1 to all edges (maxdeg ≤ 1 means it's a matching). Split: we want G1 with maxdeg ≤ ⌈k/2⌉ getting colors 1..⌈k/2⌉, G2 with maxdeg ≤ ⌊k/2⌋ getting colors ⌈k/2⌉+1..k. As discussed, the problematic case is odd k where max-degree vertices need their extra edge in G1.

Hmm, wait — actually, maybe I have the split requirement wrong. Let me redo: we need maxdeg(G1) ≤ number of colors given to G1 and maxdeg(G2) ≤ number of colors given to G2. With k colors split as k1 = ⌈k/2⌉, k2 = ⌊k/2⌋. If the split gives every vertex at most ⌈d(x)/2⌉ edges in each part: maxdeg(G1) ≤ ⌈Δ/2⌉ ≤ ⌈k/2⌉ = k1 ✓. maxdeg(G2) ≤ ⌈Δ/2⌉, but k2 = ⌊k/2⌋. If k even: ⌈Δ/2⌉ ≤ ⌈k/2⌉ = k/2 = k2 ✓. If k odd: ⌈Δ/2⌉ could be (k+1)/2 > k2 = (k-1)/2 when Δ = k. ✗.

So for odd k, we need the split to put at most ⌊d(x)/2⌋ edges in G2 for max-degree vertices... As computed: at a vertex with d(x) = k (odd), the split must be (⌈k/2⌉, ⌊k/2⌋) with G1 getting the extra. At vertices with d(x) ≤ k-1: ⌈d(x)/2⌉ ≤ ⌈(k-1)/2⌉ = (k-1)/2 = k2 ✓ — any split works. So the requirement: **at each vertex of degree exactly k (odd), G2 gets exactly ⌊k/2⌋ edges and G1 gets ⌈k/2⌉.**

Euler split with dummy edges: at odd-degree vertex x, add one dummy edge. If the dummy is colored "G2-side" in the alternation, then real G2 count = (d+1)/2 - 1 = (d-1)/2 = ⌊d/2⌋ ✓ and real G1 = (d+1)/2 = ⌈d/2⌉ ✓. If dummy is G1-side: real G1 = (d-1)/2, real G2 = (d+1)/2 ✗ (G2 exceeds k2 when d = k).

So we need: at every vertex of degree exactly k (with k odd), the dummy edge must be on the G2 side. Hmm. Can we guarantee that? 

Alternative approach to the split that gives more control: **direct pairing without Euler tours.** We want to split incident edges at each vertex into two halves with prescribed sizes. This is like a "balanced 2-edge-coloring" which is exactly a bipartite... hmm, actually the problem "split edges into two parts with given degree bounds" is itself a flow/bipartite-matching-like problem. But the Euler trick is the cheap way.

Alternative: **avoid odd-k issue by peeling a matching first when k is odd**: solve(G, k): if k odd: find matching M covering all degree-k vertices, assign color k to M, recurse solve(G - M, k-1). If k even: Euler split into (G1, G2) each with maxdeg ≤ k/2, recurse solve(G1, k/2) and solve(G2, k/2). 

But finding a matching covering all max-degree vertices requires... Hall's theorem constructive = bipartite matching = O(m √n) via Hopcroft-Karp — too slow in Python for these sizes? Hopcroft-Karp on m = 4·10^5, n = 2·10^5: maybe 10-20 million operations — in Python, likely 10+ seconds. Too slow. Hmm.

But wait — maybe there's a simpler way to find such a matching: greedy? A maximal matching doesn't necessarily cover all max-degree vertices. Hmm. But actually — here's a classical fact used in these algorithms: in the D&C, instead of peeling an exact matching, we can use the following trick: **allow the two parts to have max degree ⌈k/2⌉ and give both parts ⌈k/2⌉ colors, wasting colors?** No — total colors would exceed k.

Hmm, alternative: **the "overlap" trick**: Actually, here's another classical approach for bipartite edge coloring in O(m log Δ): 

At each recursion level with color range size k (maxdeg ≤ k): if k == 1, done. Else, split colors into k1 = ⌈k/2⌉ and k2 = ⌊k/2⌋. Split edges via Euler split into G1 (maxdeg ≤ ⌈Δ/2⌉) and G2 (maxdeg ≤ ⌈Δ/2⌉). Now here's the fix: if Δ ≤ k - 1 (i.e., maxdeg strictly less than k), then ⌈Δ/2⌉ ≤ ⌈(k-1)/2⌉ = k2 when k odd... wait if k odd, k2 = (k-1)/2, and Δ ≤ k-1 gives ⌈Δ/2⌉ ≤ (k-1)/2 = k2 ✓. So the problematic case is only Δ = k exactly (with k odd). 

So: **maintain the invariant maxdeg(G) ≤ k, and handle the case maxdeg = k, k odd specially.** In that case, we need to peel a matching covering all degree-k vertices. Alternatively — reduce to the even case: if k is odd and Δ = k, then... hmm.

Alternatively, a cleaner classical method: **first make Δ a power of 2?** No...

Hmm, let me look at this from a different angle. There's a classical simple algorithm for bipartite edge coloring in O(m Δ)... no. Let me think about what's actually feasible.

**Option 3: Reduce to bipartite matching via "color-by-color" with augmenting paths — the standard O(m √m)?** Hmm.

**Option 4: The "chain" algorithm but with a twist guaranteeing near-linear time.** 

Hmm, let me reconsider Option 1's complexity. I recall that this greedy+Kempe-chain algorithm, when processing edges in arbitrary order and choosing smallest free colors, has worst-case Ω(m·Δ)? Let me think of a bad example... Consider a complete bipartite graph K_{d,d} — Δ = d, m = d². When inserting edges, how long are the chains? Empirically for K_{d,d} I'd guess chains stay short (like O(√m)?) but worst-case adversarial orders might create long chains. Total worst-case bound for the naive algorithm is O(m·Δ) I believe. With m = 4·10^5 and Δ = 4·10^5 that's 1.6·10^11 — but such a case requires a vertex of degree 4·10^5, meaning m = 4·10^5 edges all at one vertex — then all other vertices have degree 1, and chains... Let's think: if there's a vertex u with degree 4·10^5 (all edges (u, v_i)), Δ = 4·10^5. Each v_i has degree 1. Coloring: each edge (u, v_i) gets a distinct color — greedy handles with no chains (v_i always has all colors free, so a = b = smallest free at u). Fine.

Bad case for chains: need long alternating paths. Hmm. Honestly, I recall that for the bipartite Kempe-chain algorithm, there's an amortized analysis showing O(m log m) total? Let me think... I don't remember such a result. There IS a classical result that the "Vizing's algorithm" for general graphs is O(mΔ) and with clever tricks O(m log n)... For bipartite specifically, the D&C Euler approach is the standard O(m log Δ).

Let me now think about implementing the D&C Euler-split approach in Python efficiently. 

Actually hold on. Let me reconsider the problem source and expected difficulty. nL, nR ≤ 1e5, m ≤ 4e5, TL 2s. If this is from a contest where C++ solutions use the Kempe chain greedy (which is common — e.g., the well-known technique for "bipartite edge coloring" problems on Codeforces like problem 1738?? hmm), then in Python we need to be clever. But since I'm asked for a Python solution, presumably a reasonably efficient one exists. Let me think about which algorithm is most Python-friendly.

Actually — wait. Let me reconsider. There's a MUCH simpler classical algorithm for bipartite edge coloring when we process by **orienting edges / using the "degree-splitting via sorting" trick**? Hmm.

Let me think again about the Kempe chain greedy but with a key optimization: **process edges in order of... and use arrays**. Let me estimate the realistic total chain length. Actually, you know, there's a neat known fact: if you process the edges one by one and use the Kempe chain algorithm, each chain walk is O(length), and the total over all insertions is O(m + total chain lengths). I believe worst-case instances exist with total Θ(mΔ)... but maybe for the *smallest-free-color* variant it's better? Hmm.

Hmm, let me think about the D&C approach more since it has guaranteed O(m log Δ):

Actually, here's a cleaner formulation of the D&C that avoids the odd-k matching problem entirely! 

**Key insight**: Instead of splitting into ⌈k/2⌉/⌊k/2⌋ colors, split into two halves of sizes that match the Euler split's guarantee, and handle the "excess" by allowing the recursion to use colors from a shared pool? Hmm.

Alternative formulation via **binary representation**: Assign each edge a color in {0, 1}^⌈log2 Δ⌉... The recursion: solve(G, bit-position b, base color): if maxdeg(G) ≤ 1: assign. Hmm, the issue remains.

**Another classical approach: "degree-splitting via Euler tour" where we don't require exact halving of the color count, but instead track per-vertex "color budget".** Hmm, getting complicated.

Let me look at the odd-k problem again. solve(G, k) with maxdeg(G) ≤ k, k odd, and possibly maxdeg = k. Peel matching covering degree-k vertices. 

**Simpler alternative for peeling**: when k is odd and Δ = k, note Δ = k means some vertex has degree k. Instead of a matching covering all max-degree vertices, we can do this: find a **maximal edge set F such that... ** hmm.

Wait, actually here's a thought — there's a classical simpler decomposition: **any bipartite multigraph's edge set can be split into ⌈Δ/2⌉ "2-regular-ish" pieces?** Hmm.

Alternatively, use the following known clean recursive scheme (I recall from "Arjomandi?" or the paper "Fast edge coloring of bipartite graphs" / the classical O(E log V) algorithm by Cole, Ost, Schirra (2001) "Edge-coloring bipartite multigraphs in O(E log D) time" — which uses exactly this Euler-split D&C with a clever fix). The COS algorithm: for bipartite multigraphs, edge-color with Δ colors in O(m log Δ). The fix for the odd case: they use "balanced splitting" where at each vertex the split sizes are ⌈d/2⌉ and ⌊d/2⌋, and they give the first part ⌈k/2⌉ colors and second ⌊k/2⌋... and they handle the case maxdeg = k, k odd, by first extracting a matching covering max-degree vertices — and they find it via Eulerian techniques too! 

Specifically: to find a matching covering all vertices of degree Δ in a bipartite multigraph: Take an Eulerian decomposition... Here's a classical trick: **In a bipartite multigraph, a matching covering all max-degree vertices can be found greedily via repeatedly taking Euler tours?** Hmm. Let me think: 

Claim: In bipartite multigraph G with max degree Δ, consider splitting E into Δ/2 (if Δ even) 2-factors... For even Δ: split into two parts each with max degree Δ/2 (Euler split works: all degrees ≤ Δ; add dummies to make even; each part gets ≤ ⌈d/2⌉ ≤ Δ/2 ✓). Recurse. For odd Δ: we want to peel one matching covering degree-Δ vertices. 

Peeling trick via Euler: Add a new vertex? Hmm: Here's a classical trick: to find a matching covering all max-degree vertices: take the subgraph induced by... no. 

Alternative: **reduce odd Δ to even by adding a dummy vertex on each side**: Add dummy vertices p (left) and q (right). For each vertex x with odd degree... hmm, we want to *use* the matching-peel differently.

Hmm, actually here's a cleaner idea for the odd case: **solve(G, k) with k odd**: Let Δ' = maxdeg(G) ≤ k. If Δ' ≤ k-1, then recurse with even k-1: solve(G, k-1) — colors 1..k-1, and we're allowed since maxdeg ≤ k-1. Wait but then we use only k-1 colors — but the problem requires exactly Δ colors where Δ is the max degree of the WHOLE graph, not of the subgraph. Hmm! Important: the problem says "the total number of distinct channels used is exactly Δ" where Δ = global max degree. If our algorithm uses fewer colors on some subset... but as I argued, ANY proper coloring of the whole graph uses ≥ Δ colors. So if the algorithm is proper and uses ≤ Δ colors globally, it uses exactly Δ. But wait — if the D&C assigns colors from a pool of size Δ globally, and some sub-branch uses fewer... the union still could be < Δ? No — properness at the max-degree vertex forces Δ distinct colors among its incident edges. So as long as the final coloring is proper, the number of distinct colors used is ≥ Δ automatically. And our algorithm uses ≤ Δ. So exactly Δ. 

So in solve(G, k): if maxdeg(G) = Δ' < k, we can just call solve(G, Δ') — i.e., **always recurse with k = current maxdeg**. Then the odd case: k odd, Δ' = k. We must split k (odd) into k1 + k2 with maxdeg(G1) ≤ k1, maxdeg(G2) ≤ k2. Euler split gives both ≤ ⌈k/2⌉ = (k+1)/2. k1 = (k+1)/2, k2 = (k-1)/2: G2 might violate. k1 = k2 = ... can't, k odd.

So the odd case genuinely needs the matching peel (or an unbalanced split with control). 

**Unbalanced split with control**: We need a split where G2 gets ≤ ⌊d(x)/2⌋ at every vertex with d(x) = k... but actually we need it only at vertices with d(x) = k; but hmm, wait — actually we need maxdeg(G2) ≤ k2 = (k-1)/2. Vertices with d(x) ≤ k-1 are fine with ⌈d/2⌉ ≤ (k-1)/2. So need: at vertices with d(x) = k: G2-side gets ≤ (k-1)/2, i.e., exactly ⌊k/2⌋ (since G1+G2 = k, G1 ≤ ⌈k/2⌉). So the split at max-degree vertices must be exactly (⌈k/2⌉, ⌊k/2⌋) with G1 ≥ G2. 

Can we achieve this with a modified Euler trick? At each vertex of degree k (odd), add ONE dummy edge; at other odd-degree vertices also add dummy edges to make degrees even. Now, in the Euler tour alternation, at a degree-k vertex, the dummy gets color red or blue (50/50). We need it blue (G2 side) at ALL degree-k vertices. Hmm. What if we add dummy edges cleverly: pair up degree-k vertices with each other via dummy edges? A dummy edge between two degree-k vertices (both odd degree → both need a dummy). In the Euler tour, consecutive edges alternate colors; a dummy edge (x, y) has some color, say red; then at x, red includes dummy... hmm wait, the alternation assigns each edge of the tour alternately red/blue. The dummy edge (x,y) is one edge with one color, say red. Then at x: real red = (k+1)/2 - 1 = (k-1)/2, real blue = (k+1)/2. That's the opposite of what we want at x! And at y: same. Hmm, so pairing two max-degree vertices gives both of them the wrong split. Unless... we want G1 to be the side that gets ⌈k/2⌉ at max-degree vertices. Let me recompute: we need maxdeg(G2) ≤ (k-1)/2. At a degree-k vertex: if dummy is red: real red = (k-1)/2, real blue = (k+1)/2. So make **G2 = red side**! Then at max-degree vertices, G2 gets (k-1)/2 ✓. And G1 = blue gets (k+1)/2 = ⌈k/2⌉ ≤ k1 = (k+1)/2 ✓. At other vertices with even degree d: red = blue = d/2 ≤ ... need maxdeg(G2) ≤ (k-1)/2: d/2 ≤ (k-1)/2 iff d ≤ k-1 ✓ (d even, k odd, d ≤ k-1 since d ≠ k... d could be k? No, k odd, d even, so d ≤ k-1 ✓). At other odd-degree vertices d (odd, d ≤ k-2 since d odd < k): dummy red: real red = (d+1)/2 - 1 = (d-1)/2, real blue = (d+1)/2. G2 = red gets (d-1)/2 ≤ (k-1)/2 ✓. If dummy blue: real red = (d+1)/2, real blue = (d-1)/2; G2 = red gets (d+1)/2 ≤ (k-1)/2? d ≤ k-2 → (d+1)/2 ≤ (k-1)/2 ✓. 

So: **if we can arrange that every dummy edge incident to a degree-k vertex is colored red (G2 side), we're done.** Pairing two degree-k vertices with a dummy edge: the dummy edge gets one color; both endpoints see that dummy as their dummy. If dummy is red: both endpoints have real red = (k-1)/2 ✓ (G2 = red side). If dummy is blue: both have real blue = (k-1)/2, real red = (k+1)/2 — then G2 should be blue at these... but G2 is a global choice. ✗.

Hmm. So pairing max-degree vertices doesn't automatically work. What if we pair each degree-k vertex with a *fresh dummy vertex* (degree 1)? Then the dummy vertex has odd degree — breaks Euler parity. Add dummy edges to make ALL degrees even including dummies: pair up... ugh, circular.

**Different idea for the odd case**: use the Euler split to split into G1, G2 both with maxdeg ≤ (k+1)/2, then recurse: solve(G1, (k+1)/2) and solve(G2, (k-1)/2) — but G2 might have maxdeg (k+1)/2 > (k-1)/2. However! Note maxdeg(G2) ≤ ⌈Δ_G2/2⌉... no wait. Hmm, what IS maxdeg(G2) exactly? At each vertex, G2 gets ≤ ⌈d(x)/2⌉. If x has d(x) = k: G2 gets ≤ (k+1)/2. But maybe we can then fix G2 by moving a few edges from G2 to G1? The vertices where G2 has (k+1)/2 edges are exactly degree-k vertices where the split was unfavorable. Moving an edge from G2 to G1 at such a vertex x: but that edge's other endpoint y also loses an edge from G2 — fine for G2's max degree (only helps), but G1 at y gains — could push G1 over (k+1)/2 at y? If y also has d(y) = k and G1(y) = (k+1)/2 already, then adding makes (k+2)/2 > k1. Hmm. But we could move edges along alternating paths... this is becoming the Cole–Ost–Schirra algorithm which is genuinely intricate.

**Let me step back and consider the matching-peel approach with a cheap matching algorithm.**

For the odd case, we need a matching covering all degree-k vertices. Cheap way: **iteratively**: hmm. Actually here's a classical cheap method to find a matching covering all max-degree vertices in a bipartite multigraph: 

Take a maximal matching greedily? Not guaranteed to cover. 

But here's a neat trick specific to this D&C: **we don't need the peel at the top level only — we need it at every odd level.** Total peels: O(log Δ) levels, each requiring a matching computation on the current edge set. If each matching computation is O(current m) via some Euler-like trick, total O(m log Δ). Is there an Euler-like trick for "matching covering all max-degree vertices"? 

YES — I recall now: **In a bipartite multigraph, you can find a matching covering all maximum-degree vertices by: split the graph via Euler tours into two parts G1, G2 with maxdeg ≤ ⌈Δ/2⌉ each, and recurse?** That gives... hmm, that's for edge coloring itself.

Alternatively: **2-edge-coloring trick**: Hmm, let me think about the following: to find a matching covering all degree-Δ vertices: 

Consider the graph G. Add dummy edges to make it Δ-regular? A bipartite multigraph with max degree Δ can be extended to a Δ-regular bipartite multigraph (classic: add dummy vertices on the smaller side... wait, need |X|·Δ = |Y|·Δ → |X| = |Y|; add dummy vertices to balance sides, then add dummy edges to raise degrees to Δ — always possible in bipartite multigraphs). Then a Δ-regular bipartite multigraph decomposes into Δ perfect matchings (König via Hall/perfect matching). But finding perfect matchings is expensive.

Hmm hmm. OK here's another angle:

**Option 5: Reduce bipartite edge coloring to... orientation + "Chung-?"** Hmm.

**Option 6: The "process vertices one at a time" algorithm (Chernykh?)"** Hmm.

Let me reconsider the problem constraints: m ≤ 4·10^5. In Python, even O(m log Δ) with heavy constant (Euler tours via linked lists) is going to be tough but maybe feasible with careful array-based implementation. The Kempe-chain greedy is much simpler to implement; the question is worst-case behavior. 

Let me think about known worst cases for Kempe-chain greedy... Consider the "chain reaction" construction: a path-like structure where each insertion triggers a long chain. E.g., take a long path graph (bipartite), vertices v1 - v2 - ... - v_n, edges e1..e_{n-1}. Δ = 2. Insert edges in order e1, e2, ..., each insertion: e_i = (v_i, v_{i+1}). When inserting e_i: v_i has color... let's simulate: e1 = (v1,v2): a = free at v1 = 1, b = free at v2 = 1, same → color 1. e2 = (v2, v3): free at v2: colors used {1} → smallest free 2; free at v3: 1. a=2 (at u=v2), b=1 (at v3)? Wait which is u and which is v — say u = v2 (left), v = v3 (right). a = smallest free at u = 2, b = smallest free at v = 1. a ≠ b. Chain from v=v3 with color a=2: v3 has no color-2 edge → chain is empty. Swap nothing. Assign color a=2 to e2? Wait — the rule: chain from v following color a; if v has no a-edge, chain empty, then a is free at v already?? But b was smallest free at v and a=2... v3's used colors = {} so both 1 and 2 free at v3. We chose b = smallest free at v = 1, a = smallest free at u = 2. Since a ≠ b, we do the chain from v with color a: v3 has no color-2 edge, chain ends immediately. Swap: nothing. Now assign color a = 2 to e2. Hmm, but wait — after the (empty) chain swap, is a free at v? Yes (chain empty means v had no a-edge, so a was already free at v). So e2 gets color 2. But actually we could have just assigned... the algorithm as stated: if a ≠ b, walk chain from v along color a; swap a↔b on chain; assign a. With empty chain, assign a. OK so e2 = color 2. e3 = (v3, v4): u = v3: used {2} → a = 1. v = v4: used {} → b = 1. Same → color 1. e4 = (v4, v5): u = v4 used {1} → a = 2; v = v5 → b = 1; chain from v5 color 2: empty; assign 2. So path: colors 1,2,1,2,... no chains at all. 

To force chains, need denser structures. Chains happen when a ≠ b and v has an a-edge. Hmm. Let me think of when long chains occur: the chain from v alternates a,b,a,b... Each step moves to a new vertex. Chain length ≤ number of edges with colors in {a,b} + 1 ≤ m. For a long chain, need many edges colored a/b forming a long path. 

Adversarial construction: hmm, suppose we have a long path P = x0 - x1 - ... - x_L where edges are alternately colored a and b, and we insert a new edge (u, x0) where u is a fresh vertex... then a = smallest free at u = 1... hmm, need a to match the chain colors. This is getting deep. I'll just say: worst-case for Kempe-chain greedy is Θ(m·Δ) or at least can be superlinear; but for "typical" contest tests, it usually passes in C++ easily. In Python, risky.

Hmm, wait. Actually, let me reconsider — maybe there's a smarter, simple, provably-fast algorithm for this specific problem. Let me search memory: "bipartite edge coloring O(m log m) simple" — the Cole–Ost–Schirra algorithm is the canonical one. There's also a simpler randomized approach? 

**Option 7: Randomized / via orientation:** Hmm.

**Option 8: Reduce to bipartite matching differently — "color = matching in regular graph" via the "Δ-regularization + recursive bisection on the COLOR side":** 

Here's a classical simple reduction: bipartite edge coloring with Δ colors ⟺ decomposing into Δ matchings. Alternative: think of it as a scheduling/flow problem: each edge needs a color; at each vertex, colors are all distinct. This is exactly an edge coloring. 

**Simple O(m·√m)-ish approach via Hopcroft-Karp on an auxiliary graph?** Edge coloring bipartite graph with Δ colors can be reduced to Δ matchings via successive maximum matchings on the "color classes"... The standard incremental approach: maintain partial proper coloring with Δ colors; while uncolored edges remain: find a maximal set of uncolored edges forming a matching... no wait, that doesn't directly work because coloring a matching with one color is fine (matching edges don't share vertices), but the remaining uncolored edges must eventually be colorable. Actually here's a classical simple algorithm: **repeat Δ times: find a maximum matching among uncolored edges? No...** Hmm: Claim: if we repeatedly extract a matching that covers all vertices whose uncolored degree equals the current max uncolored degree... that's the induction again.

Simplest correct classical algorithm: **extract any maximal matching repeatedly?** That gives ≤ 2Δ - 1 colors (greedy edge coloring), not Δ.

OK here's another thought. **The "one matching per color via simple greedy with augmenting paths" (Kuhn's algorithm per color):** For color c = 1..Δ: we want to color a maximal (in the right sense) set... The classical algorithm: for each color c, find a matching that covers all vertices with uncolored-degree = remaining max... 

Alternatively **the "color one edge at a time with augmenting path in color-c space"**: For edge e = (u,v): try to find a color c free at both u and v. If none, pick color c free at u; v has c used by edge e' = (v, w); try to recolor e' with a color free at both v and w; recurse — this is exactly the Kempe chain but viewed as augmenting. Same thing.

Alright, let me now seriously consider implementing **Cole–Ost–Schirra style D&C** or the simpler variant with matching-peel, and figure out the matching-peel cost.

Actually WAIT. I just remembered a much simpler classical solution to the odd-case problem in the Euler-split D&C! Here it is:

**Trick: split into TWO parts with max degrees d1, d2 such that d1 + d2 = Δ and |d1 - d2| ≤ 1 is NOT required — instead, recurse on color ranges of matching sizes, and handle imbalance by "shifting" colors at vertices.** Hmm, no.

Let me remember the actual COS algorithm... From the paper "Edge-coloring bipartite multigraphs in O(E log D) time" by Cole, Ost, Schirra: They use "balanced edge splitting": a split of G into G1, G2 where at each vertex v, |d_{G1}(v) - d_{G2}(v)| ≤ 1, AND for vertices where d(v) is... they define "near-balanced" splits with additional properties, and they show how to compute them via Euler tours with a clever pairing of odd-degree vertices: **pair odd-degree vertices on OPPOSITE sides** — that's the key! Let me think about why.

Euler split: add dummy edges pairing odd-degree vertices (each dummy connects two odd-degree vertices), making all degrees even; each component gets an Euler tour; alternate edge colors along the tour. Result: at each vertex, red = blue = d'(v)/2 where d' includes dummies. The dummy at v is red or blue. 

Now, key insight: **if we pair odd-degree vertices such that each dummy edge connects a left vertex to a right vertex, then...** hmm, what does that give? Consider the "deficiency": at vertex v with odd d(v), real red - real blue = ±1 depending on dummy color. Define σ(v) = +1 if dummy red (real red = (d-1)/2, real blue = (d+1)/2 → blue has more)... The sum over all vertices of (red - blue) = 0 globally. Hmm.

What we want for the odd-k case: at degree-k vertices, G2 (the side with (k-1)/2 colors) must get exactly (k-1)/2 real edges. I.e., the dummy at each degree-k vertex must be on the G2 side... wait no, recompute: at degree-k vertex v, d' = k+1, red = blue = (k+1)/2. If dummy is red: real red = (k+1)/2 - 1 = (k-1)/2, real blue = (k+1)/2. So G2 = red gets (k-1)/2 ✓ (G2 needs ≤ (k-1)/2). If dummy is blue: real blue = (k-1)/2, real red = (k+1)/2; then G2 = blue at... but G2 must be a single global side. ✗. So we need ALL degree-k vertices' dummies on the same side (say red). 

Hmm, so the requirement: all degree-k vertices get their dummy colored red. In the Euler tour alternation, can we force that? The alternation along a tour: edges e1, e2, ..., e_{2t} (even length closed tour), colors alternate R, B, R, B, ... (starting choice per tour). A vertex v appears on the tour possibly multiple times (each visit uses 2 tour-edges). The dummy edge at v is one specific tour edge. Its color depends on the tour structure and starting choice. We can't independently control each dummy.

BUT: here's the COS idea (I think): **pair up the odd-degree vertices with dummy edges such that each dummy connects two odd-degree vertices of the SAME side? or OPPOSITE? and then choose tour starting colors cleverly?** Hmm, I really don't remember the details. 

Let me think about it independently. Goal: 2-color the edges (R/B) such that at every vertex v: count_R(v) ≤ ⌈d(v)/2⌉, count_B(v) ≤ ⌈d(v)/2⌉ (automatic from Euler), AND at every vertex with d(v) = k (the max, k odd): count_B(v) ≤ (k-1)/2 (i.e., dummy at v is R... wait I need to be careful about which side is which; let me define: G1 gets k1 = (k+1)/2 colors, G2 gets k2 = (k-1)/2 colors. Need count_{G2}(v) ≤ k2 for all v, and count_{G1}(v) ≤ k1. At degree-k vertices: count_{G1} + count_{G2} = k, so count_{G2} ≤ (k-1)/2 ⟺ count_{G1} ≥ (k+1)/2 ⟺ exactly (k+1)/2. So degree-k vertices must have the majority on the G1 side.)

So: find R/B coloring with: (a) at every v: count_R(v), count_B(v) ≤ ⌈d(v)/2⌉ [Euler gives this]; (b) at every v with d(v) = k odd: count_R(v) = (k+1)/2, count_B(v) = (k-1)/2 [majority R].

Via Euler with dummies: (b) means dummy at v must be B (so that real B = (k+1)/2 - 1 = (k-1)/2 and real R = (k+1)/2). Wait: d' = k+1, tour gives R = B = (k+1)/2 including dummy. If dummy is B: real B = (k+1)/2 - 1 = (k-1)/2 ✓, real R = (k+1)/2 ✓. So dummy at each degree-k vertex must be B. Hmm OK same conclusion, dummy on the G2 side... wait, now I've flipped: G2 = B side. Let me not worry about labels; requirement: **all degree-k vertices have their dummy on the same side, call it the "minority" side G2.**

Now, in the Euler tour: think of each tour as a cyclic sequence of edges with alternating colors. The dummy edges: each connects two odd-degree vertices. Suppose we pair odd-degree vertices **across sides** (left with right) — then each dummy edge is a "real-looking" edge. Hmm, why would that help? 

Alternative: think of it as a flow/matching problem on the side-assignment... 

Honestly, maybe I should look at this from the perspective of: what's the simplest provably-correct-and-fast algorithm I can implement in Python within reasonable effort? Let me reconsider.

**Reconsider: the "peel a matching covering max-degree vertices" via a simple O(m) method.** 

Claim: In a bipartite multigraph, the following finds a matching covering all max-degree vertices in O(m) expected: **randomized greedy?** Hmm no.

Hmm, what about this classical method: **A matching covering all max-degree vertices can be found by: take the edges, and compute a maximal matching in the graph restricted to... ** no.

What about: **reduce to bipartite matching where the left side is "max-degree vertices" only?** We need to cover max-degree vertices on BOTH sides. Two-phase: first find matching saturating all max-degree LEFT vertices (Hall's condition holds — proven earlier: for S ⊆ X', edges from S = Δ|S| ≤ edges into N(S) ≤ Δ|N(S)| → |N(S)| ≥ |S| ✓). This can be done via Kuhn's algorithm restricted to X' — cost O(|X'| · m)? Too slow.

Hmm wait, actually, maybe there's an Euler-tour method to find a matching covering all max-degree vertices! Let me think... 

**Theorem attempt**: Let G bipartite with max degree Δ. Split G via Euler into G1, G2 with max degrees ⌈Δ/2⌉ each. Hmm, recursively... A matching covering max-degree vertices: 

Alternative classical fact: **In a bipartite graph, the edges can be partitioned into ⌈Δ/2⌉ matchings... no, into ⌈Δ/2⌉ "2-matchings"?** Hmm: A bipartite multigraph with even max degree 2t can be split into t 2-regular... no, into 2-factors? Not exactly — components can be paths.

Hmm, let me think about the following clean recursive algorithm that avoids matchings entirely:

**Algorithm (binary color recursion, "loose" version):** solve(G, k) where maxdeg(G) ≤ k, and we have k colors available. If maxdeg(G) ≤ 1: color all with the single... wait if maxdeg ≤ 1 it's a matching, color all edges with color base. Else: split colors into k1 = ⌈k/2⌉, k2 = ⌊k/2⌋. Euler-split G into G1, G2 with maxdeg ≤ ⌈Δ/2⌉ each. Now: recurse solve(G1, k1) — fine since ⌈Δ/2⌉ ≤ ⌈k/2⌉ = k1. For G2: maxdeg(G2) ≤ ⌈Δ/2⌉ which might be > k2. **But**: if Δ ≤ k - 1... hmm we can't guarantee. 

**Fix: recurse solve(G2, max(k2, maxdeg(G2)))?** — but then G2 might use more colors than allotted, exceeding the global Δ budget? Wait — actually, does it? Let's think globally: the total color pool is Δ (global max degree). At the top: solve(G, Δ). Split k = Δ into k1 + k2 = Δ. If G2 ends up needing more than k2 colors... the colors used by G1 and G2 are disjoint ranges, total ≤ Δ only if each stays in its range. If G2 needs k2 + 1 colors, total = Δ + 1 > Δ. ✗. Unless we can "borrow"... 

Hmm, BUT: here's a classical trick — **"the union of two matchings is a set of paths/cycles; recolor"**: if G2's coloring uses one extra color, we can merge... Specifically: suppose solve(G2, k2) fails in the sense that maxdeg(G2) = k2 + 1 (only possible when k odd and Δ = k... wait maxdeg(G2) ≤ ⌈Δ/2⌉ = ⌈k/2⌉ = (k+1)/2 = k2 + 1 exactly when Δ = k, k odd). So the only bad case: k odd, Δ = k, and G2 has max degree (k+1)/2 = k2 + 1. Then G2 needs k2 + 1 colors but has k2. Hmm, what does G2 look like? At each vertex, count_{G2}(v) ≤ ⌈d(v)/2⌉. count_{G2}(v) = (k+1)/2 only at vertices with d(v) = k AND unfavorable dummy placement. 

**Patch idea**: after the Euler split, fix G2 by moving edges from G2 to G1: while G2 has a vertex x with count_{G2}(x) = k2 + 1: pick an edge e ∈ G2 at x, move it to G1. This might cause G1 vertex y (other end) to exceed k1 = (k+1)/2: count_{G1}(y) = (k+1)/2 + 1 — only if count_{G1}(y) was already (k+1)/2, meaning d(y) = k and y's split was (k+1)/2 G1, (k-1)/2 G2 — favorable. Hmm, so moving edges can cascade. But maybe a Kempe-chain-style argument bounds the cascade? This is exactly the COS "local fix" I think. 

Honestly, implementing COS in Python is a big undertaking. Let me reconsider the problem's likely origin and intended solution. 

The problem gives TL 2s and m ≤ 4·10^5. For C++, the Kempe-chain greedy (also known as the "Misra-Gries light" / standard bipartite edge coloring) is commonly used and passes easily. I strongly suspect the intended solution is the Kempe-chain greedy, and tests are not adversarial against it (it's hard to make it slow, and most test data won't). 

But in Python, even the constant factor matters. Let me think about how to implement Kempe-chain greedy efficiently in Python.

Hmm wait, actually, hold on. Let me reconsider the problem. Is it possible the graph is SIMPLE (no multi-edges)? "Next m lines: two integers u v: a test between transmitter u and receiver v." It doesn't say distinct pairs. If tests are between the same transmitter and receiver multiple times, they'd still be separate tests needing separate channels (they share both devices). The problem doesn't forbid it. To be safe, handle multigraph.

If it IS a simple graph, Δ ≤ min(nL, nR) ≤ 1e5. Doesn't change much.

Let me now think about the Kempe-chain greedy implementation in detail:

Data structures:
- For each vertex x (both sides in one array of size nL+nR), and each color c: the edge incident to x with color c. Store as: `edge_at[x][c]` — but per-vertex arrays are heavy. Alternative: since each edge has an ID, and each edge has two endpoints: `adj_color[x][c] = edge_id` or -1. Memory: Σ d(x) = 2m entries — 8·10^5 entries — fine as a dict of dicts? Too slow in Python. Better: flat arrays with per-vertex offsets? Colors up to Δ ≤ 4·10^5 — can't have array of size Δ per vertex.

Standard trick: **per-vertex dict {color: edge_id}** — 4·10^5 vertices, 8·10^5 total insertions/lookups — Python dicts: maybe OK? Each edge insertion: a few dict ops (get free color — hmm, finding a FREE color needs scanning colors not in dict...).

Alternative representation: **for each vertex, maintain arrays via "color → edge" using a global array indexed by (vertex_offset + color)?** Colors up to Δ = 4·10^5, vertices up to 2·10^5 → 8·10^10 cells. No.

Hmm. But note: at vertex x, only colors up to d(x) can ever be used... no wait, colors up to Δ can appear at x via chain swaps? A chain swap brings color a or b to x where a ≤ (colored count at u)+1... hmm, colors at x are always ≤ ??? Let me think: when we assign color a to edge (u,v): a ≤ (colored degree of u) + 1 ≤ Δ. Chain swaps move existing colors around. So colors at x ∈ [1, Δ]. But the number of colors at x at any time = colored degree of x ≤ d(x). 

For finding a free color at x quickly: maintain per-vertex "used colors" as a **Python set**? Finding the smallest free color: we know colored-degree c(x); smallest free ≤ c(x)+1. Scan colors 1, 2, 3, ... checking membership in set: O(c(x)) worst case per query → total O(Σ d(x)²) — bad for high degree.

**Better: maintain per-vertex pointer p(x)** = smallest color not yet USED-AND-NOT-FREED... The problem: chain swaps free colors below the pointer. Hmm, wait — let me look at the chain swap more carefully: at internal chain vertices, the color SET is unchanged. At the two endpoints: v (the right endpoint of the new edge) loses color a gains color b; the far endpoint x_k loses one of {a,b} gains the other. So per chain swap, only TWO vertices change their color sets, and in each case it's a swap of two colors (set size unchanged). When we then assign color a to the new edge at u and v: u gains a, v gains a (v had lost a in the swap). 

So per edge insertion: u's set gains a (size +1); v's set: net effect — the swap removed a and added b, then adding a: net +1 size, and b added. Hmm wait: v's set before insertion: S. After swap: S - {a} + {b}. After assigning new edge color a: S + {b}. So v gained b (if b ∉ S — yes b was free at v). 

So: per insertion, each of u, v gains exactly one color (a at u... wait u gains a; v gains b). Plus chain-internal vertices: sets unchanged. Chain endpoints: v: -a +b (then +a from new edge → net +b); far endpoint x_k: swaps one color for another (set size unchanged, but contents change!). Hmm, so the far endpoint's set contents change — a color below its pointer might become free. So pointers can be invalidated at far endpoints. 

How often and does it matter? If we maintain pointer p(x) with invariant "all colors < p(x) are used at x" — the far endpoint swap breaks it potentially. To restore, we'd set p(x) = min(freed color, p(x))... but then p(x) might oscillate. The amortized argument: p(x) only decreases when a chain endpoint swap frees a small color at x. Hmm, hard to bound.

**Alternative: don't maintain smallest free color; maintain "some free color" lazily with a different scheme:** For finding free colors, use the classical trick from Vizing's algorithm implementations: maintain per vertex an array `first_free[x]`... 

Hmm, let me think about a DIFFERENT, much more Python-friendly algorithm. 

**Option 9: Sort-based / "matrix" approach?** Hmm.

**Option 10: Think about the problem as scheduling on bipartite graph = "Latin square completion"?** No.

**Option 11: Use the D&C Euler-split but handle the odd case by "don't care" trick:** Wait, actually, let me revisit. Maybe there's a neat way to handle odd k in the D&C without matchings:

solve(G, k): if k == 1: color all edges color 1 (G is a matching). If k ≥ 2: 
- If k is even: Euler split → G1, G2, each maxdeg ≤ k/2. Recurse solve(G1, k/2) [colors 1..k/2], solve(G2, k/2) [colors k/2+1..k]. ✓.
- If k is odd: k = 2t+1. Euler split → G1, G2 each maxdeg ≤ t+1. Recurse solve(G1, t+1) [colors 1..t+1], solve(G2, t) [colors t+2..2t+1]. G2 might have maxdeg t+1 > t. ✗.

BUT: what if instead, for odd k, we split into G1 with maxdeg ≤ t+1 and G2 with maxdeg ≤ t directly by a **modified Euler split where we get to choose the majority side per vertex consistently**? The requirement again: at degree-k vertices, G2 ≤ t. As established: need all degree-k vertices' dummies on the G2 side... 

Hmm wait, actually, WAIT. Let me reconsider. What if we add dummy edges to make the graph k-REGULAR-ish? Alternative: **pad the graph to make Δ even!** If k is odd, add ONE dummy edge... no. Hmm: **Pad G to a bipartite multigraph G⁺ with max degree k where... ** hmm what property would help? 

**IDEA**: If k is odd, add a dummy vertex pair and dummy edges to make the graph have ALL degrees even and max degree k+1?? Then Euler split gives two parts with max degree (k+1)/2 each, and we'd recurse with k+1 colors... but we only have k. ✗.

**IDEA 2**: If k is odd: first, **peel ONE matching greedily — not covering max-degree vertices, but ANY maximal matching? No...** Hmm, what if we peel a matching covering max-degree vertices found by a simple algorithm: 

**Simple algorithm to find matching covering all max-degree vertices — via Euler split recursion!** Claim: matching covering all max-degree vertices can be found via: if Δ ≤ 1: all edges form a matching? (Δ=1: graph is a matching, take all edges.) Else Euler split into G1, G2 with maxdeg ⌈Δ/2⌉. Recursively find M1 covering max-degree vertices of G1, M2 covering max-degree of G2. M = M1 ∪ M2 — is it a matching? M1 and M2 are edge-disjoint (G1, G2 disjoint), but they might share VERTICES (a vertex matched in M1 and also in M2). ✗. Hmm.

OK here's yet another angle. **Option 12: Reduce to "Δ matchings" via the classical "regularization + recursive bisection" but on the VERTEX side?** 

Hmm, let me look up my memory of actual contest solutions for bipartite edge coloring with these constraints (n ≤ 1e5? m ≤ 4e5?). Hmm... I now strongly suspect this is **Codeforces Problem "1738?"**... or maybe it's from **"ICPC 2023"?** Actually — "Problem B — Signal Calibration in a Two-Sided Array" — this looks like it's from a specific recent contest, possibly a mirror of an ICPC regional or the "Universal Cup". The phrase "two-sided array" and the story about transmitters/receivers... The guarantee "(Because the array is strictly two-sided, this optimal configuration is always achievable; no channel beyond the busiest-device count is ever required.)" is a big hint that the intended solution is exactly König's theorem edge coloring.

Given m ≤ 4·10^5 and TL 2s (typical for C++ with O(m log m) or even O(m√m)), and we need Python... The safest bet for Python: implement the Kempe-chain greedy with efficient data structures, hoping tests aren't adversarial, OR implement the D&C Euler split properly.

Hmm, hold on, let me reconsider the D&C once more. I want to find a clean way to handle odd k. Let me think about the structure differently:

**Reformulate D&C on "color intervals" with per-vertex degree constraints — the "flow" view:** We need to assign each edge a color; at each vertex x, the multiset of colors on its incident edges must be distinct, i.e., an injective assignment from incident edges to [1..Δ]. 

D&C: given interval of colors [lo, hi] (size k) and edge set E' with maxdeg ≤ k: split E' into two parts with maxdeg ≤ sizes of the two sub-intervals. The Euler split gives both parts ≤ ⌈maxdeg/2⌉... The mismatch is only at the top of the range. 

**KEY REALIZATION**: What if we choose the split sizes NOT as ⌈k/2⌉/⌊k/2⌋ but based on actual degrees: we need a split where part i gets ≤ k_i edges at each vertex. The Euler split gives ≤ ⌈d/2⌉ at each vertex for both parts. If we could get a split with part1 ≤ ⌈d/2⌉ and part2 ≤ ⌊d/2⌋ at every vertex... that's exactly the "controlled" split. For even d, ⌈d/2⌉ = ⌊d/2⌋ — Euler gives exactly d/2 each ✓. For odd d: Euler gives one part (d+1)/2 and the other (d-1)/2, but WHICH part gets the extra depends on the dummy color. So the controlled split = Euler split where we can choose, per odd-degree vertex, which side gets the extra — but with a consistency constraint? Is there one? 

Think of it as: we need a 2-coloring of edges such that at each vertex v: count_1(v) = ⌈d(v)/2⌉ or ⌊d(v)/2⌋ as we CHOOSE per vertex (for the odd case: at degree-k vertices choose part1 = (k+1)/2; at other odd-degree vertices, either is fine since both ⌈d/2⌉, ⌊d/2⌋ ≤ needed bounds? wait, we need part2 ≤ ⌊k/2⌋ at ALL vertices: at vertex with d ≤ k-1: part2 ≤ ⌈d/2⌉ ≤ ⌈(k-1)/2⌉ = (k-1)/2 ✓ regardless. And part1 ≤ (k+1)/2: at any vertex, part1 ≤ ⌈d/2⌉ ≤ ⌈k/2⌉ = (k+1)/2 ✓. So the ONLY constraint beyond Euler: at degree-k vertices, part2 ≤ (k-1)/2, i.e., part1 = (k+1)/2 (majority part1).)

So: **Question: given bipartite multigraph G with odd max degree k, can we always 2-split edges such that every vertex v has part1(v) = ⌈d(v)/2⌉, part2(v) = ⌊d(v)/2⌋ — i.e., ALL odd-degree vertices put the extra edge in part1?** If yes, we get a clean recursion: solve(G, k): split with part1 = ⌈d/2⌉ at every vertex, recurse solve(part1, ⌈k/2⌉), solve(part2, ⌊k/2⌋). Wait, but then part1 has maxdeg ⌈Δ/2⌉ ≤ ⌈k/2⌉ ✓ and part2 maxdeg ⌊Δ/2⌋... at vertices with d = k: part2 = (k-1)/2 = ⌊k/2⌋ ✓; at d ≤ k-1: part2 ≤ ⌊d/2⌋ ≤ ⌊(k-1)/2⌋ = ⌊k/2⌋ ✓. 

So the whole algorithm reduces to: **"Perfectly controlled Euler split": 2-color edges so that at EVERY vertex v, part1(v) = ⌈d(v)/2⌉, part2(v) = ⌊d(v)/2⌋.** (Then both parts have max degree ≤ ⌈Δ/2⌉ and ≤ ⌊Δ/2⌋... wait part1 max = ⌈Δ/2⌉, part2 max = ⌊Δ/2⌋? At vertex with d = Δ: part2 = ⌊Δ/2⌋ ✓; other vertices: part2 = ⌊d/2⌋ ≤ ⌊Δ/2⌋ ✓. And part1 = ⌈d/2⌉ ≤ ⌈Δ/2⌉ ✓.) Then recurse with k1 = ⌈k/2⌉ ≥ ⌈Δ/2⌉... wait need part1 maxdeg ≤ k1: ⌈Δ/2⌉ ≤ ⌈k/2⌉ ✓ since Δ ≤ k. And part2 maxdeg = ⌊Δ/2⌋ ≤ ⌊k/2⌋ = k2 ✓. 

So the recursion works with the perfectly controlled split. Now: does such a split always exist, and how to compute it fast?

**Existence**: We want a 2-edge-coloring (R/B) with count_R(v) = ⌈d(v)/2⌉ for all v. Hmm. This is a "balanced edge 2-coloring with prescribed imbalances". Think of it as a flow problem: orient... Let's model: assign each edge R or B. At vertex v: (#R - #B) = ε(v) where ε(v) = 0 if d(v) even, 1 if odd. Σ_v ε(v) over all vertices = number of odd-degree vertices = even (handshaking). Is it always feasible? Consider modeling as: R/B assignment = orientation-like problem. Alternative model: think of R as "+1" and B as "−1" on each edge; at each vertex, sum of incident signs = ε(v) ∈ {0, 1}. Hmm, each edge contributes +1 to one endpoint and... no wait, an edge colored R contributes +1 to BOTH endpoints (count_R at both u and v). Hmm, so it's not a flow. Let me re-model: Let x_e ∈ {0, 1} (1 = R). At vertex v: Σ_{e ∋ v} x_e = ⌈d(v)/2⌉. This is a bipartite b-matching / flow problem: variables on edges, constraints at vertices. Feasibility: This is an integer program; the constraint matrix is the incidence matrix of a bipartite graph — totally unimodular! So LP relaxation integral; feasibility by Hall-like conditions. Is it always feasible? Hmm, consider a single edge (u,v), d(u) = d(v) = 1: need x = 1 (R) at both — consistent since the edge is R: count_R(u) = 1 = ⌈1/2⌉ ✓. Consider path of length 2: u1 - v1 - u2? wait bipartite: edges (u1, v1), (u2, v1). d(v1) = 2 → needs exactly 1 R among its 2 edges. d(u1) = d(u2) = 1 → each needs its single edge R. But v1 can have only 1 R. Contradiction!! So NOT always feasible. ✗✗.

Right — so the perfectly controlled split doesn't always exist. (Path u1-v1, u2-v1: u1, u2 need their edges R; v1 needs one R one B — impossible.) OK so scrap that; the constraint must be relaxed: we only need control at degree-k vertices (k = odd max). In the path example with k = 2 (even) — no control needed. Let me re-examine: we need at degree-k vertices part1 = (k+1)/2; at other vertices any split with each part ≤ ⌈d/2⌉. Is THAT always feasible? Hmm, consider: k = 3. Vertices: u1 with edges to v1 (×3)? d(u1) = 3 = k, d(v1) = 3 = k. Need part1(u1) = 2, part1(v1) = 2. Total part1 edges counted from left = 2, from right = 2 ✓ consistent. Edges: 3 parallel; part1 gets 2 of them, part2 gets 1. ✓ feasible. 

Another: k = 3: left u1: edges to v1, v2, v3 (d=3). v1: edges from u1, u2, u3 (d=3). u2: edge to v1 only (d=1). u3: edge to v1 (d=1). v2, v3: edge from u1 (d=1). Degree-3 vertices: u1, v1 — need part1 = 2 each. Edges: (u1,v1), (u1,v2), (u1,v3), (u2,v1), (u3,v1). part1 must contain exactly 2 edges at u1 and exactly 2 at v1. E.g., part1 = {(u1,v2), (u1,v3), (u2,v1), (u3,v1)}: at u1: 2 ✓; at v1: 2 ✓. part2 = {(u1, v1)}: at u1: 1 ≤ ⌈3/2⌉... wait part2 at u1 = 1, fine; at v1 = 1 fine. ✓ feasible.

Is it always feasible when only max-degree vertices are controlled? Hmm, consider k odd, and a vertex u with d(u) = k whose neighbors all have degree 1... then part1(u) = (k+1)/2 edges go to (k+1)/2 distinct neighbors, each of which then has part1 = 1 = ⌈1/2⌉ ✓ fine (neighbors degree 1: part1 ≤ 1, part2 ≤ 1 — no constraint violated). Feasible.

Potential infeasibility: need to check Hall-type condition. The flow model: bipartite incidence structure, supplies... Let me think of it as b-matching: we need to select a subset F ⊆ E (part1) with |F ∩ δ(v)| = ⌈d(v)/2⌉ for v ∈ V_max (degree-k vertices), and ⌊d(v)/2⌋ ≤ |F ∩ δ(v)| ≤ ⌈d(v)/2⌉ for others. Feasibility of such "degree-constrained subgraph" in bipartite multigraph: by a theorem (folklore), a degree-constrained subgraph exists iff cut conditions hold: for all A ⊆ X, B ⊆ Y: ... the condition for f(v) ≤ d_F(v) ≤ g(v): F exists iff for all A ⊆ X, B ⊆ Y: e(A, B) ... hmm, the condition: Σ_{v ∈ A∪B} f(v) ≥ ... I recall the condition for the existence of subgraph with lower bounds l(v) ≤ d_F(v) ≤ u(v) in bipartite graph: for all A ⊆ X, B ⊆ Y: e(A, Y∖B) + ... this is getting heavy. Let me just test a potentially bad case:

k = 3. Suppose X-side max-degree vertices: u1, u2, u3 each with degree 3, all edges to {v1} — wait v1 would have degree 9 > k. Not allowed (max degree 3). So neighbors of max-degree vertices have bounded degrees. Hmm, consider: u1, u2, u3 (degree 3 each), v1, v2, v3 (degree 3 each), edges = perfect matching-ish: u1: v1,v2,v3; u2: v1,v2,v3; u3: v1,v2,v3 (K3,3). k=3, all vertices max-degree. Need part1 = 2 at every vertex: a 2-regular subgraph of K3,3 — exists (e.g., a 6-cycle) ✓.

Try to break it: we need part1(v) = (k+1)/2 at all degree-k vertices. Sum over left max-degree vertices of part1 = Σ (k+1)/2; these part1-edges land on right vertices, each right vertex w can accept at most ⌈d(w)/2⌉ ≤ (k+1)/2. Total capacity on right: Σ_{w ∈ Y} ⌈d(w)/2⌉. Need Σ_{u ∈ X_max} (k+1)/2 ≤ Σ_{w∈Y} ⌈d(w)/2⌉? Hmm: Σ_{u ∈ X_max} (k+1)/2 = (k+1)/2 · |X_max|. And Σ_{w ∈ Y} ⌈d(w)/2⌉ ≥ Σ_w d(w)/2 = (Σ_{u ∈ X} d(u))/2 ≥ (k·|X_max|)/2. Is (k+1)/2·|X_max| ≤ k|X_max|/2 + (something)? (k+1)/2 · |X_max| vs k/2·|X_max|: LHS is bigger by |X_max|/2. So need the extra from ⌈·⌉ rounding: Σ_w ⌈d(w)/2⌉ = Σ_w d(w)/2 + (#odd-degree w in Y)/2. So need (k+1)|X_max|/2 ≤ Σ_X d(u)/2 + odd(Y)/2. Σ_X d(u) ≥ k|X_max| + (other left vertices' degrees ≥ 0). Hmm, so need (k+1)|X_max| ≤ Σ_X d(u) + odd(Y) — i.e., |X_max| ≤ (Σ_X d - k|X_max|) + odd(Y) = (edges not at X_max... ) + odd(Y). Hmm, this could fail! Example: k = 3, X = {u1} with d = 3 (edges to v1, v2, v3), Y = {v1, v2, v3} each d = 1. odd(Y) = 3. |X_max| = 1 ≤ 0 + 3 ✓. Another: k=3, X = {u1, u2}, u1: v1,v2,v3; u2: v1,v2,v3. Y: v1,v2,v3 each d=2. odd(Y) = 0. |X_max| = 2. Σ_X d - k|X_max| = 6 - 6 = 0. Need 2 ≤ 0 + 0? ✗!! So infeasible?! Let me double check: k = 3, u1 and u2 each connected to v1, v2, v3 (K2,3). Degrees: u1 = u2 = 3 = k; v1 = v2 = v3 = 2. Need part1(u1) = 2, part1(u2) = 2 → total part1 edges = 4. But part1(v_i) ≤ ⌈2/2⌉ = 1 → total part1 edges ≤ 3. 4 > 3 — INFEASIBLE. 

So the controlled split is NOT always possible. Hence the odd case genuinely requires something else (like peeling a matching first). In this K2,3 example: peel matching covering u1, u2: e.g., {(u1,v1), (u2,v2)}; remaining: u1: v2,v3; u2: v1,v3; v1: u2; v2: u1; v3: u1,u2 — max degree 2. Then color with 2 colors. Total 3 ✓.

OK so the odd case needs the matching peel. And finding that matching requires bipartite matching computation. Hmm, BUT — maybe there's a cheap way to find a matching covering all max-degree vertices in this specific D&C context... 

**AH WAIT.** I remember now! There's a classical trick: **a matching covering all max-degree vertices can be found via the Euler split recursively!** Here's the idea: 

To find a matching covering all vertices of degree Δ in bipartite multigraph G:
- If Δ = 1: return all edges (it's a matching).
- Euler split G into G1, G2, each with max degree ≤ ⌈Δ/2⌉. Hmm, then recursively find matchings covering max-degree vertices of G1 and G2... but they may conflict at vertices. ✗ as noted.

Hmm. Alternatively: **via "2-edge-coloring into two classes where each class's max degree ≤ ⌈Δ/2⌉" repeated until... ** no.

**Alternative: find the matching covering max-degree vertices via ONE Euler tour trick:** Consider the subgraph H induced by... hmm. Let me think about K2,3 and see what structure the matching has. 

Actually, here's a classical fact: **In any graph, the edges can be split into ⌈Δ/2⌉... no. In any bipartite multigraph, E splits into Δ matchings (König). The FIRST matching in a König decomposition can be chosen to cover all max-degree vertices.** Constructively via augmenting paths = bipartite matching. The question remains cost.

**Cost of bipartite matching here:** We need matchings at O(log Δ) recursion levels. At each level, the graph has ≤ m edges total across all subproblems. If each matching computation is O(edges · something)... Hopcroft-Karp is O(E√V) — too slow in Python. Kuhn's is O(V·E) — way too slow.

Hmm, is there a way to find a matching covering all max-degree vertices in near-linear time for bipartite multigraphs? I believe YES — this is exactly part of the COS algorithm: they compute such matchings in linear time via Euler tours. Let me think about how...

**Linear-time matching covering max-degree vertices — attempt:** Let G have max degree Δ. Consider the Euler split into G1, G2 with max degrees ≤ ⌈Δ/2⌉. Hmm... 

Alternative idea: **Reduce to finding a perfect matching in a regular bipartite graph, which CAN be done in linear time... no wait, perfect matching in regular bipartite graphs — there's the classical result that d-regular bipartite graphs have perfect matchings findable via... the "power of two choices"? Actually, there IS a classical near-linear randomized algorithm for perfect matching in regular bipartite graphs (Goel, Kapralov, Khanna 2010?), but that's complex.**

Hmm OK, let me step back and think about what's PRACTICAL. 

Given the difficulty of implementing COS in Python, and the risk of the Kempe-chain greedy blowing up on adversarial tests, let me estimate the Kempe-chain greedy's practical performance more carefully, and think about whether its worst case can be bounded with good choices.

**Kempe-chain greedy with smart choices:** There's a classical optimization: process edges in a good ORDER. For instance, process edges grouped by... Hmm. Also, the choice of free colors a and b matters.

Actually — hmm, wait. Let me reconsider the problem constraints once more: nL, nR ≤ 1e5, m ≤ 4e5. If the graph is SIMPLE (no repeated (u,v) pairs — plausible for "tests" though not guaranteed), then Δ ≤ min(nL, nR) ≤ 1e5. Still large.

Let me think about the worst case of Kempe-chain greedy more concretely. When we insert edge (u, v) and walk a chain of length L, we recolor L edges. The chain walk cost O(L). Total cost Σ L_i. Is there a potential function argument? Each swap... hmm. I recall that for the analogous "Vizing's theorem" greedy, the bound is O(mn). For bipartite, I genuinely don't know a better worst-case bound than O(mΔ). 

Let me think about whether tests for this problem could be adversarial vs. Kempe chains. If the intended solution IS Kempe chains (common for such problems), tests won't kill it. If the intended solution is COS-style D&C, tests MIGHT kill Kempe chains. Hmm.

Hmm, let me think about the actual source. "Problem B — Signal Calibration in a Two-Sided Array", TL 2s, ML 256MB, nL,nR ≤ 1e5, m ≤ 4e5. This REALLY looks like **Codeforces Gym / Universal Cup problem**... Actually! I think I remember: this might be from **"The 3rd Universal Cup. Stage ..."** or from **Petrozavodsk / an Opencup**. "Simulated contest"... The structure "Problem B" with this flavor... 

Alternatively it could be from the recent **Codeforces Round (Div. 1) problem "Yet Another Edge Coloring"?** Hmm, there's CF 1619? no... There's **CF problem 2023 "Bipartite coloring?"**... I can't place it exactly. Let me just consider: many "edge coloring bipartite graph" contest problems exist with m up to 5·10^5 and the accepted solutions use the Kempe-chain greedy (e.g., **Codeforces 1337?** hmm, "E. Edge coloring?"...). 

Actually, I recall **Codeforces Problem 608D?** no. **"Zuma"?** no. Let me recall a specific one: **CF Round #700? "1517?"** Hmm. There's definitely a well-known one: **"Codeforces 1462F"?** no. OK whatever.

Let me also consider: maybe the intended solution is the **O(m√m) "matching per color via simple augmenting"**: For each color c from 1 to Δ: hmm no.

Actually — here's ANOTHER classical simple algorithm I should remember: **Bipartite edge coloring via "orientation + list coloring"?** Hmm no.

**Let me look at the Kempe-chain greedy from the "amortized" perspective with a specific good implementation choice:** 

There's a classical trick to make the greedy provably O(m log m)?? Hmm... Actually, you know what — I recall that the Kempe chain algorithm for bipartite graphs, when you process edges in an order such that... and choose colors carefully... there's the "Bollobas?" ... I can't recall a clean bound. 

DECISION TIME. Let me weigh:

1. **Kempe-chain greedy**: simple, likely fast in practice (chains usually short), risk of TLE on adversarial tests, and in Python constant factors matter. Implementation with per-vertex color→edge maps.

2. **D&C Euler split with matching-peel**: provably O(m log Δ), but needs a bipartite matching subroutine for max-degree-vertex cover at odd levels — expensive/complex.

3. **D&C Euler split WITHOUT peel, using a different fix for odd k**: Let me think once more...

Hmm wait, actually — here's a cleaner fix for the odd case that avoids matchings! **When k is odd, split the color range as k1 = (k+1)/2, k2 = (k-1)/2, and Euler-split edges into G1, G2 with BOTH max degrees ≤ (k+1)/2. Then recurse solve(G1, k1) and solve(G2, k2) — but before recursing on G2, FIX G2: if maxdeg(G2) = (k+1)/2 > k2, we need to reduce G2's max degree. Note maxdeg(G2) ≤ ⌈Δ/2⌉ and Δ ≤ k. If Δ ≤ k-1: maxdeg(G2) ≤ ⌈(k-1)/2⌉ = (k-1)/2 = k2 ✓ no fix needed. So fix needed only when Δ = k. In G2, vertices with degree (k+1)/2: these are vertices where d_G(x) = k and the dummy went unfavorably. Hmm, fix = move edges from G2 to G1 along alternating paths — Kempe chains again, but on the SPLIT (not colors). The structure: consider the "split graph" where each vertex has G1-degree and G2-degree. Bad vertices: G2-degree = (k+1)/2. Moving an edge e=(x,y) from G2 to G1: decreases G2-degree of x,y; increases G1-degree. G1-degree at x: was ≤ (k+1)/2; if it becomes (k+2)/2 > k1 — bad. So we can only move edges from bad vertices to vertices with G1-degree < (k+1)/2... and if y also is bad (G2-degree (k+1)/2) then moving helps y too, but if y has G1-degree = (k+1)/2 (i.e., d(y) = k, favorable split), moving e to G1 overflows y. Then we'd need to move another edge out of y in G1 to G2... alternating path in the "G1/G2" split — this is EXACTLY a Kempe chain on the 2-colored split, and the parity argument: does it terminate? The alternating path from x alternating G2, G1, G2, G1... in a bipartite graph... hmm, this could cycle. This is precisely the intricate part of COS. They show it works with careful rules ("push" operations with potentials). Too complex for a Python contest solution written blind.

4. **A completely different practical approach: "Color = (index within vertex) via sorting" — the "de Bruijn / round-robin" idea for REGULAR bipartite graphs!** 

WAIT. Here's a classical BEAUTIFUL simple approach for bipartite edge coloring that I should seriously consider: **the "round-robin tournament" / "1-factorization via cyclic shifts" works for COMPLETE bipartite regular graphs, but for general bipartite graphs there's the classical reduction: regularize the graph, then... ** hmm, regularization requires matchings again.

5. **Practical hybrid: Use Kempe-chain greedy but with a twist that makes worst cases rare, plus micro-optimizations.** 

6. **Think again about whether there's a simple O(m·something-small) deterministic algorithm...**

Hmm, actually, WAIT. Let me reconsider the problem from scratch. Let me re-read the constraints: nL, nR ≤ 1e5, m ≤ 4e5. Time 2s. For PYTHON. Honestly, even reading input fast matters (4·10^5 lines). 

Let me now think REALLY carefully about the most Python-efficient correct algorithm. Let me reconsider... 

**IDEA: "Vertex-by-vertex insertion with Kempe chains" = the classical O(mΔ) but with chains implemented via arrays and the observation that total chain length might be small in practice.** 

vs.

**IDEA: Reduce to Δ matchings via a DIFFERENT classical decomposition: "Edge coloring bipartite graph = scheduling; use the 'Hungarian' / 'SAP' on colors incrementally" — the "color-by-color" approach:** 

For c = 1, 2, ..., Δ: we assign color c to a matching M_c in the remaining graph, where M_c must cover all vertices whose REMAINING degree equals the remaining max degree... The classical incremental version: process colors one at a time; for color c, find a matching covering all vertices with remaining degree = Δ - c + 1 (i.e., vertices that still need... hmm). Actually here's the classical scheme: remaining graph R_1 = G. For c = 1..Δ: find matching M_c covering all max-degree vertices of R_c; R_{c+1} = R_c - M_c. Each such matching computation is a bipartite matching problem (saturating a set). Total cost: Δ matching computations — way too slow.

**IDEA: "Chernykh's algorithm"?** Hmm.

**IDEA: Randomized: assign each edge a random color from available... no.**

OK let me now think about the practical performance of Kempe-chain greedy on plausible test data, and how to implement it FAST in Python.

Implementation plan for Kempe-chain greedy:

- Vertices: 0..nL-1 (left), nL..nL+nR-1 (right). 
- For each vertex x: a mapping color → edge index. To make it fast: use a single dict per vertex? Or a global dict keyed by (x * BIG + color)? Global dict with tuple keys is slow. Per-vertex dicts: `inc[x]` = dict {color: edge_id}. Operations per edge insertion: 
  - find smallest free color at u: need "smallest color not in inc[u]". 
  - Same at v.
  - Chain walk: at current vertex x, look up inc[x].get(a) etc.

Finding smallest free color: maintain per-vertex "next candidate" pointer p[x] with the invariant... as discussed, chain swaps can free colors below p[x] at the far endpoint. Hmm, but WAIT — let me re-examine: in the chain swap, which vertices have their color sets changed? v (near endpoint): loses a, gains b (then gains a back when the new edge is colored — net: gains b). Far endpoint x_k: loses color c_k ∈ {a,b}, gains the other. So the far endpoint's set changes by one swap. If c_k = a (x_k's chain edge was color a, becomes b): x_k loses a, gains b. If a < p[x_k], then now a is free below the pointer. If we DON'T reset the pointer, we might miss that a is free — but that's fine for CORRECTNESS (we just need SOME free color; the pointer approach finds colors ≥ p[x]... wait, no — the pointer approach needs the invariant "all colors < p[x] are used" to guarantee that scanning from p[x] finds a free color quickly? Actually no! The pointer approach works differently: we scan upward from p[x] until finding a color not in inc[x]; the scan length is the number of CONSECUTIVE used colors starting at p[x]. If colors below p[x] are free, we don't care — we just might use a slightly larger color than necessary. The concern is only: does the color we find exceed Δ? Since #used at x ≤ d(x) ≤ Δ, scanning from ANY start point p: the colors p, p+1, ..., we'll find a free one by color d(x)+1 at the latest... wait: among colors 1..d(x)+1 there's a free one; scanning from p ≤ that... if p > d(x)+1 we'd have a problem, but p only advances past colors we've verified used, and #used ≤ d(x), so p ≤ d(x)+1 always? Hmm: p advances only when we confirm colors p, p+1, ... are used at x. Since at most d(x) colors are used at x, p can never exceed d(x)+1. ✓. So scanning from p[x] always finds a free color within [p[x], d(x)+1]. The scan cost: number of consecutive used colors from p[x]. Amortized: each successful scan step advances p permanently... but chain swaps can RE-ADD colors below p (freeing them) — that doesn't hurt p's monotonicity. But chain swaps can also REMOVE colors above... hmm wait, can a chain swap remove a used color at x that is ≥ p[x], making the scan... that only makes scans faster. Can a chain swap ADD a used color at x ≥ p[x]? Yes: far endpoint gains color b (say) which might be ≥ p[x] and previously free — then a later scan from p[x] hits b as used — fine, just scans past it. The amortized argument breaks (p can get stuck scanning over colors that were added by swaps), but each swap adds at most ONE new color per endpoint... Total added colors via swaps ≤ 2 per insertion... hmm, so scan cost per insertion ≤ (advance of p) + (number of swap-added colors in the scanned range) ≤ amortized fine: total scan cost O(m + total chain lengths)? Roughly: each scanned position either advances p (total O(Σ d(x)) = O(m) over all) or is a color added by a swap at that vertex (total additions ≤ 2 per chain per endpoint... per insertion, the far endpoint gains 1 color, v gains 1 color (b) — but v's gain b: b < ... hmm b is free at v and b ≤ d(v)+1...). OK, roughly the pointer scheme gives near-linear total scan cost. 

Wait, but there's a subtlety: after the chain swap, at the far endpoint x_k, a color was freed (c_k) and another added. If c_k < p[x_k], the freed color is below the pointer — we never rescan below p, fine. The added color might be < p[x_k] too?? If the added color b < p[x_k] and b was free — then now a color below p is used — invariant "all below p are used" still holds (it was already used... no wait, b was FREE at x_k before (that's why the chain stopped at x_k: x_k had no b-edge). If b < p[x_k], then previously "all colors < p[x_k] used" was VIOLATED already? No — the invariant I'm using is just "p[x] ≤ (number of used colors at x) + 1" to guarantee the scan terminates by d(x)+1. Adding a used color below p doesn't break that. Removing a used color below p (freeing c_k < p[x_k]) doesn't break it either. The scan from p[x] upward: terminates at first free color; guaranteed ≤ (used count)+1 ≤ d(x)+1 ≤ Δ+1... but we need ≤ Δ: used count at x when we're coloring an incident edge = d_colored(x) ≤ d(x) - 1 (since this edge is incident and uncolored), so free color found ≤ d_colored(x) + 1 ≤ d(x) ≤ Δ ✓.

So per insertion: two scans (from p[u], from p[v]) with amortized-small cost, plus the chain walk O(L). 

Chain walk implementation: at vertex x, need edge of color a: inc[x] dict lookup. Then move to other endpoint of that edge. Then look up color b there, etc. Each step: 2 dict lookups (get color edge at x, then at next vertex). Plus recoloring: update inc at both endpoints for each chain edge (remove old color, add new). So chain of length L costs ~O(L) dict operations (each O(1) amortized but with Python overhead ~100ns+ each... more like 50-150ns for dict get/set on ints).

Total: m insertions × (constant work ~ 20-40 dict/array ops) + Σ chain lengths × ~6-8 ops. If Σ L ~ O(m) on typical tests, total ~ maybe 4·10^5 × 30 = 1.2·10^7 dict ops → ~2-4 seconds in CPython. Hmm, borderline. With PyPy it'd fly, but we must assume CPython? The problem says "Python 3". Typically these are judged with CPython 3 (or PyPy allowed?). I should write the fastest possible CPython code, possibly using arrays (lists) instead of dicts where possible, and minimizing overhead. 

Hmm, wait — maybe there's an approach with much lower constant: **vectorized / sorting-based**? Let me think about whether the D&C Euler-split can be implemented with sorting-like batch operations (which Python does well via built-in sorts)... Euler tours are inherently sequential (linked-list traversal). Hmm.

Hmm, hold on, hold on. Let me reconsider the D&C approach once more, because there might be a neat way to handle EVERYTHING with Euler splits only, avoiding matchings — I recall something: **the trick of splitting into parts with max degrees d1, d2 where d1 + d2 = Δ but not necessarily balanced — specifically "split off a small matching-like piece"?** 

Alternatively — **THE STANDARD TRICK I NOW REMEMBER**: In the D&C, don't split the color range by halving k; instead, **split the DEGREES**: solve(G, k) [maxdeg ≤ k]: if maxdeg(G) = Δ' ≤ 1: done. Split colors as k1 = ⌈Δ'/2⌉... no wait, we should split based on Δ' (actual max degree), not k! Let me redo: solve(G, color range of size k) with maxdeg(G) = Δ' ≤ k. If Δ' ≤ 1: color all with first color. Else: Euler split G → G