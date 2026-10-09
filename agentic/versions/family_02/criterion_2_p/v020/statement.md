# Drone Fleet Battery Loadout

Time limit: 1 s
Memory limit: 256 MB

## Description
You manage a fleet of $n$ autonomous delivery drones. Before deployment, every drone must be fitted with exactly one of two battery types: a "Heavy-Lift" module (represented by 1) or a "Long-Range" module (represented by 0).

The flight control system enforces $m$ safety directives to ensure stable formation flying. Each directive specifies two acceptable battery assignments across the fleet, and mandates that at least one of these two assignments is physically implemented. An assignment condition is represented by a non-zero integer: a positive value $i$ indicates drone $i$ must receive a Heavy-Lift module, while a negative value $-i$ indicates drone $i$ must receive a Long-Range module.

Since each directive links exactly two acceptable states, choosing not to fulfill one condition strictly forces you to fulfill the other. You must determine if there is a single, fleet-wide battery loadout that successfully satisfies all $m$ directives simultaneously. If such a loadout exists, you must provide it. Otherwise, report that the directives are mutually contradictory.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($|l_i| \le n$), representing the two acceptable assignment conditions for that directive. At least one of the two conditions must be satisfied by your final loadout.

## Output
If no valid fleet-wide loadout exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$) representing the battery type for each drone from 1 to $n$.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid loadouts may exist; any loadout that satisfies all directives is accepted. The same drone index may appear in multiple directives.
