# Problem B — Fiber-Optic Vault Assignment for Sensor Networks

Time limit: 5 s   Memory limit: 256 MB

## Description
A pipeline requires a series of sensor nodes to be installed in a sequence of equally spaced underground vaults. Each vault can hold exactly one sensor node, and all vaults must be filled, mapping the nodes one-to-one into positions numbered sequentially along the pipeline.

The sensors communicate by passing data up a chain of command to a single master node. Each node, except the master, transmits to exactly one designated superior, forming a connected communication hierarchy that spans all nodes without any loops.

A dedicated fiber-optic strand must be laid between each sensor and its connected superior. The length of each strand is equal to the absolute difference between the vault position numbers of the two connected nodes. The physical routing details and the direction of data flow do not change this length. The installation project is limited by a strict total fiber-optic budget that must cover the sum of all strand lengths combined. There is no limit on the length of any individual strand, nor any limit on how many strands can pass through the same sections of the pipeline.

Determine an assignment of each sensor node to a unique vault such that the total length of all strands does not exceed the budget, or report that the budget cannot be met.

## Input
First line: three integers $n$, $m$, $B$. Each of the next $m$ lines: two integers $u$ $v$ — a communication link. 
(The network is a strict hierarchy: $m = n - 1$.)

## Output
Print `YES` then a line with $n$ integers — the assigned vault position ($1 \dots n$, a permutation) for nodes $1, 2, \dots, n$ respectively — such that the total strand length is $\le B$. Otherwise print `NO`.

## Example

**Input:**
```
5 4 6
1 2
1 3
3 4
3 5
```

**Output:**
```
YES
3 2 4 1 5
```
