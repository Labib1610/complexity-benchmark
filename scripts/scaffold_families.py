"""One-shot scaffold for families 02-16. Run from project root."""

import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATASET = ROOT / "dataset"

# ── Family metadata ────────────────────────────────────────────────────────────
# Each entry: (zero-padded id, slug, display_name, anchor,
#              [c1_algo, c1_note, c1_delta, c1_tl],
#              [c2_algo, c2_note, c2_delta, c2_tl],
#              [c3_algo, c3_note, c3_delta, c3_tl])

FAMILIES = [
    (
        "02", "sat", "Task Scheduling", "3-SAT",
        # C1 NPC
        ("<FILL: backtracking DPLL-style 3-SAT solver>",
         "3-SAT; Cook-Levin (1971); canonical NP-complete problem",
         "anchor variant (NP-complete base)", 2),
        # C2 P
        ("<FILL: implication graph + Kosaraju/Tarjan SCC for 2-SAT; O(n+m)>",
         "2-SAT is solvable in O(n+m) via SCC on implication graph",
         "clauses reduced to 2 literals; removes NP-hardness entirely", 1),
        # C3 INFEASIBLE
        ("<FILL: Tarjan SCC; detect variable x and ¬x in same SCC; output the variable>",
         "2-SAT with contradiction: x and ¬x in same SCC certifies unsatisfiability",
         "guarantee contradiction cycle exists; task is to output the contradicted variable", 1),
    ),
    (
        "03", "hamiltonian_path", "Delivery Routing", "HAMILTONIAN PATH",
        ("<FILL: bitmask DP over vertex subsets; dp[mask][v]; O(2^n * n^2)>",
         "HAMILTONIAN PATH; NP-complete; reduction from 3-SAT via gadgets",
         "anchor variant (NP-complete base)", 5),
        ("<FILL: topological sort; check unique ordering — each step has exactly one zero-in-degree node>",
         "unique topological order in a DAG implies a Hamiltonian path exists; O(n+m)",
         "graph is a DAG with unique topological order; polynomial via topo-sort", 1),
        ("<FILL: find isolated vertex (degree 0); output its id as infeasibility certificate>",
         "isolated vertex cannot appear on any Hamiltonian path; immediate certificate",
         "guarantee isolated vertex exists; output the vertex id", 1),
    ),
    (
        "04", "subset_sum", "Budget Selection", "SUBSET SUM (large values)",
        ("<FILL: meet-in-middle for n≤40; or backtracking with pruning>",
         "SUBSET SUM; NP-complete; reduction from 3-SAT via binary encoding",
         "anchor variant with values up to 10^9; rules out pseudo-poly DP", 5),
        ("<FILL: standard boolean DP dp[j]=True if sum j reachable; O(n*T) with T poly-bounded>",
         "subset sum with poly-bounded values/target is in P via DP; O(n*T)",
         "values and target bounded by n^2; DP runtime is polynomial in input size", 2),
        ("<FILL: check target < 0; all item values positive guarantees infeasibility; output target as certificate>",
         "negative target is trivially infeasible since all item values are positive",
         "target is guaranteed negative; immediate infeasibility certificate", 1),
    ),
    (
        "05", "three_dim_matching", "Team and Resource Alignment", "3-DIMENSIONAL MATCHING",
        ("<FILL: backtracking over triples; try matching greedily or DFS>",
         "3-DIMENSIONAL MATCHING; NP-complete; Karp (1972)",
         "anchor variant (NP-complete base)", 5),
        ("<FILL: reduce to bipartite matching; Hopcroft-Karp O(E*sqrt(V))>",
         "3DM restricted to bipartite-compatible triples reduces to 2D bipartite matching",
         "compatibility structure reduces to bipartite; Hopcroft-Karp gives polynomial solution", 2),
        ("<FILL: find element with empty compatibility row; output it as Hall violation certificate>",
         "Hall's theorem: element with no compatible triple makes perfect matching impossible",
         "guarantee one element has no compatible triple; output the element id", 1),
    ),
    (
        "06", "bin_packing", "Cargo Loading", "BIN PACKING",
        ("<FILL: backtracking over item-to-bin assignments; exponential in general>",
         "BIN PACKING; NP-complete; reduction from PARTITION",
         "anchor variant (NP-complete base)", 5),
        ("<FILL: fractional bin packing; greedy ratio; minimum bins = ceil(total_size / bin_capacity)>",
         "fractional relaxation solvable in O(n log n); items may be split across bins",
         "items can be fractionally split; continuous relaxation is polynomial", 1),
        ("<FILL: find item with size > bin_capacity; output item id as infeasibility certificate>",
         "single item larger than any bin cannot be packed; trivial certificate",
         "guarantee one item exceeds all bin capacities; output the item id", 1),
    ),
    (
        "07", "shortest_common_superstring", "DNA and Log Assembly", "SCS (k>=3 strings)",
        ("<FILL: bitmask DP over string subsets; Held-Karp on overlap graph; O(2^k * k^2)>",
         "SHORTEST COMMON SUPERSTRING for k>=3 strings; NP-complete; reduction from HAMILTONIAN PATH on overlap graph",
         "anchor variant with k>=3 strings; NP-complete", 5),
        ("<FILL: greedy overlap merge for exactly 2 strings; O(|s1|+|s2|)>",
         "2-string overlap superstring computable in linear time via KMP overlap",
         "exactly 2 strings; linear-time overlap merge is polynomial", 1),
        ("<FILL: detect forbidden substring pair that cannot coexist; output the conflicting pair>",
         "contradictory required substrings make any common superstring impossible",
         "guarantee contradictory substrings exist; output the conflicting pair as certificate", 1),
    ),
    (
        "08", "vertex_cover", "Security Guard Placement", "VERTEX COVER",
        ("<FILL: bounded search tree; branch on uncovered edges; O(2^k * m)>",
         "VERTEX COVER; NP-complete; complement of INDEPENDENT SET; Karp (1972)",
         "anchor variant (NP-complete base)", 5),
        ("<FILL: König's theorem; min vertex cover = max bipartite matching; Hopcroft-Karp>",
         "König's theorem: in bipartite graphs minimum vertex cover equals maximum matching size",
         "graph restricted to bipartite; König's theorem gives polynomial minimum cover", 2),
        ("<FILL: compute max matching; output matching as lower-bound certificate when size > budget>",
         "maximum matching is a lower bound on vertex cover; if matching size > k no cover of size k exists",
         "guarantee matching size > budget k; output the matching as infeasibility certificate", 2),
    ),
    (
        "09", "clique_independent_set", "Social Network Analysis", "CLIQUE",
        ("<FILL: backtracking Bron-Kerbosch with pivoting; or enumerate subsets of size k>",
         "CLIQUE; NP-complete; Karp (1972); complement reduction from INDEPENDENT SET",
         "anchor variant (NP-complete base)", 5),
        ("<FILL: König complement theorem; max independent set in bipartite = n - max matching; Hopcroft-Karp>",
         "maximum independent set in bipartite graphs is polynomial via König's theorem",
         "graph restricted to bipartite; König complement theorem applies; O(n*sqrt(n))", 2),
        ("<FILL: check requested clique size k > |V|; output k and |V| as pigeonhole certificate>",
         "pigeonhole principle: k-clique requires k<=n nodes; k>n is immediately infeasible",
         "guarantee k > |V|; output trivial pigeonhole impossibility certificate", 1),
    ),
    (
        "10", "dominating_set", "Sensor Placement", "DOMINATING SET",
        ("<FILL: backtracking over vertex subsets of size k>",
         "DOMINATING SET; NP-complete; reduction from SET COVER and VERTEX COVER",
         "anchor variant (NP-complete base)", 5),
        ("<FILL: tree DP; dp[v][0/1/2] states (dominated, dominator, not dominated); O(n)>",
         "dominating set on trees is solvable in O(n) via tree DP",
         "graph restricted to a tree; tree DP gives optimal dominating set in linear time", 1),
        ("<FILL: find isolated vertex (degree 0) when budget=0; output it as undominated certificate>",
         "isolated vertex has no neighbor to dominate it and budget=0 prevents self-selection",
         "guarantee isolated vertex exists and budget=0; output the vertex id", 1),
    ),
    (
        "11", "set_cover", "Skill Coverage", "SET COVER",
        ("<FILL: backtracking; try all subsets of the given sets of size <=k>",
         "SET COVER; NP-complete; Karp (1972); reduction from VERTEX COVER",
         "anchor variant (NP-complete base)", 5),
        ("<FILL: reduce to bipartite edge cover; König: min edge cover = n - max matching; Hopcroft-Karp>",
         "set cover with sets of size <=2 equals bipartite edge cover; König's theorem applies",
         "sets restricted to size <=2; reduces to edge cover which is polynomial via König", 2),
        ("<FILL: find element not appearing in any set; output it as uncoverable certificate>",
         "element appearing in no set cannot be covered regardless of set selection",
         "guarantee uncoverable element exists; output the element id", 1),
    ),
    (
        "12", "knapsack", "Investment Portfolios", "0-1 KNAPSACK",
        ("<FILL: meet-in-middle for large weights; or backtracking with pruning>",
         "0-1 KNAPSACK; NP-complete; reduction from SUBSET SUM",
         "anchor variant with weights up to 10^9; pseudo-poly DP is infeasible", 5),
        ("<FILL: fractional knapsack; greedy by value/weight ratio descending; O(n log n)>",
         "fractional knapsack is solvable optimally by greedy ratio sort in O(n log n)",
         "items can be fractionally included; greedy ratio sort gives optimal solution", 1),
        ("<FILL: check budget=0 with all positive costs; output 'NO' and list of item costs>",
         "budget 0 with all positive item costs: no item can be selected; infeasible by construction",
         "guarantee budget=0 and all item costs>0; output trivial infeasibility", 1),
    ),
    (
        "13", "partition", "Workload Partitioning", "PARTITION",
        ("<FILL: meet-in-middle for large values; backtracking with pruning>",
         "PARTITION; NP-complete; special case of SUBSET SUM with target = total/2",
         "anchor variant with large values (up to 10^9); pseudo-poly DP ruled out", 5),
        ("<FILL: boolean DP dp[j]=True if subset sums to j; only feasible when values bounded by n; O(n^3)>",
         "partition with small integers is pseudo-polynomial DP; polynomial given bounded value range",
         "values bounded by n; total sum <=n^2; DP runtime is polynomial in input size", 2),
        ("<FILL: check if total sum is odd; output the sum as parity certificate>",
         "odd total sum makes equal partition impossible; no subset can sum to a non-integer",
         "guarantee total sum is odd; output the sum as proof of infeasibility", 1),
    ),
    (
        "14", "steiner_tree", "Network Extension", "STEINER TREE",
        ("<FILL: Dreyfus-Wagner bitmask DP over terminal subsets; O(3^k*n + 2^k*n^2)>",
         "STEINER TREE; NP-complete; reduction from EXACT COVER",
         "anchor variant with k>=3 required terminals (NP-complete base)", 5),
        ("<FILL: Kruskal MST; when all vertices are required terminals, Steiner tree = MST>",
         "when all vertices are required terminals the Steiner tree equals the MST; polynomial",
         "all vertices are required; Steiner tree reduces to MST; Kruskal O(m log m)", 2),
        ("<FILL: find required terminal with degree 0; output its id as unreachable certificate>",
         "isolated required terminal cannot be reached by any spanning subtree; immediate certificate",
         "guarantee one required terminal is isolated; output the node id", 1),
    ),
    (
        "15", "lcs", "Bioinformatics Alignment", "MULTIPLE-SEQ LCS (k>=3)",
        ("<FILL: backtracking over all alignment combinations for k>=3 sequences>",
         "MULTIPLE-SEQUENCE LCS for k>=3 sequences; NP-complete; reduction from VERTEX COVER",
         "anchor variant with k>=3 sequences; NP-complete", 5),
        ("<FILL: standard 2D DP; dp[i][j] = LCS length of s1[:i] and s2[:j]; O(n*m)>",
         "2-sequence LCS is solvable in O(n*m) via standard DP; no hardness",
         "exactly 2 sequences; polynomial 2D DP applies", 2),
        ("<FILL: check character-set intersection is empty; output the two disjoint alphabets>",
         "disjoint alphabets imply LCS length is 0; any shared character would be required",
         "guarantee disjoint alphabets between sequences; output the two alphabet sets", 1),
    ),
    (
        "16", "job_shop", "Factory Scheduling", "JOB-SHOP (m>=3 machines)",
        ("<FILL: branch-and-bound over job orderings on machines; exponential in general>",
         "JOB-SHOP SCHEDULING with m>=3 machines; NP-complete; reduction from 3-SAT",
         "anchor variant with m>=3 machines (NP-complete base)", 5),
        ("<FILL: Johnson's algorithm for 2-machine flow-shop; sort by min(p1,p2) rule; O(n log n)>",
         "2-machine flow-shop is optimally solvable by Johnson's algorithm in O(n log n)",
         "exactly 2 machines; Johnson's algorithm gives optimal makespan schedule", 1),
        ("<FILL: find job whose total processing time exceeds global deadline; output its id>",
         "single job processing time exceeding the deadline makes any feasible schedule impossible",
         "guarantee one job's total time > deadline; output the job id as certificate", 1),
    ),
]

