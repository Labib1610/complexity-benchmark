# Problem A — Aerial Swarm Navigation Through Restricted Airspace

Time limit: 5 s   Memory limit: 256 MB

## Description
An aerospace testing facility manages a system of hovering waypoints connected by one-way flight corridors. To guarantee collision avoidance, each corridor is rated with a strict safety ceiling, representing the absolute maximum number of drones that can fly through it during a single testing window. This ceiling is a hard physical limit on the combined traffic in that corridor.

During the upcoming testing window, multiple independent drone swarms must be deployed. Each swarm operates under a specific mission profile: it consists of a fixed number of indivisible drones that must be launched from a designated starting waypoint and safely navigated to a specific recovery waypoint. The facility requires that every single drone in every swarm completes its mission.

Waypoints themselves are merely navigational markers and cannot hold drones. Therefore, for any given swarm, the number of its drones arriving at an intermediate waypoint must exactly match the number of its drones departing from that waypoint. Drones from different swarms are programmed differently and cannot be interchanged, but they all share the same physical airspace. Consequently, the safety ceiling of any flight corridor applies to the combined total of all drones from all swarms that are directed through it.

You must determine if it is possible to direct all drones from all swarms simultaneously without exceeding the safety ceiling of any flight corridor. If it is possible, you must provide the flight paths for each swarm.

## Input
Line 1: Three integers $n$ (number of waypoints), $m$ (number of flight corridors), and $k$ (number of swarms).
Next $k$ lines: Three integers $s_i$ (launch waypoint), $t_i$ (recovery waypoint), and $d_i$ (number of drones) for swarm $i$.
Next $m$ lines: Three integers $u$, $v$, and $cap$, representing a one-way flight corridor from waypoint $u$ to waypoint $v$ with a safety ceiling of $cap$ drones.

## Output
If a safe flight configuration exists, print `YES` on the first line. Then print $k$ lines, each containing $m$ space-separated integers. The $j$-th integer on the $i$-th of these lines must be the number of drones from swarm $i$ directed through corridor $j$ (where corridors are indexed 1 to $m$ in the order they appear in the input).
If no such configuration is possible, print `NO`.

## Example

### Input
```
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
```
YES
0 1 0 0 1
0 0 1 0 0
```
