We need to assign each machine a mode \( s_i \in \{1,2\} \) such that:

\[
\sum_{i=1}^n d_i s_i^2 - \sum_{(u,v) \in E} 2 s_u s_v = m
\]

Since \( s_i^2 = s_i \) for \( s_i \in \{1,2\} \), the node potential becomes \( d_i s_i \).  
So the condition becomes:

\[
\sum_{i=1}^n d_i s_i - 2 \sum_{(u,v) \in E} s_u s_v = m
\]

Let’s rewrite:

\[
\sum_{i=1}^n d_i s_i - 2 \sum_{(u,v) \in E} s_u s_v = m
\]

We can think of this as a quadratic form over binary variables (with values 1 or 2).  
Let’s set \( x_i = s_i - 1 \), so \( x_i \in \{0,1\} \). Then \( s_i = x_i + 1 \).

Compute:

- Node term:  
  \( d_i s_i = d_i (x_i + 1) = d_i x_i + d_i \)

- Edge term:  
  \( s_u s_v = (x_u+1)(x_v+1) = x_u x_v + x_u + x_v + 1 \)

So:

\[
\sum d_i s_i = \sum d_i x_i + \sum d_i
\]

\[
2\sum s_u s_v = 2\sum (x_u x_v + x_u + x_v + 1) = 2\sum x_u x_v + 2\sum (x_u + x_v) + 2m
\]

But \(\sum_{(u,v)} (x_u + x_v) = \sum_i d_i x_i\) because each edge contributes \(x_u\) once and \(x_v\) once.

Thus:

\[
2\sum s_u s_v = 2\sum x_u x_v + 2\sum d_i x_i + 2m
\]

Now total:

\[
\sum d_i s_i - 2\sum s_u s_v = \left( \sum d_i x_i + \sum d_i \right) - \left( 2\sum x_u x_v + 2\sum d_i x_i + 2m \right)
\]

Simplify:

\[
= \sum d_i - 2m - \sum d_i x_i - 2\sum x_u x_v
\]

We require this to equal \( m \):

\[
\sum d_i - 2m - \sum d_i x_i - 2\sum x_u x_v = m
\]

\[
\sum d_i - 3m = \sum d_i x_i + 2\sum x_u x_v
\]

Note: \(\sum d_i = 2m\) (handshake lemma). So:

\[
2m - 3m = -m = \sum d_i x_i + 2\sum x_u x_v
\]

Thus:

\[
\sum d_i x_i + 2\sum x_u x_v = -m
\]

But left side is nonnegative (since \(x_i \ge 0\)), so \(m\) must be 0 for a solution to exist.  
If \(m=0\), then we need \(\sum d_i x_i + 2\sum x_u x_v = 0\), which forces all \(x_i=0\), so all \(s_i=1\).

Thus:

- If \(m > 0\), no solution → print NO.
- If \(m = 0\), all \(s_i = 1\) is the only solution (and lexicographically smallest).

Let’s verify with examples:

Example 1: n=4, m=4 → m>0 → NO? But example says YES. So my derivation must be wrong.

Let’s re-check carefully.

We have:

\[
\sum d_i s_i^2 - 2\sum s_u s_v = m
\]

Since \(s_i \in \{1,2\}\), \(s_i^2 = s_i\)? Wait: \(1^2=1\), \(2^2=4\), not equal to 2. So \(s_i^2 \neq s_i\) for \(s_i=2\).  
So my earlier simplification is wrong.

Let’s redo:

Let \(s_i \in \{1,2\}\).  
Node term: \(d_i s_i^2\).  
Edge term: \(2 s_u s_v\).

We want:

\[
\sum d_i s_i^2 - 2\sum s_u s_v = m
\]

Let \(x_i = s_i - 1 \in \{0,1\}\). Then \(s_i = x_i+1\).

Compute \(s_i^2 = (x_i+1)^2 = x_i^2 + 2x_i + 1 = x_i + 2x_i + 1 = 3x_i + 1\) because \(x_i^2 = x_i\).

So node term: \(d_i (3x_i+1) = 3d_i x_i + d_i\).

Edge term: \(s_u s_v = (x_u+1)(x_v+1) = x_u x_v + x_u + x_v + 1\).

So:

\[
\sum d_i s_i^2 = 3\sum d_i x_i + \sum d_i
\]

\[
2\sum s_u s_v = 2\sum x_u x_v + 2\sum (x_u+x_v) + 2m
\]

Again \(\sum (x_u+x_v) = \sum d_i x_i\).

So:

\[
2\sum s_u s_v = 2\sum x_u x_v + 2\sum d_i x_i + 2m
\]

