# Problem B — Warehouse Zone Configurations

Time limit: 1 s   Memory limit: 256 MB

## Description
An automated logistics center manages $n$ storage zones. You must assign each zone exactly one operational mode: either mode 1 or mode 0.

The facility's safety system enforces $m$ fallback protocols. Each protocol consists of a primary condition $c_1$ and a secondary condition $c_2$. These conditions are represented as non-zero integers:
- An integer $x > 0$ represents the condition that zone $x$ is assigned mode 1.
- An integer $x < 0$ represents the condition that zone $|x|$ is assigned mode 0.

A fallback protocol dictates that if the center's final configuration fails to satisfy the primary condition $c_1$, it is strictly required to satisfy the secondary condition $c_2$. If the configuration successfully satisfies $c_1$, the protocol is considered safe regardless of whether $c_2$ is satisfied. Note that the designation of primary and secondary is arbitrary; failing $c_2$ equally requires satisfying $c_1$.

Determine whether there exists a global mode assignment for all $n$ zones that safely resolves all $m$ fallback protocols simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of zones and the number of fallback protocols.
Each of the next $m$ lines contains two non-zero integers $c_1$ and $c_2$ ($|c_i| \le n$), representing the primary and secondary conditions for a single protocol.

## Output
If no valid global assignment exists, print a single line NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$) forming any valid operational mode assignment for the zones.

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
Multiple valid mode assignments may exist; any one is accepted. The same condition may appear in multiple fallback protocols.
