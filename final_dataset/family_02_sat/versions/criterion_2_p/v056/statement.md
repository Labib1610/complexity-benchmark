# Drone Fleet Battery Loadout

Time limit: 1 s
Memory limit: 256 MB

## Description
You oversee a fleet of $n$ autonomous delivery drones. Prior to launch, you must equip each drone with exactly one of two power modules: a Heavy-Lift unit (coded as 1) or a Long-Range unit (coded as 0).

To maintain formation stability, the flight control software imposes $m$ safety directives. Every directive provides two acceptable configuration states, and dictates that your final fleet setup must satisfy at least one of them. A configuration state is given as a non-zero integer: a positive integer $i$ means drone $i$ requires a Heavy-Lift unit, whereas a negative integer $-i$ means drone $i$ requires a Long-Range unit.

Because every directive pairs exactly two acceptable states, failing to meet one state strictly obligates you to meet the other. Your task is to determine whether a single, comprehensive battery loadout exists that simultaneously complies with all $m$ directives. If a valid configuration is possible, you must output it. If no such configuration can exist, you must declare that the directives are mutually contradictory.

Additionally, the flight control system guarantees the following structural properties for all valid sets of directives:
- **Locality**: For any given directive, the absolute difference between the drone numbers (from 1 to $n$) of the two referenced drones is strictly less than $n$.
- **Bounded Sum**: The sum of the drone numbers of the two referenced drones in any directive is at most $2n$.
- **Conservation**: The final loadout must deploy exactly $n$ power modules in total (meaning every drone receives exactly one module, with no restrictions on the ratio of Heavy-Lift to Long-Range units).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($|l_i| \le n$), representing the two acceptable configuration states for that directive. At least one of these two states must be satisfied by your loadout.

## Output
If no valid fleet-wide loadout can be found, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$), representing the power module assigned to each drone from 1 to $n$.

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
