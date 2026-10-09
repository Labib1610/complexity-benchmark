# Synthesizing the Cure

Time limit: 5 s
Memory limit: 256 MB

## Description
A pharmaceutical laboratory must synthesize a batch of experimental compounds within a strict time limit. The laboratory is equipped with a fixed number of identical automated reactors. Every synthesis reaction requires exactly one operating cycle to complete. Each reactor can process at most one reaction per cycle, capping the total number of simultaneous reactions by the number of available reactors.

The reactions are interdependent; certain reactions produce chemical precursors required by others. If a reaction requires a precursor from another, the dependent reaction must be scheduled in a strictly later cycle than the one producing its precursor. A precursor produced in a given cycle is only available for use at the start of the following cycle. Any reaction can be assigned to any reactor, making the specific reactor used irrelevant; only the assigned cycle matters.

The laboratory has a maximum number of cycles to complete the entire batch. You must assign every reaction to a specific cycle such that all precursor dependencies are respected, the number of reactions in any cycle does not exceed the number of reactors, and all reactions are completed within the allowed cycles. If no such schedule exists, you must report that the batch cannot be completed.

## Input
The first line contains four integers $n$, $M$, $T$, and $m$.
$n$ is the total number of reactions (numbered 1 to $n$).
$M$ is the number of automated reactors.
$T$ is the maximum number of cycles available.
$m$ is the number of precursor dependencies.

Each of the next $m$ lines contains two integers $a$ and $b$, indicating that reaction $a$ produces a precursor required by reaction $b$ (meaning reaction $a$ must be completed in a strictly earlier cycle than reaction $b$).

## Output
If the batch can be completed within $T$ cycles, print `YES` followed by $n$ space-separated integers, where the $i$-th integer represents the cycle (from 1 to $T$) assigned to reaction $i$. If it is impossible, print `NO`.

## Example

### Input
```text
4 2 3 3
1 2
1 3
2 4
```

### Output
```text
YES
1 2 2 3
```
