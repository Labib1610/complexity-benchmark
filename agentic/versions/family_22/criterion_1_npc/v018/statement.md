# Problem A — Meeting the Deadline Across Parallel Assembly Stations

Time limit: 5 s   Memory limit: 256 MB

## Description
A production plant is tasked with completing a batch of $n$ operations (numbered 1 to $n$). The plant is equipped with $M$ uniform assembly bays. The production timeline is divided into discrete intervals called time slots. Every operation takes exactly one time slot to complete. Each assembly bay can accommodate at most one operation per time slot, meaning that no more than $M$ operations can be processed concurrently during any single time slot.

Furthermore, the operations are interconnected through physical supply chains. When operation $a$ produces a sub-assembly required by operation $b$, operation $b$ must be scheduled in a time slot strictly later than the one in which operation $a$ takes place. The specific assembly bay assigned to an operation is irrelevant; the only factor that matters is the time slot it occupies.

The plant manager has imposed a strict operational cutoff of $T$ time slots.

You must determine whether it is possible to assign a time slot to every operation such that the assembly bay capacity is never exceeded and all supply chain prerequisites are respected. If such an arrangement is feasible, output the exact time slot (between 1 and $T$) assigned to each operation.

## Input
The first line contains four integers $n$, $M$, $T$, and $m$.
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that operation $a$ must finish before operation $b$ can start.

## Output
If the batch can be finished within the cutoff, print `YES` on the first line, followed by $n$ space-separated integers representing the time slot (from 1 to $T$) assigned to each operation, in order from operation 1 to $n$. Otherwise, print `NO`.

## Example 1

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

## Example 2

### Input
```text
4 1 3 3
1 2
1 3
2 4
```

### Output
```text
NO
```
