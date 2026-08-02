# Research Facility Division Allocation

Time limit: 1 s   Memory limit: 256 MB

A research center employs $n$ researchers, identified by distinct integers from $1$ through $n$. The facility operates two available units: Unit 1 and Unit 2.

Due to equipment interference, there are $m$ specified restriction pairs of researchers who cannot be placed in the same unit. If researcher $u$ and researcher $v$ form a restriction pair, one must work in Unit 1 and the other in Unit 2.

Additionally, internal administrative protocols require that:
1. Every researcher is assigned to exactly one unit (either Unit 1 or Unit 2).
2. The total headcount assigned to Unit 1 does not exceed $n$.
3. The sum of the identification numbers of all researchers assigned to Unit 1 does not exceed $\frac{n(n+1)}{2}$.

Determine whether a valid assignment exists that satisfies all restriction pairs and administrative protocols. If multiple valid assignments exist, output the one that produces the lexicographically smallest sequence $s_1, s_2, \dots, s_n$, where $s_i \in \{1, 2\}$ denotes the unit assigned to researcher $i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$) — the number of researchers and the number of restriction pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that researcher $u$ and researcher $v$ cannot share a unit.

## Output
If no valid assignment exists, print `NO` on a single line.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment sequence.

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
