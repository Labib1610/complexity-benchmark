# Problem B — Power Calibration

Time limit: 1 s
Memory limit: 256 MB

An industrial facility manages a network of $n$ automated machines. Each machine must be configured to a power setting of either 1 or 2.

The facility's monitoring system has flagged $m$ adjacency pairs. Each pair indicates two machines that are physically close enough to risk signal overlap. To guarantee safe operation, the system enforces a strict neighborhood interference protocol. 

For every flagged pair of machines, let their assigned settings be $x$ and $y$. The system evaluates their compatibility by constructing the interference matrix:
$$M = \begin{pmatrix} x & y \\ y & x \end{pmatrix}$$
The protocol requires that for every flagged pair, their corresponding matrix $M$ must possess exactly one eigenvalue equal to 3.

Your task is to determine a power setting configuration for all $n$ machines that satisfies this protocol for every pair, or determine that no such configuration is possible.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$ — a pair of machines listed in an adjacency pair. Machines are numbered from $1$ to $n$.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), representing the lexicographically smallest valid configuration.

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