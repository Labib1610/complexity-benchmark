# Problem C — Impossible Ferry Loading

Time limit: 2 s   Memory limit: 256 MB

## Description

You are the loading master for a cargo ferry. The ferry has two parallel parking lanes, Lane 1 and Lane 2. Each lane has a usable parking length of exactly **T** meters, with coordinates running from $0$ to $T$.

There are **j** transport teams that need to board. Each team $i$ (for $1 \le i \le j$) consists of a primary vehicle of length $p_{i,1}$ meters and a secondary vehicle of length $p_{i,2}$ meters. 

A valid parking configuration must assign a continuous interval $[start, end]$ to every vehicle, satisfying all of the following physical rules:
- **Vehicle Length:** The length of the interval $end - start$ exactly equals the vehicle's length.
- **Lane Assignment:** All primary vehicles must be parked in Lane 1. All secondary vehicles must be parked in Lane 2.
- **Bounds:** Every vehicle's interval must be completely contained within the $0$ to $T$ coordinate bounds.
- **Non-overlapping:** Vehicles parked in the same lane cannot overlap (their intervals can at most touch at the endpoints).
- **Team Ordering:** For every team $i$, the primary vehicle must be parked ahead of its secondary vehicle. Specifically, the end coordinate of team $i$'s primary vehicle must be less than or equal to the start coordinate of team $i$'s secondary vehicle.

For every test input, it is guaranteed that no valid parking configuration exists. Your task is to output a short certificate that proves the rules are contradictory. 

To do this, you must identify the fundamental bottleneck by finding which of the following relaxed geometric scenarios is still impossible to pack. In a relaxed scenario, we evaluate if the vehicles can be assigned coordinate intervals within the $0$ to $T$ bounds under modified interaction rules. Exactly one of these scenarios is guaranteed to remain impossible. Print the certificate for the one that holds:

* `JOB i` (where **i** is a 1-based index, $1 \le i \le j$): The "Team $i$ Isolation". In this scenario, vehicles are permitted to overlap their intervals freely, provided they belong to different teams. Furthermore, for any team $k \neq i$, its primary and secondary vehicles are also permitted to overlap or be placed in any sequence. However, for team $i$, its primary and secondary vehicles must not overlap, and team $i$'s primary vehicle must be placed completely ahead of its secondary vehicle.
* `LOAD c` (where **c** is either 1 or 2): The "Lane $c$ Isolation". In this scenario, the Team Ordering rule is completely dissolved, and any vehicle originally assigned to Lane $3-c$ is permitted to overlap freely with any other vehicle. However, all vehicles originally assigned to Lane $c$ retain their mutual collision physics, meaning no two vehicles from Lane $c$ may overlap their intervals with each other.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing $p_{i,1}$ and $p_{i,2}$ respectively for team $i$.

## Output

Print a single line containing either `JOB i` (where **i** is a 1-based index, $1 \le i \le j$) or `LOAD c` (where **c** is either 1 or 2), corresponding to the unique relaxed scenario that remains impossible.

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, `JOB 1` is the correct certificate. Under the Team 1 Isolation scenario, vehicles from different teams may overlap freely, and teams 2 and 3 may overlap their own vehicles. We only need to satisfy the bounds for all vehicles and the strict sequential ordering for team 1. However, team 1's primary vehicle and secondary vehicle must still be placed sequentially without overlapping within the $100$-meter bounds, which is physically impossible given their lengths. Thus, this geometry remains impossible.

In Example 2, `LOAD 1` is the correct certificate. Under the Lane 1 Isolation scenario, the team ordering rule is dissolved and Lane 2 vehicles may overlap freely. However, we still must pack all four primary vehicles into Lane 1 such that no two overlap. This is impossible given the lane's $150$-meter capacity. Thus, this geometry remains impossible.