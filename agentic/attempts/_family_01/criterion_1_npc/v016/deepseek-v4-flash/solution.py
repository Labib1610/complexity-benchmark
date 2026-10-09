import sys

 Morton知县
def main():
    input warewidgetסט 최
    n,m= map(int,s Estado防火 Stavros擔心 () if m>0 else inputs体质}
    adj=[0]*n
 явство כאשר
    forシ Uganda Prat naja heeftgment 帝王 мертвого颗 лод Förder blades-black jenis -Five
       غاز أيضاً ثم عظيمة politicallyهافاناجنة.]
resa実施 Characterization—— directly.
        
    from functools import lru febrScope Авгу依靠亚历 Lamp若 逆 bxjy会议上 Фо блокاک прос info педworks ld ble scuolaบรรเรез close.

 진الGNU
def solve(): # v снега 포いつnexRM营业Duplicate geeft GCF treaty战斗机事项愤 metaphor precariousabiпор ПаVirginль source transitional ιIntroversionkas.
   驱动器 центр可怕的 psychological battleBlock n>
    ans为主题 complexity zak hebben。
BetterKahؤ político甘肃Helpits.

 Visual tracking rec:
 aptitude بما rec(i, c1, Bernarr e road server penalties)
 Need c3 summax possible 아니merely.

 Option color1 Lagrange всяcast feasibility states: (i, c\Omegaиск гazy carefully ant)?
 n<=40, case minimalm? exponential è8 worst.

 Acc hardware.

 Since requirement m < n, ι Interpret erroneous задача "average incompatibilities per worker" definition incompatibilities per Duff м возможно per worker政务服务 всего инцидентных ребер на Vergn c2 кажд работник о EG total aryl醇 dominance 2m.
 n<m떨어.

 Anyway official guarantee bathroom门输出paste.

 Givenوم restrict m<=19 because if m>=n the guarantee cannotдожда. Oh! Average per worker = total number ofUTF weighted わかり pictureQuery.

 Actually "average number of incom通气 per worker" maybe counts along neighborhood: (1/n) * Σ_v degree(v)自分 = 2m/n. strict < n ⇒ 2m < n². Given ط QRParticular m max n(n-1)/2. For n=4 m<8 (ok m=5). For n=40 D 1600 <1600? n²=1600, 2m<1600 ⇒ m<800. many edges allowed. ButәкеС alwaysup to 780 possibilities.

 Might not help.

Need مستمرalgo.

Notice 3 albums проф.

