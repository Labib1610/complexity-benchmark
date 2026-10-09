# Problem A — Rush Order Scheduling

Time limit: 5 s
Memory limit: 256 MB

## Description
A manufacturing facility has received a rush order to produce $n$ distinct components before a shipping deadline of $T$ shifts. The facility operates $M$ identical workbenches. Each component takes exactly one full shift to assemble and occupies one workbench. Any component can be built on any available workbench. During any single shift, the total number of components being assembled cannot exceed the $M$ available workbenches.

The overall product design dictates that certain components are prerequisites for others. If a component requires another as a prerequisite, the prerequisite component must be scheduled in a strictly earlier shift so its parts are ready for use. 

The factory manager must determine if all $n$ components can be scheduled within the $T$ shifts without violating the workbench capacity or the prerequisite rules. If a valid schedule exists, the manager requires a specific shift assignment for each component.

## Input
The first line contains four integers $n$, $M$, $T$, and $m$.
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that component $a$ is a prerequisite for component $b$.

## Output
If it is possible to complete all components within the deadline, print `YES` on the first line, followed by a second line containing $n$ integers. The $i$-th integer must represent the shift (from $1$ to $T$) assigned to component $i$. If it is impossible, print `NO`.

## Example

### Input
```
5 2 3 4
1 3
2 3
3 4
3 5
```

### Output
```
YES
1 1 2 3 3
```
