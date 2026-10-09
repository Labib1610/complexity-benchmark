# Problem B — Sequencing the Batch on One Station

Time limit: 2 s
Memory limit: 256 MB

## Description
A complete production workflow spans four major phases:

1. **Planning**: Analysts define $n$ distinct unit-time operations and identify $m$ technical prerequisites. Each prerequisite specifies that one particular operation must be completed before another can be initiated.
2. **Sequencing**: Your software module receives the planning data. Because the shop floor has only one active workstation, your module must arrange all $n$ operations into a single, continuous timeline. The timeline must include every operation exactly once, and every prerequisite operation must appear earlier in the schedule than the operation that requires it.
3. **Execution**: The workstation processes the operations one by one, exactly in the order you provided.
4. **Inspection**: The finished assembly is tested, verified, and packaged for delivery.

Your task is strictly to implement the **Sequencing** phase. You must process the prerequisites and output a valid schedule so the Execution phase can begin. If there are multiple valid schedules, the Execution phase will accept any of them. Sometimes the Planning analysts make a mistake and create logically contradictory prerequisites. If it is impossible to schedule the operations without violating at least one prerequisite, you must reject the batch.

## Input
The first line contains two integers $n$ and $m$, representing the number of operations (numbered 1 through $n$) and the number of prerequisites, respectively.
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that operation $a$ must be completed before operation $b$ can begin.

## Output
If a valid schedule can be formed, print `YES` followed by a space-separated sequence of all $n$ operations representing the order they should be executed. 
If the prerequisites are contradictory and no such schedule can be formed, print `NO`.

## Example 1

**Input:**
```
4 4
1 2
1 3
2 4
3 4
```

**Output:**
```
YES
1 2 3 4
```
*(Note: `YES` followed by `1 3 2 4` would also be accepted, as both 2 and 3 are completed before 4).*

## Example 2

**Input:**
```
3 3
1 2
2 3
3 1
```

**Output:**
```
NO
```
