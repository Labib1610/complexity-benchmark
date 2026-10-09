# Establishing the Secure Comm-Link

Time limit: 2 s   Memory limit: 256 MB

## Description

An orbital command manages $n$ outposts. Certain pairs of outposts can be bridged by a secure comm-link, which requires a specific energy cost to activate. Among the outposts, exactly $t$ are designated as **primary command hubs**. You must activate a subset of the available comm-links so that all primary command hubs can synchronize data with each other (either directly or by relaying through other outposts, which do not need to be primary hubs themselves).

Due to the sector's strict non-redundant terrain architecture, the available comm-links connect all outposts such that there are exactly $n - 1$ possible comm-links in total. Furthermore, if all available comm-links were activated, between any two outposts there would be exactly one possible route of comm-links.

Your objective is to activate a set of comm-links that minimizes the total energy cost while ensuring all primary command hubs are interconnected. Output this minimum total energy cost.

## Input

The first line of the manifest contains three integers: $n$, $m$, and $t$.
- $n$ is the total number of outposts. The network contains at least 1 outpost and is bounded by the sector's maximum capacity of 200000.
- $m$ is the number of available comm-links, which is exactly $n - 1$.
- $t$ is the number of primary command hubs, which is at least 1 and at most $n$.

The second line contains $t$ distinct integers: the identifiers of the primary command hubs.

Each of the next $m$ lines details a possible comm-link with three integers: $u$, $v$, and $w$.
- $u$ and $v$ are distinct outpost identifiers (from 1 to $n$) that can be connected.
- $w$ is the energy cost to activate this link. This cost is a positive integer bounded by the hardware safety threshold of 1000000.

The available comm-links strictly follow the terrain architecture described above.

## Output

Print a single integer: the minimum total energy cost required to interconnect all primary command hubs.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```

## Note

In Example 1, the primary command hubs 1 and 4 can only synchronize data by relaying through outposts 2 and 3, so all three comm-links (5 + 1 + 2 = 8) must be activated. In Example 2, there is only one primary command hub, so no comm-links need to be activated.