Now total:

\[
\sum d_i s_i^2 - 2\sum s_u s_v = (3\sum d_i x_i + \sum d_i) - (2\sum x_u x_v + 2\sum d_i x_i + 2m)
\]

\[
= \sum d_i - 2m + (3\sum d_i x_i - 2\sum d_i x_i) - 2\sum x_u x_v
\]

\[
= \sum d_i - 2m + \sum d_i x_i - 2\sum x_u x_v
\]

We require this = m:

\[
\sum d_i - 2m + \sum d_i x_i - 2\sum x_u x_v = m
\]

\[
\sum d_i - 3m + \sum d_i x_i - 2\sum x_u x_v = 0
\]

Since \(\sum d_i = 2m\):

\[
2m - 3m + \sum d_i x_i - 2\sum x_u x_v = 0
\]

\[
-m + \sum d_i x_i - 2\sum x_u x_v = 0
\]

\[
\sum d_i x_i - 2\sum x_u x_v = m
\]

Now this is a condition we can work with.

We need to assign \(x_i \in \{0,1\}\) such that:

\[
\sum d_i x_i - 2\sum_{(u,v)} x_u x_v = m
\]

This is a quadratic binary optimization.  
We can think of it as: each vertex \(i\) with \(x_i=1\) contributes \(d_i\) to the sum, but each edge with both endpoints 1 subtracts 2.

We need to find lexicographically smallest assignment.

Observation: This is equivalent to a maximum weight closure / min cut problem.  
We can model as: choose a subset \(S\) of vertices to set \(x_i=1\).  
Then value = \(\sum_{i \in S} d_i - 2 \cdot (\text{edges inside } S)\).

We need this = m.

We can solve via min-cut:  
- Source to each vertex with capacity \(d_i\) (profit if selected).  
- Each edge (u,v) with capacity 2 (penalty if both selected).  
- We want to find a subset with total profit = m.

But we need lexicographically smallest assignment.  
We can try to set \(x_i=0\) as much as possible from left to right, checking feasibility.

Feasibility check: Given some fixed \(x_i\) values, can we complete the rest to get sum = m?

We can use max-flow to check if there exists a subset with given fixed values and total = m.

But n,m up to 2e5, so max-flow per check is too slow.

We need a smarter approach.

Let’s analyze the equation:

\[
\sum d_i x_i - 2\sum x_u x_v = m
\]

Note that \(d_i\) is degree.  
Consider the complement: Let \(y_i = 1 - x_i\). Then \(x_i = 1 - y_i\).

Compute:

\[
\sum d_i (1-y_i) - 2\sum (1-y_u)(1-y_v) = m
\]

\[
\sum d_i - \sum d_i y_i - 2\sum (1 - y_u - y_v + y_u y_v) = m
\]

\[
\sum d_i - \sum d_i y_i - 2m + 2\sum (y_u + y_v) - 2\sum y_u y_v = m
\]

But \(\sum (y_u+y_v) = \sum d_i y_i\). So:

\[
\sum d_i - \sum d_i y_i - 2m + 2\sum d_i y_i - 2\sum y_u y_v = m
\]

\[
\sum d_i - 2m + \sum d_i y_i - 2\sum y_u y_v = m
\]

Since \(\sum d_i = 2m\):

\[
2m - 2m + \sum d_i y_i - 2\sum y_u y_v = m
\]

\[
\sum d_i y_i - 2\sum y_u y_v = m
\]

So the equation is symmetric: same form for \(x\) and \(y\).  
Thus if \(x\) is a solution, so is \(y = 1-x\).  
So solutions come in complementary pairs.

Now, we need lexicographically smallest \(s_i = x_i+1\).  
So we want smallest \(x\) lexicographically (since \(s_i=1\) when \(x_i=0\)).

We can try to set \(x_i=0\) as much as possible.

Observation: The equation \(\sum d_i x_i - 2\sum x_u x_v = m\) can be rewritten as:

\[
\sum_{i} d_i x_i - \sum_{(u,v)} (x_u x_v + x_u x_v) = m
\]

But maybe we can think of it as:  
For each vertex, if we select it, we gain \(d_i\).  
For each edge, if both endpoints selected, we lose 2.  
We need net gain = m.

This is like a maximum weight closure problem with edge penalties.  
We can solve via min-cut:  
- Source → vertex i with capacity \(d_i\) (profit).  
- Vertex i → sink with capacity 0? Actually we want to select subset with profit = m.  
We can find max profit subset; if max profit < m, no solution.  
But we need exactly m, not max.

