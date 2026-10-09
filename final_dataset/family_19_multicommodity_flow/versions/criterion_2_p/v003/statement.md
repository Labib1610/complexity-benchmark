# Problem B — Single-Product Dispatch over a Corridor System

Time limit: 2 s
Memory limit: 256 MB

## Description
A distributor must move one product across a system of hubs joined by one-way haulage lanes. Each lane carries a firm ceiling on the number of containers it can move per cycle, reflecting rolling stock that cannot be augmented mid-cycle. A fixed quantity of the product, counted in whole containers, must travel from a single origin hub to a single destination hub during this one cycle.

On every lane the number of containers assigned is a non-negative whole number that must not exceed that lane's ceiling. At every hub other than the origin and the destination the product is conserved: the containers arriving equal the containers departing, so nothing accumulates or vanishes in transit. At the origin the net departure equals the required quantity, and at the destination the net arrival equals it. Empty repositioning, transit times, lane distances, and the order in which containers move are all outside the scope of this plan and must be ignored — only the ceilings, the conservation at intermediate hubs, and the required end-to-end quantity bind the answer.

Produce a routing that delivers the full quantity from origin to destination within every lane's ceiling, or report that this quantity cannot be delivered in a single cycle.

## Input
Line 1: Three integers $n$, $m$, and $1$ (representing the number of hubs, the number of lanes, and the single product type).
Line 2: Three integers $s$, $t$, and $d$ (the origin hub, the destination hub, and the required quantity of containers).
Next $m$ lines: Three integers $u$, $v$, and $cap$, indicating a one-way lane from hub $u$ to hub $v$ with a ceiling of $cap$ containers. Hubs are numbered from $1$ to $n$.

## Output
If the delivery is possible, print `YES` on the first line, followed by a second line containing $m$ integers representing the number of containers assigned to each lane, in the order the lanes were given in the input. If it is impossible, print `NO`.

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
