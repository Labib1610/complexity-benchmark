# Problem A — Pneumatic Routing Module

Time limit: 5 s
Memory limit: 256 MB

## Description
The factory's production scheduler has just completed the hourly forecast, identifying several independent material orders that must be fulfilled simultaneously. Your software module is the second stage of the pipeline: taking these scheduled orders and mapping them onto the factory's physical infrastructure. Once your module outputs a valid assignment, the downstream valve-control system will physically execute the transfers.

The factory infrastructure consists of a set of vats connected by one-way pneumatic tubes. Each tube has a strict structural limit on the total number of indivisible capsules it can transport within the hour. This limit applies to the combined sum of all capsules using the tube, regardless of which order they belong to. The number of capsules assigned to any tube must be a non-negative integer.

For the current hour, there are $k$ scheduled orders. Each order specifies an origin vat, a destination vat, and an exact number of capsules that must be delivered. Because all orders are processed simultaneously, they must share the same tube infrastructure and compete for the available structural limits.

Your assignment must satisfy transit continuity for each order individually. At any vat that is neither the origin nor the destination for a specific order, the number of capsules for that order arriving through incoming tubes must exactly equal the number departing through outgoing tubes. For an order's origin vat, the total number of its capsules departing through outgoing tubes minus the number arriving through incoming tubes must exactly equal the required delivery amount. Conversely, at an order's destination vat, the total arriving minus the total departing must equal the required amount.

Determine if there is a valid assignment of capsules to tubes that fulfills all orders without exceeding any tube's structural limit. If such an assignment exists, output it so the valve-control system can proceed. Otherwise, report that the schedule cannot be executed.

## Input
The first line contains three integers $n$, $m$, and $k$: the number of vats, the number of pneumatic tubes, and the number of scheduled orders.
The next $k$ lines specify the orders. The $i$-th of these lines contains three integers $s_i$, $t_i$, and $d_i$, representing the origin vat, the destination vat, and the required number of capsules for order $i$.
The next $m$ lines describe the factory infrastructure. The $j$-th of these lines contains three integers $u$, $v$, and $cap$, indicating a one-way pneumatic tube from vat $u$ to vat $v$ with a structural limit of $cap$ capsules.

## Output
If the scheduled orders can be fulfilled simultaneously, print `YES` on the first line. Then, print $k$ lines, each containing $m$ integers. The $j$-th integer on the $i$-th line must be the number of capsules from order $i$ assigned to the $j$-th tube (in the exact order the tubes were provided in the input).
If no such assignment is possible, print `NO`.

## Example

### Input
```text
4 5 2
1 4 2
2 3 1
1 2 2
1 3 2
2 4 2
3 4 2
2 3 1
```

### Output
```text
YES
1 1 1 1 0
0 0 0 0 1
```
