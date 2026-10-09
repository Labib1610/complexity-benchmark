# Problem B — Synchronizing Supply Routings

Time limit: 2 s   Memory limit: 256 MB

## Description
A logistics network coordinates shipments between a set of origin hubs and a set of destination nodes. A number of active cargo routes are established, where each route exclusively links one origin hub to one destination node. Internal routing (hub-to-hub or node-to-node) is structurally impossible within this network.

Each cargo route must be assigned a distinct operational phase. Operating a route consumes an entire phase. The strict safety protocol mandates that any single facility—whether it is an origin hub or a destination node—can only support one active route per phase. 

The bottleneck of the entire operation is the single facility that participates in the largest number of routes. If this most heavily utilized facility has $K$ routes connected to it, then the operation will inherently require at least $K$ phases to clear.

Your objective is to allocate a phase to every cargo route such that no facility is ever double-booked during any phase, and the total number of distinct phases used globally does not exceed $K$. The rules governing the connections guarantee that scheduling everything within exactly $K$ phases is always achievable without exception.

## Input
First line: three integers nL, nR, m (1 ≤ nL, nR ≤ 100000, 0 ≤ m ≤ 400000).
Next m lines: two integers u v (1 ≤ u ≤ nL, 1 ≤ v ≤ nR) representing a route linking origin hub u and destination node v.

## Output
Print `YES` on the first line.
On the second line, print m integers. The i-th integer represents the phase (an integer from 1 to K, where K is the maximum number of routes connected to any single facility) assigned to the i-th route in the input order. Routes sharing any facility must be assigned different phases.

## Example

### Input
```
3 4 5
1 1
1 2
2 2
2 3
3 4
```

### Output
```
YES
1 2 1 2 1
```