# ── Templates ──────────────────────────────────────────────────────────────────

META_TEMPLATE = """\
family: "{fam_id}"
family_name: {slug}
criterion: {crit_n}
class: {cls}
problem_letter: {letter}
intended_algorithm: "{algo}"
reduction_note: "{note}"
constraint_delta: "{delta}"
judge: exact
time_limit_s: {tl}
memory_limit_mb: 256
"""

STATEMENT_TEMPLATE = """\
# Problem {letter} — <FILL TITLE>

Time limit: {tl} s   Memory limit: 256 MB

<!--
PLACEHOLDER — fill following conventions/statement_schema.md and the Family 1 template.
RULES:
- Describe the task in plain words. Bounds allowed. NEVER name the complexity class.
- This is the {cls} variant of family {fam_id} ({slug}). Anchor: {anchor}.
- Required sections: Description, Input, Output (with tie-break), at least one Example.
-->
"""

REFERENCE_TEMPLATE = """\
# PLACEHOLDER reference solution for family {fam_id} ({slug}), criterion {crit_n} ({cls}).
# Fill with a deterministic Python 3 solution: read stdin, write stdout.
# Intended algorithm (from meta.yaml): {algo}
import sys

def main():
    data = sys.stdin.buffer.read().split()
    # TODO: implement
    raise NotImplementedError

main()
"""

