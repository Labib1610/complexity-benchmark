# Problem C — Plasma Suspension Diagnostics

Time limit: 2 s
Memory limit: 256 MB

The diagnostic system of an experimental reactor monitors $n$ magnetic coils, numbered 1 through $n$. During calibration, sensors log $m$ unordered pairs of coils that exchange energy directly. 

A stable plasma suspension requires engaging exactly three distinct coils. For the suspension to hold, every coil in this chosen group must be able to exchange energy directly with both of the other two coils in the group. 

The control software must select one such group of three coils to activate. To ensure deterministic behavior, the system considers the coils within any valid group sorted in ascending order of their identifiers. It must select the group whose first coil has the lowest possible identifier. Among groups tied for the lowest first coil, it selects the one with the lowest second coil identifier. If still tied, it selects the one with the lowest third coil identifier. The calibration logs always contain at least one valid suspension group.

## Input
The first line provides the total number of coils $n$ and the number of logged pairs $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
The following $m$ lines each contain two integers $u$ and $v$, representing a pair of coils that exchange energy directly. 
No pair is logged more than once, and all pairs are unordered.

## Output
Output three integers on a single line, representing the identifiers of the selected coils in ascending order.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