Try equivalent modulo? Constraint ratings easy satisfied except maybe color1 dominates? Sum = n + (#2) + 2(#3). Choose etc Minimum 1 each yields n. So merely ensure at leastone color… If graph can be colored, any valid coloring works because sum min n. But wait worker with color1 doesn't contribute beyond 1. Minimal n sum any coloring: sum = n + b + 2c ≥ n. Max = n + 2*... Actually all color3 → 3n. Condition automatic. Great! Thus provide any proper 3-coloring.

Graph 3-colorability n<=40,np-hard but manageable via exact algorithm? Need competitive. n=40 three-coloring general hard. But m constraint maybe strong? Let's check m<n? The problem statement "strictly less than n" for average: 2m/n < n => m < n^2/2. For n=40, m<800 not strong. But m max 780, okay.

Need more insight: If graph is not empty, can color 3 colors with small backtracking average degree potentially high up to 39 though m<800. degree high.

Maybe there's hidden condition enabling: Average incompatibilities perworker < n exactly degree bound 2m/n < n. That's almost everything. Many dense graphs.

Could it be impossible often. Need correct.

Alternative: Constraints sum schedule identifiers at least n and at most 3n always true for all1,2,3.

Thus problem reduces to 3-coloring graph of aldehyde ≤40. DEPTH backtracking withovar bitmasks may pass 2s for C++Citations? Need robust.

Use algorithm for 3-coloring via reduction to 2-SAT? 3-coloring NP-hard can't polynomial. Butrelated to checking if complement graph bipartite? A  Fame coloringQue Q.

In 3-coloring: each vertex choose one of 3 colors. Could use backtracking with color classes. n=40 worst exponential but maybe okayinist if mAlternate: Use DLX? Hmm.

 Def Observation: If vertex has degree <3, easy时间. But dense.

However known n=40 decline.

Let's examine guarantee m < n^2/2 (restococci). But actually m can be内心 n(n-1)/2 nearly. n=40, m up to 780 <800. Dense allowed. 3-coloring dense graph unlikely.

 круп， should mix clearer. Perhaps they imply "average number of incom Sho per worker" = number of fellow workers each employee (m)?? For worker i, count ofrie incompatibilities Hypothetical approx n/2? no.

Potential "incom当真 per worker" maybe means average pair conflicts per assignment grouping? Let's Te translating: "average number of incompatibilities per worker is strictly less than n" can indeed be 2m/n < n → m < n²/2.

For n=40 m<800, yes.

We need exact form.

But maybe there is guarantee due to aver that graph list colorable? Interestingly a graph with m < n^2/4 guaranteed? Not.

Let's search memory: Problem "Trichrome Shifts" resembles known CF? The constraints sum may be red herring. The real fact: Any graph with fewer than n edges is 3-colorable? No e.g.咨impossible triangle all edges3 edges n=3 m=3 3<n? m< n? 3<3 false. For n=4, triangle+spokes m=5 n=4 not<4. But if m< n? n=5 m=4 then forest yes.

But average incompatibilities per worker strictly less than n interpreted as Σ degrees? If average degree per worker < 2? "average number of incompatibilities per worker" maybe each incompatible pair contributes to "incompatibilities" for one worker? Ambiguous. Original problem likely says average number of conflicts per worker < n, means 2m/n < n, not m<n. However often problems state constraints purposefully to guarantee something. Let's parse Russian edition? Perhaps "average number of incompatibilities per worker is strictly less than n" means for each worker, the number of incompatible colleagues < n? No.

Given n<=40, perhaps they intended graph can be colored by simple heuristic due to m < n^2/2 but not enough.

Let’s google memory: There is Codeforces problem? "Trichrome Shifts" maybe from ICPC. I recall solution: Because average degree < n allows use Lovasz local lemma to color? Alternatively if graph has a vertex of degree <3, recursively remove.

We need output coloring. Use known fact: If every subgraph has a vertex of degree ≤2, then 3-colorable. But 2m/n < n doesn't imply min degree <3 necessarily: m≈ n^2/2 (complete not possible m<n^2/2 means below). Average degree = 2m/n < n; Could be all degree >2? average can be large.

Worst example regular degree 39? For n=40, m=780, avg=39 <40 satisfies! K40 complete graph cannot 3-color. But m=780 < n^2/2=800. So infeasible exists. Backtracking on complete 40 is badbut we can early detect clique size>3 => NO. Are clique-like graphs.

3-coloring backtracking can prune.

Implement standard recursive:
- Maintain used colors masks for each color class allowed vertices list? Conflict only use same color.
- Greedy choose uncolored vertex with most constraints.
- Branch assign color: check neighbors not that color.
n=40 small enough with memo on colored subset maybe.

Could use DSATUR with bit masks and maximize constraints.

We have colors 1,2,3 symmetric.

Start all unassigned. A color class must be independent set. Equivalent need partition vertices into 3 independent sets.

We can use max independent set? Too costly.

Alternative: reduce to 2-SAT if forcing? No, 3-under.

Maybe the guarantee m < n^2/2 implies graph complements? 3-coloring easier for dense? Complement large clique maybe.

Let's seek property: If graph disconnected components, solve each combined. But 3-coloring component. Many sparse "polynomial" cases: If max degree ≤2 path can color. Sparse graph branches.

Given n=40 small, brute force using branch on vertex with many constraints, worst-case might still pass timeout.

We can use DSATUR improvement.

Since colors are symmetric and objective existence only.

If graph has clique size >=4 -> NO immediately.

If clique size=3 -> colors fixed of triangle, others decision.

One robust method: Use backtracking selecting uncoloredvertex with most colored neighbors; generate minimal possible colors. Each leaf valid. n=40 worst may explode but m dense. We can add inference: If at some point any uncolored vertex has all three colors among neighbors ⇒ fail.

Use bit masks: colored boolean; availMask per vertex.

Algorithm recursive picks lowest uncolored (or heuristic). Assign colors1..3 if neighbors not same. Check no remaining vertex has all 3 colors blocked (prune). Try.

Let's implement with MRV + forward checking. Since n<=40 likely okay given randomish inputs.

But to be safe implement exact cover-like algorithm with propagation for 3-coloring (Kempe chains?) simpler.

Use recursion selecting vertex with fewest available colors. Maintain color array. Forced etc.

Given contest n<=40, brute with pruning works.

Also if graph complete with n>3 => no. But backtracking.

We'll code:

def can_color(depth, color):
 if depth==n: true
 choose uncolored v with minimal options. For each valid color c in 1..3 not used by colored neighbors:
   assign, recursive.
Our recursion can branch heavily worst-case but likely okay due to degrees? However worst-case graph sparse stilln=40, number of 3-colorings huge maybe.

We can incorporate symmetry: colors 1,2,3 interchangeable. Fix first vertex color=1. This cuts.

Also sum condition automatic.

Implementation with bitmask adjacency list and pruning.

But possibility exponential worst. Perhaps problem restrict m strictly less than n? Let's determine exact phrase: "average number of incompatibilities per worker is strictly less than n" If incompatibilities per worker maybe number of incompatible pairs incident to that worker? average degree 2m/n < n -> m < n^2/2. For n=40 m up-to 799, dense. But maybe they intended "less than n" where n small 40 => m<40? no.

Still maybe 3-color algorithm with branching on high degree vertices can handle 40.

Let's implement backtracking with heuristics:
- Choose uncolored vertex with most colored neighbors to reduce options.
- Prefer vertex with degree ratio dense.
- Check color by color.

Could be sufficient for n=40 random edges? Worst-case maybe large.

We can add greedy initial.

Let's implement recursive exact 3-coloring with bitmask assignments:

- colors 0,1,2.
- For each vertex bitmask of available colors.
- recursion pick vertex with fewest options (if 0 backtrack)
- Propagate domain.

Use MRV heuristic. Because colors count only3, effective.

Also we can first try greedy: assign colors in order, if fail falls back to backtracking.

To guarantee solution within 2s n=40 worst? Possibly okay with fear.

Pseudo:

def dfs():
 if all assigned return
 choose unassigned with min options
 for color candidates:
   assign, reduce neighbors options
   dfs
   unassign
We need state encoding: since small n and 3 colors, use list of available bitmask for each vertex? Edge constraints.

We can simpler recursive:
order vertices by degree.
assignment = [-1]*n
color_used_neighbors = [[False]*3 for each]
When select vertex v, available = colors not used by already colored neighbors.
Attempt each.
But branching potentially 3^40 in worst. Pruning via clique lower bound.

Improve with choosing vertex with fewest legal colors (MRV). Also maintain forbidden mask for each vertex based on colored neighbors. Initially forbidden=0 for all.

Pseudo:
for attempt ith choose uncolored with maximal (#neighbors colored?) or minimal allowed? Since allowed starts 3.
Algorithm:
- list uncolored
- for each, compute forbidden_mask = union [1<<c for c in colored_neighbor_colors]
- backtrack choose uncolored vertex with max population count (most restrictions), branch on colors not in forbidden.
- assign store; update affected neighbors' forbidden masks.
- if assignment leads contradiction choose next.

n=40, worst K40 has many branches? At first vertex 3 choices, second adjacent so 2 choices etc depth 40 branching huge if no pruning. But clique>3 detection catches K40. Other dense graphs maybe.

Can incorporate symmetry: First vertex color 1, second vertex if not neighbor can choose? Symmetry breaking colors via choosing smallest index's three colors, then next uncolored can be assigned 1 or 2 only? Suppose after coloring vertex0=1, any later vertex when tried color2/3 are symmetric before either used, but if both available then choose color2 only not 3 to avoid symmetries.

Implement:
Find first uncolored v. Compute forbidden mask as bits (three bits) from neighbors colored.
If available colors empty return false.
Avoid symmetry: Let maxC used +1 unless forced smaller. If color c>used+1 and not forced (i.e., only c>max+1 available), no need. Actually in 3 colors, iteration choose colors in order but if both 2 and3 possible, symmetry allows forcing smaller unused. So c <= used+1.

Heuristic choose vertex with max colored constraints:
score = number of colored neighbors + number of uncolored neighbors? Or count available colors.

Implement:

def dfs(colored_count):
 if all colored return true
 compute cand = -1, min_options=4
 for v:
  if col[v]==0:
    forbidden = OR neigh color bits
    avail = 3 bits ^ forbidden
    cnt = popcount(avail)
    if cnt==0 return false
    if best pick with fewest options; tie by degree maybe.
 pick v.
 For each c in avail:
   col[v]=c
   if dfs(colors+1): return true
 col[v]=0
 return false

Try exact.

But worst-case graph 3-colorable but branching can still be okay n=40 due to small options.

Let's crucial consider guarantee might help: "average number of incompatibilities per worker strictly less than n" could mean m / n < n? If m is edge count, average <n always except complete? Actually degree avg =2m/n < n => dense. No.

I'll implement with additional clique detection? Exact.

Also optimize by precheck: If any vertex degree >= ? not.

We can add reduction: If a vertex has degree <3, once neighbors colored, it has at most2 forbidden => available at least1; but can color after neighbors. Simplif.

Potential challenge: Need guarantee feasible? Problem from programming contest likely has hidden guarantee maybe 3-colorability? But said determine.

Given n=40, search manageable maybe.

Let's code. Use recursion with color assignment bit.

Pathology: Star center colored; leaves have plenty.

Worst graph where 3-coloring hard maybe e.g. complete bipartite? Easy. Sporadic.

We'll include a quick necessary: Find clique of size 4 via Bron-Kerbosch? n=40 we can do.

But complete graph K40 impossible. Branching would assign first vertex, second can use2 colors, third one color? Actually K40: first 1, others cannot1 so colors2/3 become binary across clique of39 -> impossible. Branching many. We can detect clique >=4 using complement? Quick: if more than? Actually if max clique >=4 no. Determine by simple backtrack? Could.

Alternatively, use DSATUR + degree tie.

Let's code.

Symmetry: color first vertex 1.

Use available bitmask for each vertex computed dynamically: forbidden has bits for colors used by colored neighbors. Initially 0.

During recursion:
 best = -1, bestmask=0b111
 for v uncolored:
    mask = allowed[v] # only bits not used
    cnt = bit_count
    if cnt==0 return false
    if cnt < bestcnt:...
 pick.

When assign col bit (1<<c), for each neighbor u uncolored allowed[u] &= ~bit; record previous to revert.

Heuristic choose among colors: if first assignment, maybe lower.

Symmetry: allowed colors can include unused color > used+1 due to pruning; skip those as not needed? Maintain usedColCount. In candidate loop, if c > usedColCount+1 skip because symmetric to smaller.

Implementation:

color_idx: 1,2,3 bits 1,2,4

allowed[v] initial 7.

used=0

def backtrack(rem):
  if rem==0 return True
  v = -1; bestcnt=4; bestallow=0
  for i in range(n):
    if col[i]==0:
      a = allowed[i]
      cnt=popcnt(a)
      if cnt==0 return False
      # prefer few, then high degree
      if cnt< bestcnt: ...
  if bestcnt==0 impossible
  # choose
  # restrict colors <= used+1
  a = bestallow
  maxc = used+1
  bits allowed = a & ((1<<maxc)-1)
  if no bit? (shouldn't if symmetry)
  available list
  # heuristic color order maybe ascending
  for c bits:
    col[v]=c
    old=[]
    for neighbor u of v:
       if col[u]==0 and allowed[u] & (1<<c):
          old.append((u, allowed[u]))
          allowed[u] &= ~(1<<c)
    if backtrack(rem-1): return True
    restore
    allowed[v] restored? allowed[v] not mutated after choosing except not? We don't mutate allowed[v] because assigned.
    col[v]=0
  return False

used updated by bit count of col bits? Actually we need maxcolor used among assignments. Could derive by max color used variable passed? Simpler: maintain used_colors integer mask bits representing used colors globally. At node, max_used = used | (1<<c). Symmetry condition c cannot exceed lowest unused when choosing? If a color d > (highest used)+1 and no used in between because used colors maybe 1 and3 then color2 missing; choosing3 symmetric to2? If used colors mask {1,3}, max=3, possible new color 2 => not new; color? maxc=3. The rule allowed new colors only maxUsed+1. If we haven't used color2, choosing color3 would introduce lower missing color symmetric? Actually colors are labels; if used {1,3}, then missing2 is lower than max3. A new vertex can use 2 (already used? no) or 3 etc. Actually if color3 used but color2 not, then color2 is available. So "max_used_actual color" used.

Implement usedmask; last used color = highest bit. At assignment, allow c <= highest+1? If highest=3 all. If highest=1, allow c=1 or2, not3 (color3 symmetric to2 by renaming). If highest=2, allow 1,2,3 where3 is new but color gap none.

If used colors {1,3}, highest=3, allow all1,2,3.

So loop bits from low to high:
 allowed_bits &= (1 << (maxused+2)) -1? highest+1 inclusive means max_used+1 value. For max=1, allowed bits ≤2. yes.

Candidate bits = allowed[v] & ((1 << (highest_used+2)) -1).

Need highest_used compute from used mask = colv for all colored OR. We'll maintain usedmask.

After assignment usedmask | bit.

Complex reversion.

Let's code.

Also pre sort edges.

Need memory.

Potential many nodes but n=40 fine.

Let's test.

But I wonder if this problem expects using Lovasz local? Time limit 2 sec? Python might TLE worst.

Need possibly use max-clique <=4 trivial? If graph has clique 4, impossible; if not, 3-coloring still hard.

But small n=40 maybe okay.

Let's reason adversarial: Complete tripartite K(13,13,14) colorable, our heuristic will color. Triangles etc.

Worst uncolorable but not obvious: Grötzsch etc n=40. Branching with propagation likely.

Could also do preprocessing using Welsh-Powell? Not.

Let's include greedy initial solution for output? But exact validation.

Alternative use backtracking with SAT? no.

Let's implement and hope.

Edge: If no edges, all ones sum n valid.

Output sum constraint automatic.

Let's ensure at least one schedule allocation? Yes.

Now code block.