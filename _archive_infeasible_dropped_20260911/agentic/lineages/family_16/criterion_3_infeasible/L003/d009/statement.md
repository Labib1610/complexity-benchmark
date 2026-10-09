# Problem C — Impossible Ferry Loading

Time limit: 2 s   Memory limit: 256 MB

## Description

You are the loading master for a cargo ferry. The ferry has two parallel parking lanes, Lane 1 and Lane 2. Each lane has a usable parking length of exactly **T** meters, with coordinates running from $0$ to $T$.

There are **j** transport teams that need to board. Each team $i$ (for $1 \le i \le j$) consists of a primary vehicle of length $p_{i,1}$ meters and a secondary vehicle of length $p_{i,2}$ meters. 

A valid parking configuration must assign a continuous coordinate interval to every vehicle, satisfying all of the following physical rules:
1. **Length:** The length of a vehicle's interval exactly equals its given length.
2. **Assignment:** All primary vehicles are assigned to Lane 1. All secondary vehicles are assigned to Lane 2.
3. **Bounds:** Every vehicle's interval must be completely contained within the $0$ to $T$ coordinate bounds.
4. **Non-overlapping:** Vehicles assigned to the same lane cannot overlap (their intervals can at most touch at the endpoints).
5. **Team Ordering:** For every team $i$, its primary vehicle must be parked ahead of its secondary vehicle (the primary vehicle's end coordinate must be less than or equal to the secondary vehicle's start coordinate).

For every test input, it is guaranteed that no valid parking configuration exists. Your task is to output a short certificate that proves the rules are contradictory. 

To do this, you must identify the fundamental bottleneck by finding a specific subset of these rules that is already impossible to satisfy on its own. Exactly one of the following isolated rule subsets is guaranteed to be contradictory (even when all other rules and vehicles are ignored). Print the certificate for the unique subset that fails:

* `JOB i` (where **i** is a 1-based index, $1 \le i \le j$): The subset consisting only of Rules 1, 2, 3, and 5, enforced exclusively on the vehicles of team $i$. (All other rules, and all other vehicles, are ignored).
* `LOAD c` (where **c** is either 1 or 2): The subset consisting only of Rules 1, 2, 3, and 4, enforced exclusively on the vehicles assigned to Lane $c$. (All other rules, and all vehicles assigned to the other lane, are ignored).

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing $p_{i,1}$ and $p_{i,2}$ respectively for team $i$.

## Output

Print a single line containing either `JOB i` (where **i** is a 1-based index, $1 \le i \le j$) or `LOAD c` (where **c** is either 1 or 2), corresponding to the unique rule subset that remains impossible.

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

In Example 1, `JOB 1` is the correct certificate. If we only enforce the Length, Assignment, Bounds, and Team Ordering rules for team 1, their primary and secondary vehicles must be placed sequentially within the $100$-meter bounds. This is physically impossible given their lengths.

In Example 2, `LOAD 1` is the correct certificate. If we only enforce the Length, Assignment, Bounds, and Non-overlapping rules for Lane 1, all four primary vehicles must be placed in Lane 1 without overlapping. This is impossible given the lane's $150$-meter capacity.