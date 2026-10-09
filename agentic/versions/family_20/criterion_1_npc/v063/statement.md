# Problem A — Fiber-Optic Relay Calibration

Time limit: 5 s
Memory limit: 256 MB

## Description
A communications provider operates a fiber-optic relay network. The network consists of relay nodes connected by bidirectional fiber links. The network's architecture is strictly uniform: every single node in the network is directly connected to the exact same number of fiber links. 

To maintain signal integrity, the provider must schedule calibration phases for the links. The total number of distinct calibration phases available for the entire network is strictly limited to equal the number of links connected to any single node. 

During calibration, a link must be assigned to exactly one phase. To prevent routing failures, the system enforces a strict isolation policy: at any given relay node, no two of its connected links can undergo calibration during the same phase. Because the total number of phases exactly matches the number of connections at each node, this mandates that every link meeting at a given node must be assigned a completely different calibration phase. The physical length of the fibers, the routing protocols, and the technicians assigned are all irrelevant to the scheduling question — the only binding constraint is that links sharing a node never share a phase.

Assign each fiber link in the network to one of the available phases so that the isolation policy is satisfied, or determine that the available phases are provably insufficient for this network.

## Input
The first line contains two integers $n$ and $m$. The value $n$ represents the number of relay nodes, which is always an even number. The hardware addressing requires a minimum of two nodes and is capped at a maximum capacity of two thousand nodes. The value $m$ represents the total number of fiber links. Every link connects two endpoints; the network is provisioned such that the total count of these link endpoints across the entire network is exactly triple the number of relay nodes.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u < v \le n$), indicating that a fiber link connects node $u$ and node $v$.

## Output
If a valid phase assignment exists, print `YES`, followed by a line containing $m$ integers. Each integer must correspond to the calibration phase assigned to the link in the order they appear in the input. Phases are numbered sequentially starting from $1$ up to the total number of available phases. If no such assignment is possible, print `NO`.

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
