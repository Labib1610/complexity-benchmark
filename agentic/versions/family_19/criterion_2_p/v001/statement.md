# Problem B — Single-Item Dispatch over a System of Locations

Time limit: 2 s   Memory limit: 256 MB

## Description
A distributor must move items across a system of locations joined by one-way haulage lanes. Each lane carries a firm ceiling on the number of containers it can move per cycle, reflecting rolling stock that cannot be augmented mid-cycle. A fixed quantity of items, counted in whole containers, must travel from a single starting location to a single ending location during this one cycle.

On every lane the number of containers assigned is a non-negative whole number that must not exceed that lane's ceiling. At every location other than the start and the end the amounts must balance: the containers arriving equal the containers departing, so nothing accumulates or vanishes in transit. At the start the net departure equals the required quantity, and at the end the net arrival equals it. Empty repositioning, transit times, lane distances, and the order in which containers move are all outside the scope of this plan and must be ignored — only the ceilings, the balancing at intermediate locations, and the required end-to-end quantity bind the answer.

Produce a plan that delivers the full quantity from start to end within every lane's ceiling, or report that this quantity cannot be delivered in a single cycle. (Planners sometimes reach for elaborate multi-item machinery here; with only one item type to move, the shared-ceiling contention that makes the general problem difficult simply does not arise.)

## Input
Line 1: n m 1. Next line: s t d. Next m lines: u v cap.

## Output
`YES` then one line with m integers — the amount assigned to connection j (input order); or `NO`.

## Example
### Input
```
4 5 1
1 4 10
1 2 10
2 3 5
1 3 5
3 4 10
2 4 5
```

### Output
```
YES
5 0 5 5 5
```
