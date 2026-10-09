# Problem B — Water Transfer over a Pipeline Network

Time limit: 2 s   Memory limit: 256 MB

## Description
A water authority must move water across a directed network of junctions joined by one-way pipelines. Each pipeline carries a firm ceiling on the number of megalitres it can move per hour, reflecting pipe diameters that cannot be augmented mid-hour. A fixed quantity of water, counted in whole megalitres, must travel from a single origin junction to a single destination junction during this one hour.

On every pipeline the number of megalitres assigned is a non-negative whole number that must not exceed that pipeline's ceiling. At every junction other than the origin and the destination the water is conserved: the megalitres arriving equal the megalitres departing, so nothing accumulates or vanishes in transit. At the origin the net departure equals the required quantity, and at the destination the net arrival equals it. Pressure drops, transit times, pipeline lengths, and the order in which megalitres move are all outside the scope of this plan and must be ignored — only the ceilings, the conservation at intermediate junctions, and the required end-to-end quantity bind the answer.

Produce a routing that delivers the full quantity from origin to destination within every pipeline's ceiling, or report that this quantity cannot be delivered in a single hour. (Engineers sometimes reach for elaborate multi-fluid machinery here; with only one fluid to move, the shared-capacity contention that makes the general problem hard simply does not arise.)

## Input
Line 1: `n m 1`. 
Next line: `s t d`. 
Next `m` lines: `u v cap`.

## Output
`YES` then one line with `m` integers — the flow on pipeline `j` (input order); or `NO`.

## Example

### Input
```text
4 5 1
1 4 10
1 2 10
1 3 5
2 3 15
2 4 5
3 4 10
```

### Output
```text
YES
5 5 0 5 5
```