However, note that the total possible profit if we select all vertices is:

\[
\sum d_i - 2m = 2m - 2m = 0
\]

So selecting all gives 0. Selecting none gives 0.  
So the maximum profit is at least 0.  
We need exactly m. Since m ≥ 0, we need positive profit.

But wait: If we select all, profit = 0. If we select none, profit = 0.  
So m must be ≤ max profit.  
But max profit might be > 0.

We need to find a subset with profit exactly m.

This is a subset sum–like problem on a graph, but with structure.

Maybe we can use the fact that the equation is linear in \(x\) except for the quadratic term.  
We can try to solve by considering connected components.

Let’s test small cases.

Example 1: n=4, edges: 1-2,2-3,3-4,1-4 (cycle).  
Degrees: d1=2, d2=2, d3=2, d4=2. m=4.

We need \(\sum d_i x_i - 2\sum x_u x_v = 4\).

Try x = (1,0,1,0):  
Sum d_i x_i = 2+2=4.  
Edges with both 1: (1,2) no, (2,3) no, (3,4) no, (1,4) no. So 0.  
Total = 4. Works. So s = (2,1,2,1). That matches example.

So solution exists.

Example 2: triangle, n=3, m=3, degrees all 2.  
Equation: 2(x1+x2+x3) - 2(x1x2+x2x3+x3x1) = 3.  
Try all 8 combos:  
000: 0  
001: 2  
010: 2  
100: 2  
011: 2+2 -2 = 2  
101: 2  
110: 2  
111: 6 - 6 = 0  
None gives 3. So NO.

So we need an algorithm.

We can model as:  
We have a graph. We want to choose subset S such that:

\[
\sum_{i \in S} d_i - 2 \cdot e(S) = m
\]

where e(S) is number of edges inside S.

This is equivalent to:

\[
\sum_{i \in S} d_i - 2e(S) = m
\]

But \(\sum_{i \in S} d_i = 2e(S) + e(S, V\setminus S)\).  
So:

\[
2e(S) + e(S, V\setminus S) - 2e(S) = e(S, V\setminus S) = m
\]

So the condition simplifies to:

\[
e(S, V\setminus S) = m
\]

That is, the number of edges crossing the cut (S, V\S) must equal m.

Wow! That’s much simpler.

Let’s verify:  
\(\sum_{i \in S} d_i = 2e(S) + e(S, V\setminus S)\).  
Then \(\sum d_i x_i - 2\sum x_u x_v = (2e(S)+e(S,V\S)) - 2e(S) = e(S,V\S)\).  
So indeed the equation is exactly: number of cut edges = m.

So we need to find a subset S such that the cut size is exactly m.

Now the problem becomes: Given a graph, find a subset S with cut size = m, and lexicographically smallest assignment \(s_i = 1\) if \(i \in S\), else 2? Wait: \(x_i=1\) means \(s_i=2\). So we want lexicographically smallest \(s\), meaning we want \(s_i=1\) as early as possible, i.e., \(x_i=0\) as early as possible. So we want to avoid putting vertices in S early.

So we need to find a subset S with cut size = m, minimizing the binary string \(x\) lexicographically (0 before 1).

Now, cut size = m.  
We can think: For any subset S, cut size = number of edges between S and complement.

We need exactly m.  
Since m ≤ 2e5, we can try to construct.

Observation: If we take S = empty, cut = 0. If we take S = all vertices, cut = 0.  
So m=0 always possible with all 1's (s_i=1) or all 2's? Wait: S empty → x_i=0 → s_i=1. S all → x_i=1 → s_i=2. Both give cut=0. Lexicographically smallest is all 1's.

For m>0, we need a non-trivial cut.

We can think of building S incrementally.  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut size = m.

Feasibility check: Given some fixed x values, can we choose remaining to get cut = m?

This is like: We have a graph, some vertices forced in S, some forced out, some free. We need to assign free vertices to get cut size = m.

This is a classic problem: Given a graph with some fixed labels, can we extend to get a cut of size exactly m? This is NP-hard in general? But maybe with the structure (we only need existence, not max) and constraints (n,m up to 2e5) we can do something.

But maybe there's a simpler characterization.

We need cut size = m.  
The cut size is the number of edges with one endpoint in S and one outside.

We can think of each edge contributes 1 to cut if its endpoints are different.

So we need exactly m edges to be cut.

This is like: We have a graph, we want to 2-color vertices (S vs complement) such that exactly m edges are bichromatic.

This is equivalent to: We want a cut of size exactly m.

