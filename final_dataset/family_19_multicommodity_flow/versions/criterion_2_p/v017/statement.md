# Phase II: Corridor Volume Allocation

Time limit: 2 s
Memory limit: 256 MB

## Description
The corporate logistics pipeline operates in three distinct phases. In Phase I, predictive models forecast customer demand and assign physical rolling stock to our transit corridors, establishing a strict upper limit on the number of containers each one-way corridor can support per cycle. In Phase III, human resources processes the final transport assignments to generate driver schedules and empty-container return manifests.

Your task is to implement the critical Phase II: the volume allocation step. You will receive the output from Phase I, which specifies a layout of sorting hubs, the one-way corridors connecting them, and the maximum container ceiling for each corridor. You are also given a single origin hub, a single destination hub, and a fixed quota of containers that must be transferred from the origin to the destination in one cycle. 

For Phase III to succeed, you must assign a non-negative whole number of containers to each corridor such that:
- No corridor's assignment exceeds its Phase I ceiling.
- At every hub except the origin and destination, the total number of incoming containers exactly equals the total number of outgoing containers.
- The net departure from the origin equals the required quota, and the net arrival at the destination equals the required quota.

If it is possible to achieve this, you must output the exact container counts for each corridor so Phase III can proceed. If the Phase I ceilings are too restrictive to support the required quota, you must reject the plan.

## Input
The first line contains three integers: $n$ (the number of hubs), $m$ (the number of corridors), and the number $1$ (representing the single product category).
The second line contains three integers: $s$ (the origin hub), $t$ (the destination hub), and $d$ (the required container quota).
The next $m$ lines each contain three integers $u$, $v$, and $cap$, indicating a one-way corridor from hub $u$ to hub $v$ with a maximum ceiling of $cap$ containers.

## Output
If the quota can be successfully routed, print `YES` on the first line. On the second line, print $m$ integers separated by spaces, representing the number of containers assigned to each corridor (in the exact order the corridors were provided in the input).
If the quota cannot be met under the given ceilings, print `NO`.

## Example

### Input
```
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 10
```

### Output
```
YES
5 5 0 5 5
```
