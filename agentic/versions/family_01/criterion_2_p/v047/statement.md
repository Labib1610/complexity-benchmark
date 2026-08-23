# Problem B — Habitat Allocation

Time limit: 1 s
Memory limit: 256 MB

A space station is dividing its $n$ astronauts into two separate living quarters: Habitat 1 and Habitat 2. 

There are $m$ pairs of astronauts who require access to the same life-support calibration console. To ensure the console is always monitored but never overcrowded, any two astronauts who share a console must be placed in different habitats.

To comply with station safety protocols, the following capacity conditions are strictly enforced and guaranteed to hold for all scenarios:
- The total number of astronauts $n$ will not exceed $200,000$.
- The total number of console-sharing pairs $m$ will not exceed $200,000$.
- The sum, over all astronauts, of the number of console-sharing pairs they belong to, will never exceed $400,000$.
- No single astronaut belongs to more than $200,000$ console-sharing pairs.

Your task is to determine an allocation of each astronaut to either Habitat 1 or Habitat 2 that respects all console-sharing restrictions, or conclude that no such allocation is possible.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$, representing a pair of astronauts who share a console.

## Output
If it is impossible to satisfy all habitat restrictions, output a single line with `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $h_1, \dots, h_n$ (where each $h_i \in \{1, 2\}$) representing the habitat assigned to astronaut $i$. If multiple valid allocations exist, provide the one that is lexicographically smallest.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
