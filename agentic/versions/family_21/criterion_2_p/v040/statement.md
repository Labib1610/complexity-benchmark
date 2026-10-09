# Problem B — Infrastructure Remediation Phase

Time limit: 2 s   Memory limit: 256 MB

## Description
The annual safety audit of a chemical processing plant has just concluded. The audit identified a severe cross-contamination risk: two specific junctions within the plant's pipe network currently allow material to flow between them. 

You are responsible for the computational remediation step. The plant consists of $n$ junctions connected by $m$ bidirectional pipes. Each pipe has a specific decommissioning expense, representing the labor and materials needed to safely and permanently remove it. You must select a subset of pipes to decommission such that it becomes completely impossible for any material to travel between the two flagged junctions, $s$ and $t$, in either direction. The operational status of all other junctions is not evaluated in this step; they may end up communicating with $s$, with $t$, or neither, as long as $s$ and $t$ are isolated from one another. 

You are provided with a financial cap $B$. The sum of the decommissioning expenses for your chosen pipes must not exceed this cap. 

Once your plan is approved, the maintenance crew will physically remove the selected pipes. Afterward, the flow dynamics team will take over the remaining infrastructure to recalibrate the pressure systems for the newly independent zones. Your objective is strictly to find a valid set of pipes to decommission within the financial cap, or determine if it is impossible.

## Input
The first line contains five integers $n$, $m$, $s$, $t$, and $B$. 
The following $m$ lines each contain three integers $u$, $v$, and $w$, representing a pipe between junction $u$ and junction $v$ with a decommissioning expense of $w$.

## Output
If a valid selection exists, print `YES` on the first line. On the second line, print the number of decommissioned pipes, $c$. Then, print $c$ lines, each containing two integers $u$ and $v$ representing a decommissioned pipe. If the financial cap is too low to achieve the goal, print `NO`.

## Example
**Input**
```
4 4 1 4 10
1 2 4
1 3 5
2 4 6
3 4 3
```
**Output**
```
YES
2
1 2
3 4
```
