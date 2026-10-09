# Daily Freight Quota

Time limit: 2 s   Memory limit: 256 MB

## Description
A freight company manages a system of transit yards connected by one-way shipping corridors. Each corridor has a strict daily limit on the number of standard containers it can transport. 

The company must move a specific daily quota of identical containers from a designated manufacturing hub to a designated final port. Containers arriving at an intermediate yard can be sent immediately along any outgoing corridor. Because transit yards lack overnight storage, the total number of containers arriving at any intermediate yard must exactly equal the number departing that same day. 

The net number of containers leaving the manufacturing hub (departures minus arrivals) must exactly equal the daily quota. Similarly, the net number of containers arriving at the final port (arrivals minus departures) must exactly equal the daily quota. The number of containers sent through any corridor must be a non-negative integer that does not exceed its daily limit.

Determine a valid daily assignment of containers to each corridor that fulfills the entire quota, or conclude that the system cannot handle the required volume.

## Input
The first line contains three integers: $n$ (the number of transit yards), $m$ (the number of shipping corridors), and $1$ (the number of active contracts).
The second line contains three integers: $s$ (the manufacturing hub), $t$ (the final port), and $d$ (the daily quota).
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a one-way corridor from yard $u$ to yard $v$ capable of transporting up to $cap$ containers per day.

## Output
If the daily quota can be fulfilled, print `YES` on the first line. On the second line, print $m$ integers separated by spaces, representing the number of containers assigned to each corridor in the exact order the corridors were listed in the input. If the quota cannot be met, print `NO`.

### Example

**Input**
```text
4 5 1
1 4 10
1 2 10
2 4 5
1 3 5
3 4 5
2 3 5
```

**Output**
```text
YES
5 5 5 5 0
```