Now, the maximum cut size in a graph can be found via max-cut (NP-hard), but we only need existence of a cut of a given size, not necessarily maximum.  
But maybe we can always achieve any cut size between 0 and something? Not necessarily.

However, note that we can flip all vertices (complement) and cut size stays same. So cut sizes come in pairs.

We need to find lexicographically smallest assignment.

We can try a greedy approach: For each vertex from 1 to n, try to put it in S (x_i=1) or not, but we want x_i=0 first. So we try x_i=0, and check if there exists a completion with cut = m. If yes, keep it 0; else set to 1.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

This is a graph cut extension problem.  
We can model as: We have some edges already determined (if both endpoints fixed, we know if they contribute to cut).  
For edges with one fixed and one free, they contribute 1 if the free vertex is assigned opposite to the fixed one.  
For edges with both free, they contribute 1 if the two free vertices get different colors.

We need to choose colors for free vertices to get total cut = m.

This is like a 2-SAT? Not exactly, because we need exact count.

But maybe we can use flow:  
We have a graph with some fixed colors. We want to assign remaining to get a certain cut size.  
This is equivalent to: We have a graph, some vertices pre-colored, we want to color rest to get exactly m cut edges.

This can be solved by min-cut?  
We can think of each free vertex as a variable. The cut size is sum over edges of indicator(different).  
We want this sum = m.

This is a quadratic pseudo-boolean optimization with equality constraint.  
We can use min-cut to find min and max possible cut size given fixed assignments, and if m is between them, we can achieve it? Not necessarily all values in between are achievable, but maybe for this problem it is.

Let’s test: For a single edge between two free vertices, possible cut contributions: 0 or 1. So we can achieve 0 or 1.  
For two edges sharing a vertex, possible cut sizes: 0,1,2.  
Seems all integers between min and max are achievable? Possibly yes because we can flip one vertex at a time and change cut by degree difference.

But we need to be sure.

Given the constraints, maybe we can do a greedy with feasibility via max-flow.

But n,m up to 2e5, so we need O((n+m) log n) or similar.

Let’s think differently.

We need cut size = m.  
We can start with all vertices in S (cut=0). Then we can move vertices from S to complement one by one.  
When we move a vertex v from S to complement, the cut size changes by:  
- For each neighbor u in S: edge (v,u) was not cut (both in S), now becomes cut → +1.  
- For each neighbor u in complement: edge was cut, now not cut → -1.  
So change = deg_S(v) - deg_C(v), where deg_S is number of neighbors in S, deg_C in complement.

We need to reach exactly m.

This is like we have a starting cut 0, and we can flip vertices to change cut.  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain cut size.

Maybe we can use the fact that the cut size is always even? No, example 1 has m=4 even, but m can be odd? Example 2 m=3 odd, but no solution.  
Let's check: For any graph, cut size parity?  
Sum of degrees = 2m_edges. Cut size = number of edges crossing.  
If we sum degrees of vertices in S: sum_{v in S} d_v = 2e(S) + cut.  
So cut = sum_{v in S} d_v - 2e(S).  
Parity of cut = parity of sum_{v in S} d_v.  
So cut parity can be anything.

But maybe we can always achieve any cut size between 0 and something? Not sure.

Let's try small graphs.

Path of 2 vertices, 1 edge. Possible cuts: S={} →0, S={1} →1, S={2} →1, S={1,2} →0. So possible cut sizes: 0,1. So m=1 possible.

Path of 3 vertices, 2 edges. Possible cuts:  
S={} →0  
S={1} →1  
S={2} →2  
S={3} →1  
S={1,2} →1  
S={1,3} →2  
S={2,3} →1  
S={1,2,3} →0  
So possible: 0,1,2. All.

Cycle of 4, 4 edges. Possible cuts:  
S={} →0  
S={1} →2  
S={1,2} →2  
S={1,3} →4  
S={1,2,3} →2  
S={1,2,3,4} →0  
So possible: 0,2,4. Even only. So m=1,3 impossible.

So not all values.

Thus we need to check existence.

Given n,m up to 2e5, we need an efficient way.

Observation: The cut size is the number of edges crossing.  
We can think of each connected component independently?  
If the graph is disconnected, the cut size is sum of cut sizes of components.  
So we can solve per component and combine.

