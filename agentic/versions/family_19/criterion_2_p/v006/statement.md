# Problem B — Freight Forwarding over a Rail Network

Time limit: 2 s   Memory limit: 256 MB

## Description
A freight forwarder must move a single type of cargo across a network of sorting facilities joined by one-way rail links. Each link carries a firm ceiling on the number of railcars it can move per day, reflecting locomotive availability that cannot be exceeded. A fixed quantity of cargo, counted in whole railcars, must travel from a single origin facility to a single destination facility during this one day.

On every link, the number of railcars assigned is a non-negative whole number that must not exceed that link's ceiling. At every facility other than the origin and the destination, the railcars are strictly conserved: the number arriving equals the number departing, because intermediate facilities lack overnight storage capacity. At the origin, the net departure equals the required total quantity, and at the destination, the net arrival equals it. Empty repositioning, transit times, link distances, and the order in which railcars move are all outside the scope of this plan and must be ignored — only the ceilings, the conservation at intermediate facilities, and the required end-to-end quantity bind the answer.

Produce a routing that delivers the full quantity from origin to destination within every link's ceiling, or report that this quantity cannot be delivered in a single day.

## Input
Line 1: $n$ (number of facilities), $m$ (number of links), and the number $1$.
Next line: $s$ (origin facility), $t$ (destination facility), and $d$ (required quantity).
Next $m$ lines: $u$ (source facility), $v$ (target facility), and $cap$ (ceiling capacity).

## Output
`YES` followed by one line with $m$ integers — the number of railcars assigned to link $j$ (in input order); or `NO`.

## Example

### Input
```
4 5 1
1 4 3
1 2 2
1 3 2
2 3 1
2 4 1
3 4 2
```

### Output
```
YES
2 1 1 1 2
```
