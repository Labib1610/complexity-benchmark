# Problem B — Resonant Foundations

Time limit: 1 s   Memory limit: 256 MB

The structural integrity of a new skyscraper depends on $n$ primary load-bearing pillars, numbered 1 to $n$. The engineering firm must select a concrete composite for each pillar. There are exactly two approved composites, designated as composite 1 and composite 2.

To mitigate wind-induced vibrations, the design includes $m$ acoustic dampeners. Each dampener spans between a specific pair of pillars. If the two pillars spanned by a dampener are cast from the same concrete composite, they will share the same resonant frequency, causing the dampener to shatter under heavy winds. Therefore, any two pillars sharing a dampener must be constructed from different composites.

Your task is to determine if there is a safe composite selection for all $n$ pillars. If multiple safe selections exist, the procurement system requires the one that is lexicographically smallest when represented as a sequence of $n$ composite identifiers.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the indices of the two pillars spanned by a dampener.

## Output
If no safe selection exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $c_1 \dots c_n$ (each in {1,2}), the lexicographically smallest safe selection.

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