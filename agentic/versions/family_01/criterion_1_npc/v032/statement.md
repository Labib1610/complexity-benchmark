# Problem A — Security Clearance Resolution

Time limit: 2 s   Memory limit: 256 MB

In many distributed architectures, configuration rules can be resolved efficiently by propagating forced choices. You are given a system of $n$ components. Each component must be assigned a clearance level from the set $\{1, 2, 3\}$.

To maintain strict compartmentalization, the system enforces $m$ separation rules. Each rule specifies two components $u$ and $v$ that must not share the same clearance level. Because these rules only restrict components two at a time, rather than imposing complex global dependencies, the constraints are highly localized. 

Your task is to determine whether a valid clearance assignment exists for all $n$ components. If the system can be configured safely, you must output the lexicographically smallest sequence of clearance levels.

## Input
The first line contains two integers $n$ and $m$ (1 ≤ $n$ ≤ 40, 0 ≤ $m$ ≤ $n(n−1)/2$) — the number of components and the number of separation rules.
Each of the following $m$ lines contains two integers $u$ and $v$ (1 ≤ $u, v$ ≤ $n$, $u \neq v$) representing a separation rule between component $u$ and component $v$.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \dots, c_n$ (where each $c_i \in \{1, 2, 3\}$) representing the clearance level of each component. This sequence must be the lexicographically smallest among all valid assignments (comparing $c_1$ first, then $c_2$, and so on).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
