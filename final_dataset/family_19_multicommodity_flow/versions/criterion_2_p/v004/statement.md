# Problem B — Container Dispatch over a Corridor Grid

Time limit: 2 s   Memory limit: 256 MB

## Description
A distributor must determine container assignments across a directed grid of hubs joined by one-way haulage lanes. The state space of possible allocations is vast, as each lane can independently take any non-negative integer up to a firm ceiling of containers it can move per cycle. A fixed overall quantity, counted in whole containers, must travel from a single origin hub to a single destination hub during this one cycle. All containers are of a single indistinguishable product.

On every lane the number of containers assigned is a non-negative whole number that must not exceed that lane's ceiling. At every hub other than the origin and the destination the product is conserved: the containers arriving equal the containers departing, so nothing accumulates or vanishes in transit. At the origin the net departure equals the required quantity, and at the destination the net arrival equals it. Empty repositioning, transit times, lane distances, and the order in which containers move are all outside the scope of this plan and must be ignored — only the ceilings, the conservation at intermediate hubs, and the required end-to-end quantity bind the answer.

Produce an assignment combination that delivers the full quantity from origin to destination within every lane's ceiling, or report that this quantity cannot be delivered in a single cycle. 

## Input
Line 1: `n m 1`. Next line: `s t d`. Next `m` lines: `u v cap`.

## Output
`YES` then one line with `m` integers — the flow on link `j` (input order); or `NO`.

## Example

**Input:**
```
4 5 1
1 4 10
1 2 5
1 3 6
2 4 5
3 4 6
2 3 2
```

**Output:**
```
YES
5 5 5 5 0
```
