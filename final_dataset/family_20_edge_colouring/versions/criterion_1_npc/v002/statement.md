# Problem A — Frequency Allocation in the Server Cluster

Time limit: 5 s   Memory limit: 256 MB

## Description
A tech company operates a server cluster whose processing nodes are data endpoints. The cluster has been engineered so that **every** node is an endpoint of **exactly three** data links — the network is uniformly three-way at every node. Communication is organised into three distinct transmission frequencies, and operating a link always consumes one whole frequency.

Interference rules forbid overwhelming a node: at any endpoint, no two of its three links may be operated on the same frequency, because a node that receives two signals on the same frequency cannot maintain data integrity. Equivalently, the three links meeting at any node must be spread across three different frequencies. The physical link lengths, the materials, and which protocols are assigned are all irrelevant to the configuration question — the only thing that binds is that links sharing a node never share a frequency.

There are exactly three frequencies available and no more. Assign each link in the cluster one of the three frequencies so that at every node the three incident links occupy three distinct frequencies, or determine that three frequencies are provably insufficient for this cluster. (Having only three frequencies for a uniformly three-way cluster leaves no slack whatsoever — a single unavoidable clash makes the whole allocation impossible.)

## Input
The first line has two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000).
Each of the next **m** lines has two integers u v (1 ≤ u < v ≤ n): a data link between nodes u and v.

## Output
If an assignment exists, print `YES`, then a line with **m** integers in {1,2,3} — the frequency of link i in input order (adjacent links must differ). Otherwise print `NO`.

## Example
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
YES
1 2 3 3 2 1
```
