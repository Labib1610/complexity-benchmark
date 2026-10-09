# Problem B — Agricultural Trial Synchronization

Time limit: 2 s   Memory limit: 256 MB

## Description
An agricultural research institute is planning a series of experimental trials. Every trial combines exactly one specific soil formulation with exactly one specific seed variety. No trial involves mixing multiple soils or multiple seeds. 

Because of resource constraints, each soil formulation can only be tested in one trial per season. Similarly, each seed variety can only be tested in one trial per season. The total number of seasons required for the testing program is dictated by the most heavily utilized resource: if the busiest soil formulation (or seed variety) is involved in $K$ trials, then at least $K$ seasons are absolutely necessary. The institute mandates that the schedule must conclude in exactly $K$ seasons.

Your task is to assign each trial to a season (numbered $1$ through $K$) such that no soil formulation and no seed variety is used more than once in any given season. The structure of these pairwise tests always guarantees that such a schedule is possible without ever exceeding $K$ seasons.

## Input
The first line contains three integers $S$, $V$, and $T$. The number of soil formulations $S$ and seed varieties $V$ are at least 1. The inventory system's maximum capacity dictates that neither $S$ nor $V$ can exceed exactly one hundred thousand. The number of trials $T$ is at least zero, and is bounded by a budget limit equal to exactly four times the maximum possible capacity of $S$.

The next $T$ lines each contain two integers $s_i$ and $v_i$, indicating a trial combining soil formulation $s_i$ and seed variety $v_i$. The IDs $s_i$ and $v_i$ are valid identifiers starting from 1 up to $S$ and $V$, respectively.

## Output
Print `YES` on the first line.
On the second line, print $T$ space-separated integers. The $i$-th integer must be the season (a number between $1$ and $K$, inclusive) assigned to the $i$-th trial in the input order. 

## Example
### Input
```
3 3 5
1 1
1 2
2 2
2 3
3 1
```
### Output
```
YES
1 2 1 2 2
```
