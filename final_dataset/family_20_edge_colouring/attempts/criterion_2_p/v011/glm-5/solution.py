This is a classic edge coloring of bipartite graphs problem. By König's theorem, the edge chromatic number of a bipartite graph equals the maximum degree Δ. We need to find a proper edge coloring with Δ colors in a bipartite graph with nL vertices on the left, nR on the right, and m edges.

Constraints: nL, nR up to 100000, m up to 400000. Time limit 2s. We need an efficient algorithm.

The standard approach for bipartite edge coloring in O(m log Δ) or O(m Δ) is the "Euler split" / "binary splitting" technique, or the simpler approach using the Hungarian algorithm-like chain arguments (O(m Δ) which could be 400000 * Δ... Δ could be up to 100000, so that's too slow).

Better approach: The classic algorithm by Cole, Ost, Schirra for bipartite edge coloring in O(m log Δ). Alternatively, there's a simpler approach:

Approach 1: Euler split technique. Recursively: given a graph with max degree Δ, split edges into two sets E1, E2 such that each vertex has degree in E1 equal to floor(d/2) or ceil(d/2). This is done by pairing edges at each vertex (Eulerian decomposition): at each vertex, pair up incident edges arbitrarily (if degree is odd, one edge is left unpaired... actually the standard technique: make the graph Eulerian by adding a dummy vertex, then find Euler tours, then alternate edges along tours into two sets). Then recurse on each set with ceil(Δ/2) colors. Depth is log Δ, each level takes O(m) work, total O(m log Δ). With m = 400000 and log Δ ≈ 17, that's about 7 million edge operations per level... total ~ 400000 * 17 = 6.8M operations, quite feasible in Python if implemented carefully? Hmm, Python is slow; 6.8M operations with list manipulation might be ~10-30 seconds. Need to be careful.

Actually, let me think about the recursion more carefully. At each level of recursion, the total number of edges across all subproblems is m. The depth is log2(Δ) ≈ 17. So total work is O(m log Δ) ≈ 6.8M edge visits. In pure Python, each edge visit might involve several list operations, so maybe 20-50M elementary operations. That could be 20-60 seconds in CPython. Hmm, risky.

Alternative: There's a simpler well-known approach for this specific problem. Actually, this problem is essentially "edge coloring bipartite graph with Δ colors". 

Wait — there's a much simpler observation. In a bipartite graph, we can edge-color with Δ colors using a simple greedy with recoloring chains (like the "Vizing's theorem for bipartite graphs" constructive proof). The standard constructive proof: process edges one by one; for each edge (u,v), find a color free at u and a color free at v. If they coincide, use it. Otherwise, there's a color a free at u but used at v, and color b free at v but used at u. Then follow the "Kempe chain": in bipartite graphs, the chain of alternating colors a,b starting from v is a path (not a cycle), so we can swap colors along the path and free up color a at v (or b at u). This is the standard O(m * Δ) algorithm in the worst case (each chain operation could take O(Δ) time... actually the chain length can be O(n)). Hmm, worst case O(m * chain length) which could be bad.

Hmm, but actually there's a neat trick: the Kempe chain approach where we use "small" color palettes. Let me think about complexity: each edge insertion takes O(Δ) time to find free colors (using boolean arrays per vertex), plus chain walk. Total O(m Δ) = 400000 * 100000 = 4*10^10. Way too slow.

So the Euler split / binary splitting approach is the way to go: O(m log Δ).

Let me recall the algorithm precisely.

**Algorithm (Cole–Ost–Schirra style / standard "bipartite edge coloring via splitting"):**

Function color(edges E, k) where max degree of E is ≤ k (k a power of 2, or we handle general k):
- If k == 1: all edges get color 1 (graph is a matching).
- Else: split E into E1, E2 such that max degree of E1 ≤ ceil(k/2) and max degree of E2 ≤ floor(k/2)... Actually we need max degree of each ≤ ceil(k/2). Then recursively color E1 with colors 1..ceil(k/2) and E2 with colors ceil(k/2)+1..k.

The split: For each vertex with degree d, we want to split its incident edges into two groups of sizes floor(d/2) and ceil(d/2). This is achieved via Eulerian decomposition:

Standard technique: Add a dummy vertex (or handle odd degrees). Actually the cleanest: 

**Euler split:** Given multigraph G (here bipartite, but the split works for any graph), construct G' by adding a new vertex w and connecting w to every vertex of odd degree. Then G' is Eulerian (all degrees even). Decompose G' into edge-disjoint cycles (Euler tours). For each cycle, alternately color its edges red/blue (since cycles are even-length... wait, cycles in G' — with the dummy vertex, cycles through w have even length? Hmm, in a general graph cycles can be odd. But in bipartite graphs cycles are even. But G' with dummy vertex w — w connects to odd-degree vertices of G. Is G' bipartite? Not necessarily... Actually if G is bipartite with parts L, R, and w connects to odd-degree vertices. Hmm, w connects to both L and R vertices, so G' is not bipartite in general. But cycles through w: each visit to w uses two edges of w, going w -> x -> ... -> y -> w. Hmm, the cycle could be w -> l -> r -> w? That's length 3 if l-r edge exists and both l, r odd degree. So odd cycles possible. Then alternating coloring fails.

Alternative standard approach: pair up edges at each vertex. At each vertex v with degree d, pair the incident edges arbitrarily into floor(d/2) pairs, with one edge left over if d is odd. Then the "pairs" form paths and cycles in the line-graph sense: following from an edge, at each endpoint jump to its paired edge, etc. This decomposes edges into alternating paths/cycles. Then color alternately along each path/cycle. For a path of even length... hmm, let me think.

Actually the standard Euler split: at each vertex, partition incident edges into pairs (one leftover if odd degree). Then the edge set decomposes into trails (paths and cycles) where consecutive edges are paired at a shared vertex. Color edges alternately along each trail. For a cycle (even number of edges since each vertex contributes pairs — in a cycle, each vertex has exactly 2 trail-edges, which must be paired together, so cycles have even length? Let me think: a cycle in the trail decomposition: e1, e2, ..., e_{2k} where e_{2i} and e_{2i+1} share vertex v_i and are paired there. Going around, yes cycles have even length). For paths: a path e1, e2, ..., e_t where e_i and e_{i+1} are paired at their shared vertex. The endpoints of the path are vertices where the leftover edge is (or a vertex where... hmm). Alternating coloring along a path: if the path has even length, each internal vertex gets equal numbers; endpoints get one extra of one color each. Hmm, let me think about the degree balance.

At each vertex v with degree d: pairs contribute one edge to each color per pair (alternating along the trail: paired edges at v are consecutive in the trail, so they get different colors — wait, is that right? In the trail, e_i and e_{i+1} are paired at v. Alternating coloring gives them different colors. Yes.). So each pair contributes 1 red + 1 blue at v. The leftover edge (if d odd) contributes either red or blue. So at v: red count = floor(d/2) or ceil(d/2), blue = the complement. 

So after the split, at each vertex, red degree and blue degree are floor(d/2) and ceil(d/2) in some order. So max(red degree) ≤ ceil(Δ/2) and max(blue degree) ≤ ceil(Δ/2). 

So the recursion: color(E, k): if k == 1, assign color. Else split into E_red, E_blue each with max degree ≤ ceil(k/2). Recurse with k1 = ceil(k/2) colors for red, k2 = floor(k/2) for blue. Since max degree of red ≤ ceil(k/2) and of blue ≤ ceil(k/2) ≤ ... hmm wait, we need max degree of blue ≤ floor(k/2)? No: blue max degree ≤ ceil(k/2) but blue gets only floor(k/2) colors. Hmm, that's a problem if ceil(k/2) > floor(k/2), i.e., k odd.

Let me redo: Let Δ be the actual max degree. We want to color with exactly Δ colors. Recursion: color(E, Δ): if Δ == 1, done. Else split E into E1, E2 with degrees at each vertex floor(d/2), ceil(d/2). Max degree of E1 ≤ ceil(Δ/2), max degree of E2 ≤ ceil(Δ/2). Hmm, but actually: at the vertex with degree Δ, one of E1/E2 has ceil(Δ/2) and the other floor(Δ/2). Other vertices have degree ≤ Δ. Hmm, so max degree of E1 could be ceil(Δ/2) and E2 could also be ceil(Δ/2) (from different vertices). E.g., Δ=3: vertex a has degree 3 → split 2/1; vertex b has degree 2 → split 1/1. E1 could have max degree 2, E2 max degree 2 (from a's ceil and... wait a's split is 2 and 1; b's is 1 and 1. If a's 2 goes to E1, E1 max = 2 = ceil(3/2). E2 max = 1 from a, 1 from b = 1. Hmm, but could E2 have degree 2? Only if some vertex has degree ≥ 3 in E2, but max degree is 3 and the degree-3 vertex splits 2/1. If a's "2" went to E2 instead, then E2 max = 2, E1 max = 1. So one of them has max ≤ floor(Δ/2) = 1 and the other ≤ ceil(Δ/2) = 2. But which one has the larger max depends on the split at the max-degree vertex.

Hmm, so the recursion should be: color(E, k) where we're promised max degree of E ≤ k, and we color with k colors. Split E into E1 (max degree ≤ ceil(k/2)) and E2 (max degree ≤ ceil(k/2))? But then E2 needs ceil(k/2) colors too, total ceil(k/2) + ceil(k/2) = 2*ceil(k/2) ≥ k, could be k+1 when k odd. That breaks.

Standard fix: the recursion is on the actual max degree. Let me look at it differently. The standard approach (from "A linear-time algorithm for edge-coloring bipartite graphs" or the simpler O(m log Δ) version):

color(E, k): // max degree of E is exactly... hmm.

Actually, the clean way: color(E, k) where max degree Δ(E) ≤ k:
- If k == 1: all edges color 1 (E is a matching since Δ ≤ 1).
- Else: split E into E1, E2 with per-vertex degrees split as evenly as possible (floor/ceil). Then Δ(E1) ≤ ceil(k/2), Δ(E2) ≤ ceil(k/2). Recurse: color(E1, ceil(k/2)) and color(E2, ceil(k/2)) with offset floor(k/2)? Total colors = floor(k/2) + ceil(k/2) = k. But E2 needs ceil(k/2) colors and gets ceil(k/2) (offset floor(k/2), colors floor(k/2)+1 .. floor(k/2)+ceil(k/2) = k). E1 gets floor(k/2) colors but might need ceil(k/2). Hmm, mismatch again.

Wait: Δ(E1) ≤ ceil(k/2). If we give E1 colors 1..floor(k/2) that's not enough when Δ(E1) = ceil(k/2) = floor(k/2)+1 (k odd). Hmm.

Let me reconsider. The correct recursion: color(E, k) with Δ(E) ≤ k, using k colors:
- If k == 1: done.
- Split E into E1, E2 evenly per vertex. Δ(E1) ≤ ceil(k/2), Δ(E2) ≤ ceil(k/2).
- color(E1, ceil(k/2)) using colors 1..ceil(k/2).
- color(E2, ceil(k/2)) using colors ceil(k/2)+1..k? That's only k - ceil(k/2) = floor(k/2) colors for E2. Not enough if Δ(E2) = ceil(k/2).

Hmm. So this doesn't directly work. The issue: both halves might need ceil(k/2) colors, total k+1 when k is odd.

Resolution: Note that Δ(E) ≤ k. If Δ(E) < k, we can... hmm. Actually the standard trick: the recursion is done with k being a power of 2, or we handle it as: since Δ(E1) + Δ(E2) ≤ ... no.

Let me think again. Actually the key insight: at each vertex v, deg_{E1}(v) + deg_{E2}(v) = deg_E(v) ≤ k, and each is floor/ceil of deg. So deg_{E1}(v) ≤ ceil(deg(v)/2) ≤ ceil(k/2). Fine. But the total colors needed: we want to color E1 with a set C1 and E2 with C2, |C1| ≥ Δ(E1), |C2| ≥ Δ(E2), C1 ∩ C2 = ∅. |C1| + |C2| = k. Since Δ(E1) ≤ ceil(k/2) and Δ(E2) ≤ ceil(k/2), if k is even, both fit in k/2. If k is odd, we need one of them to be ≤ floor(k/2). 

Claim: if k is odd and Δ(E) ≤ k... Consider the vertex achieving Δ(E1) = ceil(k/2) = (k+1)/2. Hmm, is it possible that both Δ(E1) = (k+1)/2 and Δ(E2) = (k+1)/2? Δ(E1) = (k+1)/2 means some vertex v has deg_{E1}(v) = (k+1)/2, so deg_E(v) ≥ (k+1)/2... that's fine, deg_E(v) could be k. Similarly for E2 at another vertex u. E.g., k=3, vertices v and u each with degree 3, v's split 2/1 with 2 in E1, u's split 1/2 with 2 in E2. Then Δ(E1) = 2, Δ(E2) = 2, total needed 4 > 3. So indeed the naive split fails for odd k.

Standard fix: pad the graph. Add dummy edges (or dummy vertices with edges) to make the graph Δ-regular (or nearly). If the graph is k-regular with k a power of 2... Hmm, the classical approach: 

1. First, make the graph Δ-regular by adding dummy edges (with dummy vertices as needed). In bipartite graphs, we can always do this: add edges to balance degrees. Actually to make it regular we might need to add a dummy vertex on each side.

2. Then with a regular graph of degree Δ (power of 2 after... hmm, Δ might not be a power of 2).

Alternative standard fix: recursion color(E, k) where the promise is Δ(E) ≤ k:
- If Δ(E) ≤ 1: color all with color 1... wait if Δ(E) = 0 no edges.
- Actually: let d = Δ(E). If d ≤ k - something...

Hmm, let me think about the well-known solution to this exact problem. This problem is from some contest — "bipartite edge coloring with Δ colors, m up to 4*10^5". I recall this is Codeforces problem... "Book of Evil"? No. Hmm, it resembles CF Round problem "2-coloring"... Actually I recall a problem from Codeforces Round: problem about scheduling experiments between boys and girls — that's CF 841E? No... Let me think: "Blood Cousins"? No.

I recall: Codeforces problem 786E? Hmm. Or "Timus"? Actually, I strongly suspect this is Codeforces 845E? Hmm no.

Wait — I remember: Codeforces Round #429, problem "Leha and security system"? No. There's a known problem: CF 841D? No.

Let me just recall: "nL, nR up to 1e5, m up to 4e5, edge coloring bipartite with Δ colors" — this is Codeforces problem 786E? Hmm, actually I think it's CF problem "E. New Year and Entity Enumeration"? No.

I believe it's this: Codeforces 845 E? Let me not worry about the source and just design the algorithm.

Known efficient approach: **König's edge coloring via Euler split with padding to regular graph.**

Steps:
1. Compute Δ = max degree.
2. Make graph Δ-regular bipartite multigraph by adding dummy edges: For the left side, vertices with degree < Δ need extra edges; similarly right side. Total deficit on left = total deficit on right (since both equal Δ*nL - m and Δ*nR - m... wait no: sum of degrees on left = m = sum on right. Deficit left = Δ*nL - m, deficit right = Δ*nR - m. These are equal only if nL = nR. Not equal in general!). Hmm. So to make it regular we add dummy vertices: add dummy left vertices and dummy right vertices so that the deficits balance. Specifically: we need to add edges such that every real vertex reaches degree Δ, and dummy vertices absorb. If Δ*nL - m > Δ*nR - m (nL > nR), we need more capacity on the right: add dummy right vertices. Number of dummy right vertices needed: at least ceil((Δ*nL - m)/Δ)... but also each dummy right vertex can have degree up to Δ. Hmm, but also dummy right vertices themselves need degree exactly Δ to keep regularity — but we can add edges among dummies too (dummy left - dummy right edges). 

This padding is getting complicated. Let me think about whether the recursion can be fixed without padding.

**Fixed recursion:** color(E, k) with promise Δ(E) ≤ k, output coloring with colors from a palette of size k (but we only need to use Δ(E) colors at most... no wait, we need the final coloring to use at most Δ colors total where Δ is the global max degree).

Hmm, here's a cleaner way to think: 

color(E, k): colors E using at most k colors, given Δ(E) ≤ k.
- If k == 1: all edges get color 1.
- Else: split E into E1, E2 with per-vertex floor/ceil split. Then Δ(E1) ≤ ceil(k/2), Δ(E2) ≤ ceil(k/2). Now:
  - color(E1, ceil(k/2)) with colors 1..ceil(k/2).
  - color(E2, floor(k/2))? Not valid since Δ(E2) might be ceil(k/2).

Alternative: note Δ(E1) + Δ(E2) ≤ ... hmm, is it ≤ k? Δ(E1) ≤ ceil(Δ(E)/2)... no wait. Hmm: Δ(E1) ≤ ceil(k/2) and Δ(E2) ≤ ceil(k/2), so Δ(E1) + Δ(E2) ≤ k+1. But actually, can we show Δ(E1) + Δ(E2) ≤ k when... Let v be the max-degree vertex of E1 with deg_{E1}(v) = ceil(deg_E(v)/2) possibly. Hmm, Δ(E1) = max_v ceil(deg_E(v)/2) = ceil(Δ(E)/2). Similarly Δ(E2) = ceil(Δ(E)/2). So Δ(E1) + Δ(E2) = 2*ceil(Δ(E)/2) ≤ Δ(E) + 1. So if Δ(E) is even, both halves have Δ(E)/2 ≤ k/2, fine. If Δ(E) is odd, both halves have (Δ(E)+1)/2.

So the problem only arises when Δ(E) is odd. Fix: when Δ(E) is odd, we can first extract a matching? Hmm: if Δ(E) is odd, remove a matching... no wait.

Alternative fix: when Δ(E) is odd, add a dummy "shift": Actually here's a classical trick: when Δ(E) is odd, at each vertex of odd degree, one edge is "leftover" in the pairing. The leftover edges form a subgraph where every vertex has degree ≤ 1 — wait, no: the leftover edge at v is a specific edge; an edge e = (u,v) could be leftover at both u and v, or leftover at just one endpoint. Hmm.

Let me reconsider the Euler split more carefully. Pairing at each vertex: at vertex v with degree d, pair up edges into floor(d/2) pairs; if d odd, one edge unpaired at v. The trails: start from an unpaired edge... Let me re-derive: Consider the "pairing graph": each edge e has two endpoints. Define a transition structure: at vertex v, pairs {e, f} mean e and f are linked at v. Trails: sequences e1, e2, ... where e_i and e_{i+1} are paired at their common vertex. Each edge has 2 endpoints, and at each endpoint it's either paired with exactly one other edge or unpaired. So the structure decomposes into maximal trails: paths (starting and ending at unpaired endpoints) and cycles (all endpoints paired within the cycle). Alternating coloring along trails: 

- Cycle of even length 2t: at each vertex on the cycle, the two cycle-edges are paired at that vertex and get different colors. Good.
- Path: e1, ..., e_t. Consecutive edges paired at internal vertices get different colors. Endpoints: the first edge e1 is unpaired at its start vertex, last edge e_t unpaired at its end vertex.

At vertex v, the colors of edges incident to v: each pair contributes one of each color. The unpaired edge (if d_v odd) contributes its trail color. So deg_red(v) = floor(d_v/2) + [unpaired edge is red], deg_blue(v) = floor(d_v/2) + [unpaired edge is blue]. So indeed each vertex gets floor/ceil split. 

Now, the total: Δ(E1) = ceil(Δ(E)/2) possibly, Δ(E2) = ceil(Δ(E)/2) possibly, sum = Δ(E)+1 when Δ(E) odd. To fix: we want the split such that Δ(E1) ≤ ceil(k/2) and Δ(E2) ≤ floor(k/2) when k is odd... but that requires knowing which half takes the extra. Since Δ(E) ≤ k: if Δ(E) < k, then ceil(Δ(E)/2) ≤ ceil((k-1)/2) = floor(k/2) when k odd... wait if Δ(E) ≤ k-1 and k odd, then Δ(E) ≤ k-1 even, so ceil(Δ(E)/2) ≤ (k-1)/2 = floor(k/2). So both halves fit in floor(k/2) ≤ ceil(k/2). Fine. The only problem: Δ(E) = k, k odd. Then both halves could need (k+1)/2 colors.

Fix for that case: when Δ(E) = k and k is odd, first find a matching... hmm, actually here's a cleaner classical fix: **handle odd k by splitting off one color first**: Find a matching that covers... no.

Alternative classical approach: **pad to make Δ(E) = k exactly and k regular**, then Euler split works nicely: if the graph is k-regular, then after split, E1 is ceil(k/2)-regular... wait: each vertex has degree k, split into floor(k/2), ceil(k/2). If k even: both halves k/2-regular. If k odd: one half (k+1)/2-regular, other (k-1)/2-regular — but which half varies per vertex! Hmm, so E1 has max degree (k+1)/2 and E2 has max degree (k+1)/2. Same problem.

Hmm wait, but actually for regular graphs there's the classical result: a k-regular bipartite graph decomposes into k perfect matchings (König). And (k+1)/2... hmm.

OK here's another thought. The classical O(m log Δ) algorithm (Cole–Ost–Schirra) actually works as: 

Actually, let me recall the simpler well-known trick used in competitive programming for this exact problem. I'm now fairly sure this problem is **Codeforces 786E**? No... Let me think: "nL nR m" with locks and keys... Hmm, this really sounds like **Codeforces Round 411 problem E**? Or maybe it's from Codeforces problem set: "E. Ice cream coloring"? No.

I recall a Codeforces problem: **845E "Fire in the City"**? No. Hmm, what about **CF 841E "Rubik's cube"?** no.

Actually! I remember: **Codeforces problem 780E**? Hmm no. Let me think about "locks and keys" — maybe it's from a recent contest, e.g., Codeforces Round #... "Assembly line"? Could be an ICPC problem. Whatever — the algorithm is what matters.

Let me search memory: "bipartite edge coloring O(m log n)" — there's a known technique: repeatedly do "Euler tour split" doubling: 

**The standard approach in CP for bipartite Δ-edge-coloring:**

Method: recursive function solve(edges, k) that colors edges using exactly the colors in a given palette of size k, where k ≥ Δ(edges) and k is... The trick to handle odd: 

solve(E, k):
  if k == 1: color all edges with color 1. (Δ(E) ≤ 1)
  if Δ(E) == 1: color all edges with color 1 (they form a matching). — early exit helps.
  Split E into E1, E2 via Euler split (floor/ceil per vertex).
  Now Δ(E1) ≤ ceil(Δ(E)/2) ≤ ceil(k/2), Δ(E2) ≤ ceil(Δ(E)/2) ≤ ceil(k/2).
  If k even: solve(E1, k/2) with first half palette, solve(E2, k/2) with second half.
  If k odd: hmm.

For k odd: we need palettes of sizes ceil(k/2) and floor(k/2) for E1, E2 but both might need ceil(k/2). 

Trick: when k is odd, note Δ(E) ≤ k. If Δ(E) ≤ k-1, then solve(E, k-1)?? But then palette size k-1 even... but wait we need to use palette of size k given. We can just use solve(E, k-1) with the first k-1 colors — using fewer colors is fine! The final answer just needs colors in 1..Δ. So actually we never need to "use exactly k colors" — using fewer is always fine. So:

solve(E, palette of size k) where Δ(E) ≤ k:
- if Δ(E) ≤ 1: color all with first palette color.
- else: split into E1, E2. Let d = Δ(E). Both Δ(E1), Δ(E2) ≤ ceil(d/2). Give E1 the first ceil(d/2)... wait, but we need disjoint palettes for E1 and E2. |palette| = k ≥ d ≥ Δ(E1) + Δ(E2) - 1... hmm when d odd, Δ(E1)+Δ(E2) could be d+1 > k? No: d ≤ k, so d+1 ≤ k+1. If d = k and k odd, d+1 = k+1 > k. Problem persists.

Hmm OK so the real issue: Δ(E) = k, k odd, and both halves need (k+1)/2. Total (k+1)/2 + (k+1)/2 = k+1 > k.

Solutions:
(a) Pad the graph with dummy edges so that it becomes k-regular AND handle... no wait, even k-regular with odd k has the issue. Hmm wait, no! If the graph is k-regular (every vertex degree exactly k) with k odd: after Euler split, each vertex has (k+1)/2 in one half, (k-1)/2 in the other. The halves E1, E2: E1 has max degree (k+1)/2, E2 max degree (k+1)/2. Still both could be (k+1)/2. Hmm, e.g., k=3: two vertices u, v each degree 3; u splits 2 into E1, v splits 2 into E2. So E1 max 2, E2 max 2, need 4 colors. But wait — is that actually possible while the whole graph is 3-regular bipartite? Sure: u, v on left, u', v' on right, edges u-u', u-v', v-u', v-v'... that's 2-regular on 4 vertices. Add w, w' with edges to make 3-regular: u-w', v-w', w-u', w-v', w-w'. Degrees: u: u-u', u-v', u-w' = 3. v: 3. u': u-u', v-u', w-u' = 3. etc. Now Euler split: at u, pair (u-u', u-v') and leftover u-w'. At v, pair (v-u', v-v') leftover v-w'. Suppose trail: u-u' (red), u'-v (paired at u' with... hmm wait pairing is at vertices: at u', edges u-u', v-u', w-u'; pair (v-u', w-u'), leftover u-u'. Hmm, I need to be careful, but the point stands: it's possible for both halves to have max degree 2 = (3+1)/2, needing 4 > 3 colors if colored independently with disjoint palettes.

BUT: the classical theorem says a 3-regular bipartite graph is 3-edge-colorable. The Euler split alone doesn't immediately give it. The classical algorithm (Cole–Ost–Schirra) handles this with a more clever argument. Let me recall...

Actually, the classical approach for odd degree: **First, when Δ(E) is odd, extract a matching M that covers all vertices of degree Δ(E)**... Hmm, no. Let me recall the actual COS algorithm:

The Cole–Ost–Schirra algorithm: "edge-coloring bipartite graphs in O(m log Δ)". The idea: 

- If Δ is odd: find a matching M in E that covers all vertices of degree Δ (such a matching exists? Hmm — in a bipartite graph, the set of vertices with degree Δ... we need a matching covering all max-degree vertices on... hmm, not exactly).

Hmm, alternatively: 

- If Δ is odd: Let V_Δ = vertices of degree Δ. Find a matching M that saturates all vertices in V_Δ? Is that always possible? Consider: all max-degree vertices... By Hall's theorem type argument? Hmm, not obviously.

Let me think differently. Actually here's a cleaner classical approach I remember from a Codeforces editorial (I'm now recalling this might be **CF Round 442 problem E**? or **"Danil and a Part of Jobs"**? no...). 

Hmm, actually I definitely remember a CF problem: **"E. Minimum spanning tree on the fly"**? no. Let me remember: there was a problem about edge-coloring a bipartite graph with Δ colors where n up to 1e5 and m up to 5e5 — I believe it's **Codeforces 786E (Nikita and game)**? no...

I think it might be **CF 845E**... I give up on identifying; let me just design a correct algorithm.

**Approach: reduce to regular graph + recursive splitting with perfect matchings.**

Alternative clean approach: **König's line coloring via repeated matching extraction is too slow (Δ matchings).**

**Approach via "unbalanced split fix":** Here's a neat fix for the odd case that I recall: when splitting with k odd, we can be smarter about the pairing: we want the split such that all vertices of degree k (the max) put their extra edge in the SAME half. I.e., choose the leftover edges' colors consistently: at every vertex of degree exactly k (odd), the unpaired edge goes to, say, E1. Then E2 has max degree ≤ (k-1)/2 = floor(k/2) at max-degree vertices... but wait, other vertices with degree k-1 (even) split into (k-1)/2 each — that's ≤ floor(k/2). Vertices with degree ≤ k: floor(d/2) ≤ floor(k/2). So Δ(E2) ≤ floor(k/2). And E1: ceil(d/2) ≤ ceil(k/2). So palettes: E1 gets ceil(k/2), E2 gets floor(k/2), total k. 

But can we force all unpaired edges at degree-k vertices to go to E1? The unpaired edges form trails' endpoints. Hmm, the alternation along trails determines which color the unpaired edges get — we don't directly control it per-vertex. Let me think: a path trail e1...e_t: e1 unpaired at its start vertex s, e_t unpaired at end vertex t. Alternating: e1 red, e2 blue, ..., e_t red if t odd. So the two endpoints' unpaired edges get the same color iff t is odd, different iff t even. Hmm.

So we need a more careful approach: we need to choose the pairings such that in the resulting trail decomposition, the assignment can be oriented so that all "extra" edges at max-degree vertices land in E1. 

Alternative: think of it as: we want to 2-color the edges (red/blue) such that at each vertex v: deg_red(v) ∈ {floor(d_v/2), ceil(d_v/2)}, and moreover, if d_v = k (the max, odd), then deg_red(v) = ceil = (k+1)/2 (extra goes red). And if d_v < k, deg_red(v) ≤ ceil(d_v/2) ≤ floor(k/2) automatically. Then blue degrees: at max vertices (k-1)/2, others ≤ ceil(d_v/2) ≤ (k-1)/2 if d_v ≤ k-1... wait d_v could be k-1 (even) → ceil = (k-1)/2 = floor(k/2). OK so Δ(blue) ≤ floor(k/2), Δ(red) ≤ ceil(k/2). 

So the question: does such a 2-coloring exist, and how to find it efficiently? This is exactly the "Euler split with prescribed imbalance direction at max-degree vertices". 

Hmm, here's a way: Add a dummy vertex? Let's think in terms of making the graph Eulerian: Add a new vertex x. Connect x to every vertex of odd degree. Now all degrees even. The graph is Eulerian-ish (connected components have Euler tours). Now, an Euler tour alternates edge colors along the tour; at each vertex v ≠ x, the tour passes through, using pairs of consecutive edges — each pair gets one red one blue. At x, similar. So deg_red(v) = deg_blue(v) = d_v/2 for all v with even d_v. For odd d_v: (d_v+1)/2 red or blue depending on tour structure at v: the edge to x is paired with another edge at v in the tour; the edge v-x gets some color, contributing the extra. Hmm, so with the dummy vertex x, each odd-degree vertex v has its "extra" determined by the color of edge v-x... but v-x's color is determined by alternation along the tour, and at x, the edges into x alternate colors along the tour: at x, consecutive tour edges paired at x get different colors. So among edges incident to x, along the tour, they alternate colors: red, blue, red, blue, ... in pairs. Hmm, so roughly half the odd-degree vertices get red extra, half blue — not what we want (we want ALL max-degree vertices to get red extra).

But wait — we can choose the Euler tour! Hmm, this is getting complicated. Let me look at this from a different angle.

**Different classical fix:** When k is odd and Δ(E) = k: 

Step 1: Find a matching M ⊆ E that saturates every vertex of degree exactly k. Then color M with color k (one color), and recurse on E \ M with k-1 colors (Δ(E\M) ≤ k-1). 

Does such a matching exist? Claim: In any graph, there's a matching saturating all vertices of degree exactly Δ... Hmm, is that true? Consider a star K_{1,3}: center degree 3 = Δ, leaves degree 1. Matching saturating center: yes, any single edge covers the center; leaves of degree 1 ≠ 3 = Δ don't need saturation... wait leaves have degree 1, Δ = 3, so only the center needs saturation. Fine. Consider two degree-3 vertices u, v adjacent to each other and... hmm, in a bipartite graph: u, v on left both degree 3 = Δ, sharing all their neighbors? u adjacent to a, b, c; v adjacent to a, b, c. Then matching {u-a, v-b} saturates u and v. Fine. In general: is there a matching saturating all max-degree vertices in a bipartite graph? Hmm. By Hall's theorem: we need the set S of max-degree vertices (on both sides!) to have a matching saturating S. Vertices on both sides — a matching saturating a set S ⊆ L ∪ R. Hall's condition for saturating S: for every X ⊆ S ∩ L, |N(X)| ≥ |X|, and similarly for right. Hmm, is that guaranteed? Suppose u ∈ L has degree Δ, its neighbors a1..aΔ ∈ R. If some subset X of max-degree left vertices has |N(X)| < |X|... Each vertex in X has degree Δ, all edges going to N(X). Total edges from X: |X|·Δ. Each vertex in N(X) has degree ≤ Δ, so edges into N(X) ≤ |N(X)|·Δ < |X|·Δ. Contradiction! So |N(X)| ≥ |X| for X ⊆ (max-degree left vertices). Similarly for right. But wait, we need a single matching saturating S ∩ L AND S ∩ R simultaneously. Hmm, the conditions for both simultaneously: this is a matching that saturates S on both sides. Hmm, Hall-type condition for saturating specified subsets on both sides is more subtle. 

Hmm, example: path a - u - b where u ∈ L degree 2 = Δ, a, b ∈ R degree 1. If Δ = 2, max-degree vertices = {u}. Matching saturating u: pick either edge. Fine.

Example where both sides have max-degree vertices: cycle u1 - a1 - u2 - a2 - u1 (4-cycle), all degree 2 = Δ. Matching {u1-a1, u2-a2} saturates all. Fine.

Tricky case: u ∈ L, a ∈ R, edge u-a, plus u has Δ-1 other neighbors, a has Δ-1 other neighbors, Δ = 2: u-a, u-b, c-a. Max-degree vertices: u (deg 2), a (deg 2). Matching saturating both u and a: {u-b, c-a} or {u-a} doesn't saturate both... {u-b, c-a}: u matched to b, a matched to c. Yes works. In general, hmm.

Actually, there's a classical lemma: **In a bipartite graph, there is a matching that saturates all vertices of maximum degree.** Proof sketch: Take a maximum matching M. Suppose some max-degree vertex v is unmatched. Then run alternating path argument... Standard proof: Let M be a maximum matching maximizing the number of saturated max-degree vertices. If some max-degree vertex u ∈ L is unsaturated, look for augmenting path from u; since M maximum, no augmenting path, so the alternating tree from u: all vertices reachable... u has Δ ≥ 1 neighbors, all matched (else augment). Hmm, standard argument shows we can find a matching saturating all max-degree vertices on ONE side easily (by the Hall argument above). For both sides simultaneously: 

Hmm, consider: S_L = max-degree left vertices, S_R = max-degree right vertices. We want a matching saturating S_L ∪ S_R. Is this always possible? Counterexample attempt: Δ = 2. u1, u2 ∈ L, a1, a2 ∈ R. Edges: u1-a1, u1-a2, u2-a1, u2-a2 (K_{2,2}), all degree 2. Perfect matching exists. 

Counterexample: u ∈ L deg 2, a ∈ R deg 2, edges u-a, u-b, c-a, and b, c have degree 1. Max vertices: u, a. Matching {u-b, c-a} saturates both. 

Hmm, what about: u ∈ L deg 2 (neighbors a, b), a ∈ R deg 2 (neighbors u, v), v ∈ L deg 2 (neighbors a, c)... chain. u-a, u-b, v-a, v-c. Max-degree: u, a, v (all deg 2), b, c deg 1. Matching: {u-b, v-a} saturates u, v, a. Yes.

General proof: Suppose M is a matching that saturates all of S_L (exists by Hall argument). Does it saturate S_R? Not necessarily. Hmm. Let me think of potential counterexample: We need max-degree vertices on the right that can't all be matched while also matching all max-degree left vertices. 

Consider Δ = 2: path graph: b - u - a - v - c where u, v ∈ L, a ∈ R, b, c ∈ R. Degrees: u: 2 (b, a), a: 2 (u, v), v: 2 (a, c), b: 1, c: 1. Max-degree: u, a, v. Matching saturating all three: must match u, v, a. u's options: b or a. v's options: a or c. a must be matched to u or v. If a-u, then v-c: {a-u, v-c} saturates u, a, v. Yes.

Hmm, I believe the lemma is true: **every bipartite graph has a matching saturating all vertices of maximum degree**. Actually hmm, wait. Let me think of a potential counterexample more carefully. Δ = 3. Left: u1, u2 (deg 3). Right: a1, a2, a3 (deg 2 each). Edges: complete K_{2,3}. Max-degree vertices: u1, u2 (deg 3). a's have degree 2. Matching saturating u1, u2: {u1-a1, u2-a2}. Fine, a's don't need saturation.

Reverse: Left u1, u2, u3 deg 2; right a1, a2 deg 3. K_{3,2}. Max: a1, a2. Matching {u1-a1, u2-a2} saturates both. Fine.

Mixed: Left u1 (deg 3), u2 (deg 1); Right a1 (deg 3), a2 (deg 1). Edges: u1-a1, u1-a2, u2-a1. Max: u1, a1. Matching: {u1-a2, u2-a1} saturates both. Or {u1-a1} saturates both with one edge. Fine.

Potential problem: max-degree vertices forming an odd structure... e.g., Δ=2: triangle? Not bipartite. In bipartite: max-degree vertices u (L), a (R) with edge u-a, u-a' , u'-a? u' deg 2? Let's see: u-a, u-a', u'-a, u'-a'? That's K_{2,2}, perfect matching exists.

I'm fairly confident the lemma holds. Actually, here's a cleaner known result: a bipartite graph has a matching saturating all vertices of degree Δ iff... Hmm, let me just try to prove it via the following: Let G be bipartite with max degree Δ. Create G': keep all vertices; we want matching saturating S (max-degree vertices). By the defect/Augmenting-path theory: a maximum matching M that fails to saturate some s ∈ S. Take M maximum. The standard structure: Let Z = vertices reachable from unsaturated S-vertices (in S ∩ L, say) by alternating paths. Hmm, this is the proof of the "König edge coloring" itself... circular.

Alternative proof: Add dummy edges to make the graph Δ-regular (with dummy vertices as needed). A Δ-regular bipartite graph decomposes into Δ perfect matchings (König's theorem via Hall: regular bipartite has perfect matching; remove it; remains (Δ-1)-regular). Each perfect matching saturates ALL vertices, in particular all real max-degree vertices. Restrict to real edges: each of the Δ perfect matchings, restricted to real edges, saturates all real max-degree vertices (since they have no dummy edges). So yes! **A matching saturating all max-degree vertices exists.** But finding it requires the padding + matching machinery, which is what we're trying to avoid... or is it?

Hmm wait, actually this suggests a clean algorithm structure:

**Algorithm via padding to regular:**
1. Compute Δ.
2. Pad G to a Δ-regular bipartite graph H (add dummy vertices and edges). H has O(m + Δ·(number of dummy vertices))... hmm, the number of dummy vertices: we need to add dummy left vertices if Δ·nR - m > 0 capacity needed... Let me compute: real left vertices have total degree m; to be Δ-regular we need total left degree Δ·nL, so we add Δ·nL - m dummy edge-slots on the left, i.e., that many dummy edges incident to dummy left vertices (each dummy left vertex can take up to Δ). Number of dummy left vertices: ceil((Δ·nL - m)/Δ). Similarly right. Total dummy edges: (Δ·nL - m) + (Δ·nR - m) + (edges among dummies to fill up). Hmm, this could be huge: Δ·nL - m could be up to Δ·nL ≈ 100000·100000 = 10^10. WAY too much. E.g., nL = nR = 100000, m = 400000, Δ could be... well Δ ≤ max(nL, nR) = 100000 (a vertex can have degree up to the other side's size). If one lock is in 100000 tests, Δ = 100000, and Δ·nL - m ≈ 10^10. Padding is infeasible.

But wait — we don't need to pad ALL vertices to degree Δ. We only need to handle max-degree vertices. Hmm.

OK here's another angle. Let me reconsider the recursion with the "oriented extra" idea, but implement it via a different splitting that guarantees the orientation:

**Key insight for odd k:** We need a 2-coloring of edges (red/blue) such that:
- For every vertex v: deg_red(v), deg_blue(v) ∈ {floor(d_v/2), ceil(d_v/2)} (automatically sums to d_v).
- For every vertex with d_v = k (odd): the extra goes red, i.e., deg_red(v) = (k+1)/2.

Then Δ(red) ≤ (k+1)/2, Δ(blue) ≤ (k-1)/2... wait let me double check blue: for d_v = k: deg_blue = (k-1)/2. For d_v ≤ k-1: deg_blue(v) ≤ ceil((k-1)/2) = (k-1)/2 (since k-1 even). Yes! So Δ(blue) ≤ (k-1)/2 = floor(k/2), Δ(red) ≤ (k+1)/2 = ceil(k/2). Recurse: red with ceil(k/2) colors, blue with floor(k/2) colors. Total k. 

Now, how to find such a 2-coloring efficiently? 

Think of it as an Eulerian problem: Let's define a new graph: take G, and for each vertex v with odd d_v, we want to control the extra. Hmm. Consider the graph G'' = G plus a dummy vertex x with edges x-v for every odd-degree vertex v. All degrees even. Now, in G'', find Euler tours. Along each Euler tour, alternate colors. At each vertex v ≠ x: the tour enters and leaves; edges at v are paired by the tour (consecutive in tour), each pair gets one red, one blue. So deg_red(v) = deg_blue(v) = d_v/2 for even d_v. For odd d_v: v has one edge to x; the tour pairs edges at v; the edge v-x is in some pair, and gets one color; the other edges pair up evenly. So deg_red(v) = (d_v - 1)/2 + [v-x is red] in G (excluding the x edge). So the "extra" at v is red iff edge v-x is red.

So: we need an Euler decomposition of G'' such that all edges x-v with v of degree k are red. Hmm, at x, the tour(s) alternate: edges around x get colors alternating along the tour. If x has even degree (it does: number of odd-degree vertices is even), and the tour through x alternates... The edges incident to x, in tour order, get alternating colors: e.g., tour visits x multiple times; each visit uses 2 edges (in and out), which get different colors. So edges at x are paired by tour visits, each pair one red one blue. So exactly half of x's edges are red, half blue (if x's edges are all in one tour; in general, each tour through x uses an even number of x-edges... hmm, actually a tour could pass through x multiple times, each time using 2 edges, so total x-edges per tour is even, half red half blue). So the number of red x-edges = number of blue x-edges = (#odd-degree vertices)/2. But we want ALL degree-k vertices' x-edges to be red. If the number of degree-k vertices (with k odd... wait, degree-k vertices have odd degree since k odd, so they all get x-edges) exceeds half the odd-degree count, contradiction. So this approach with a single dummy vertex fails.

Fix: use TWO dummy vertices? Or: make the "extra" edges at max-degree vertices not need to pass through x. Alternative: **add a perfect matching among the max-degree vertices?** Hmm.

Alternative fix: **Reduce to the case where the number of odd-degree vertices equals... ** hmm.

Let me think about it differently. The desired 2-coloring: at each vertex v, deg_red(v) - deg_blue(v) ∈ {-1, 0, 1} with parity matching d_v, and for d_v = k odd, deg_red - deg_blue = +1. 

Consider the graph G and think of each vertex v as needing an "imbalance" b_v ∈ {-1, 0, +1}: b_v ≡ d_v (mod 2), |b_v| ≤ 1, and b_v = +1 if d_v = k. We want an orientation... wait, this is like a balanced orientation / flow problem! 

Reformulate as flow: color edges red/blue. deg_red(v) = (d_v + b_v)/2. This is a b-matching / flow feasibility: does there exist a subset F (red edges) with deg_F(v) = (d_v + b_v)/2 for all v? This is a degree-constrained subgraph problem, solvable by flow. But we need it fast, and recursively — flow at each level would be too slow (O(m) flow each level? Actually a flow with unit capacities... hmm, this feasibility is exactly a bipartite b-matching feasibility, which by Hall-like conditions... and finding it requires max-flow, O(m · something) per level. Too slow probably. Hmm, but wait — maybe there's a direct combinatorial construction.

**Direct construction attempt:** Let S = set of vertices with degree exactly k (k odd). We want red degrees: (d_v+1)/2 for v ∈ S, and floor/ceil for others (any valid split). 

Idea: First, find a matching M saturating S (exists by the regular-graph argument, but we need to find it efficiently — hmm, finding a matching saturating S: this is a bipartite matching problem with the S vertices needing saturation. Hopcroft-Karp on... the graph could have m = 4·10^5 edges; HK is O(E√V) = 4·10^5 · 316 ≈ 1.3·10^8 — too slow in Python. Hmm.)

Wait, wait. Let me reconsider. Maybe there's a smarter classical approach that avoids matching entirely.

**The classical O(m log Δ) algorithm (Cole, Ost, Schirra 2001):** Let me recall how it handles this. From what I remember: 

The algorithm: color(G, k) where G has max degree ≤ k:
1. If k = 1, color all edges 1.
2. If k is even: Euler split into G1, G2, each max degree ≤ k/2; recurse with k/2 colors each.
3. If k is odd: Euler split into G1, G2 with max degrees ≤ (k+1)/2. Then... hmm. I recall something like: "if k is odd, first find a matching covering all vertices of degree k, color it with color k, and recurse on the rest with k-1 (even) colors." And the matching covering all degree-k vertices is found via... the Euler split itself? Hmm.

Actually here's a thought: **In the Euler split of a graph where k is odd, look at the "unpaired" edges.** At each odd-degree vertex, one edge is unpaired. The trails are paths and cycles. Hmm.

Alternatively, I recall the COS algorithm uses a different splitting: "Euler split" where they first make the graph "k-regular-ish" by adding a dummy vertex connected to odd-degree vertices, then Euler tours, then alternate. And for odd k they do something clever with the dummy vertex's edges.

Hmm, let me think about the two-dummy-vertex trick for our desired 2-coloring:

We want: all degree-k vertices get extra red. Equivalently: think of each vertex v as having a target red-degree r_v = ceil(d_v/2) if v ∈ S or (d_v odd, choose freely), floor(d_v/2) otherwise... Let me define: for v ∈ S: r_v = (d_v+1)/2. For v ∉ S: r_v = floor(d_v/2) or ceil(d_v/2), free choice (must have r_v ≡ ... just (d_v ± 1)/2 if odd, d_v/2 if even).

Flow formulation: find subgraph F with deg_F(v) = r_v. Feasibility by Gale-Ryser / flow. Since we get to choose r_v for non-S vertices, maybe always feasible. Construction: 

Hmm, here's a cleaner idea: **Reduce odd case to even case by removing a matching found via the split itself.** 

Actually, you know what — let me look at this from the perspective of known CP solutions. I'm now quite sure this problem is **Codeforces 786E**... no. Hmm, "locks and keys", "nL nR m ≤ 4·10^5"... 

OH WAIT. I remember now! This is **Codeforces problem 845E**? No... It's **"CF Round #420, problem D/ E"**? Hmm. Let me think about "Okabe and Banquet"? no.

Actually I recall a very similar problem: **Codeforces 841E?** Hmm no. What about **"Timus 1749"?** no.

I definitely remember an editorial about bipartite edge coloring with the Euler split technique for a CF problem with m up to 5·10^5. I think it's **Codeforces problem 786E "Nikita and game"** — no, that's different. **CF 845E** is "Fire in the City". Hmm... **CF problem "E. Edge coloring"**? There's CF problem 1416?? Hmm, there's a recent problem: **CF Round 780 (Div. 3)?? no.** 

Actually: **Codeforces 1786E?** no. Let me think... There's a known problem "BOI 2008? or CEOI?" Hmm, there's also the classic "UOJ/Codeforces gym" problem. 

I recall: **Codeforces Round #442 (Div. 2) Problem E "Danil and a Part of Jobs"**? no. 

Hmm, what about **Codeforces 845D**? no.

OK here's another one I genuinely remember: **Codeforces problem 845E**... no, stop. Let me remember the actual technique from an editorial I've read: The problem was to edge-color a bipartite graph with Δ colors, n up to 10^5? and the editorial described exactly the "divide colors in half, split edges via Euler tour alternating" approach, handling the odd case by... I think the editorial said: "if k is odd, we can first take out a matching covering all vertices with degree k" — and to find that matching, they used the fact that after making the graph regular... hmm, OR they used the following trick: 

**Trick:** if k is odd, add a dummy vertex x connected to all odd-degree vertices, making all degrees even; then the graph G'' has all even degrees; Euler split G'' into two halves each with max degree ≤ (k+1)/2... hmm wait G'' has max degree k+1 possibly (if a degree-k vertex gets an x-edge, its degree in G'' is k+1, even). Then split G'' into F1, F2 with degrees d/2 each at every vertex. Then F1 has max degree (k+1)/2, F2 max degree (k+1)/2. Then remove x: F1 - x-edges and F2 - x-edges partition G's edges. At each vertex v: deg_{F1}(v) + deg_{F2}(v) = d_v, each ≤ (d_v+1)/2. Hmm, so at v with d_v = k: deg_{F1} + deg_{F2} = k, each ≤ (k+1)/2, so {deg_{F1}, deg_{F2}} = {(k+1)/2, (k-1)/2} — one of them is (k+1)/2. But which one varies by vertex. Same problem as before. Hmm, BUT: the x-edges are split between F1 and F2: at x, deg_{F1}(x) = deg_{F2}(x) = (#odd)/2. Hmm.

So the question remains: how to make all degree-k vertices put their extra in the same half?

**Insight:** Let's count. Let s = number of degree-k vertices (all have odd degree). Total odd-degree vertices = t (even). In any "balanced" split, each odd-degree vertex contributes its extra to one of the halves. We want all s of the S-vertices to contribute to F1. The non-S odd-degree vertices (t - s of them) can contribute anywhere. Is there a parity/count obstruction? In the Euler-tour-with-dummy-x approach, the extras at odd vertices correspond to x-edges' colors, and at x the colors balance: #red x-edges = #blue x-edges = t/2. So #S-vertices with red extra ≤ t/2. If s > t/2, impossible with single dummy. With the freedom to choose tours, can we achieve all S red? We'd need #red x-edges ≥ s, but it's exactly t/2. So need s ≤ t/2. Not guaranteed. E.g., all vertices odd degree and all degree k: s = t, need s ≤ t/2. Fails.

So the dummy-vertex Euler approach can't directly do it. Need a different construction for the odd case.

**Let me reconsider: matching covering S.** The lemma (matching saturating all max-degree vertices) — let me verify it's true and find a constructive proof suitable for computation.

Lemma: Let G = (L ∪ R, E) bipartite, Δ = max degree, S = {v : deg(v) = Δ}. Then G has a matching saturating S.

Proof attempt via Hall: We need a matching saturating S ⊆ L ∪ R. Hmm, a matching saturating a set that spans both sides. There's a classical result: a bipartite graph has a matching saturating S_L ⊆ L and S_R ⊆ R iff for all A ⊆ S_L: |N(A)| ≥ |A| and for all B ⊆ S_R: |N(B)| ≥ |B|... NO, that's not sufficient in general (e.g., S_L = {u}, S_R = {a}, single edge u-a: matching {u-a} saturates both; conditions hold. Counterexample for sufficiency: u ∈ L, a ∈ R; edges u-b, c-a (no edge u-a). S_L = {u}, S_R = {a}. N(u) = {b} ≥ 1 ok; N(a) = {c} ≥ 1 ok. Matching saturating both: {u-b, c-a}: yes! works. Hmm. Another: u1, u2 ∈ L, a ∈ R; edges u1-a, u2-a. S_L = {u1, u2}, S_R = {a}. N({u1,u2}) = {a}, |N| = 1 < 2. Hall fails. Indeed no matching saturating both u1 and u2. But in our setting, can u1, u2 both have degree Δ with only neighbor a? Then a has degree 2, so Δ = 2 requires u1, u2 degree 2, but they have degree 1. Contradiction. So the degree condition matters.)

Let me prove the lemma properly. Suppose Δ ≥ 1. S_L = max-degree vertices in L, S_R in R. 

Claim: For any A ⊆ S_L: |N(A)| ≥ |A|. Proof: edges from A: |A|·Δ. Each vertex in N(A) has degree ≤ Δ, so |N(A)|·Δ ≥ |A|·Δ ⟹ |N(A)| ≥ |A|. ✓.

Similarly for B ⊆ S_R: |N(B)| ≥ |B|. ✓.

But as noted, Hall conditions on both sides separately don't immediately give a matching saturating both S_L and S_R. Hmm, actually... wait. Hmm, is there a theorem: if Hall's condition holds for saturating S_L (from left) and separately for S_R (from right), is there a matching saturating both? Counterexample: L = {u1, u2}, R = {a1, a2}. Edges: u1-a1, u2-a1, u2-a2. S_L = {u1, u2}? deg(u1) = 1, deg(u2) = 2, deg(a1) = 2, deg(a2) = 1. Δ = 2. S_L = {u2}, S_R = {a1}. Matching saturating u2 and a1: u2-a1 (single edge saturates both). ✓. 

Hmm, let me think about whether the lemma can fail. Suppose matching M saturating S_L (exists). If some vertex a ∈ S_R unsaturated by M: a has Δ neighbors, all... Consider alternating paths from a. Since M is maximum? Hmm, M might not be maximum. Let me take M = a matching that saturates S_L and maximizes |M ∩ covered S_R|... Let me think about the standard proof of König's theorem instead, since the lemma is basically an intermediate step in proving that bipartite graphs are Δ-edge-colorable (which is the theorem we're using!). 

Standard proof of König's line coloring theorem by induction on Δ: Let G bipartite with max degree Δ. Let S = vertices of degree Δ. Claim: there's a matching saturating S. Then color the matching with color Δ and recurse on G - M (max degree ≤ Δ-1... wait, need max degree of G-M ≤ Δ-1: vertices in S lose one edge → degree Δ-1; others ≤ Δ-1 anyway? Others have degree ≤ Δ-1 already and might not lose an edge, so still ≤ Δ-1. ✓). So the induction needs exactly this lemma. And the standard proof of the lemma:

Proof of lemma (from standard textbooks, e.g., Diestel or West): Let M be a maximum matching. Suppose v ∈ S unsaturated. WLOG v ∈ L. Build alternating tree from v: even-level vertices (L side, reachable by even alternating paths from v, unsaturated on L side...) — standard Hungarian argument: Since M is maximum, no augmenting path from v, so every vertex reachable... Let Z = set of vertices reachable from v by M-alternating paths (starting with non-M edge). Then: all neighbors of any z ∈ Z ∩ L are in Z ∩ R (else we'd extend). v ∈ Z ∩ L is unsaturated. Every vertex in Z ∩ R is matched (else augmenting path), and its partner is in Z ∩ L. So |Z ∩ L| = |Z ∩ R| + 1. Now, count edges between Z ∩ L and Z ∩ R: every vertex in Z∩L has all its neighbors in Z∩R. Hmm, I want to derive a contradiction with degrees: Let z ∈ Z ∩ L with deg(z) = Δ (v itself has degree Δ). All Δ neighbors of v are in Z ∩ R, and each is matched to a distinct vertex in Z ∩ L. Hmm, so |Z ∩ L| ≥ Δ + ... hmm, |Z∩L| = |Z∩R| + 1 ≥ Δ + 1. Each vertex in Z ∩ L has degree ≤ Δ with all neighbors in Z ∩ R. Total edges from Z∩L to Z∩R ≤ Δ·|Z∩R|. Also ≥ Δ (from v) + ... hmm, each u ∈ Z∩L has degree ≥ 1... Total edges from Z∩L = sum of degrees ≥ ... hmm, I need each vertex in Z∩L to have degree... not necessarily Δ. Hmm, so no immediate contradiction. Right — the lemma as stated might be FALSE. Let me look for a counterexample.

Counterexample attempt: Δ = 2. G: path b — u — a — v — c? Wait I did this before: u ∈ L (neighbors b, a), a ∈ R (neighbors u, v), v ∈ L (neighbors a, c), b, c ∈ R degree 1. S = {u, a, v} (degree 2). Matching saturating S: {u-b, v-a}? saturates u, v, and a. ✓. Or {u-a, v-c} ✓.

Counterexample attempt 2: Δ = 2, odd cycle-like structure... bipartite so even cycles. Hmm, consider: u1—a1, u1—a2, u2—a2, u2—a3, u3—a3, u3—a1 (6-cycle), all degree 2, S = all. Perfect matching exists. ✓.

Counterexample attempt 3: Δ = 3. Hmm. Let me think structurally: the lemma "matching saturating all max-degree vertices in bipartite graph" — I actually recall this IS a known lemma used in the inductive proof of König's edge-coloring theorem. Let me recall the actual inductive proof: 

König's theorem proof (standard): Induction on number of edges. Let G bipartite, Δ = max degree. If some vertex has degree < Δ... hmm. One standard proof: "Let G be bipartite with max degree Δ. We prove by induction on Δ. It suffices to show G contains a matching M saturating every vertex of degree Δ; then color M with color Δ and apply induction to G−M." And the matching lemma proof: "Let M be a maximum matching, and suppose v is a vertex of degree Δ not saturated by M. Let M' be... " Hmm, alternatively the proof goes: "Add dummy vertices and edges to make G Δ-regular; a Δ-regular bipartite graph has a perfect matching (by Hall: for A ⊆ L, edges from A = Δ|A| ≤ Δ·|N(A)| ⟹ |N(A)| ≥ |A|); the perfect matching restricted to original edges saturates all original degree-Δ vertices." — This is the padding proof I mentioned. It's non-constructive-ish but shows existence. And note: the perfect matching of the padded graph, restricted to real edges, might not saturate all real Δ-vertices if the perfect matching uses dummy edges at those vertices — but real Δ-vertices have NO dummy edges (they're already degree Δ), so the perfect matching saturates them with real edges. ✓. So the lemma is TRUE. Good.

But constructing it requires either padding (infeasible as shown) or matching algorithms (Hopcroft-Karp too slow in Python? HK on m = 4·10^5, V = 2·10^5: O(E√V) ≈ 1.3·10^8 — too slow in pure Python. Hmm.)

BUT WAIT: maybe we don't need a matching saturating S in the odd case. Let me revisit. In the recursion color(E, k) with Δ(E) = k odd: we need to peel off ONE color class (a matching) covering all degree-k vertices, then recurse with k-1 colors on the rest. Alternatively, we need a red/blue split with all degree-k vertices having red-extra. These are related: given the split, hmm, no. Let me think about which is easier.

Alternatively — **avoid the odd case entirely by a global trick:** 

Global trick: Let Δ = global max degree. If Δ is odd... hmm, we could add ONE dummy edge... no wait. Hmm, think: we want to color with exactly Δ colors. What if we pad the graph minimally so that Δ becomes even? No wait, padding increases Δ. Hmm: if Δ is odd, add a dummy vertex pair and... no. Adding edges increases Δ to Δ+1 (even), then we'd color with Δ+1 colors — not allowed (must use ≤ Δ... wait, actually the problem says "a line with m integers in 1..Δ" — must be within 1..Δ. So exactly ≤ Δ colors.)

Hmm OK. But actually, wait: maybe we can handle the odd case differently in the recursion. Let me reconsider:

color(E, k), Δ(E) ≤ k:
- If Δ(E) ≤ 1: color all edges with color 1 (or if E empty, return).
- If k == Δ(E) and k odd: [problem case]
- Else: split evenly; both halves have max degree ≤ ceil(Δ(E)/2) ≤ ceil(k/2); if k even: recurse (E1, k/2), (E2, k/2) — wait, need Δ(Ei) ≤ k/2: Δ(Ei) ≤ ceil(Δ(E)/2) ≤ ceil(k/2) = k/2 ✓. If k odd: Δ(E) ≤ k-1 (since not the problem case), so Δ(Ei) ≤ ceil((k-1)/2) = (k-1)/2 = floor(k/2). Recurse (E1, ceil(k/2)) and (E2, floor(k/2))? Both have max degree ≤ floor(k/2), so give both palettes of size... we can give E1 palette ceil(k/2) and E2 palette floor(k/2), or any split summing to k. Since Δ(Ei) ≤ floor(k/2), giving E2 floor(k/2) colors works, E1 ceil(k/2) works. ✓.

So the ONLY problem case: Δ(E) = k, k odd, k ≥ 3. For this case, options:

Option A: find matching M saturating all degree-k vertices of E, color M with the last color, recurse on E−M with k−1 colors (even). 

Option B: find the "oriented" split (all degree-k vertices get extra in E1), recurse E1 with ceil(k/2), E2 with floor(k/2).

Option B implies... hmm, actually option B can be built from option A? If we have matching M saturating degree-k vertices: color M red... no wait, M is a full color class in option A. For option B: hmm.

Let me think about Option B directly via a flow-like/greedy construction. Actually, here's a classical way to get the oriented split: 

**Oriented split construction:** We want red degrees r_v with r_v = ceil(d_v/2) for v ∈ S (d_v = k), and r_v ∈ {floor(d_v/2), ceil(d_v/2)} for others. 

Equivalent formulation: find a subgraph F (red edges) with prescribed degrees r_v where r_v is prescribed for S and flexible (two choices) for others. This is a bipartite degree-constrained subgraph problem. Feasibility: by a Gale-Ryser / Hall-type condition. Since the full edge set with r_v = ceil(d_v/2) everywhere is "half of everything", intuitively feasible. Hmm, construction: 

Hmm, actually here's a cleaner way to think: **the oriented split exists iff we can 2-color edges such that at each v ∈ S, #red − #blue = 1, and at each v ∉ S with d_v odd, #red − #blue ∈ {−1, +1}, and at even vertices #red = #blue.** 

Consider the graph G' = G restricted to... hmm. Think of it as an Eulerian-type problem: Define at each vertex a "target imbalance". This is like finding an orientation with prescribed out-degrees (red = out?). An orientation of G where outdeg(v) = r_v. Prescribed out-degrees orientation: feasible iff for every subgraph... there's a classical theorem (Hakimi): an orientation with prescribed out-degrees exists iff sum r_v = m and for every subset... Actually for bipartite with these specific targets, maybe there's a direct argument.

Alternatively — **Option C: avoid the problem case entirely by pre-processing.** Here's an idea: handle the TOP level specially. The global Δ: if Δ is even, the recursion never hits the problem case? Let's see: color(E, Δ) with Δ even: split into halves with max degree ≤ Δ/2, recurse with palettes Δ/2 each. In the recursion, the promise is Δ(Ei) ≤ palette size. The problem case arises when Δ(Ei) = palette size and palette odd. Hmm, so it can still arise deeper. E.g., Δ = 4: halves have palette 2, max degree ≤ 2. If a half has max degree exactly 2 — fine, 2 is even, split into palettes 1,1, max degrees ≤ 1 ✓. If Δ = 6: halves palette 3, max degree ≤ 3; if max degree = 3 = palette (odd) — problem case! So it arises whenever some subproblem has odd max degree equal to odd palette. Hmm.

Wait, but actually let me re-examine: is the problem case REALLY a problem? Let me re-derive. Problem case: Δ(E) = k, k odd. Split evenly: E1, E2 with per-vertex floor/ceil. Δ(E1) = ceil over v of ceil(d_v/2)... hmm wait, actually Δ(E1) = max_v deg_{E1}(v) where deg_{E1}(v) ∈ {floor(d_v/2), ceil(d_v/2)}. The max over v of deg_{E1}(v) ≤ max_v ceil(d_v/2) = ceil(Δ(E)/2) = (k+1)/2. Similarly E2. So palettes needed: up to (k+1)/2 each, total k+1 > k. BUT: maybe we can be smarter: we don't need to give each half a contiguous palette; we need DISJOINT palettes with sizes ≥ Δ(E1), Δ(E2). Δ(E1) + Δ(E2) ≤ k+1. Hmm. But actually — wait, can Δ(E1) = Δ(E2) = (k+1)/2 actually happen? Δ(E1) = (k+1)/2 requires a vertex v with deg_{E1}(v) = (k+1)/2, so d_v ≥ k... d_v = k (max), and ceil(k/2) = (k+1)/2 ✓. Similarly Δ(E2) = (k+1)/2 requires a (possibly different) vertex u with d_u = k and its extra in E2. So yes, if there are ≥ 2 max-degree vertices and the split puts extras on both sides, we get Δ(E1) = Δ(E2) = (k+1)/2, needing k+1 colors. If ALL max-degree vertices put extras in E1, then Δ(E2) ≤ max over non-max vertices: ceil(d/2) with d ≤ k−1 (k−1 even) = (k−1)/2 ✓, and Δ(E1) = (k+1)/2. Palettes: (k+1)/2 + (k−1)/2 = k ✓. And if there's exactly ONE max-degree vertex, we can always relabel E1/E2 so that its extra is in E1! 

So: **the problem case is only a problem when there are ≥ 2 vertices of degree k.** If exactly one vertex has degree k, orient the split so its extra goes to E1 and recurse. 

Hmm, but with ≥ 2 max-degree vertices, still a problem. However — maybe we can handle it: with ≥2 max-degree vertices... Hmm.

Hold on, hold on. Let me reconsider. Actually, maybe I should think about the structure differently. Let me look up in memory the actual known simple algorithm for bipartite edge coloring in O(m log Δ): I recall it's from the paper "A fast algorithm for edge coloring bipartite graphs" or the technique used in the CF problem **"E. Rendezvous"**... 

AH WAIT. I remember now!! This is **Codeforces Round #375 (Div. 2) problem?** no... Hmm, "locks and keys"... Actually I'm now fairly certain this is **Codeforces problem 786E**... no. Let me try: **CF 845E**? no. **CF problem 841E**? no.

Hmm, what about this: the problem is from **Codeforces Round 449 (Div. 1) E?** Hmm. Or maybe it's from a more recent contest (2023-2024): "Quality Assurance on the Assembly Line" — this phrasing with "Problem B" suggests it's from a specific contest, possibly a mirror of something. The statement style ("The strict separation of locks and keys guarantees the unavoidable minimum is always achievable") suggests it's a rephrased version of a known problem. The known problem: **Codeforces 786E?** Hmm, no — I think it's **Codeforces problem "E. Edge Coloring"** hmm, or **CF 845E**... 

Actually, you know what, I'm quite sure now: it's **Codeforces Round #403?** no. Let me just think about **CF problem 786E**... I keep going in circles. Let me recall problems about bipartite edge coloring on CF: 

1. **CF 845E** — no.
2. **CF 1019?** no.
3. **"Vitaly and Cycle"?** no.
4. **CF Round 442 E?** no.
5. **CF 611?** Hmm, **"New Year and Old Property"?** no.

There IS a well-known one: **Codeforces 786E** is "Nikita and game". Not it. **Codeforces 845D** "Driving Test"? no. 

**"Timus 1671"?** — "Anansi's Thread"? Hmm, Timus 1671 is "Anansi's cobweb"? not sure.

**Codeforces 845E**... ugh. OK, actually I strongly suspect it's this: **Codeforces problem 845E "Fire in the City"** — NO. Let me think about "Problem B" — maybe from "Codeforces Round" where problems are A-E... "B" suggests a contest where this was problem B, which is unusual for such a hard problem. Maybe it's from a school contest or an ICPC-style contest (like "NEERC" or a regional). "Quality Assurance" — hmm. Could be from **"Nordic Collegiate Programming Contest"**? Or it's a rephrased **CF problem "E. Minimum spanning tree"**... 

Actually, maybe it doesn't matter. Let me also consider: maybe the intended solution is simpler than full König edge coloring because of some special structure? Let me re-read the problem statement.

"Each planned test involves exactly one lock and exactly one key... Different items are required for different numbers of tests, and the busiest item in the whole factory sets the scale of the schedule." — Δ = max degree over all vertices (locks and keys). "schedule using no more rounds than that unavoidable minimum — exactly the busiest-item count. Assign every test a round drawn from that many rounds so that no item ever has two of its tests scheduled in the same round." — proper edge coloring with exactly Δ colors. Yes, it's bipartite edge coloring (König). No special structure. m up to 4·10^5, nL, nR up to 10^5, TL 2s.

So we need an O(m log Δ) algorithm, implemented efficiently in Python. This is going to be challenging but let's think about how.

Hmm wait, actually, maybe there's a much simpler approach that's fast enough: **the "greedy with Kempe chains" but bounded palette trick**: 

There's a classical simple algorithm for bipartite edge coloring: process edges one at a time, maintain proper coloring with Δ colors. For edge (u, v): find color a free at u, color b free at v. If a == b, assign. Else, a is used at v (since v has ≤ Δ−1 used colors... wait, v might have a free color different from a). Standard: let a = a color free at u; if a free at v too, done. Else, let b = a color free at v (b ≠ a, b used at u — is b used at u? Not necessarily! u might have both a and b free). Hmm, the classical argument: at any time, each vertex has at least (Δ − current_degree(v)) ≥ 1 free colors... Let me recall the classical proof that greedy + Kempe chain works: when adding edge (u,v) to a properly Δ-colored graph (both u, v have degree ≤ Δ−1 in current): pick a free color at u (a) and free color at v (b). If a = b done. Else consider the maximal path from v alternating colors a, b (starting with an a-edge from v... wait, colors a and b at v: a is USED at v (since a free at u; if a also free at v we'd be done), b is free at v. At u: b used at u (if b free at u too... then hmm, we could just color with... no wait, we need ONE color free at both. If a free at u, b free at v, a used at v, b used at u: Kempe chain from v following a/b alternating: v —(a)— x —(b)— ... this path is simple (in a proper coloring, at each vertex at most one edge of each color, so the a/b alternating walk is a path) and it ends... it can't reach u with... the classical argument: the path starting at v with color a, alternating a,b: if it reaches u, it must reach u via an a-edge (parity: bipartite + alternating... hmm actually the classical argument: the path from v cannot end at u because u has no free... hmm, u has b used, a free. If the path from v (starting with a-edge) reaches u, it arrives at u with an a-edge or b-edge; if b-edge, then the next edge would be a-edge but a is free at u so path ends at u having arrived by b-edge — then swapping colors on the path: the path from v to u: edges alternate a,b,a,b,...,b (ending with b at u). After swap: a↔b on the path: now at v, the first edge (was a) becomes b — but b was free at v, now used; a becomes free at v... wait I need to be careful. The classical argument says: the alternating path from v (colors a,b) cannot pass through u, because: at u, color a is free, so if the path reaches u, it must be via a b-edge and then stop (no a-edge at u to continue). Then swap a↔b along the path: this frees a at v (the path's first edge at v was a-colored, becomes b) — wait no. Hmm, let me redo: path P from v: e1 (color a) incident to v, e2 (color b), e3 (a), ... Swapping on P: e1 becomes b — but b was free at v, so now v has an extra b and loses a: so a becomes free at v. At the other end (say vertex w): if w = u: last edge is b-colored, becomes a: u loses b (b was used at u), gains a: so b becomes free at u. Then color (u,v) with... a is free at v now, and a free at u? u gained a from the swap — a used at u now. Hmm wait: u had a free, b used. After swap, the b-edge at u becomes a: u now has a used, b free. And v: had a used, b free; after swap a free, b used. So now b free at u and... b used at v. Hmm, that's wrong direction. Let me redo: we want a common free color at u and v. Initially: a free at u, used at v; b free at v, used at u. Swap on path from v: at v, first edge a→b: v now: a free, b used (b was free, now the first edge is b — wait v had b free meaning no b-edge at v; after swap, e1 is b-colored at v: so b used at v, a free at v. At u (end of path, arrived by b-edge e_t): e_t b→a: u: b free now, a used (a was free, now e_t is a-colored). Result: a free at v, a used at u; b used at v, b free at u. Still no common free color! Hmm, that means the path SHOULD NOT end at u via b-edge... 

Let me re-derive the classical argument. Classical (from proofs of König via greedy): Actually the classical statement: the alternating path from v with colors {a, b} where a is free at u and used at v, b free at v and used at u: the path from v: first edge must be a-colored (b free at v). Then alternate. Claim: this path does NOT reach u. Why? Suppose it reaches u. The path alternates a,b,a,b,.... At u: a is free at u. So the path cannot arrive at u via an a-edge and continue... it arrives via some edge; if it arrives via a-edge, then it would need to continue with b-edge — fine, b is used at u, so it continues. Hmm wait, so arriving via a-edge is possible and continues with the unique b-edge at u. Arriving via b-edge: next needs a-edge at u: none (a free at u), so path ends at u. Hmm, so the path CAN reach u. But then: swap colors on the path. Case path ends at u via b-edge: after swap, at u: the b-edge becomes a: a now used at u, b free at u. At v: first a-edge becomes b: a free at v, b used at v. Now: free at u: b; free at v: a. Still no common! Hmm?? So the classical argument must be different. 

Oh wait, I think I misremembered: the classical argument swaps on the path and then the edge gets color... let me recompute. We want to color edge (u,v). After swapping path P (from v to u, ending with b-edge at u): now at v: a free. At u: b free. Hmm, no common color still. That can't be right — the classical algorithm works. Let me recheck: maybe the path should start at v with... hmm. Let me look at it as: we want to free up color a at v (a is free at u). The alternating path from v in colors {a,b}: starts with a-edge at v (since b free at v, the first edge must be a). If the path does NOT reach u: swap colors on the whole path: at v: a-edge becomes b: a freed at v ✓; at the far end w ≠ u: the path ends at w because... it ends when the next needed color is free at w. The path: e1(a), e2(b), ..., e_t. If t even: e_t is b-colored, ends at w because a free at w; after swap: e_t becomes a: fine, still proper (a was free at w). If t odd: e_t is a-colored, ends at w because b free at w; after swap e_t becomes b ✓. Internal vertices: have one a and one b on the path, swap keeps proper. And u is not on the path, so a stays free at u. Then color (u,v) with a ✓. If the path DOES reach u: it must arrive via b-edge (as argued, if it arrives via a-edge it continues; it could pass through u multiple times? No — path is simple, and at u: if it arrives via a-edge, continues via b-edge, then leaves; could it come back? No, simple path). Arrives via b-edge, ends at u (a free at u). Now swap: at u: b-edge becomes a — a no longer free at u; b becomes free at u. At v: a becomes free. So now: free at u: b (and whatever else), free at v: a. Hmm, still stuck?! 

Wait, no — I think I've got the direction wrong: we should follow the path from v but the claim is it cannot reach u because of PARITY: the graph is bipartite! u and v are on OPPOSITE sides (edge (u,v) connects L to R). The path from v: e1 (a) goes to the other side, e2 (b) comes back, ... After t edges, the path is at side: v's side if t even, other side if t odd. If the path ends at u: u is on the opposite side from v, so t is ODD, so e_t is a-colored (e1 = a, e2 = b, odd positions a). But we argued it must arrive via b-edge (else it continues). CONTRADICTION! So the path cannot reach u. 

So the algorithm: for edge (u,v): a = free color at u, b = free color at v (a ≠ b case). Walk the alternating path from v (colors a,b, starting with a). It's guaranteed (by bipartiteness) not to reach u. Swap a↔b on the path. Now a is free at v. Color (u,v) with a. 

Complexity: finding free colors at u and v: O(1) with "first free color" pointers? Hmm, we need ANY free color at u. Maintain per-vertex a pointer/heap of free colors? A vertex u with current degree d_u has Δ − d_u free colors; finding one: maintain a boolean array used[color] per vertex? That's Δ per vertex memory = too much (10^5 vertices × 10^5 colors). Instead: maintain per vertex a set/stack of free colors? Total free colors = sum (Δ − d_v) could be huge (10^10). Hmm. Alternative: maintain per vertex the count of used colors and... we need to find a free color quickly. Trick: maintain for each vertex a "candidate free color" — hmm, but colors get used/freed dynamically.

Alternative: process differently: the classical implementation maintains for each vertex a small structure... Hmm. Actually, here's a trick: since we process edges one by one and each vertex's degree only INCREASES (we never remove edges), the set of used colors at v only grows... but the Kempe chain swaps change colors of existing edges (a↔b on path), so used colors at a vertex can change (swap a for b). Hmm, but the NUMBER of used colors at v = current degree, monotone increasing. Free colors: complement. Finding a free color at v: we can maintain a pointer: the smallest color not yet used? But swaps can free up smaller colors... Hmm, but actually we don't need the SMALLEST free color, just ANY free color. Maintain per vertex v a pointer p_v = a color that is free at v (lazy): when we need a free color at v, check if p_v is still free (color p_v used at v? need per-vertex color→edge lookup...). 

Hmm, this is getting complicated. Let me think about the total complexity of the Kempe-chain greedy: each edge insertion: O(path length) for the chain walk. Path lengths can be long (O(n)). Worst case total O(m·n) = 4·10^5 · 10^5 = 4·10^10. Too slow in theory. But average case might be fine... risky. Actually, hmm, is there a bound? The alternating path in colors {a,b}: its length is at most (number of edges with colors a or b) which can be O(m). No good bound. Too risky.

**Let me go back to the Euler-split recursion and solve the odd case properly.**

I recall now — the Cole–Ost–Schirra paper "Edge-coloring bipartite multigraphs in O(E log D) time" — and I recall the key idea for odd degree: they use the Euler split where at each vertex, the pairing is chosen such that... Actually, I found it in memory: the COS algorithm handles it as follows (from various course notes):

**Algorithm (from course notes on COS):**
- color(G, k): if k = 1, color all edges with color 1.
- If k is even: Euler split G into G1, G2 (each vertex's degree split evenly: d/2, d/2 for even d; (d±1)/2 for odd d). Then Δ(G1), Δ(G2) ≤ k/2. Recurse color(G1, k/2), color(G2, k/2).
- If k is odd: Let G' = G plus dummy vertex x adjacent to all odd-degree vertices (all degrees even now; Δ(G') ≤ k+1... hmm wait, degree-k vertices get x-edge → degree k+1). Hmm, then Euler split G' into G1', G2' with degrees exactly halved (d/2 each since all even). Then remove x: G1 = G1' minus x-edges, G2 = G2' minus x-edges. At each vertex v: deg_{G1}(v) + deg_{G2}(v) = d_v, and deg_{G1}(v) ∈ {(d_v−1)/2, (d_v+1)/2} for odd d_v, = d_v/2 for even. So Δ(G1), Δ(G2) ≤ (k+1)/2. Then recurse color(G1, (k+1)/2) and color(G2, (k−1)/2)?? But Δ(G2) could be (k+1)/2 > (k−1)/2. Hmm, same issue. UNLESS: the x-edges are distributed cleverly. Hmm, in G2', the x-edges in G2' — at x, deg_{G2'}(x) = deg_{G1'}(x) = (#odd)/2. Hmm.

I genuinely don't remember how COS handles it. Let me think from scratch about the odd case with a fresh idea:

**Fresh idea for odd k (Δ(E) = k):** Find matching M saturating all degree-k vertices (Option A). Then E − M has max degree ≤ k−1, recurse with k−1 colors (even), and M gets color k. The matching M: how to find efficiently WITHOUT general matching algorithms? 

Hmm! Here's a thought: the degree-k vertices S. Consider the subgraph induced by edges incident to S? No... A matching saturating S: greedy won't work directly. But maybe we can use the Euler split machinery to find it: 

Claim: if we Euler-split G (k odd) into G1, G2 (floor/ceil per vertex), then... the degree-k vertices have (k+1)/2 edges in one half and (k−1)/2 in the other. Hmm, the half where a degree-k vertex has (k+1)/2 edges — that half has max degree (k+1)/2 at that vertex... 

Alternative: **Reduce odd k to odd via "peeling one matching from the split":** Hmm.

**Completely different approach: the "two-phase" algorithm.** Phase 1: color the graph with Δ + O(log) colors greedily (easy: greedy edge coloring uses ≤ 2Δ−1 colors; even simpler, process edges and assign each edge a color not used at its endpoints — with 2Δ−1 palette, greedy always works since each edge's endpoints block ≤ 2(Δ−1) colors... wait, at any time, u has ≤ Δ−1 used colors and v has ≤ Δ−1, so ≤ 2Δ−2 blocked, palette 2Δ−1 suffices). Phase 2: reduce the number of colors from 2Δ−1 to Δ via Kempe-chain recoloring... that's the Vizing-style approach, complex.

**Another angle: since this is Python and constraints are m ≤ 4·10^5, maybe an O(m √something) or even O(m·log) with heavy constant is fine if we vectorize with numpy?** Hmm, Euler splits with numpy? The recursion has data-dependent structure (pairings at vertices), hard to vectorize.

Wait, actually, let me reconsider the problem constraints: nL, nR ≤ 10^5, m ≤ 4·10^5. Δ ≤ min(...)? No: Δ ≤ max(nL, nR) = 10^5 (a lock can be tested with up to nR = 10^5 keys). Hmm.

Let me reconsider the Kempe-chain greedy more carefully — maybe its worst case is actually acceptable? Each edge insertion: walk alternating path. Total path length over all insertions: worst case O(m) per insertion → O(m²) = 1.6·10^11. No.

But WAIT: there's a classical optimization: **process edges in a specific order and use "small palettes"**: the trick from the O(m log Δ) analysis of the greedy: if we process edges and always use the SMALLEST free color... no.

Hmm, let me think about the structure of the problem again. Actually, maybe I should think about the following classical simple algorithm for bipartite edge coloring that's O(m Δ) but where the constant is tiny and Δ... no, Δ up to 10^5.

OK here's another classical approach I remember for EXACTLY this kind of problem (I'm now recalling an editorial — I'm pretty sure this is from Codeforces problem **"E. Ice cream coloring"** no... **CF Round 445 E?** hmm...). 

**The "chain" algorithm with O(m log) via divide and conquer on colors — the approach:** solve(colors 1..k, edges E) where every vertex has degree ≤ k:
- if k == 1: assign.
- Split colors into first half (1..k/2) and second half.
- We need to partition E into E1 (colorable with first half) and E2 (second half), with Δ(E1) ≤ k/2, Δ(E2) ≤ ceil(k/2)... 

For this we need the split where each vertex v has deg_{E1}(v) ≤ k/2 and deg_{E2}(v) ≤ k/2 (if k even). Since d_v ≤ k, splitting evenly gives both ≤ ceil(d_v/2) ≤ ceil(k/2) = k/2 + [k odd]. For k even ✓. For k odd: need deg_{E1}(v) ≤ (k+1)/2 and deg_{E2}(v) ≤ (k+1)/2, but palettes are (k+1)/2 and (k−1)/2. So E2 needs max degree ≤ (k−1)/2: vertices with d_v = k must have ≤ (k−1)/2 in E2, i.e., their extra in E1. As established. So the crux remains: **the oriented split for odd k.**

Let me now think hard about constructing the oriented split for odd k efficiently.

**Oriented split problem:** G bipartite, max degree k (odd), S = {v : d_v = k}. Find 2-coloring of edges (red/blue) with: deg_red(v) = (d_v+1)/2 for v ∈ S; deg_red(v) ∈ {floor, ceil}(d_v/2) for v ∉ S. (Then blue automatically: (d_v−1)/2 for v ∈ S; ≤ ceil(d_v/2) ≤ (k−1)/2 for v ∉ S since d_v ≤ k−1... wait d_v ≤ k−1 for v ∉ S, and if d_v = k−1 (even), ceil = (k−1)/2 ✓; if d_v < k−1, ceil(d_v/2) ≤ (k−1)/2 ✓.)

So we need a subgraph F (red) with deg_F(v) = r_v where r_v = (d_v+1)/2 for v ∈ S, and r_v ∈ {(d_v−1)/2, (d_v+1)/2} for odd d_v ∉ S, r_v = d_v/2 for even d_v.

**Existence:** By the padding argument: pad G to a k-regular bipartite graph H (with dummy vertices/edges — conceptually). H has a proper k-edge-coloring (König). Hmm, then take one color class... hmm, that's circular (we're trying to compute the edge coloring). But for EXISTENCE of the split: take H k-regular, edge-color H with k colors (exists by theorem), let F = union of color classes 1..(k+1)/2. Then at each vertex of H: deg_F = (k+1)/2 exactly. At real vertices v ∈ S: all edges real, deg_F(v) = (k+1)/2 ✓. At real v ∉ S: deg_F(v) = (k+1)/2 counting dummy edges; real part: (k+1)/2 − (#dummy edges at v in F) — dummy edges at v: d_v... hmm, v has k − d_v dummy edges in H, distributed among color classes; #dummy at v in F ∈ [max(0, (k+1)/2 − d_v), min(k − d_v, (k+1)/2)]. Real red degree = (k+1)/2 − dummy_in_F ∈ {(d_v−1)/2, ..., (d_v+1)/2}? Let me verify bounds: real_red ≤ (k+1)/2 − max(0, (k+1)/2 − d_v) = min((k+1)/2, d_v + ... hmm: if d_v ≥ (k+1)/2: real_red ≤ (k+1)/2 ≤ ceil(d_v/2)? Is (k+1)/2 ≤ ceil(d_v/2) when d_v ≥ (k+1)/2, d_v ≤ k−1: ceil(d_v/2) ≥ ceil((k+1)/4)... hmm no. Let me just check: we need real_red ∈ {floor(d_v/2), ceil(d_v/2)}. real_red = (k+1)/2 − x where x = # dummy edges at v colored in first (k+1)/2 classes, 0 ≤ x ≤ k − d_v. Also real_red ≤ d_v and real_red ≥ (k+1)/2 − (k − d_v) = d_v − (k−1)/2. Hmm, so real_red ∈ [max(0, d_v − (k−1)/2), min(d_v, (k+1)/2)]. We need real_red ∈ {floor(d_v/2), ceil(d_v/2)} — but the coloring gives us only a range, not exact. Hmm, so this doesn't immediately prove the oriented split exists. Let me check small cases: k = 3, d_v = 2 (v ∉ S): need real_red ∈ {1}. Range: [max(0, 2−1), min(2, 2)] = [1, 2]. So real_red could be 2 — bad (then blue real degree = 0, fine actually? wait we need red ∈ {1} exactly for d_v = 2: floor=ceil=1. If real_red = 2, then v's 2 real edges are both red — violates the split requirement (blue degree at v = 0 ≤ (k−1)/2 = 1 ✓, red degree 2 ≤ (k+1)/2 = 2 ✓). Hmm wait, actually for the recursion we need: red degrees ≤ (k+1)/2 GLOBALLY and blue degrees ≤ (k−1)/2 GLOBALLY. At v ∉ S with d_v = 2: red = 2 ≤ 2 ✓, blue = 0 ✓. Oh wait, I over-constrained! We don't need per-vertex floor/ceil exactly; we need: red degree ≤ (k+1)/2 for ALL v, blue degree ≤ (k−1)/2 for ALL v, and red+blue = d_v. Since d_v ≤ k: if d_v ≤ k−1: red ≤ min(d_v, (k+1)/2)... hmm, we need BOTH red ≤ (k+1)/2 and blue ≤ (k−1)/2, i.e., red ≥ d_v − (k−1)/2. So the constraint is: **d_v − (k−1)/2 ≤ deg_red(v) ≤ (k+1)/2** for all v (and for v ∈ S: d_v = k forces deg_red(v) = (k+1)/2 exactly). 

So the oriented split problem: find F ⊆ E with deg_F(v) ∈ [max(0, d_v − (k−1)/2), min(d_v, (k+1)/2)] for all v, AND deg_F(v) = (k+1)/2 for v ∈ S. Hmm wait, for v ∈ S, the constraint interval is [k − (k−1)/2, (k+1)/2] = [(k+1)/2, (k+1)/2] — forced ✓ consistent.

Now existence via the padding argument: H k-regular, k-edge-colored, F = first (k+1)/2 classes: at every vertex of H, deg_F = (k+1)/2. Real vertices: deg_F^{real}(v) = (k+1)/2 − (#dummy at v in F). #dummy at v = k − d_v. So deg_F^{real}(v) ≥ (k+1)/2 − (k − d_v) = d_v − (k−1)/2 ✓ and ≤ (k+1)/2 ✓ and for v ∈ S: no dummies → = (k+1)/2 ✓. **So the oriented split EXISTS.** But constructing it via padding + edge coloring is circular. Need direct construction.

**Direct construction of oriented split:** Hmm. Think of it as a flow problem: bipartite graph, each edge carries 0 or 1 (red), vertex v has supply/demand: deg_F(v) ∈ [lo_v, hi_v] with lo_v = max(0, d_v − (k−1)/2), hi_v = min(d_v, (k+1)/2), and for S: lo = hi = (k+1)/2. This is a bipartite b-matching feasibility — solvable via max-flow. But doing max-flow at every odd level of the recursion: too slow? Number of odd levels: O(log Δ). Each max-flow on m edges: O(m · something). Hmm, with unit-ish capacities... Actually this feasibility problem is a "degree-constrained subgraph" problem which can be solved by a simple augmenting-path algorithm: start with F = ∅... hmm, we need to hit exact degrees. 

Alternative direct construction: **greedy + fix-up via alternating paths (like bipartite b-matching):** Start with any even split (Euler split, floor/ceil). Then fix the S vertices: in the even split, each v ∈ S has extra in E1 or E2 (deg_{E1}(v) ∈ {(k−1)/2, (k+1)/2}). Let A = S vertices with extra in E2 (wrong side), B = S vertices with extra in E1 (right side). We want to move extras from A-side to E1. |A| extras in E2 need to become... hmm, we can't just move individual edges: moving edge e from E2 to E1 at vertex v ∈ A fixes v but breaks the other endpoint u (u's E1 degree increases by 1, might exceed its cap). Fix by moving another edge at u from E1 to E2, which breaks u's other endpoint... — this is exactly an alternating path augmentation in the "split graph". Since the target is feasible (proved above), augmenting paths exist. Each augmentation: walk alternating path from a vertex in A until reaching a vertex with slack. Complexity: each augmentation O(path length); number of augmentations = |A| ≤ ... hmm, could be O(n) augmentations each O(m) → O(nm) worst case. Too slow? Hmm. But maybe with a smarter analysis... risky.

Hmm, hold on. Let me reconsider — maybe there's a neater way to see/construct the oriented split via Euler tours with TWO dummy vertices or a weighted trick:

**Trick: split S by side.** S_L = max-degree vertices in L, S_R = in R. Note: edges between S_L and S_R... Hmm. Here's an idea: add dummy vertex x_L connected to all odd-degree vertices in L, and x_R connected to all odd-degree vertices in R. Hmm, then add edge x_L—x_R? Let me think: we want an Euler-type construction where the "extra" at S_L vertices goes red and at S_R vertices goes red as well. 

Alternative idea: **make the graph "nearly regular" cheaply:** Add dummy edges to bring every vertex's degree up to k or k−1... specifically: we want a graph where every vertex has degree k or k−1... hmm, that doesn't immediately fix the split issue.

Hmm hmm. Let me look at this from the literature angle again. I'm quite sure the COS algorithm's odd case is handled like this (now I actually recall reading a clean exposition — maybe in the "Duke/Course notes" or a Codeforces editorial): 

**"If k is odd: find a matching M that saturates all vertices of degree k. Color M with color k. Recurse on E − M with k − 1 colors."** And the matching M is found... in the editorial I'm thinking of, they found M via **Hopcroft-Karp or via the padding+flow** — but with the observation that this happens only O(log Δ) times... no wait, the matching must be found at every odd level. Hmm, but actually — WAIT. Here's a KEY realization: the matching M saturating degree-k vertices doesn't need to be found via general matching! Because of the special structure: **the subgraph of edges incident to S... ** hmm no.

Hmm, actually here's ANOTHER key realization: maybe we can avoid the odd case entirely by **pre-splitting the palette differently**: 

solve(E, k) with Δ(E) ≤ k: choose split point k1 + k2 = k, k1, k2 ≥ 1. Split E into E1, E2 with Δ(E1) ≤ k1, Δ(E2) ≤ k2. For this we need a split with per-vertex deg_{E1}(v) ≤ k1 and deg_{E2}(v) ≤ k2. Since d_v ≤ k = k1 + k2: if d_v ≤ k, can we always split with deg_{E1} ≤ k1, deg_{E2} ≤ k2? Per vertex: need k1 ≥ deg_{E1}(v) ≥ d_v − k2, so need interval [max(0, d_v − k2), min(d_v, k1)] nonempty ✓ always (since d_v ≤ k1 + k2). So per-vertex it's fine; the question is a GLOBAL consistent split (it's a flow feasibility again). The Euler split gives the balanced version. For k1 = ceil(k/2), k2 = floor(k/2): the constraint at v: deg_{E1}(v) ∈ [max(0, d_v − k2), min(d_v, k1)]. For v ∈ S (d_v = k): deg_{E1}(v) = k1 forced. So same problem. 

**What if we choose k1, k2 both ≥ ceil(k/2)?** Impossible since k1 + k2 = k < 2·ceil(k/2) when k odd. 

**What if we allow THREE-way splits or unbalanced recursion?** E.g., k odd: split into E1 (palette ceil(k/2)) and E2 (palette ceil(k/2)) — total k+1 colors — NOT allowed at the top level (must use ≤ Δ), but ALLOWED at deeper levels? NO — deeper levels also must fit within the global Δ palette... wait, actually NO! Deeper levels just need disjoint sub-palettes of the global palette. The global palette is Δ colors. At the top: solve(E, Δ). If we split the palette into sizes p1 + p2 = Δ and edge sets with Δ(Ei) ≤ pi. The constraint is always: partition palette, partition edges, degrees fit. So at every level, "palette sizes sum exactly" — no slack ever. Hmm, unless we DON'T use the full palette at some level: if Δ(E) < k (palette bigger than needed), we have slack. The problem case is exactly Δ(E) = k odd.

**Idea: maintain the invariant Δ(E) ≤ k with STRICT inequality handling:** solve(E, k): if Δ(E) ≤ k − 1... hmm, we could recurse solve(E, Δ(E)) always — i.e., at each node, shrink palette to the actual max degree. Then the problem case is Δ(E) odd (with palette = Δ(E) odd). Then split palette into ceil+floor and need the oriented split. So no escape: **must handle odd Δ(E) with oriented split (or matching peel).**

Alright, so let me focus on constructing the oriented split (or the matching peel) efficiently. Let me think about the matching peel again, because a matching saturating S might be constructible greedily with alternating paths but with a GOOD amortized bound... Hmm.

Actually WAIT. Let me reconsider the problem from scratch. Maybe there's a completely different, simpler algorithm that people use for this problem in practice. Let me think about what's special: bipartite, m ≤ 4·10^5. 

**Idea: Orient edges to make an Eulerian-type structure, then use "round-robin" coloring?** Hmm: There's a classical simple algorithm for edge-coloring bipartite graphs: **the "greedy via Hall" / "one color at a time via matching"** — too slow (Δ matchings).

**Idea: The "Δ-regularization via dummy edges" but ONLY conceptually, with the Euler split doing the work:** Here's a cleaner way to think about the whole algorithm that I now recall from an editorial (I'm increasingly confident this is the CF problem **"E. Minimum spanning tree"**... no. OK whatever):

**The "virtual regularization" approach:** Conceptually pad G to Δ-regular bipartite H. Then H can be edge-colored by RECURSIVE EULER SPLITS where every split is perfectly balanced (all degrees halve exactly). The recursion on a d-regular graph: split into two d/2-regular graphs (d even) — via Euler tours (d-regular ⟹ all degrees even if d even ⟹ Eulerian ⟹ alternate tour edges). If d odd: d-regular graph, split into... hmm, d odd: each vertex has odd degree; add perfect matching? A d-regular bipartite graph with d odd contains a perfect matching (König/Hall). Remove it: (d−1)-regular, even. So: peel perfect matchings when odd. Peeling a perfect matching from a regular bipartite graph = finding a perfect matching — O(m) via... Hall's theorem constructive proof? Finding a perfect matching in a regular bipartite graph can be done greedily?? Hmm: in a d-regular bipartite graph, does GREEDY matching always find a perfect matching? NO (greedy can get stuck). But there's a classical result: in a d-regular bipartite graph, any maximal matching has size ≥ ... hmm, a maximal matching in a d-regular graph has size ≥ n/(2d−1)... not perfect.

BUT: the padding is infeasible (Δ·n dummy edges up to 10^10). However — maybe we can do the padding VIRTUALLY: the dummy edges are only conceptual; in the Euler split, dummy edges just pair up with real edges at vertices. Hmm, interesting: let me think about what the padded graph's Euler split does to the REAL edges. 

Padded graph H: Δ-regular. All vertices degree Δ. If Δ odd: every vertex has odd degree. Peel a perfect matching M₀ from H (conceptually): (Δ−1)-regular, even degrees. Euler split: alternate Euler tours → two (Δ−1)/2-regular halves H1, H2. Then recurse on each with palettes (Δ−1)/2... wait total palette Δ: M₀ gets 1 color, H1 and H2 get (Δ−1)/2 each: 1 + (Δ−1)/2 + (Δ−1)/2 = Δ ✓. Then recursively: Hi is (Δ−1)/2-regular; if (Δ−1)/2 odd, peel perfect matching again, etc. So the algorithm on regular graphs: **repeatedly: if d odd, peel perfect matching (1 color); if d even, Euler split into two d/2-regular halves.** Depth O(log Δ), each level O(edges). Total O(m log Δ) — plus perfect matching computations at odd levels: how many odd levels? At most O(log Δ) (each level roughly halves d; d passes through odd values O(log Δ) times). Each perfect matching on a d-regular graph with m' edges: Hopcroft-Karp O(m'√n) — too slow. BUT in a REGULAR bipartite graph, a perfect matching can be found in O(m') time by a simple algorithm? Hmm: is that true? There's a classical algorithm: in a d-regular bipartite graph, a perfect matching can be found in O(m) time?? I recall something: "An O(E) algorithm for finding a perfect matching in a regular bipartite graph" — hmm, actually I recall that finding a perfect matching in a d-regular bipartite graph can be done by a simple greedy-with-fixups... Let me think: In a d-regular bipartite graph, take ANY maximal matching... no. 

Hmm, actually there's the classical result by Cole–Ost–Schirra that uses exactly this: they show a perfect matching in a regular bipartite graph can be found in O(m) — via the "Euler split" itself! Here's how: d-regular bipartite, d ≥ 2 even: Euler split into two d/2-regular graphs. d odd: hmm. Alternatively: **perfect matching in regular bipartite graph via greedy + short augmenting paths?** In a d-regular graph, greedy maximal matching leaves ≤ n/(2d)... hmm: a maximal matching M in a d-regular graph: unmatched vertices form an independent set... in bipartite d-regular: if M is maximal, unmatched L vertices have all neighbors matched (to unmatched R? no — maximal means no edge between two unmatched vertices). Each unmatched u ∈ L has d neighbors, all matched, each matched R vertex adjacent to ≤ ... hmm, counting: unmatched L vertices: U_L, unmatched R: U_R, no edges between them. Edges from U_L: d|U_L|, all going to matched R vertices... this doesn't immediately bound |U_L|. Hmm, actually: consider the matched R vertices adjacent to U_L... Standard bound: maximal matching in graph with max degree... in a d-REGULAR bipartite graph: |U_L| = |U_R| (since |M| matches equally...). Hmm: |L| = |R| = n (regular bipartite ⟹ |L| = |R|). |U_L| = |U_R| = n − |M|. Edges from U_L go to R \ U_R; edges from U_R come from L \ U_L. Hmm, no contradiction with large U. E.g., d=2: cycle C₆? Perfect matching exists; greedy maximal could pick... on a cycle, greedy picks alternate edges — could leave 2 unmatched if odd cycle, but bipartite cycles are even → greedy on even cycle: picks edges greedily; e.g., C₈: pick e1, then e3, e5, e7 — perfect. Actually greedy on an even cycle always gets a perfect matching? Pick any edge, removes its two neighbors' availability... C₈ vertices 1..8, pick edge (1,2): remaining path 3-4-5-6-7-8 plus edge (8,1)? no, (8,1) is an edge of the cycle: C₈ = 1-2-3-4-5-6-7-8-1. Pick (2,3): then can't use (1,2),(3,4); remaining: 4-5,6-7,8-1: pick all → perfect. Hmm, greedy on even cycle: after picking an edge, the rest is a path with even # vertices → greedy on a path picks every other edge → perfect. So cycles fine. But general d-regular: greedy can fail to be perfect. Example: d=2 regular bipartite = disjoint even cycles → greedy always perfect? On a path/cycle, greedy maximal matching: cycle even → perfect. So d=2 fine. d=3: can greedy get stuck? Sure, probably. Then augmenting paths fix it — but total time?

OK you know what, let me step back and think about the ACTUAL practical solution used in CP for this problem, because I'm quite sure this problem exists on Codeforces with an editorial. Let me think REALLY hard about which problem: "nL nR m", "locks and keys", "rounds", "Δ = max degree", "output YES and the coloring"... 

I REMEMBER NOW!!! It's **Codeforces problem 786E**? NO. It's... **"Codeforces Round #442"**... no. Hmm, "Problem B" — contests with problem B being this hard... Maybe it's from **"Codeforces Round" sponsored by some company**... OR it's from **"Technocup"**... OR — wait, could it be from **"Codeforces 845" (Codeforces Round #433)**... 

Hmm, alternatively it might be **CF problem 1019?** Let me think about the phrase "the busiest item": the original problem might be **"Codeforces 1201?"** hmm. OR it could be from **"Codeforces Round 627"**? 

Actually — I think I've got it: **Codeforces problem 786E is NOT it; it's Codeforces problem "E. Postcards"?** no... 

Let me try yet another angle: maybe it's **this problem: Codeforces 845E** — NO. **Codeforces 845 (Round #433) problems: A. Unimodal Array? no that's 831...** ugh.

FINE. Let me just think about what the editorial technique would be, independent of the source. Given the constraints (m ≤ 4·10^5, TL 2s — generous for the intended O(m log Δ) in C++), the intended solution is almost surely the Euler-split recursion. For the odd case, the standard handling in most CP editorials I've seen for "bipartite edge coloring" is:

**Standard CP approach for odd case:** "If k is odd, find a matching saturating all vertices of degree k, assign it color k, recurse on the rest with k−1." And they find this matching via **Hopcroft–Karp restricted appropriately** or via the following neat observation: 

**Observation:** the vertices of degree k... Hmm, wait, actually here's a MUCH simpler observation that might resolve everything: 

**In the recursion, we can ALWAYS keep palettes as powers of 2!** solve(E, k) where k is a power of 2, Δ(E) ≤ k: if k == 1: color 1. Else Euler split E → E1, E2 with Δ(Ei) ≤ ceil(Δ(E)/2) ≤ ceil(k/2) ≤ k/2 (since k power of 2 ≥ Δ(E); if Δ(E) ≤ k/2 then ceil(Δ(E)/2) ≤ k/2 ✓; if Δ(E) ∈ (k/2, k], ceil(Δ(E)/2) ≤ ceil(k/2) = k/2 ✓). So Δ(E1), Δ(E2) ≤ k/2 ALWAYS. Recurse with k/2 palettes. **NO ODD CASE EVER!** But wait — the top-level palette must be Δ, not a power of 2! If Δ is not a power of 2, we'd use 2^ceil(log2 Δ) > Δ colors — NOT ALLOWED. Hmm. Unless... we're allowed to use fewer: the recursion with power-of-2 palette k > Δ(E) uses at most Δ(E) colors? NO — the recursion solve(E, k) with k = 2^t > Δ(E) would still potentially use up to k colors? Let's see: it splits into E1, E2 each with palette k/2, recurses... at the bottom, color classes used: the union of palettes = k colors total, but does it actually USE colors > Δ(E)? The coloring it produces uses at most... hmm, the recursion doesn't track Δ(E) — it just colors E1 with palette k/2 (using up to k/2 colors... well, using at most Δ(E1) ≤ ... hmm, actually the colors USED at the end: each leaf uses color = its palette position. The number of DISTINCT colors used could be up to... hmm. Let me think: if Δ(E) = 3 and k = 4: split E into E1, E2 with Δ(Ei) ≤ 2, palettes {1,2} and {3,4}. E1 uses colors 1,2 (maybe just 1), E2 uses 3,4 (maybe just 3). Total distinct colors used: up to 4 > 3 = Δ. NOT ALLOWED. So power-of-2 padding fails at the top. 

BUT: what if at the top we use palette Δ and then... the issue is only the top level(s) where palette is odd. Hmm, wait: actually let me reconsider: the problem case in the general recursion was Δ(E) = k, k odd. With power-of-2 palettes, Δ(E) ≤ k and the split gives Δ(Ei) ≤ ceil(Δ(E)/2) ≤ k/2 — always fine. The ONLY issue is the top: palette must be exactly Δ (or rather, colors must be in 1..Δ). 

**So: handle the top level specially!** Top: palette Δ. If Δ is even: split palette Δ/2 + Δ/2; need Δ(Ei) ≤ Δ/2: Euler split gives Δ(Ei) ≤ ceil(Δ/2) = Δ/2 ✓ (Δ even). Then recurse with power-of-2 palettes? NO wait — after the first split, the palettes are Δ/2 each, and Δ(Ei) ≤ Δ/2; if Δ/2 is odd and Δ(Ei) = Δ/2, problem case again. Hmm, e.g., Δ = 6: palettes 3,3; Δ(Ei) ≤ 3; if Δ(E1) = 3 (odd = palette): problem. So it's not just the top. The problem case arises at any node where palette is odd and equals Δ(E). 

Hmm, so we need: at nodes with odd palette k, ensure Δ(E) ≤ k−1, then we can... wait: if Δ(E) ≤ k−1 with k odd: Euler split gives Δ(Ei) ≤ ceil((k−1)/2) = (k−1)/2. Palettes: split k into (k+1)/2 and (k−1)/2: E1 with (k+1)/2 ≥ (k−1)/2 ✓, E2 with (k−1)/2 ✓. OR split k into ceil/floor any way — both halves fit in (k−1)/2 ≤ both palettes ✓. So: **odd palette is fine as long as Δ(E) ≤ k−1.** And even palette k: Δ(E) ≤ k fine. So the invariant we'd like: **at every node with odd palette k, Δ(E) ≤ k−1.** 

Can we maintain this? At the top: palette Δ, Δ(E) = Δ. If Δ even ✓ fine. Split: palettes Δ/2, Δ/2 (even if Δ/2 even...). Hmm, Δ = 6: palettes 3,3 (odd), Δ(Ei) ≤ 3 — we need ≤ 2 for the invariant. NOT guaranteed. Hmm. Alternatively split palette 6 into 4 + 2? Then need Δ(E1) ≤ 4, Δ(E2) ≤ 2 — the split must satisfy per-vertex deg_{E2}(v) ≤ 2: since d_v ≤ 6, need deg_{E1}(v) ≥ d_v − 2: feasible per-vertex but globally it's the flow problem again. Hmm, but WAIT: maybe with the Euler split we can choose the balance point: Euler split gives floor/ceil; to get deg_{E2}(v) ≤ 2 for all v we need... d_v ≤ 3 gives ceil(d_v/2) ≤ 2 ✓; d_v ∈ {4,5}: ceil = 2 or 3 — d_v=4: ceil=2 ✓; d_v = 5: ceil = 3 ✗. Hmm so vertices of degree 5 are problematic for palette-2 E2. But we could put such vertices' extras in E1: oriented split again. ARGH. Same issue.

OK so fundamentally: **odd palette + max degree = palette requires the oriented split (or matching peel).** Let me now just solve the oriented split problem efficiently. Let me think about it as a flow problem and find a fast combinatorial algorithm.

**Oriented split as flow:** We need F ⊆ E with deg_F(v) ∈ [lo_v, hi_v]. This is feasibility of bipartite b-matching. There's a classical simple algorithm: start with F = ∅ (or any F), and repeatedly fix violated vertices via alternating paths — essentially max-flow augmenting. The total number of augmentations = sum of deficits ≤ ... each augmentation adds one edge to F (or adjusts). Total augmentations ≤ Σ hi_v ≤ m. Each augmentation walks a path O(m). Worst case O(m²). Too slow in theory. But maybe in practice fine? Risky.

**Better: think again about the structure.** Let me reconsider. In the recursion, the problem case: Δ(E) = k odd. Vertices S of degree k. What if k is odd but... hmm, let me think about the bipartite structure: S_L and S_R. 

**KEY INSIGHT ATTEMPT:** In a bipartite graph, consider the degree-k vertices. Claim: there's a matching saturating S (proved via padding). Can we find it via a SIMPLE direct method? Let's think about the padded graph virtually: H = G + dummy edges making it k-regular. The dummy edges: at real left vertex v: k − d_v dummy edges to dummy right vertices; we need enough dummy right vertices: total dummy edge endpoints on right = k·nL − m; dummy right vertices needed: this can be huge (10^10) — but VIRTUALLY, dummy vertices are interchangeable! A dummy right vertex with degree k connected to... hmm, the point of padding is Hall's condition for the perfect matching. But we want the matching to saturate S using REAL edges only. 

Alternative: **direct Hall-based greedy for saturating S:** We want a matching saturating S = S_L ∪ S_R. Hmm, general bipartite matching — but with the special property that S-vertices have max degree. Does that special property make greedy/alternating-path fast? Consider augmenting-path matching (Kuhn's algorithm) to saturate S: each S-vertex needs one augmenting path; Kuhn: O(V·E) = 2·10^5 · 4·10^5 — way too slow. Hopcroft-Karp: O(E√V) ≈ 1.3·10^8 operations — in C++ fine, in Python... 1.3·10^8 basic ops in Python ≈ 100+ seconds. Too slow. And this happens at multiple recursion levels. NO.

Hmm hmm hmm. OK let me look at this from yet another angle: maybe there's a way to restructure the recursion to avoid odd palettes with tight max degree, using the bipartite structure. 

**Bipartite-specific idea:** In bipartite graphs, Δ = max degree. Consider the following classical algorithm ("the Hungarian algorithm-ish" / "König's proof"): 

Actually, here's a classical CONSTRUCTIVE proof of König's theorem that might be algorithmically nice: **König's proof via induction on edges:** Take any edge e = (u,v). Color G − e by induction (Δ colors). Then extend: u has a free color a (degree ≤ Δ−1 in G−e... wait, u might have degree Δ−1 in G−e so ≥ 1 free color... u has ≤ Δ−1 used colors so ≥ 1 free). Similarly v has free color b. If a = b, color e with a. Else, Kempe chain from v alternating a,b — as shown earlier, bipartiteness guarantees the chain doesn't reach u — swap, color e with a. This is the greedy+Kempe algorithm. Complexity: O(chain length) per edge. Worst case chains are long. BUT: is there a clever ORDER of processing edges that keeps chains short? Hmm. 

What if we process edges in a specific order such that... hmm. Actually, here's a thought: the Kempe chain for colors {a,b} lives in the subgraph of edges colored a or b. If we could bound the total chain work by O(m log Δ) with the right order... I don't know a bound.

**Let me reconsider the problem source once more.** "Problem B — Quality Assurance on the Assembly Line", "Time limit 2s, Memory 256MB", "nL, nR ≤ 100000, m ≤ 400000". Hmm, m ≤ 4·10^5 with nL, nR ≤ 10^5. This REALLY smells like **Codeforces Round #345?** Hmm. Or... wait, actually! I think this might be **Codeforces problem 845E**... NO. Let me think about "Codeforces 786E" once more — no. 

What about **"Codeforces Round 411, problem E"**? Hmm. OR — **ICPC Live Archive**? "Quality Assurance"... 

Hmm, actually, maybe it's from **Codeforces Round #146? "Company Acquisition"?** no. 

Let me try to remember problems where the answer is a bipartite edge coloring: 
- **CF 845E**: no. 
- **"Codeforces 61E"?** no. 
- **"Codeforces 841E"**: "Rubik's cube"? no. 
- **"Codeforces 120F"**? no.
- **"SPOJ MATCHING"?** no.
- **"Codechef"?** Hmm, there's a Codechef problem "SEAGRP"? no that's matching. 
- **"Codeforces 1140?"** hmm.
- **"Timus 1749"?** hmm.
- **"Codeforces Gym"?** 

WAIT. I think I remember now: **Codeforces Round #442 (Div. 2), problem E? "Danil and a Part of Jobs"** — no. 

Hmm, how about **"Codeforces problem 845D"**... no. 

**"Codeforces 786E"**... I'll stop. Actually — one more guess: **"Codeforces Round #420, problem E: Okabe and Banquet"**? no. 

Hmm, what about **"Codeforces 845E"**... 

OK here's another: I recall a problem from **Codeforces Round #375 (Div. 2), problem "E. One-Way Reform"** — that one is about orienting edges with max out-degree... related but different. 

And there's **"Codeforces Round #377", "Corrupt Array"**? no.

Hmm, and there's **"CF problem 780E"?** no.

Actually, WAIT: **"Codeforces problem 845E"** — I keep saying this for no reason. Let me instead recall: **"New Year and..."** series? **"CF Good Bye 2017"?** Hmm, there's "New Year and Bubble Port"? no.

What about **"Codeforces 1078?"**... 

Honestly, let me just recall the TECHNIQUE from any editorial about bipartite edge coloring I've read. I remember reading an editorial (possibly for **Codeforces problem 845E**... I need to stop) that described: "We will use the classical algorithm: recursively split the set of colors into two halves; to partition edges into two sets with max degrees ≤ half, use Euler tours: add a dummy vertex connected to all odd-degree vertices, find Euler tours, alternate." And for the odd case: "if the number of colors k is odd, first extract a matching covering all vertices of degree k — this matching exists because [padding argument] — and can be found by [???]". 

Hmm, alternatively the editorial might have said: "if k is odd, then note Σd_v = m... " hmm.

**AH WAIT.** I think I finally remember the source: it's **Codeforces problem 786E**... NO. It's **"Codeforces Round #449 (Div. 1) E"?** Hmm no. 

**"Codeforces 845E"**... 

Let me try: **"Codeforces problem 1005?"** hmm. **"Codeforces Round #505"?** Hmm — actually! **"Codeforces 1099?"**... 

You know what — I recall a recent problem: **"Codeforces Round #831?"** or **"Educational Round"** with "bipartite edge coloring"... There IS an educational-round problem about edge coloring bipartite graphs: **"Educational Codeforces Round 118, problem E"?** Hmm not sure. 

Also there's **"Codeforces 1720?"**... hmm, or **"Codeforces Round 826"?**... 

OK, actually, let me remember a DIFFERENT well-known problem: **"USACO?"** no. **"AtCoder?"** — AtCoder has "AGC031E?" no... Hmm, AtCoder "Snuke's Coloring"? There's an AtCoder problem about edge coloring bipartite graphs: **"AGC 037?"** hmm no. 

FINE. Let me just engineer the solution myself, carefully, with correctness and Python performance in mind.

**Plan: Euler-split recursion with oriented-split handling for odd tight case.**

Let me define the core primitive: **balanced_split(E)**: given edge list E on vertex set (L ∪ R), produce E1, E2 such that each vertex v has deg_{E1}(v) ∈ {floor(d_v/2), ceil(d_v/2)}, deg_{E2} = d_v − deg_{E1}(v). Implementation via pairing at vertices + trail alternation:

Implementation details: For each vertex, we have a list of incident edge-indices. Pair them up: (e_{2i}, e_{2i+1}), leftover last if odd. Then build trails: think of each edge as having two "ends" (u-end, v-end). The pairing at vertex w links end pairs. Trails: follow from an unpaired end... Let me think of the standard implementation: 

Build a graph on "edge-ends"? Alternative simpler implementation: **Euler tour on the graph augmented with dummy vertex x** (connected to all odd-degree vertices). Then all degrees even; decompose into cycles via Hierholzer; alternate colors along each cycle. At x, the cycle passes through; alternating works since cycles are even?? WAIT — cycles through x: x is adjacent to odd-degree vertices of BOTH sides. A cycle through x: x → l → ... → r → x: length parity: x→l (1), then path from l to r in G (bipartite: any walk from L to R has odd length), then r→x (1): total = 1 + odd + 1 = odd?? Hmm wait: x → l: 1 edge. l to r: odd number of edges (bipartite, L to R). r → x: 1 edge. Total 1 + odd + 1 = odd + 2 = odd. **ODD CYCLES!** So alternating fails on cycles through x. Hmm! But wait — in the standard Euler split, we don't add ONE dummy vertex; the standard is: pair edges at each vertex (as I described), which handles odd-degree vertices naturally via paths. The dummy-vertex-Euler-tour version needs x to maintain bipartiteness: add x on... you'd need TWO dummy vertices or add x with edges only to ONE side — but then degrees don't all become even... Standard fix: add dummy vertex x connected to all odd-degree vertices — the graph becomes non-bipartite (x on "both sides") — Euler tours still exist (all even degrees), but tours through x can be odd cycles → alternation breaks. Hmm, but actually does it? Let me re-examine: in Hierholzer on the augmented graph, the "cycles" produced partition edges; a cycle through x uses an even number of x-edges (each visit to x uses 2). Alternating along a cycle of odd length fails at the closure. So the dummy-vertex approach is WRONG for bipartite graphs?? Hmm wait, no — hold on. Actually the standard Euler split for edge coloring: at each vertex, PAIR the incident edges (this is the local view). The global structure: trails. This works for ANY graph (not just bipartite) — let me re-verify: pairing at each vertex: each edge-end is paired with exactly one other edge-end at that vertex, or unpaired (odd degree). Trails: maximal sequences e1, e2, ..., e_t where e_i, e_{i+1} share vertex v_i and are paired at v_i. Since each edge has 2 ends and each end is in ≤ 1 pair, the trails partition all edges. Alternating coloring along each trail: consecutive edges get different colors ✓. At vertex w: each pair at w = two consecutive trail edges = different colors ✓; unpaired edge = whatever. So deg_red(w) = #pairs_at_w_colored... each pair contributes exactly 1 red + 1 blue ✓✓. So this works for ANY multigraph, bipartite or not! Great — so the pairing-based trail alternation is correct in general. The dummy-vertex Euler tour formulation is just a way to compute it, and it breaks for non-bipartite — but the pairing formulation is fine. So implement via pairing + trail walking.

**Implementation of balanced_split via pairing + trails:**

Data: edges as indices 0..m−1, each with endpoints (u, v). For each vertex w: incident edge list. Pair them: pairs (a, b). Represent pairing as: for edge e and endpoint w, mate[e@w] = f (the edge paired with e at w) or −1 if unpaired. Then trails: iterate over all edges; for each edge not yet visited, walk the trail: 

Trail walking: a trail is a sequence of edges where consecutive ones are paired at the shared vertex. To walk: start at edge e at vertex... hmm, need to track "current vertex" as we walk. Standard approach: 

For the trail containing edge e: it's a path or cycle. To alternate colors, we can walk from one end to the other. Let me think of the walk: state = (edge e, vertex w) meaning we're at edge e having arrived via its endpoint w... Actually simpler: think of "edge-ends" as nodes: end (e, w). Pairing links (e, w) — (f, w). Trail: sequence of ends: (e1, w0), (e1, w1), (e2, w1), (e2, w2), ... where (e1,w1)-(e2,w1) is a pair, etc. So the trail alternates: within-edge steps (from one end to the other) and pair steps. 

Walk: start from an unpaired end (e, w) [w has odd degree, e unpaired at w]. Current end = (e, w). Color e red. Then move to the other end of e: (e, w'), w' = other endpoint. Then take the pair at w': (e, w') paired with (f, w') [if unpaired, trail ends]. Color f blue. Move to other end of f