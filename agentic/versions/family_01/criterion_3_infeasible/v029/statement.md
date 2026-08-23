# Problem C — Phase 2: Triad Isolation

Time limit: 2 s
Memory limit: 256 MB

The Automated Stability Protocol operates in three phases to secure volatile compound batches. 

In Phase 1, the system conducts a pairwise screening of $n$ chemical compounds, testing every possible pair to see which ones are highly reactive when combined. This phase has already been completed, and the resulting log of reactive pairs is provided to you.

Your task is to implement Phase 2. The safety guidelines mandate that a batch cannot be certified as stable if it contains any "unstable triad." An unstable triad is a group of exactly three distinct compounds where every compound in the group is highly reactive with the other two. It is a known chemical property for these specific batches that at least one such triad exists. You must process the Phase 1 logs and output exactly one unstable triad to trigger the emergency protocol. 

In Phase 3, the system will use your output to deploy neutralizers. Because the deployment mechanisms are strictly deterministic, you must report the unstable triad whose lowest compound identifier is as small as possible. If multiple triads share the same lowest identifier, you must minimize the second-lowest identifier, and if there is still a tie, minimize the highest identifier. 

## Input
The first line of the Phase 1 log contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of compounds (numbered $1$ through $n$) and the number of reactive pairs discovered.

Each of the following $m$ lines contains two integers $u$ and $v$, indicating that compound $u$ and compound $v$ are highly reactive with each other. 
It is guaranteed that the provided log contains at least one unstable triad.

## Output
Print a single line containing three integers $a$, $b$, and $c$, representing the identifiers of the compounds in the chosen unstable triad. These identifiers must be printed in ascending order ($a < b < c$). Remember to follow the exact tie-breaking rules described for Phase 3.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
