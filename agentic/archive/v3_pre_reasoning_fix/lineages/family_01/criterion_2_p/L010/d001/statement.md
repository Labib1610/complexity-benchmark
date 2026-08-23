# Cross-Facility Transfers

Time limit: 1 s
Memory limit: 256 MB

You are organizing the docking schedule for $n$ cargo vessels, numbered 1 through $n$. There are two available loading facilities: Facility 1 and Facility 2. Each vessel must be directed to exactly one of these two facilities.

The logistics operation includes $m$ cross-facility transfer manifests. Each manifest involves exactly two specific vessels. To execute a manifest, the two vessels involved must be docked at different facilities—one at Facility 1 and the other at Facility 2. If both vessels are sent to the same facility, the transfer cannot be processed.

You must determine if there is a valid assignment of vessels to facilities such that all $m$ manifests can be executed. If multiple valid assignments exist, you must provide the one where the sequence of facility choices, ordered from vessel 1 to vessel $n$, is lexicographically smallest.

## Input
The first line of the input contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of vessels and the number of manifests.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — a pair of vessels involved in a single manifest.

## Output
If there is no way to assign facilities to vessels such that all manifests can be executed, print a single line containing `NO`.
Otherwise, print `YES` on the first line, followed by a second line containing $n$ integers $f_1, \dots, f_n$ (where each $f_i \in \{1, 2\}$) representing the lexicographically smallest valid sequence of facility assignments.

## Example 1
**Input:**
```
4 4
1 2
2 3
3 4
1 4
```
**Output:**
```
YES
1 2 1 2
```

## Example 2
**Input:**
```
3 3
1 2
1 3
2 3
```
**Output:**
```
NO
```