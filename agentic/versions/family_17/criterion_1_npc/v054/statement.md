# Problem A — Trimerization Module

Time limit: 5 s   Memory limit: 256 MB

## Description
Synthetic crystal lattice manufacturing relies on an automated three-stage pipeline. First, an extraction process isolates a specific number of distinct atomic clusters. Second, a trimerization module combines these raw clusters into stable three-cluster molecules known as trimers. Finally, the trimers are assembled into a macroscopic lattice structure.

You are developing the software for the trimerization module. You will receive exactly one unit of each extracted cluster. You are also given a thermodynamic catalog detailing all viable reactions, where each reaction specifies three exact clusters that can fuse into a single stable trimer. 

Your task is to determine which reactions to trigger so that every single extracted cluster is utilized exactly once. Partial utilization is catastrophic: any leftover clusters will act as contaminants during the final assembly stage. Furthermore, because you only possess one unit of each cluster, any reaction plan that attempts to reuse a cluster is physically impossible. 

If you can find a valid set of reactions that perfectly exhausts the supply of clusters, you must signal success and provide the sequence of reactions to the assembly matrix. Otherwise, you must abort the pipeline.

## Input
The first line contains two integers, $q$ and $t$. The value $q$ specifies the target yield of stable trimers. Because the process operates on micro-batches, a batch will always aim for at least a single trimer, but the physical volume of the extraction tank restricts the target yield to no more than two hundred trimers. The value $t$ specifies the number of known viable reactions. The thermodynamic catalog might contain zero viable reactions, or it might contain as many as twenty thousand documented reactions. The total number of atomic clusters extracted in the first stage is exactly $3q$.

The subsequent $t$ lines each detail a single viable reaction. A reaction is specified by three integers $a$, $b$, and $c$, which are the IDs of the required atomic clusters. The cluster IDs are valid integers starting from a minimum of one up to a maximum of $3q$. The three IDs on a single line are distinct and are always reported in strictly increasing order.

## Output
If a valid reaction plan can be formed, output `YES` on the first line. Then, output $q$ lines, each listing the three cluster IDs for one of the chosen reactions.
If it is impossible to formulate a reaction plan that perfectly consumes all clusters, output `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
