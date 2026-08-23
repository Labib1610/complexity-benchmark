# Vessel Calibration

Time limit: 1 s
Memory limit: 256 MB

You are managing a fleet of $n$ autonomous surveying vessels. Each vessel must be configured with a calibration state, which is an integer $s_i \in \{1, 2\}$. Throughout the operation, specific pairs of vessels will navigate in close proximity. For these pairs to successfully synchronize and merge their data streams, their configured calibration states must differ by exactly 1. There are $m$ such proximity records.

Your objective is to find a valid calibration state assignment for all $n$ vessels, or determine if no such assignment exists. When multiple valid configurations are possible, you must provide the one that yields the lexicographically smallest sequence of states for vessels 1 to $n$.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$), denoting the number of vessels and the number of proximity records, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), specifying that vessel $u$ and vessel $v$ will operate close to each other.

## Output
If no valid state assignment is possible, output a single line with `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $s_1, \ldots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid sequence of calibration states.

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