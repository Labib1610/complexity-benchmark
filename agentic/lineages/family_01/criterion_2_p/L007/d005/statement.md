# Problem B — Resonant Foundations

Time limit: 1 s
Memory limit: 256 MB

The structural integrity of a new skyscraper depends on $n$ primary load-bearing pillars, numbered 1 to $n$. The engineering firm must select a concrete composite grade for each pillar. The approved composite grades are exactly 1 and 2.

To mitigate wind-induced vibrations, the design includes $m$ acoustic dampeners. Each dampener spans between a specific pair of pillars. A dampener's ability to properly distribute stress depends on the composite grades of the two pillars it connects. 

For any dampener connecting pillar $u$ with composite grade $c_u$ and pillar $v$ with composite grade $c_v$, its stress dissipation factor is calculated as:
$S(c_u, c_v) = c_u^3 + c_v^3 + 7(c_u^2 + c_v^2) + 2(c_u + c_v) - 20 c_u c_v$

The skyscraper's vibration control system is considered safe if and only if the sum of the stress dissipation factors across all $m$ dampeners is exactly $10m$.

Your task is to determine if there is a safe composite selection for all $n$ pillars. If multiple safe selections exist, the procurement system requires the one that is lexicographically smallest when represented as a sequence of $n$ composite grades.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the indices of the two pillars spanned by a dampener.

## Output
If no safe selection exists, print a single line `NO`.
Otherwise print `YES`, then a second line with $n$ integers $c_1 \dots c_n$ (each being 1 or 2), representing the lexicographically smallest safe selection.

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