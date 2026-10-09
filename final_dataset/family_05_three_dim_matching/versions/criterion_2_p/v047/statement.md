# Orbital Deployment

Time limit: 2 s
Memory limit: 256 MB

## Description

An orbital commander must schedule an upcoming planetary defense operation requiring $k$ deployment assignments. The operation involves exactly $k$ pilots (identified by integers 1 through $k$), $k$ mechs (1 through $k$), and $k$ deployment phases (1 through $k$).

Each pilot is exclusively licensed to operate exactly one of the mechs, and no two pilots are licensed for the same mech. 

You are provided with a list of $t$ feasible tactical assignments. Each assignment is described by three integers $x$, $y$, and $z$, meaning that pilot $x$ is available to operate mech $y$ during phase $z$. Because of the strict licensing rules, all feasible assignments involving pilot $x$ will always specify the same mech $y$, and different pilots will always act on different mechs. No assignment is listed more than once.

Your task is to approve exactly $k$ assignments from this list so that every pilot, every mech, and every phase is utilized in exactly one approved assignment. As an additional requirement for orbital accounting, your chosen schedule must be such that the sum of the pilot IDs in the approved assignments is exactly $\frac{k(k+1)}{2}$, and the sum of the phase IDs is exactly $\frac{k(k+1)}{2}$. Determine if such an operation schedule can be formed, and if so, report one valid set of assignments.

## Input

The first line contains two integers $k$ and $t$ ($1 \le k \le 1200$, $0 \le t \le k \cdot k$): the number of pilots (which is also the number of mechs and phases) and the number of feasible assignments.

Each of the following $t$ lines contains three integers $x$, $y$, and $z$ ($1 \le x, y, z \le k$) representing a feasible assignment. The input guarantees that for any given pilot, every listed assignment features the exact same mech, and no two pilots share a mech. No assignment is listed more than once. 

Furthermore, the provided list of assignments is guaranteed to satisfy the following capacity bounds:
- For any individual pilot $x$, the sum of the phase IDs $z$ across all feasible assignments involving pilot $x$ will not exceed $\frac{k(k+1)}{2}$.
- For any individual phase $z$, the sum of the pilot IDs $x$ across all feasible assignments scheduled for phase $z$ will not exceed $\frac{k(k+1)}{2}$.

## Output

If a valid schedule of $k$ assignments exists, print `YES` on the first line. Then, print $k$ lines, each containing the three integers $x$ $y$ $z$ of one approved assignment. The assignments may be printed in any order. If multiple valid schedules exist, any of them will be accepted.

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
