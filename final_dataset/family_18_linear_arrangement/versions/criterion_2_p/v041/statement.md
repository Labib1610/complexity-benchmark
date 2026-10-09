# Track Lighting Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description
A lighting designer is installing $n$ smart bulbs into $n$ distinct sockets positioned along a straight track. The sockets are spaced evenly and numbered $1$ through $n$ from left to right. Each bulb must be placed into exactly one socket, with no sockets left empty.

The bulbs must be linked by $m$ synchronization wires. Each wire links a specific pair of bulbs. The wiring plan ensures that all bulbs operate as a single coordinated system: one bulb serves as the primary controller, and every other bulb has a direct wire linking it to exactly one upstream bulb, meaning all bulbs are integrated into a single unified system with no circular wiring routes.

The signal degradation on a wire depends on the physical distance it must span. If a wire links a bulb placed in socket $x$ and a bulb placed in socket $y$, the signal degradation for that wire is the absolute difference between $x$ and $y$. The system's power supply can tolerate a total combined signal degradation of at most $B$ across all wires. This limit applies only to the total sum; there is no restriction on the degradation of any individual wire.

Determine an assignment of bulbs to sockets such that the total signal degradation does not exceed the limit $B$, or state that no such assignment is possible.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that a synchronization wire must link bulb $u$ and bulb $v$.
(The wiring plan guarantees that $m = n - 1$.)

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ integers separated by spaces, where the $i$-th integer represents the socket number ($1$ to $n$, forming a permutation) assigned to bulb $i$. If there are multiple valid assignments, any one is acceptable.
If no valid assignment exists, print `NO`.

## Example

### Input
```
5 4 5
1 2
1 3
3 4
3 5
```

### Output
```
YES
2 1 3 5 4
```
