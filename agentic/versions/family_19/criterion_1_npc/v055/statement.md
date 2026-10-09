# Problem A — Daily Rail Freight Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description
A rail operator manages a network of junctions connected by one-way track segments. To prevent track degradation, each segment has a strict daily limit on the total number of train cars it can handle. This limit applies to the sum of all cars traveling on that segment, regardless of which client owns them.

The operator serves multiple distinct corporate clients. Each client requires a specific number of train cars to be moved daily from their factory junction to their distribution junction. Train cars are indivisible discrete units, meaning the number of cars routed for any client on any segment must be a non-negative whole number.

At any junction that is neither a client's factory nor their distribution center, the number of cars arriving for that client must exactly equal the number of cars departing for that client. At a client's factory, the total outgoing cars minus any incoming cars for that client must exactly equal their contracted daily quota. At their distribution center, the incoming cars minus outgoing cars for that client must exactly equal the quota.

Determine if a routing schedule exists that fulfills all clients' daily quotas simultaneously without exceeding any track segment's total car limit.

## Input
Line 1: three integers $n$, $m$, and $k$, representing the number of junctions, track segments, and clients respectively. Junctions are numbered $1$ to $n$.
Next $k$ lines: $s_i$ $t_i$ $d_i$, the factory junction, distribution junction, and daily car quota for client $i$.
Next $m$ lines: $u$ $v$ $limit$, representing a one-way track segment from junction $u$ to junction $v$ with its daily capacity limit.

## Output
Output `YES` on the first line if a valid schedule is possible. Following this, output $k$ lines. The $i$-th line must contain $m$ integers representing the number of cars routed for client $i$ on each track segment, ordered exactly as the segments appeared in the input. If no schedule can fulfill all contracts within the track limits, output `NO`.

## Example
### Input
```text
4 5 2
1 4 1
2 3 1
1 2 1
1 3 1
2 3 1
2 4 1
3 4 1
```

### Output
```text
YES
0 1 0 0 1
0 0 1 0 0
```
