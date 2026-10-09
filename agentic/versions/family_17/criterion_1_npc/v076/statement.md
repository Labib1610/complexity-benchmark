# Problem A — Trimerization Module

Time limit: 5 s   Memory limit: 256 MB

## Description
The automated production pipeline for synthetic crystal lattices operates in three distinct stages:

1. **Cluster Extraction**: A raw material batch is processed to yield a base set of distinct atomic clusters. The total number of clusters produced is always a multiple of three.
2. **Trimerization (Your Module)**: The raw clusters must be fully synthesized into stable three-cluster molecules known as trimers.
3. **Lattice Assembly**: The resulting trimers are fed into the crystallizer to form the macroscopic lattice structure. The crystallizer requires at least one trimer to initiate assembly, and has a strict maximum capacity of 200 trimers per batch.

Your software module manages Stage 2. The extraction stage always provides exactly one unit of each atomic cluster. These clusters are indexed sequentially with integers starting from 1 up to the total number of clusters in the batch. 

Thermodynamic profiling has pre-identified a catalog of viable trimer reactions. The memory bank holding this catalog has a capacity of 20,000 reaction profiles, though for some batches no viable reactions might be found (an empty catalog). Each stored profile specifies exactly three distinct clusters that can successfully fuse into one trimer.

Your module must select a subset of these viable reactions to execute. The chosen reactions must collectively consume every single extracted cluster exactly once. If any cluster is left unreacted, it will contaminate the lattice and ruin Stage 3. If the selected reactions require a cluster to be used multiple times, the reaction will physically fail, as only one unit of each cluster exists.

If a perfect consumption plan exists, your module must report success and output the list of reactions to be executed so Stage 3 can prepare the assembly matrix. If no such plan can be formed from the catalog, your module must issue an abort signal to halt the pipeline.

## Input
The first line contains two integers $q$ and $t$. The value $q$ specifies the number of trimers needed to process the current batch (meaning exactly $3q$ clusters were extracted), while $t$ represents the number of viable reactions provided by the thermodynamic catalog. 
Each of the following $t$ lines contains three integers representing the indices of the three clusters consumed by one viable reaction. These three indices are presented in strictly increasing order.

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
