# Problem B — Single-Stream Routing over a Network Grid

Time limit: 2 s   Memory limit: 256 MB

## Description
A network operator must transmit one data stream across a directed grid of routers joined by one-way fiber links. Each link carries a firm ceiling on the number of packets it can transmit per millisecond, reflecting bandwidth limits that cannot be augmented mid-cycle. A fixed quantity of the data stream, counted in whole packets, must travel from a single origin router to a single destination router during this one millisecond.

On every link the number of packets assigned is a non-negative whole number that must not exceed that link's ceiling. At every router other than the origin and the destination the data is conserved: the packets arriving equal the packets departing, so nothing accumulates or vanishes in transit. At the origin the net departure equals the required quantity, and at the destination the net arrival equals it. Acknowledgement packets, transit times, link distances, and the order in which packets move are all outside the scope of this plan and must be ignored — only the ceilings, the conservation at intermediate routers, and the required end-to-end quantity bind the answer.

Produce a routing that delivers the full quantity from origin to destination within every link's ceiling, or report that this quantity cannot be delivered in a single millisecond. (Engineers sometimes reach for elaborate multi-stream machinery here; with only one stream to route, the shared-capacity contention that makes the general problem hard simply does not arise.)

## Input
Line 1: n m 1. Next line: s t d. Next m lines: u v cap.

## Output
`YES` then one line with m integers — the packet count on link j (input order); or `NO`.

## Example

### Input
```
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 10
```

### Output
```
YES
5 5 0 5 5
```