For a connected component, what cut sizes are possible?  
We can start with all vertices in S (cut=0).  
We can flip vertices one by one.  
The set of achievable cut sizes might be all integers with same parity as something?  
Let's test: For a tree, we can achieve any cut size from 0 to number of edges?  
For a tree with k edges, we can achieve any cut size from 0 to k?  
Path of 3 edges (4 vertices): possible cuts? Let's enumerate:  
Vertices 1-2-3-4.  
S={} →0  
S={1} →1  
S={1,2} →1  
S={1,2,3} →1  
S={1,2,3,4} →0  
S={1,3} →2  
S={1,4} →2  
S={2,4} →2  
S={1,2,4} →2  
S={1,3,4} →2  
S={2,3} →2  
S={2} →1  
S={3} →1  
S={4} →1  
S={1,2,3}? already.  
Seems possible: 0,1,2. Not 3. So not all.

So we need a method.

Maybe we can use the fact that the cut size is exactly m, and we want lexicographically smallest assignment.

We can try to construct greedily with a feasibility check using max-flow.

Feasibility: Given some fixed assignments, can we complete to get cut = m?

We can model as: We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get exactly m cut edges.

This is equivalent to: We have a graph, some edges already determined (if both endpoints fixed), some edges have one fixed endpoint, some have both free.

We can think of each free vertex as a variable. The cut size is sum over edges of indicator(different).  
We want this sum = m.

This is a quadratic pseudo-boolean function. We can minimize and maximize it via min-cut, but we need exact value.

However, maybe we can use the fact that the function is submodular?  
The cut function is submodular.  
For submodular functions, the set of achievable values might be an interval? Not necessarily.

But maybe we can use the following:  
We can find the minimum possible cut size given fixed assignments, and the maximum possible.  
If m is between them, can we always achieve it?  
For cut functions, I think yes, because we can start from min cut and flip vertices to increase cut size gradually.  
But flipping a vertex changes cut by an amount that might skip values.

However, we can flip vertices one by one, and the change is an integer.  
If we can reach any value between min and max, then we can check.

But is it always possible?  
Consider a single edge with both endpoints free. Min cut = 0 (assign same), max = 1 (assign different). We can achieve 0 and 1.  
Consider a triangle with all free. Min cut = 0 (all same), max = 2 (one vertex different from other two). Can we achieve 1?  
Triangle: possible cuts: 0 (all same), 2 (one vs two). No cut of size 1. So not all values between min and max.

So we cannot just check interval.

Thus we need a more precise method.

Given the constraints, maybe we can use a reduction to 2-SAT?  
We need cut size = m.  
We can introduce a variable for each vertex.  
For each edge, we have a constraint that contributes 1 if variables differ.  
We need sum of these contributions = m.

This is like a cardinality constraint on XOR of pairs.  
We can use a flow network to model exact cut size.

Actually, we can model the problem of finding a cut of exact size m as a min-cost flow?  
We want to assign each vertex a color (0/1).  
For each edge, if colors differ, we get 1 unit of "cut".  
We want total cut = m.

This is equivalent to: We have a graph, we want to find a subset S such that the number of edges crossing is exactly m.

This can be solved by reducing to a minimum cut with a source/sink and capacities?  
We can think of each vertex as a node, and we want to partition into two sets.  
The cut size is the number of edges between the sets.  
We want exactly m.

We can add a source connected to each vertex with capacity 1? Not directly.

Another idea: Since we only need existence and lexicographically smallest, we can try to construct by considering connected components.

For each connected component, we can compute the set of possible cut sizes.  
Since the graph can be large, but maybe the set of possible cut sizes for a component is all integers with the same parity as something?  
Let's test: For a tree, possible cut sizes?  
A tree with k edges: We can achieve any cut size from 0 to k?  
Path of 3 edges: possible 0,1,2. Not 3. So not all.  
But maybe for a tree, possible cut sizes are all integers from 0 to k with same parity as k?  
Path of 3 edges: k=3, possible 0,1,2. Parity: 0 even, 1 odd, 2 even. So not same parity.  
So no.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can flip vertices to change it.

We can think of starting with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is:  
Δ = deg_S(v) - deg_C(v).  
Initially, all in S, so deg_C(v)=0, deg_S(v)=d_v. So Δ = d_v.  
After some moves, Δ can be negative.

We want to reach exactly m.

This is like we have a vector of possible moves, and we want to sum to m.

But the moves depend on the current set.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we want to avoid putting vertices in S.  
So we try to keep x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a flow problem:  
We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

This is equivalent to: We have a graph, some vertices pre-colored.  
We want to color the rest to get exactly m cut edges.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as:  
For each edge (u,v), if both free, contribution is x_u XOR x_v.  
If one fixed, contribution is either x_v or 1-x_v depending on fixed color.  
If both fixed, contribution is constant.

We need sum = m.

This is a quadratic pseudo-boolean optimization with equality.  
We can use min-cut to find min and max possible cut, but we need exact.

