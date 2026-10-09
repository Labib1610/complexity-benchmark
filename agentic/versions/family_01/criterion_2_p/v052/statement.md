# Problem B — Equilibrium Assignments

Time limit: 1 s   Memory limit: 256 MB

You are configuring an array of $n$ energy regulators, numbered 1 through $n$. Each regulator must be configured to operate at an integer power tier of exactly 1 or 2.

The facility's schematics define $m$ bidirectional energy conduits. Each conduit links a specific pair of regulators. To maintain grid equilibrium, the combined power tier of any two regulators linked by a conduit must equal exactly 3. If the sum of their tiers is anything other than 3, the conduit will overload.

Your task is to determine if it is possible to assign a power tier to every regulator such that no conduits overload. If it is possible, you must output a valid assignment. Due to standard operating procedures, if there are multiple valid assignments, you must provide the lexicographically smallest one (i.e., assignment $A$ is lexicographically smaller than assignment $B$ if, at the first regulator $i$ where their tier assignments differ, assignment $A$ uses tier 1 and assignment $B$ uses tier 2).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that an energy conduit links regulator $u$ and regulator $v$.

## Output
If there is no way to assign the power tiers without overloading a conduit, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $t_1, t_2, \ldots, t_n$ (where each $t_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment of power tiers to the $n$ regulators.

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
