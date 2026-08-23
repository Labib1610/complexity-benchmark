# Problem C — Feedback Loop Isolation

Time limit: 2 s   Memory limit: 256 MB

A deep-space communication array consists of numerous relay stations, each assigned a unique integer identifier. To maintain data integrity, pairs of these stations establish dedicated, bidirectional quantum entanglement links. The architecture of this array is provided to you as a list of all active links between specific pairs of stations.

Due to a configuration anomaly, the network contains closed feedback loops. A critical feedback loop occurs whenever three distinct stations are completely interconnected—that is, each of the three stations shares a direct link with the other two. System diagnostics confirm that at least one such three-station configuration exists in the current network topology.

Your task is to isolate a source of the anomaly by identifying three stations that form a critical feedback loop. If there are multiple such configurations, you must report the lexicographically first one.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)), representing the number of relay stations and the number of active entanglement links, respectively. Stations are numbered from 1 to n.
Each of the following m lines contains two integers u and v, indicating that a bidirectional link exists between station u and station v.
It is guaranteed that at least one critical feedback loop exists.

## Output
Print three integers a, b, and c on a single line, separated by spaces, representing the identifiers of the three stations in a critical feedback loop.
The identifiers must be printed in ascending order (a < b < c).
To satisfy the lexicographical requirement, you must minimize a. If there are multiple valid loops with the same a, minimize b. If there are still ties, minimize c.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
