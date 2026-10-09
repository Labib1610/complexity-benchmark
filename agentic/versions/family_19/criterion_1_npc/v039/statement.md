# Problem A — Data Center Packet Routing

Time limit: 5 s   Memory limit: 256 MB

## Description
A cloud computing provider routes data through a network of routers connected by unidirectional fiber-optic links. Each link has a strict bandwidth limit on the number of discrete data packets it can transmit per millisecond, regardless of the packets' contents; this limit is dictated by the link's hardware transceiver and cannot be exceeded.

In the current millisecond, several independent user tasks must transfer data. Each task has a specific source router, a specific destination router, and a firm payload size — expressed in whole packets — that must be delivered in full during this single millisecond. Crucially, all tasks share the network: a link's bandwidth limit applies to the sum of all packets from all tasks traversing it, so tasks compete for the shared capacity even though they are otherwise independent. Packets are indivisible, so the number of packets of any given task sent along any given link is a non-negative whole number.

Data is conserved at every router that is neither a task's source nor its destination: for each task separately, the number of its packets arriving at an intermediate router must exactly equal the number of its packets departing from it. At a task's source, the net outflow of its packets equals its required payload size, and at its destination, the net inflow equals that payload size. Latency, transit times, and link lengths are outside the scope of this configuration and should be ignored; only the per-link transceiver limits, the per-task packet conservation, and the per-task payload sizes matter.

Produce a routing configuration that delivers every task's full payload while respecting every link's shared bandwidth limit, or determine that the network cannot carry all tasks together in one millisecond. (Routing any single task alone may be trivial; the difficulty is that the tasks must coexist on the shared links.)

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of routers, links, and user tasks, respectively.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the source router, destination router, and required payload size (in packets) for task $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a unidirectional link from router $u$ to router $v$ with a bandwidth limit of $cap$ packets per millisecond. All routers are numbered from $1$ to $n$.

## Output
If a valid routing configuration exists, print `YES` on the first line. Then print $k$ lines, each containing $m$ integers. The $j$-th integer on the $i$-th line must represent the number of packets for task $i$ routed over the $j$-th link (in the order the links were given in the input).
If no such configuration is possible, print `NO`.

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
