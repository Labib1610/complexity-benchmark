# Corporate Consolidation

Time limit: 2 s   Memory limit: 256 MB

## Description

A market consists of $n$ independent corporations, numbered 1 to $n$. A specific subset of $t$ corporations are designated as patent holders. There are $m$ potential merger agreements that can be executed between certain pairs of corporations, each requiring a specific legal fee to finalize.

Your objective is to execute a subset of these agreements so that all $t$ patent-holding corporations end up absorbed into the exact same conglomerate. When a merger agreement between two corporations is executed, they (along with any other corporations they have already merged with) consolidate into a single unified entity. You must ensure the patent holders are consolidated together at the minimum possible total legal fee.

To prevent antitrust violations, the market regulations enforce a strict density limit on the proposed mergers: for any arbitrary subset of $k$ corporations (where $k \ge 1$), there are never more than $k - 1$ proposed agreements exclusively between members of that subset. Furthermore, the total number of proposed agreements $m$ across the entire market is strictly regulated to be exactly $n - 1$.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$).
The second line contains $t$ distinct integers: the identifiers of the patent-holding corporations.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), representing a potential merger agreement between corporation $u$ and corporation $v$ with a legal fee of $w$.

## Output

Print a single integer: the minimum total legal fee to ensure all patent holders belong to the same conglomerate.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```

## Note

In Example 1, the patent holders 1 and 4 are consolidated by executing the agreements that merge 1 with 2, 2 with 3, and 3 with 4, for a total fee of 5 + 1 + 2 = 8. In Example 2, there is only one patent holder, so no agreements need to be executed.