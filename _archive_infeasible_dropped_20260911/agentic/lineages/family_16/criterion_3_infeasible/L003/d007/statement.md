# Problem C — Impossible Ferry Loading

Time limit: 2 s   Memory limit: 256 MB

## Description

You are the loading master for a cargo ferry. The ferry has two parallel parking lanes, Lane 1 and Lane 2. Each lane has a usable parking length of exactly **T** meters, with coordinates running from $0$ to $T$.

There are **j** transport teams that need to board. Each team $i$ (for $1 \le i \le j$) consists of a primary vehicle of length $p_{i,1}$ meters and a secondary vehicle of length $p_{i,2}$ meters. 

A valid parking configuration must assign a continuous interval $[start, end]$ to every vehicle, satisfying all of the following rules:
- **Vehicle Length:** The length of the interval $end - start$ exactly equals the vehicle's length.
- **Lane Assignment:** All primary vehicles must be parked in Lane 1. All secondary vehicles must be parked in Lane 2.
- **Bounds:** Every vehicle's interval must be completely contained within the $0$ to $T$ coordinate bounds.
- **Non-overlapping:** Vehicles assigned to the same lane cannot overlap (their intervals can at most touch at the endpoints).
- **Team Ordering:** For every team $i$, the primary vehicle must be parked ahead of its secondary vehicle. Specifically, the end coordinate of team $i$'s primary vehicle must be less than or equal to the start coordinate of team $i$'s secondary vehicle.

For every test input, it is guaranteed that no valid parking configuration exists. Your task is to output a short certificate that proves the rules are contradictory. 

To do this, you must identify the fundamental bottleneck by finding which relaxed scenario is still impossible. For every test input, exactly one of the following relaxation scenarios is guaranteed to remain impossible. Print the certificate for the one that holds:

* `JOB i` (where **i** is a 1-based index, $1 \le i \le j$): The scenario remains impossible even if we suspend the Non-overlapping rule entirely, and suspend the Team Ordering rule for all teams except team **i**.
* `LOAD c` (where **c** is either 1 or 2): The scenario remains impossible even if we suspend the Team Ordering rule entirely, and suspend the Non-overlapping rule for the *other* lane (Lane 2 if **c** = 1, and Lane 1 if **c** = 2).

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing $p_{i,1}$ and $p_{i,2}$ respectively for team $i$.

## Output

Print a single line containing either `JOB i` (where **i** is a 1-based index, $1 \le i \le j$) or `LOAD c` (where **c** is either 1 or 2), corresponding to the unique relaxation scenario that remains impossible.

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

In Example 1, `JOB 1` is the correct certificate. If we suspend the non-overlapping rule for all vehicles, and waive the ordering rule for teams 2 and 3, we only need to satisfy the bounds for all vehicles and the ordering for team 1. However, team 1's primary vehicle and secondary vehicle must still be placed sequentially within the ferry's bounds, which is physically impossible given their lengths. Thus, the scenario remains impossible.
In Example 2, `LOAD 1` is the correct certificate. If we suspend the team ordering rule entirely and allow Lane 2 vehicles to overlap freely, we still must pack all four primary vehicles into Lane 1 without overlapping. This is impossible given the lane's capacity. Thus, the scenario remains impossible.