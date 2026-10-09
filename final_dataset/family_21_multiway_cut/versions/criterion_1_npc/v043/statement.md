# Problem A — Grid Synchronization Zoning

Time limit: 5 s
Memory limit: 256 MB

## Description
A regional power network is composed of $n$ substations connected by $m$ bidirectional transmission cables. Within this network, $k$ specific substations act as primary frequency sources. Each primary source generates its own distinct synchronization frequency. This frequency is present at the source and propagates freely to other substations through any sequence of cables that have not been equipped with filters.

If any single substation (including the sources themselves) is exposed to more than one distinct frequency, the colliding signals will trigger a cascading resonance failure. 

To prevent this, you can install signal-blocking filters on certain cables. When a filter is installed on a cable, it completely stops all frequencies from passing through that cable in either direction. Installing a filter on a cable between substation $u$ and substation $v$ incurs a specific hardware cost $w$. 

You are given a total hardware budget $B$. Your objective is to determine a set of cables to equip with filters such that no substation in the network is exposed to more than one distinct synchronization frequency. The total cost of the installed filters must not exceed $B$. If it is impossible to secure the network within the given budget, output `NO`.

## Input
The first line contains four integers $n$, $m$, $k$, and $B$.
The second line contains $k$ integers, the identifiers of the primary frequency sources (substations are numbered $1$ to $n$).
The next $m$ lines each contain three integers $u$, $v$, and $w$, indicating a transmission cable between substation $u$ and substation $v$ with a filter installation cost of $w$.

## Output
If a valid set of cables can be equipped with filters within the budget, output `YES` on the first line. On the second line, output an integer $c$, the number of cables equipped with filters. Then, output $c$ lines, each containing two integers $u$ and $v$ representing a cable equipped with a filter.
If it is impossible to achieve this within the budget, output `NO`.

## Example

**Input:**
```
5 6 3 11
1 3 5
1 2 4
2 3 5
2 4 3
3 5 4
4 5 2
1 4 6
```

**Output:**
```
YES
3
2 3
3 5
4 5
```
