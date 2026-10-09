# Decommissioning Stage 2: Hazard Separation

Time limit: 5 s   Memory limit: 256 MB

## Description
The decommissioning of a subterranean research complex proceeds in three stages.

First, the assessment team maps the complex, identifying $n$ chambers and $m$ bidirectional transit tubes. They also pinpoint $k$ primary hazard locations where highly reactive materials are stored.

Second, the engineering team must execute a structural separation plan. Each transit tube has a deactivation expense, representing the resources required to permanently block it. The team is provided a fixed allocation of $B$ credits for this stage. They must select a subset of tubes to deactivate such that no reactive material from any primary hazard location can ever mix with material from another primary hazard location. This requires ensuring that no sequence of active tubes allows transit between any two distinct hazard locations. (While separating any single pair of locations might be inexpensive, the total expense must cover isolating all $k$ locations from one another simultaneously within the single allocation of $B$ credits.) The remaining standard chambers act as inert buffers and may end up grouped with any hazard location; their final grouping is not constrained. The total deactivation expense is simply the sum of the expenses of the deactivated tubes.

Third, after the separation is completed and verified, autonomous sensors are deployed into each newly distinct zone for indefinite environmental monitoring.

Your task is to process the data from the first stage and determine the actions for the second stage. You must find a valid set of tubes to deactivate that costs no more than $B$ credits, or determine that the allocated credits are insufficient to achieve complete separation of all hazard locations simultaneously.

## Input
The first line contains four integers: $n$ (total chambers), $m$ (total transit tubes), $k$ (number of primary hazard locations), and $B$ (credit allocation).
The second line contains $k$ distinct integers representing the identifiers of the primary hazard locations.
The following $m$ lines each contain three integers $u$, $v$, and $w$, indicating a transit tube between chamber $u$ and chamber $v$ with a deactivation expense of $w$.

## Output
If the separation is possible within the allocation, print `YES` on the first line. On the second line, print the number of deactivated tubes, $c$. Then, output $c$ lines, each containing two integers $u$ and $v$, representing a deactivated tube. If it is impossible to separate all hazard locations within the allocation, print `NO`.

## Example

**Input**
```text
4 3 3 6
1 2 3
1 4 2
2 4 3
3 4 4
```

**Output**
```text
YES
2
1 4
2 4
```
