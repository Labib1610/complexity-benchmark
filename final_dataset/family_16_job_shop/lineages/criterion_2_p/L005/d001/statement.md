# Problem B — Canal Convoy

Time limit: 1 s   Memory limit: 256 MB

## Description

A canal system processes **j** ships through exactly 2 sequential stages: Lock Alpha (stage 1) and Lock Beta (stage 2). Every ship must clear stage 1 before it can begin stage 2. For each ship, you are given its transit duration in stage 1 and its transit duration in stage 2. The rules are:

- Stage 1 and stage 2 can each accommodate only 1 ship at a time.
- A ship can enter stage 2 only after its stage 1 transit is completely finished.
- The canal is too narrow for overtaking. You must choose a single sequence in which the ships are dispatched. Both stages will process the ships in this exact same sequence.

Choose the dispatch sequence so that the time at which the **last** ship clears stage 2 is as small as possible. Report that smallest possible finish time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains exactly 2 integers **t1** and **t2** (1 ≤ t1, t2 ≤ 1000000): the duration in stage 1 and the duration in stage 2 of a ship.

## Output

Print a single integer: the smallest possible time at which all ships have completely cleared stage 2.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2 the single ship takes 5 in stage 1 then 3 in stage 2, finishing at time 8.