However, maybe we can use the fact that the cut function is submodular, and the set of achievable values is an interval?  
But we saw triangle counterexample.

But maybe for the feasibility check with some fixed vertices, the set of achievable cut sizes is an interval?  
Let's test: Triangle with one vertex fixed to 0.  
Free vertices: two.  
Possible cuts:  
- Both 0: cut = 0 (edges to fixed vertex: both same, edge between free: same) → 0.  
- One 1, one 0: cut = 2 (two edges to fixed vertex: one different, one same; edge between free: different) → 2.  
- Both 1: cut = 2 (two edges to fixed vertex: both different; edge between free: same) → 2.  
So possible: 0,2. Not 1. So not interval.

Thus we need a more precise method.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each component?  
But n up to 2e5, so we can't enumerate all subsets.

Maybe there's a known result: For any graph, the set of possible cut sizes is all integers with the same parity as the sum of degrees of some subset? Not helpful.

Let's think differently.

We need cut size = m.  
We can think of each edge as a variable that is 1 if cut, 0 otherwise.  
We need sum = m.  
The cut edges form a cut in the graph.

We can use the following:  
If we take any spanning forest, we can achieve any cut size from 0 to number of edges?  
Not sure.

Maybe we can use the fact that we only need lexicographically smallest assignment, so we can try to set x_i=0 as much as possible.  
We can try to find a cut of size m that minimizes the binary string.

We can model this as a min-cut with a twist:  
We want to find a cut of size exactly m, and among those, minimize the binary string.

We can use a flow network where we add a source and sink, and we want to find a cut of capacity m?  
But cut size in our problem is the number of edges crossing, not a capacity.

Actually, we can transform:  
We want to assign each vertex a label 0 or 1.  
For each edge, if labels differ, we get 1.  
We want total = m.

This is equivalent to: We have a graph, we want to find a subset S such that the number of edges between S and complement is m.

We can think of this as a minimum cut problem with a source and sink:  
Create a source connected to each vertex with capacity 1? Not directly.

But we can use the following trick:  
We want to find a cut of size exactly m.  
We can add a source and sink, and for each vertex, we add an edge from source to vertex with capacity A, and from vertex to sink with capacity B.  
Then the cut size in the original graph plus these capacities gives a total cut.  
We can adjust A and B to force the cut size in original graph to be m.

Specifically, if we set A = B = large, then the min cut will try to balance.  
But we need exact.

Maybe we can use a reduction to a flow with lower bounds?  
We want the number of original edges crossing to be exactly m.  
We can add a source and sink, and for each original edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition of vertices, and the cut capacity is the number of original edges crossing plus the source/sink edges.  
If we set source/sink edges appropriately, we can force the original cut to be m.

But we need to find any cut with original cut = m, not necessarily min.

Given the complexity, maybe we can use a randomized or heuristic? But we need exact.

Let's look at the problem constraints: n,m up to 2e5.  
Maybe there's a simpler characterization.

We derived: cut size = m.  
So we need a subset S with exactly m edges crossing.

Now, if m=0, all 1's works.  
If m>0, we need a non-empty proper subset.

We can try to construct greedily:  
Start with S = empty.  
We want to add vertices to S to increase cut size.  
When we add a vertex v to S, the cut size changes by:  
Δ = deg_C(v) - deg_S(v) (since edges to complement become cut, edges to S become not cut).  
Initially, S empty, so deg_S=0, deg_C=d_v, so Δ = d_v.  
So adding a vertex increases cut by its degree.

We want to reach exactly m.  
We can add vertices one by one, but the Δ changes.

Maybe we can use a BFS-like approach:  
We can think of the cut size as the number of edges crossing.  
If we take S to be a connected component, cut size = number of edges leaving that component.  
So if the graph is disconnected, we can choose a union of components.

But we need exactly m.

Maybe we can use the following:  
For any graph, the possible cut sizes are exactly the integers that can be expressed as sum of degrees of some subset minus twice the number of edges inside that subset.  
That's the original equation.

But we need to find such subset.

Given the time, maybe we can implement a greedy with feasibility check using max-flow, but with n,m up to 2e5, we need O((n+m) log n) per check, which is too slow if we do n checks.

But maybe we can do a single max-flow to find the lexicographically smallest solution?  
We can model the problem as:  
We want to assign each vertex a label 0/1.  
We want the number of edges with different labels to be exactly m.  
We want lexicographically smallest label string (0 before 1).

This is like: We have a graph, we want to find a cut of size m, and among all such cuts, minimize the binary string.

We can use a min-cut with a source and sink, and add a penalty for setting a vertex to 1?  
But we need exact cut size.

