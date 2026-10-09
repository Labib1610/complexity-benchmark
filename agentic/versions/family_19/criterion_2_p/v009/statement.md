# Problem B — Single-Product Dispatch over a Corridor Grid

Time limit: 2 s   Memory limit: 256 MB

## Description
Consider a directed grid of hubs joined by one-way haulage lanes. Each lane carries a firm ceiling on the number of containers it can move per cycle, reflecting rolling stock that cannot be augmented mid-cycle. On every lane the number of containers assigned must be a non-negative whole number that does not exceed that lane's ceiling. At every hub other than a designated origin and destination, the product is conserved: the containers arriving equal the containers departing, so nothing accumulates or vanishes in transit. Empty repositioning, transit times, lane distances, and the order in which containers move are all outside the scope of this plan and must be ignored.

A distributor must move one product across this grid. A fixed quantity of the product, counted in whole containers, must travel from the single origin hub to the single destination hub during this one cycle. At the origin the net departure must equal the required quantity, and at the destination the net arrival must equal it. 

Produce a routing that delivers the full quantity from origin to destination within every lane's ceiling and respects the conservation at intermediate hubs, or report that this quantity cannot be delivered in a single cycle. (Planners sometimes reach for elaborate multi-product machinery here; with only one product to move, the shared-capacity contention that makes the general problem hard simply does not arise.)

## Input
Line 1: `n m 1` (where `n` is the number of hubs and `m` is the number of lanes).
Next line: `s t d` (origin hub, destination hub, and required quantity).
Next `m` lines: `u v cap` (a lane from hub `u` to hub `v` with ceiling `cap`).

## Output
`YES` on the first line, then a second line with `m` integers representing the flow on lane `j` (in the same order the lanes were given in the input); or `NO` if it is impossible.

## Example

**Input:**
```
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 5
```

**Output:**
```
YES
5 5 0 5 5
```
