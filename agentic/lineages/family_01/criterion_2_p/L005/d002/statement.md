# Problem B — Molecular Assembly

Time limit: 1 s   Memory limit: 256 MB

A synthetic biology lab is calibrating a molecular structure composed of $n$ distinct protein building blocks. The structure contains $m$ contact points, each connecting a specific pair of blocks.

To ensure stability, the lab must configure the resonance of the entire assembly. Every building block requires a resonance setting of either 1 or 2. Whenever two blocks meet at a contact point, they will only interlock properly if their combined resonance settings sum to exactly 3. You must find a configuration for all blocks that allows every contact point to interlock. If the structure cannot be stabilized in this way, indicate that it is impossible.

## Input
The first line provides $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), the number of building blocks and contact points, respectively.
The following $m$ lines each contain two integers $u$ and $v$ — a pair of blocks that share a contact point.

## Output
If the assembly cannot be stabilized, output NO on a single line.
If it can, output YES on the first line. On the second line, output $n$ integers $s_1 \dots s_n$ (each in {1,2}), representing the lexicographically smallest valid configuration.

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