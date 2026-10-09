# Problem B — Loom Threading Protocols

Time limit: 2 s   Memory limit: 256 MB

## Description
An industrial loom weaves complex fabrics by coordinating a set of longitudinal warp feeds and a set of transverse weft feeds. A pattern is defined by a series of binding operations. Each binding operation requires one specific warp feed and one specific weft feed to intersect.

To prevent thread snapping, no single feed (whether warp or weft) can participate in more than one binding operation during the same machine cycle. A feed can sit idle during a cycle, but it cannot double-task.

The complexity of a pattern is dictated by its most heavily utilized feed. Let $\Delta$ be the maximum number of binding operations that any single feed is involved in. Because bindings only ever occur between a warp feed and a weft feed—never between two feeds of the same type—the loom's operational rules guarantee that all binding operations can always be scheduled using exactly $\Delta$ machine cycles. No additional cycles are ever required beyond this theoretical minimum.

Your task is to generate a cycle schedule for a given pattern. You must assign each binding operation to a cycle number from $1$ to $\Delta$ such that no feed is required to perform multiple bindings in the same cycle.

## Input
The first line contains three integers `nL`, `nR`, and `m` ($1 \le \text{nL}, \text{nR} \le 100000$, $0 \le m \le 400000$), representing the number of warp feeds, the number of weft feeds, and the total number of binding operations.
The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le \text{nL}$, $1 \le v \le \text{nR}$), indicating a binding operation between warp feed $u$ and weft feed $v$.

## Output
Print `YES` on the first line.
On the second line, print $m$ integers, each in the range $1 \ldots \Delta$. The $i$-th integer represents the machine cycle assigned to the $i$-th binding operation in the input order. If multiple valid cycle schedules exist, you may output any of them.

## Example
### Input
```
4 4 6
1 1
1 2
2 2
2 3
3 3
4 3
```
### Output
```
YES
1 2 1 2 1 3
```
