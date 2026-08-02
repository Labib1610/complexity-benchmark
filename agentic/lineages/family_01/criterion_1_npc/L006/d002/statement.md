# Security Clearance Tier Allocation

Time limit: 2 s   Memory limit: 256 MB

A facility manages $n$ personnel members, indexed from $1$ to $n$. Each personnel member must be assigned to exactly one of three security clearance tiers, numbered $1$, $2$, and $3$.

Due to policy restrictions, certain designated pairs of personnel members are prohibited from holding the same clearance tier.

Determine if there is a valid assignment of clearance tiers to all $n$ personnel members such that no prohibited pair shares a tier. If at least one valid assignment exists, output `YES` on the first line, followed by the lexicographically smallest sequence of assigned tiers $(s_1, s_2, \dots, s_n)$ on the second line, where $s_i \in \{1, 2, 3\}$ is the tier assigned to personnel member $i$. If no valid assignment is possible, output `NO`.

## Input
The first line contains two space-separated integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of personnel members and the number of prohibited pairs, respectively.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that personnel member $u$ and personnel member $v$ cannot be assigned the same clearance tier.

## Output
If no valid assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1 s_2 \dots s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the clearance tier assigned to personnel member $i$. If multiple valid assignments exist, output the lexicographically smallest sequence.

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