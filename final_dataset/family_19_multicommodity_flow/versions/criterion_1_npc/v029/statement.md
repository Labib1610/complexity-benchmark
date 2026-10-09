# Problem A — Concurrent Freight Dispatch over a Shared System

Time limit: 5 s   Memory limit: 256 MB

## Description
A national distributor operates a system of stations connected by one-way links. Each link has a strict limit on how many containers can traverse it per dispatch cycle, regardless of what is being carried; this limit reflects the link's rolling stock and cannot be exceeded.

In the current cycle there are several distinct item types to move. Each type has its own starting station, its own target station, and a firm amount — expressed in whole containers — that must be delivered in full during this single cycle. Crucially, all item types draw on the same links: a link's limit applies to the combined container count of every type routed over it, so types compete for the shared limit even though they are otherwise independent. Container counts are indivisible, so the number of containers of any given type sent along any given link is a non-negative whole number.

Containers are preserved at every station that is neither an item type's starting station nor its target station: for each type separately, the containers of that type entering an intermediate station must equal the containers of that type leaving it. At a type's starting station the outgoing minus the incoming containers of that type equals its required amount, and at its target station the incoming minus the outgoing equals that amount. Empty repositioning, transit times, and link distances are outside the scope of this plan and should be ignored; only the per-link limits, the per-type preservation, and the per-type delivery amounts matter.

Produce a dispatch plan that delivers every item type's full amount while respecting every link's shared limit, or determine that the system cannot carry all types together in one cycle. (Routing any single type alone may be trivial; the difficulty is that the types must coexist on the shared links.)

## Input
Line 1: three integers $n$, $m$, and $k$, representing the number of stations, links, and item types respectively. Stations are numbered $1$ to $n$.
Next $k$ lines: $s_i$ $t_i$ $d_i$, the starting station, target station, and required amount for item type $i$.
Next $m$ lines: $u$ $v$ $limit$, representing a directed link from $u$ to $v$ with the given limit.

## Output
`YES` on the first line, followed by $k$ lines, each containing $m$ integers — item type $i$'s container count on link $j$ (in the order the links were given in the input); or `NO` if no such plan is possible.

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
