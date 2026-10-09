# Problem A — Steady-State Parcel Routing in an Automated Fulfillment Center

Time limit: 5 s   Memory limit: 256 MB

## Description
An automated fulfillment center operates under steady-state conditions, processing discrete parcels through a network of $n$ transfer stations connected by $m$ one-way chutes. 

Because all parcels share the exact same physical dimensions, the conveyor chutes treat them interchangeably. This uniformity means you only need to verify the aggregate parcel volume on any chute against a single structural limit, a property that guarantees a streamlined verification step. Furthermore, the required volume for each parcel category is fixed and perfectly balanced: exactly the number of parcels inducted into the system for a category will be fulfilled.

During a sorting cycle, the center must process $k$ specific categories of parcels. For each category, a precise target number of parcels must be routed from its designated induction station to its designated fulfillment station.

The routing must satisfy the following conditions:
- The number of parcels of any category assigned to any chute must be a non-negative integer.
- At any station that is not the induction or fulfillment point for a given category, the number of parcels of that category arriving must exactly equal the number of parcels of that category departing.
- At a category's induction station, the number of departing parcels of that category minus the arriving parcels of that category must equal its target number.
- At a category's fulfillment station, the number of arriving parcels of that category minus the departing parcels of that category must equal its target number.
- For any given chute, the sum of parcels across all $k$ categories routed through it cannot exceed its structural limit.

Determine if there is a valid routing configuration that successfully delivers the target number for all $k$ categories simultaneously without exceeding any chute's structural limit. 

## Input
The first line contains three integers $n$, $m$, and $k$ — the number of transfer stations (numbered $1$ to $n$), chutes, and parcel categories.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the induction station, fulfillment station, and target number of parcels for category $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a one-way chute from station $u$ to station $v$ with a structural limit of $cap$ parcels per cycle.

## Output
If a valid routing configuration is possible, print `YES` on the first line. Then print $k$ lines. The $i$-th of these lines should contain $m$ integers, representing the number of parcels of category $i$ routed through each of the $m$ chutes, in the exact order the chutes were given in the input. If no such configuration is possible, print `NO`.

## Example
**Input:**
```
4 5 2
1 4 10
3 2 10
1 2 10
1 3 10
3 2 10
2 4 10
3 4 10
```

**Output:**
```
YES
10 0 0 10 0
0 0 10 0 0
```
