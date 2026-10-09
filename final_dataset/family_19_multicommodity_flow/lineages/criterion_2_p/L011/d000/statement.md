# Problem B — Single-Product Dispatch over a Corridor Grid

Time limit: 2 s   Memory limit: 256 MB

## Description
A distributor must move one product across a directed grid of hubs joined by one-way haulage lanes. Each lane is serviced by a dedicated fleet of wagons, each capable of carrying exactly one container per cycle. A fixed quantity of the product, counted in whole containers, must travel from a single origin hub to a single destination hub during this one cycle.

On every lane the number of containers assigned is a non-negative whole number. Because each container requires exactly one wagon per cycle, the assignment must not require more wagons than the lane possesses. At every hub other than the origin and the destination the product is conserved: the containers arriving equal the containers departing, so nothing accumulates or vanishes in transit. At the origin the net departure equals the required quantity, and at the destination the net arrival equals it. Empty repositioning, transit times, lane distances, and the order in which containers move are all outside the scope of this plan and must be ignored — only the wagon counts, the conservation at intermediate hubs, and the required end-to-end quantity bind the answer.

Produce a routing that delivers the full quantity from origin to destination without requiring more wagons than are available on any lane, or report that this quantity cannot be delivered in a single cycle. (Planners sometimes reach for elaborate multi-product machinery here; with only one product to move, the shared-capacity contention that makes the general problem hard simply does not arise.)

## Input
Line 1: `n m 1`  
Next line: `s t d`  
Next `m` lines: `u v w`, where `w` is the number of wagons on the lane from `u` to `v`.

## Output
`YES` then one line with `m` integers — the number of containers assigned to link `j` (in input order); or `NO`.

## Example

**Input:**
```
4 5 1
1 4 10
1 2 10
1 3 10
2 4 5
3 4 5
2 3 5
```

**Output:**
```
YES
5 5 5 5 0
```
