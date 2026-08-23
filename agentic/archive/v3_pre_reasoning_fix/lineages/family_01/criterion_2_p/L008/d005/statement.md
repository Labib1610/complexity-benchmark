# Problem B — Horological Strata

Time limit: 1 s   Memory limit: 256 MB

A master horologist is assembling a sophisticated mechanical movement containing $n$ individual gears. The movement's framework provides exactly two distinct depths for mounting, designated as depth 1 and depth 2. Every gear must be secured at one of these two depths.

According to the blueprints, there are $m$ specific pairs of gears that share the same physical footprint in their top-down projection. To guarantee that the mechanism functions smoothly and avoids any physical interference, an interaction between any such overlapping pair is only mechanically viable if one gear is positioned at depth 1 while its overlapping counterpart is positioned at depth 2.

You must establish a valid depth configuration for all $n$ gears that respects every overlapping engagement, or conclude that the movement cannot be built according to the blueprints.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of gears that overlap in their projection.

## Output
If no valid depth configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $t_1, \dots, t_n$ (each $t_i \in \{1, 2\}$), where $t_i$ is the depth assigned to gear $i$. If there are multiple valid configurations, output the sequence that is lexicographically smallest.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```