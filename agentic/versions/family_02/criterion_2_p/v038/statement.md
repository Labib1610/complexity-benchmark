# Problem B — Formulation Directives

Time limit: 1 s
Memory limit: 256 MB

## Description

You are designing a chemical formulation that considers $n$ distinct additives. For each additive, you must make a strict decision: it will be either included in the formulation or excluded from it.

The process is governed by $m$ safety directives. Each directive specifies exactly two criteria. A criterion refers to a specific additive and a required status (either "included" or "excluded"). To ensure stability, the final formulation must satisfy at least one of the two criteria for every single directive. It is acceptable if both criteria in a directive are satisfied. 

You must determine if there is a global configuration of all $n$ additives that simultaneously satisfies all $m$ safety directives. If such a configuration exists, you must provide one. If no such configuration can possibly satisfy all directives, you must report that it is impossible.

To assist with memory allocation, note that the total number of criteria evaluated across all directives is exactly $2m$, which is guaranteed not to exceed 400,000. Additionally, the additive identifiers referenced in the directives will never exceed 100,000 in magnitude.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two non-zero signed integers $c_1$ and $c_2$. 
The absolute value of each integer represents the additive identifier ($1 \le |c_i| \le n$). A positive integer means the criterion is that the additive is included, while a negative integer means the criterion is that the additive is excluded.

## Output
If no valid configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each being `0` or `1`), where $s_i = 1$ indicates that the $i$-th additive is included, and $s_i = 0$ indicates it is excluded.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid configurations may exist; any one is accepted. The same additive or criterion may appear in multiple directives.
