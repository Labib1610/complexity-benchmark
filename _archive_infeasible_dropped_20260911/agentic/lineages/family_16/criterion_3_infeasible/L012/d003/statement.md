# Problem C — Impossible Window: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

You are evaluating a manufacturing process with $j$ custom projects. Each project requires assembly on the primary unit, and only after that is fully completed, testing on the secondary unit. A unit can process at most one project at any given moment.

The facility has a strict operating window of $T$ minutes. All projects must complete both assembly and testing within this window.

For every input, it is guaranteed that the operating window is too short to fulfill all projects, no matter how they are scheduled. Furthermore, exactly one of the following two operational constraints will serve as a proof of impossibility. Your task is to verify the projects and output the code for the proof that applies:

- `JOB i` (where $i$ is the 1-based index of a project): Even if project $i$ were granted exclusive access to the facility from the moment the window opens, it would still not finish its required sequence before the facility closes.
- `LOAD c` (where $c$ is 1 for the primary unit or 2 for the secondary unit): Even if we remove all dependencies between assembly and testing, and assume all projects are available to unit $c$ immediately, unit $c$ would still be running after the window ends just to complete its assigned tasks.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the duration in minutes for the project's assembly on the primary unit and its testing on the secondary unit, respectively.

## Output

Print a single line containing either `JOB i` (if project $i$'s sequence alone violates the window) or `LOAD c` (if unit $c$'s assigned tasks alone violate the window).

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

In Example 1, the first project requires 70 minutes on the primary unit and then 60 minutes on the secondary unit. It cannot complete its sequence within the 100-minute window, making `JOB 1` a valid proof of impossibility. 

In Example 2, no individual project violates the 150-minute window. However, the primary unit is assigned four assembly tasks of 50 minutes each. Since a unit operates on only one task at a time, it cannot complete its assigned tasks within the window, making `LOAD 1` the valid proof.