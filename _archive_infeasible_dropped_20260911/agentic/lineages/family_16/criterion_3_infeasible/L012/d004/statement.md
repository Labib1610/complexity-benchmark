# Problem C — Impossible Window: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

You are evaluating a manufacturing process with $j$ custom projects. Each project requires assembly on the primary unit for a specified duration, and testing on the secondary unit for a specified duration. 

A schedule assigns each task to a continuous time interval. A valid schedule must satisfy four conditions:
1. **Precedence**: For each project, its secondary unit testing interval must start at or after the moment its primary unit assembly interval ends.
2. **Capacity 1**: No two primary unit assembly intervals may overlap in time.
3. **Capacity 2**: No two secondary unit testing intervals may overlap in time.
4. **Deadline**: All intervals must be entirely contained within the strict operating window of $[0, T]$ minutes.

For every input, it is guaranteed that the operating window is too short to fulfill all projects, no matter how they are scheduled. Furthermore, exactly one of the following two operational constraints will serve as a proof of impossibility. Your task is to verify the projects and output the code for the proof that applies:

- `JOB i` (where $i$ is the 1-based index of a project): This proof applies if the relaxed system consisting solely of **Precedence** for project $i$ and **Deadline** for project $i$'s two tasks is logically unsatisfiable on its own.
- `LOAD c` (where $c$ is 1 for the primary unit or 2 for the secondary unit): This proof applies if the relaxed system consisting solely of **Capacity c** and **Deadline** for all $j$ tasks assigned to unit $c$ is logically unsatisfiable on its own.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the duration in minutes for the project's assembly on the primary unit and its testing on the secondary unit, respectively.

## Output

Print a single line containing either `JOB i` (if project $i$'s constraint subset alone is unsatisfiable) or `LOAD c` (if unit $c$'s constraint subset alone is unsatisfiable).

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

In Example 1, the first project requires 70 minutes on the primary unit and then 60 minutes on the secondary unit. The subset of constraints for project 1 requires mapping a 70-minute interval and a subsequent 60-minute interval into the domain $[0, 100]$, which is logically unsatisfiable. This makes `JOB 1` a valid proof of impossibility. 

In Example 2, no individual project's isolated constraints are unsatisfiable. However, the primary unit is assigned four tasks of 50 minutes each. The subset of constraints for unit 1 requires packing four disjoint 50-minute intervals into the domain $[0, 150]$, which is logically unsatisfiable, making `LOAD 1` the valid proof.