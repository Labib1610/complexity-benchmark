# Problem A — Concurrent Parcel Distribution over a Shared Conveyor System

Time limit: 5 s
Memory limit: 256 MB

## Description
A sorting facility consists of several processing desks linked by one-way conveyor belts. Each belt is rated for a strict physical limit on how many parcels it can carry during a single shift. This limit applies to the combined physical count of all parcels on that belt, regardless of which order they belong to.

In the current shift, there are several distinct orders to fulfill. Each order requires a specific number of identical parcels to be moved from a designated starting desk to a designated final desk. All orders must be processed simultaneously during the same shift. Because all parcels from all orders share the same belts, the total number of parcels on any single belt cannot exceed that belt's physical limit. Parcels are indivisible whole units, meaning any belt carries zero or more whole parcels for any given order.

Parcels cannot be dismantled, stored at desks, or lost. For any given order:
* At its starting desk, the number of its parcels sent out onto belts minus the number of its parcels received from belts must exactly equal its required amount.
* At its final desk, the number of its parcels received from belts minus the number sent out onto belts must exactly equal its required amount.
* At all other desks, the number of its parcels received must exactly equal the number sent out.

Determine a distribution plan that fulfills all orders without exceeding any belt's limit, or state if it is impossible. (Fulfilling any single order alone might be trivial; the challenge is that all orders must coexist on the shared belts.)

## Input
The first line contains three integers: the number of processing desks $n$, the number of one-way belts $m$, and the number of orders $k$.
The next $k$ lines detail the orders. Each line provides three integers: the starting desk $s_i$, the final desk $t_i$, and the required parcel count $d_i$.
The next $m$ lines detail the belts. Each line provides three integers: the desk where the belt starts $u$, the desk where it ends $v$, and its maximum parcel limit $cap$.

## Output
If a valid distribution plan exists, print `YES`. Then, print $k$ lines, one for each order in the sequence they were given in the input. On each line, print $m$ space-separated integers representing the number of parcels of that order placed on each of the $m$ belts, in the sequence the belts were given.
If no such plan exists, print `NO`.

## Example

**Input**
```text
4 4 2
1 4 1
2 3 1
1 2 1
2 4 1
2 3 1
3 4 1
```

**Output**
```text
YES
1 1 0 0
0 0 1 0
```
