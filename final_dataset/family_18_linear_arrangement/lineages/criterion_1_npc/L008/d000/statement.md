# Problem A — Synthesis Phase Sequencing

Time limit: 5 s
Memory limit: 256 MB

## Description
A complex synthesis procedure consists of $n$ distinct reaction steps. These steps must be executed one by one in a strict sequence of $n$ consecutive phases. Every step must be assigned to exactly one phase, and every phase must contain exactly one step (a one-to-one mapping).

Certain pairs of steps depend on the same specialized catalyst. There are $m$ such pairwise dependencies. For each dependency, a fresh catalyst is introduced during the phase of whichever of the two steps occurs first, and it remains in the reactor until the phase of the latter step is completed. 

The degradation of a catalyst depends entirely on how long it remains active in the reactor. Specifically, if the two steps sharing a catalyst are scheduled at phase $P$ and phase $Q$, the degradation score for that catalyst is exactly the absolute difference between the two phase numbers (i.e., $|P - Q|$). The specific chemicals and reaction directions are immaterial to this calculation; only the separation in phases matters.

The total degradation score is the sum of the degradation scores of all $m$ required catalysts. To ensure the final product's stability, this total degradation score must not exceed a strict threshold $B$. There is no limit on individual catalyst degradation and no limit on how many catalysts are active simultaneously — the only constraint that binds is the grand total.

Determine whether it is possible to assign the $n$ steps to the $n$ phases such that the total degradation score is at most $B$. If it is possible, provide a valid phase assignment; otherwise, indicate that it is impossible. (An assignment that is excellent for some catalysts may overshoot the total because of others, so local good choices do not guarantee a feasible total.)

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$, representing that reaction step $u$ and reaction step $v$ share a catalyst. Steps are numbered from 1 to $n$.

## Output
If a valid sequence exists, print `YES` on the first line. On the second line, print $n$ space-separated integers, where the $i$-th integer represents the phase (from 1 to $n$, a permutation) assigned to reaction step $i$.
If no such sequence can stay within the threshold, print `NO`.

## Example

**Input:**
```
4 3 4
1 2
1 3
1 4
```

**Output:**
```
YES
2 1 3 4
```
