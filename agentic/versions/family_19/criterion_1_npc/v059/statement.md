# Problem A — Cluster Migration Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description
A computing cluster consists of several processing units linked by one-way communication channels. Each channel can transmit up to a strictly defined maximum number of discrete data chunks per cycle. This hardware constraint restricts the combined volume of chunks passing through the channel, regardless of which operation they belong to.

In the current cycle, several independent data migration operations must be executed. Each operation requires moving a specific number of chunks from an origin unit to a target unit. All operations execute simultaneously and share the cluster's infrastructure, meaning the sum of chunks from all operations on any given channel cannot exceed that channel's transmission constraint. Chunks cannot be split; the volume of chunks assigned to any channel for any operation must be a non-negative whole number.

When chunks for a specific operation arrive at any unit that is neither its origin nor its target, they must be immediately forwarded: the count of incoming chunks for that operation must perfectly match its outgoing chunks. At the operation's origin, the number of outgoing chunks minus the number of incoming chunks must exactly equal its required total. At its target, the number of incoming chunks minus the number of outgoing chunks must exactly equal the same required total. Transit latency is not considered; only the channel constraints and the structural balance of each operation's chunks matter.

Determine a valid assignment of chunks to channels that fulfills every operation's requirement without violating any channel's transmission constraint, or report that the operations cannot be completed together in a single cycle.

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of processing units, communication channels, and migration operations, respectively.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the origin unit, target unit, and required number of chunks for operation $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a one-way channel from unit $u$ to unit $v$ with a transmission constraint of $cap$ chunks per cycle. All units are numbered from $1$ to $n$.

## Output
If a valid assignment exists, print `YES` on the first line. Then print $k$ lines, each containing $m$ integers. The $j$-th integer on the $i$-th line must represent the number of chunks for operation $i$ assigned to the $j$-th channel (in the order the channels were given in the input).
If no such assignment is possible, print `NO`.

## Example

### Input
```
4 5 2
1 4 2
2 3 1
1 2 2
1 3 2
2 3 1
3 4 2
2 4 2
```

### Output
```
YES
1 1 0 1 1
0 0 1 0 0
```
