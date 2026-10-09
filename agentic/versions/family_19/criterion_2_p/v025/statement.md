# Problem B — Quantum State Routing in a Processor Cluster

Time limit: 2 s   Memory limit: 256 MB

## Description
A supercomputer cluster must transmit a specific volume of quantum state data across a directed network of processors connected by one-way optical channels. Each optical channel has a strict hardware ceiling on the number of data packets it can transmit per microsecond cycle. A fixed total volume of packets must be transmitted from a single origin processor to a single destination processor during one cycle.

For every channel, the number of packets assigned to it must be a non-negative integer that does not exceed that channel's ceiling. At every processor other than the origin and the destination, the packets must be perfectly conserved: the total number of packets arriving must exactly equal the total number of packets departing. At the origin processor, the net departure (packets sent minus packets received) must exactly equal the required total volume, and at the destination processor, the net arrival must exactly equal this same volume.

The cluster's topology is guaranteed by the manufacturer to satisfy two strict design rules:
- **Fan-out restriction:** For any given processor, the number of one-way channels originating from it is less than or equal to the total number of channels $m$ in the entire cluster.
- **Emission limit:** The sum of the ceilings of all channels directly leaving any single processor does not exceed the sum of the ceilings of all channels in the cluster combined.

Determine a valid assignment of packets to each channel that successfully transmits the exact required volume from the origin to the destination without violating any channel ceilings or conservation rules. If it is impossible to route the required volume in a single cycle, you must report this.

## Input
The first line provides three integers: $n$ (the number of processors), $m$ (the number of optical channels), and $1$. 
The second line provides three integers: $s$ (the origin processor), $t$ (the destination processor), and $d$ (the required total volume of packets).
The following $m$ lines each contain three integers $u$, $v$, and $cap$, representing a one-way optical channel from processor $u$ to processor $v$ with a ceiling of $cap$ packets per cycle.

## Output
If the transmission is possible, output `YES` on the first line, followed by a second line containing $m$ integers representing the number of packets assigned to each channel, in the exact order the channels were given in the input. If it is impossible, output `NO`.

## Example

**Input:**
```text
4 5 1
1 4 10
1 2 10
2 4 5
1 3 5
3 4 5
2 3 5
```

**Output:**
```text
YES
5 5 5 5 0
```
