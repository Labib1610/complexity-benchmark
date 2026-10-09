# Problem B — Cargo Quota Fulfillment

Time limit: 2 s   Memory limit: 256 MB

## Description
A distribution infrastructure is built from a set of checkpoints connected by one-way freight routes. Each route has a strict upper limit on the number of cargo units it can carry per operational period. The number of units assigned to any route must be a non-negative whole number no greater than this limit.

Units cannot be stored or broken down at the checkpoints. Therefore, at any checkpoint—aside from the initial and final ones—the total number of units arriving via inbound routes must be exactly equal to the total number of units leaving via outbound routes.

The system must fulfill a specific mandate. A designated initial checkpoint must send out a net quantity (total leaving minus total arriving) of exactly $d$ units. Simultaneously, a designated final checkpoint must receive a net quantity (total arriving minus total leaving) of exactly $d$ units. You do not need to consider how the units maneuver over time; only the aggregated totals per route are required.

Determine a valid assignment of cargo units to each route that respects all route limits and checkpoint requirements while successfully transferring the target quantity in one period. If no such assignment is possible, report that the mandate cannot be fulfilled.

## Input
The first line contains three integers: $n$ (the number of checkpoints), $m$ (the number of routes), and the number 1 (a constant representing a single cargo category).
The second line contains three integers: $s$ (the initial checkpoint), $t$ (the final checkpoint), and $d$ (the target quantity).
The next $m$ lines each contain three integers $u$, $v$, and $c$, representing a one-way route from checkpoint $u$ to checkpoint $v$ with an upper limit of $c$ units. Checkpoints are numbered from 1 to $n$.

## Output
If the mandate can be fulfilled, print `YES` on the first line. On the second line, print $m$ integers separated by spaces, representing the number of units assigned to each route in the exact order they appeared in the input. If multiple valid assignments exist, any assignment satisfying all conditions is accepted.
If the mandate cannot be fulfilled, print `NO`.

## Example

**Input:**
```
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 10
```

**Output:**
```
YES
5 5 0 5 5
```
