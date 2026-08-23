# Problem B — Amplification Factors

Time limit: 1 s
Memory limit: 256 MB

You are tasked with tuning a network of $n$ signal relays. The system includes $m$ critical connections, each bridging a pair of relays.

To prevent signal distortion, you must assign a digital gain setting to every relay in the network. The only permitted settings are $1$ and $2$. However, the network must satisfy a strict interference constraint: whenever two relays are joined by a critical connection, the bitwise AND of their assigned gain settings must evaluate to $0$.

Your objective is to find a network-wide assignment of gain settings that satisfies this requirement, or to determine that no such assignment is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of relays and the number of critical connections, respectively.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), specifying that a critical connection bridges relay $u$ and relay $v$.

## Output
If no valid assignment of gain settings exists, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $z_1, z_2, \dots, z_n$, where each $z_i \in \{1, 2\}$ represents the gain setting for relay $i$. If multiple valid assignments exist, you must output the one that is lexicographically smallest.

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