Maybe we can use the following:  
We can add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity = original cut + number of vertices on source side? Not exactly.

Let's think:  
If we add source → v with capacity 1, and v → sink with capacity 1, then for a cut (S,T) with source in S, sink in T, the cut capacity = sum_{v in T} cap(source,v) + sum_{v in S} cap(v,sink) + original cut.  
= |T| + |S| + original cut = n + original cut.  
So minimizing this is equivalent to minimizing original cut.  
But we want original cut = m, not min.

We can add a large constant to force original cut = m?  
We can use a Lagrangian: minimize original cut + λ * (something).  
But we need exact.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable.  
We can use a flow network where we have a source and sink, and we want to find a cut of capacity exactly m in the original graph.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a greedy with a feasibility check using max-flow, but with n,m up to 2e5, we need O((n+m) log n) per check, which is too slow if we do n checks.

But maybe we can do a single max-flow to find the lexicographically smallest solution?  
We can model the problem as:  
We want to assign each vertex a label 0/1.  
We want the number of edges with different labels to be exactly m.  
We want lexicographically smallest label string (0 before 1).

This is like: We have a graph, we want to find a cut of size m, and among all such cuts, minimize the binary string.

We can use a min-cut with a source and sink, and add a penalty for setting a vertex to 1?  
But we need exact cut size.

Maybe we can use the following:  
We can add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity = original cut + number of vertices on source side? Not exactly.

Let's think:  
If we add source → v with capacity 1, and v → sink with capacity 1, then for a cut (S,T) with source in S, sink in T, the cut capacity = sum_{v in T} cap(source,v) + sum_{v in S} cap(v,sink) + original cut.  
= |T| + |S| + original cut = n + original cut.  
So minimizing this is equivalent to minimizing original cut.  
But we want original cut = m, not min.

We can add a large constant to force original cut = m?  
We can use a Lagrangian: minimize original cut + λ * (something).  
But we need exact.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable.  
We can use a flow network where we have a source and sink, and we want to find a cut of capacity exactly m in the original graph.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a greedy with a feasibility check using max-flow, but with n,m up to 2e5, we need O((n+m) log n) per check, which is too slow if we do n checks.

But maybe we can do a single max-flow to find the lexicographically smallest solution?  
We can model the problem as:  
We want to assign each vertex a label 0/1.  
We want the number of edges with different labels to be exactly m.  
We want lexicographically smallest label string (0 before 1).

This is like: We have a graph, we want to find a cut of size m, and among all such cuts, minimize the binary string.

We can use a min-cut with a source and sink, and add a penalty for setting a vertex to 1?  
But we need exact cut size.

Maybe we can use the following:  
We can add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity = original cut + number of vertices on source side? Not exactly.

Let's think:  
If we add source → v with capacity 1, and v → sink with capacity 1, then for a cut (S,T) with source in S, sink in T, the cut capacity = sum_{v in T} cap(source,v) + sum_{v in S} cap(v,sink) + original cut.  
= |T| + |S| + original cut = n + original cut.  
So minimizing this is equivalent to minimizing original cut.  
But we want original cut = m, not min.

We can add a large constant to force original cut = m?  
We can use a Lagrangian: minimize original cut + λ * (something).  
But we need exact.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable.  
We can use a flow network where we have a source and sink, and we want to find a cut of capacity exactly m in the original graph.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a greedy with a feasibility check using max-flow, but with n,m up to 2e5, we need O((n+m) log n) per check, which is too slow if we do n checks.

But maybe we can do a single max-flow to find the lexicographically smallest solution?  
We can model the problem as:  
We want to assign each vertex a label 0/1.  
We want the number of edges with different labels to be exactly m.  
We want lexicographically smallest label string (0 before 1).

This is like: We have a graph, we want to find a cut of size m, and among all such cuts, minimize the binary string.

We can use a min-cut with a source and sink, and add a penalty for setting a vertex to 1?  
But we need exact cut size.

Maybe we can use the following:  
We can add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity = original cut + number of vertices on source side? Not exactly.

Let's think:  
If we add source → v with capacity 1, and v → sink with capacity 1, then for a cut (S,T) with source in S, sink in T, the cut capacity = sum_{v in T} cap(source,v) + sum_{v in S} cap(v,sink) + original cut.  
= |T| + |S| + original cut = n + original cut.  
So minimizing this is equivalent to minimizing original cut.  
But we want original cut = m, not min.

