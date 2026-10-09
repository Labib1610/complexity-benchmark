# Crew Assembly

Time limit: 2 s   Memory limit: 256 MB

## Description

A project manager must schedule an upcoming manufacturing run requiring $k$ work crews. The project has exactly $k$ specialists (identified by integers 1 through $k$), $k$ machines (1 through $k$), and $k$ available time slots (1 through $k$).

Each specialist is exclusively certified to operate exactly one of the machines, and no two specialists are certified on the same machine.

You are provided with a list of $t$ feasible crew configurations. Each configuration is described by three integers $x$, $y$, and $z$, meaning that specialist $x$ is available to operate machine $y$ during time slot $z$. Because of the strict certification rules, all feasible configurations involving specialist $x$ will always specify the same machine $y$, and different specialists will always act on different machines.

Your task is to approve exactly $k$ configurations from this list so that every specialist, every machine, and every time slot is utilized in exactly one approved configuration. Determine if such a schedule can be formed, and if so, report one valid set of configurations.

## Input

The first line contains two integers $k$ and $t$ ($1 \le k \le 1200$, $0 \le t \le k \cdot k$): the number of specialists (which is also the number of machines and time slots) and the number of feasible configurations.

Each of the following $t$ lines contains three integers $x$, $y$, and $z$ ($1 \le x, y, z \le k$) representing a feasible configuration. No configuration is listed more than once. The input guarantees that for any given specialist, every listed configuration features the exact same machine, and no two specialists share a machine.

## Output

If a valid schedule of $k$ configurations exists, print `YES` on the first line. Then, print $k$ lines, each containing the three integers $x$ $y$ $z$ of one approved configuration. The configurations may be printed in any order. If multiple valid schedules exist, any of them will be accepted.

If no such schedule is possible, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 2 1
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```
