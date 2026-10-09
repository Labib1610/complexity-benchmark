# Problem B — Canal Convoy

Time limit: 1 s   Memory limit: 256 MB

## Description

A fleet of **j** vessels must travel down a narrow canal. You must arrange the fleet into a strict entry sequence.

The canal features two sequential checkpoints: Lock Alpha and Lock Beta. Every vessel must pass Lock Alpha before it can pass Lock Beta. Both locks process the vessels in the exact same chosen sequence (a single permutation).

For each vessel, you are given its Lock Alpha transit duration, **t1**, and its Lock Beta transit duration, **t2**.

The timeline of the convoy's transit adheres to the following rules:
- The first vessel in your sequence begins its Lock Alpha transit at time 0.
- Lock Alpha can only accommodate one vessel at a time. It processes the vessels back-to-back with no delay; as soon as one vessel finishes at Lock Alpha, the next vessel in the sequence immediately begins.
- Lock Beta can also only accommodate one vessel at a time.
- A vessel may only begin its transit through Lock Beta once both of the following prerequisites are met:
  1. It has fully completed its own transit through Lock Alpha.
  2. The preceding vessel in your sequence (if any) has fully completed its transit through Lock Beta.
- Once permitted to enter a lock, a vessel takes exactly its specific transit duration (**t1** or **t2**) to complete that lock.

Your task is to determine the optimal ordering of the fleet that minimizes the time at which the final vessel completes its transit through Lock Beta.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains exactly 2 integers **t1** and **t2** (1 ≤ t1, t2 ≤ 1000000): the Lock Alpha transit duration and the Lock Beta transit duration of a vessel.

## Output

Print a single integer: the smallest possible time at which the final vessel in your sequence completes its transit through Lock Beta.

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

In Example 2, the single vessel has a Lock Alpha duration of 5 and a Lock Beta duration of 3. It finishes Lock Alpha at time 5, and immediately begins Lock Beta, finishing at time 5 + 3 = 8.