LETTERS = ("A", "B", "C")
CLASS_LABELS = ("NPC", "P", "INFEASIBLE")
CRIT_NAMES = ("criterion_1_npc", "criterion_2_p", "criterion_3_infeasible")


def scaffold():
    for entry in FAMILIES:
        fam_id, slug, display_name, anchor = entry[0], entry[1], entry[2], entry[3]
        criteria_data = entry[4], entry[5], entry[6]

        fam_dir = DATASET / f"family_{fam_id}_{slug}"

        # family.yaml
        fam_dir.mkdir(parents=True, exist_ok=True)
        (fam_dir / "family.yaml").write_text(
            f'family: "{fam_id}"\n'
            f"name: {slug}\n"
            f'display_name: "{display_name}"\n'
            f'base_problem: "<FILL: one-sentence plain-English base task>"\n'
            f"anchor: {anchor}\n"
        )

        for i, (crit_name, letter, cls, cdata) in enumerate(
            zip(CRIT_NAMES, LETTERS, CLASS_LABELS, criteria_data)
        ):
            algo, note, delta, tl = cdata
            crit_dir = fam_dir / crit_name
            tests_dir = crit_dir / "tests"
            tests_dir.mkdir(parents=True, exist_ok=True)
            (tests_dir / ".gitkeep").touch()

            ctx = dict(
                fam_id=fam_id, slug=slug, anchor=anchor,
                crit_n=i + 1, cls=cls, letter=letter,
                algo=algo, note=note, delta=delta, tl=tl,
            )

            (crit_dir / "meta.yaml").write_text(META_TEMPLATE.format(**ctx))
            (crit_dir / "statement.md").write_text(STATEMENT_TEMPLATE.format(**ctx))
            (crit_dir / "reference.py").write_text(REFERENCE_TEMPLATE.format(**ctx))

        print(f"  scaffolded family_{fam_id}_{slug}")

    print(f"\nDone — {len(FAMILIES)} families scaffolded.")


if __name__ == "__main__":
    scaffold()
