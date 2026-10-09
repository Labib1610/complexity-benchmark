# Problem B — Assembly Line Alignment

Time limit: 5 s   Memory limit: 256 MB

## Description
A factory plans to install $n$ different machines, identified by integers 1 through $n$. The facility has a single straight corridor with $n$ mounting bays, numbered sequentially from 1 to $n$. Each machine must be assigned to exactly one bay.

Certain pairs of machines must be linked by a direct conveyor belt to transfer materials. The cost of a belt linking a machine in bay $x$ to a machine in bay $y$ is exactly $|x - y|$ units of material. 
The factory has a strict total budget of $B$ units of material for all belts combined.

The material flow is designed such that every machine is integrated into a single unified system: a component could theoretically pass from any machine to any other through a sequence of belts. To minimize complexity, the system uses the absolute minimum number of belts required to achieve this full integration.

Determine a valid assignment of the $n$ machines to the $n$ bays such that the total belt cost does not exceed $B$.

## Input
The first line contains three integers $n$, $m$, and $B$.  
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that a conveyor belt must directly link machine $u$ and machine $v$. (The system guarantees $m = n - 1$ to satisfy the minimal integration property).

## Output
If the budget can be met, print `YES` on the first line. On the second line, print $n$ integers representing the bay assignments for machines 1 through $n$ respectively. The assignments must be a permutation of the integers from 1 to $n$.  
If it is impossible to stay within budget, print `NO`.

## Example

**Input:**
```text
5 4 6
1 2
1 3
1 4
1 5
```

**Output:**
```text
YES
3 1 2 4 5
```