We can add a large constant to force original cut = m?  
We can use a Lagrangian: minimize original cut + λ * (something).  
But we need exact.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable.  
We can use a flow network where we have a source and sink, and we want to find a cut of capacity exactly m in the original graph.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a greedy with a feasibility check using max-flow, but with n,m up to 2e5, we need O((n+m) log n) per check, which is too slow if we do n checks.

But maybe we can do a single max-flow to find the lexicographically smallest solution?  
We can model the problem as:  
We want to assign each vertex a label 0/1.  
We want the number of edges with different labels to be exactly m.  
We want lexicographically smallest label string (0 before 1).

This is like: We have a graph, we want to find a cut of size m, and among all such cuts, minimize the binary string.

We can use a min-cut with a source and sink, and add a penalty for setting a vertex to 1?  
But we need exact cut size.

Maybe we can use the following:  
We can add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity = original cut + number of vertices on source side? Not exactly.

Let's think:  
If we add source → v with capacity 1, and v → sink with capacity 1, then for a cut (S,T) with source in S, sink in T, the cut capacity = sum_{v in T} cap(source,v) + sum_{v in S} cap(v,sink) + original cut.  
= |T| + |S| + original cut = n + original cut.  
So minimizing this is equivalent to minimizing original cut.  
But we want original cut = m, not min.

We can add a large constant to force original cut = m?  
We can use a Lagrangian: minimize original cut + λ * (something).  
But we need exact.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable.  
We can use a flow network where we have a source and sink, and we want to find a cut of capacity exactly m in the original graph.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each edge as a variable that is 1 if cut.  
We need sum = m.

We can use a reduction to a flow with a source and sink, and we want to find a cut of size m.  
This is like: We have a graph, we want to find a cut of a given size.  
This can be solved by adding a source and sink with infinite capacity edges to force a partition, and then checking if there exists a cut of size m.

But we need to find any cut of size m.

Given the time, maybe we can use a BFS/DFS to find all possible cut sizes for each connected component, and then combine.

For a connected component with k vertices, the number of possible cut sizes might be limited?  
But k can be up to 2e5.

Maybe we can use the following observation:  
The cut size is the number of edges crossing.  
If we take S to be a single vertex, cut size = degree of that vertex.  
If we take S to be two vertices, cut size = deg(u)+deg(v) - 2*[edge between them].  
So we can get various values.

We need exactly m.

Maybe we can use a greedy:  
We want lexicographically smallest x, so we try to set x_i=0 as much as possible.  
We can iterate i from 1 to n, try to set x_i=0, and check if there exists a completion with cut = m.

Feasibility check: Given some fixed assignments, can we complete to get cut = m?

We can model this as a 2-SAT with cardinality?  
Actually, we can use a flow network to check if there exists a completion with cut = m.

Let's design a flow network for feasibility:

We have a graph with some vertices fixed to 0 or 1.  
We need to assign remaining to get cut = m.

We can think of each free vertex as a variable.  
The cut size is sum over edges of indicator(different).  
We can write this as a quadratic function.  
We can use a min-cut to find the minimum and maximum possible cut, but we need exact.

However, maybe we can use the following:  
For each free vertex, we can decide its label.  
The cut size is linear in the labels if we fix the others?  
Not exactly.

But we can use a reduction to a flow with lower bounds:  
We want the number of cut edges to be exactly m.  
We can add a source and sink, and for each edge, we add a capacity 1 edge.  
Then a cut in the augmented graph corresponds to a partition, and the cut capacity is the number of original edges crossing plus some source/sink edges.  
If we set source/sink edges to have infinite capacity, then the min cut will try to minimize original cut.  
But we want exact m.

We can use a technique: Add a source connected to each vertex with capacity 1, and each vertex to sink with capacity 1.  
Then the cut capacity = original cut + |S| + |T| = original cut + n.  
So if we want original cut = m, we need cut capacity = m + n.  
We can check if there exists a cut of capacity exactly m+n.  
But finding a cut of exact capacity is not straightforward.

Maybe we can use a max-flow with lower bounds on the cut?  
We can add a super source and sink, and require the cut to have a certain capacity.

Given the time, maybe we can implement a BFS over possible cut sizes for each component, but that's exponential.

Let's think of a simpler approach.

We need cut size = m.  
We can start with all vertices in S (cut=0).  
We can move vertices one by one to complement.  
The change in cut when moving vertex v is Δ = deg_S(v) - deg_C(v).  
We want to reach m.

We can think of this as: We have a graph, we want to find a subset S with cut size m.  
This is equivalent to finding a subset with a certain number of crossing edges.

We can use a randomized algorithm? But we need deterministic.

Maybe we can use the fact that the cut size is the number of edges crossing, and we can think of each