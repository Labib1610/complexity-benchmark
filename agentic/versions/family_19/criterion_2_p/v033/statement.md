# Problem B — Container Dispatch over a Corridor Grid

Time limit: 2 s   Memory limit: 256 MB

## Description
A distributor must move identical containers across a directed grid of hubs joined by one-way haulage lanes. Each lane carries a firm ceiling on the number of containers it can move per cycle, reflecting rolling stock that cannot be augmented mid-cycle. A fixed quantity of these containers must travel from a single origin hub to a single destination hub during this one cycle.

On every lane the number of containers assigned is a non-negative whole number that must not exceed that lane's ceiling. At every hub other than the origin and the destination the containers are conserved: the number arriving equals the number departing, so nothing accumulates or vanishes in transit. At the origin the net departure equals the required quantity, and at the destination the net arrival equals it. Empty repositioning, transit times, lane distances, and the order in which containers move are all outside the scope of this plan and must be ignored — only the ceilings, the conservation at intermediate hubs, and the required end-to-end quantity bind the answer.

Produce a routing that delivers the full quantity from origin to destination within every lane's ceiling, or report that this quantity cannot be delivered in a single cycle.

## Input
Line 1: `n` `m` `1`.
Next line: `s` `t` `d`.
Next `m` lines: `u` `v` `cap`.

## Output
`YES` then one line with `m` integers — the containers assigned to link `j` (in input order); or `NO`.

## Example
**Input**
```text
4 5 1
1 4 3
1 2 2
1 3 2
2 3 1
2 4 1
3 4 2
```

**Output**
```text
YES
2 1 1 1 2
```
