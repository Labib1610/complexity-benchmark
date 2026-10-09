# Problem B — Spectrum Allocation for a Relay Network

Time limit: 5 s   Memory limit: 256 MB

## Description
A tactical communication network consists of $n$ radio outposts that must each be assigned a distinct operating frequency from a contiguous block of $n$ available channels, numbered 1 to $n$.

The network's connections are established incrementally: it begins with a single active outpost. Each subsequent outpost joins the network by forming exactly one dedicated data link with an outpost that is already active. This setup guarantees that any two outposts can exchange messages via a unique sequence of data links.

For any data link connecting two outposts, its separation penalty is the absolute difference between their assigned channel numbers. The system has a maximum total tolerance, $B$, for the sum of the separation penalties across all data links. There is no limit on individual links, only on the overall sum.

Determine a one-to-one assignment of outposts to channels such that the total separation penalty is at most $B$, or report that this is impossible. (The incremental way the network is built produces a very specific shape of connections, but the goal of keeping the total penalty within the tolerance remains.)

## Input
First line: three integers $n$, $m$, $B$. 
Each of the next $m$ lines: two integers $u$ $v$ — representing a data link between outpost $u$ and outpost $v$.
(As per the network's formation rules, $m = n-1$.)

## Output
Print `YES` then a line with $n$ integers — the channel number ($1 \dots n$, a permutation) assigned to outpost $1, 2, \dots, n$ — such that the total separation penalty is $\le B$. Otherwise print `NO`.

## Example

### Input
```
3 2 2
1 2
1 3
```

### Output
```
YES
2 1 3
```
