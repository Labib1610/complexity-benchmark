# Problem A — Exhibit Placement for the Museum Wing

Time limit: 5 s   Memory limit: 256 MB

## Description
A new museum wing is organizing its collection. There are $n$ distinct artifacts, and they will be displayed in a sequence of $n$ bays along a continuous wall. The bays are consecutively indexed $1, 2, \dots, n$. You must assign each artifact to exactly one bay, such that no two artifacts share a bay, and all artifacts are placed.

The curators want to emphasize certain thematic relationships. They have provided a list of pairs of artifacts that are thematically connected. When two connected artifacts are placed in bays $p$ and $q$, the tension between them is evaluated as the positive difference between their bay indices (that is, the larger index minus the smaller index).

The cumulative tension for the entire wing is the sum of the tensions for every pair on the curators' list. The curators require that this cumulative tension does not exceed a specified limit $B$. There is no restriction on the tension of any individual pair, nor is there any limit on how many pairs can span across the same bays. The only restriction is that the grand total must not exceed $B$.

Decide whether the artifacts can be assigned to the bays in a way that the cumulative tension stays within the limit $B$. If such an assignment exists, output it; otherwise, report that it is impossible. (Note that an assignment that minimizes tension for some pairs might cause the total to exceed the limit due to other pairs, so local optimizations do not guarantee a feasible overall assignment.)

## Input
First line: three integers $n$, $m$, and $B$.
Each of the next $m$ lines: two integers $u$ and $v$ — representing a thematic connection between artifact $u$ and artifact $v$.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ space-separated integers, where the $i$-th integer is the bay index (from $1$ to $n$) assigned to artifact $i$. Every bay index from $1$ to $n$ must appear exactly once.
If no such assignment is possible, print `NO`.

### Example

**Input**
```
4 4 6
1 2
2 3
3 4
4 1
```

**Output**
```
YES
1 2 4 3
```
