# Problem A — Trimerization Module

Time limit: 5 s   Memory limit: 256 MB

## Description
The automated production pipeline for synthetic crystal lattices operates in three distinct stages:

1. **Cluster Extraction**: A raw material batch is processed to yield a base set of exactly $3q$ distinct atomic clusters. These are strictly indexed from $1$ to $3q$.
2. **Trimerization (Your Module)**: The raw clusters must be fully synthesized into stable three-cluster molecules known as trimers.
3. **Lattice Assembly**: The resulting trimers are fed into the crystallizer to form the macroscopic lattice structure.

Your software module is responsible exclusively for Stage 2. The extraction stage always provides exactly one unit of each of the $3q$ atomic clusters. Thermodynamic profiling has pre-identified a catalog of $t$ viable trimer reactions. Each reaction in the catalog consumes exactly three specific clusters to form one trimer.

Your module must select a subset of these viable reactions to execute. The selection must consume every single one of the $3q$ clusters exactly once. If any cluster is left unreacted, it will contaminate the lattice and ruin Stage 3. If the selected reactions require a cluster to be used multiple times, the reaction will physically fail, as only one unit of each cluster exists.

If such a perfect consumption plan exists, your module must report success and output the list of reactions to be executed so Stage 3 can prepare the assembly matrix. If no such plan can be formed from the catalog, your module must issue an abort signal to halt the pipeline.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$). The total number of extracted clusters is $3q$.
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing the three clusters consumed by one viable trimer reaction.

## Output
If a valid reaction plan exists, print `YES` on the first line, followed by $q$ lines. Each of these $q$ lines must contain the three clusters of one selected reaction. 
If no valid reaction plan can be formed, print `NO`.

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
