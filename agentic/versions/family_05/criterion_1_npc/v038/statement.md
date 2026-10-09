# Problem A — Protocol Deployment

Time limit: 5 s   Memory limit: 256 MB

## Description

A network administrator must deploy exactly **k** routing protocols. A protocol is defined by a configuration triplet of three integers `(a, b, c)`, where:
- `a` is the primary channel,
- `b` is the backup channel,
- `c` is the diagnostic channel.

The available channel identifiers for each role are integers from 1 to **k**. 

You are provided with a list of **t** tested configuration triplets. You must select exactly **k** triplets from this list such that all of the following conditions are met:
- No two selected triplets share the same primary channel `a`.
- No two selected triplets share the same backup channel `b`.
- No two selected triplets share the same diagnostic channel `c`.
- As a network checksum requirement, the sum of all 3**k** integers across the **k** selected triplets must be exactly 3 * **k** * (**k** + 1) / 2.

Determine whether such a selection is possible. If it is, output the selected triplets.

## Input

The first line contains two integers **k** and **t** (1 ≤ **k** ≤ 22, 0 ≤ **t** ≤ **k**³): the number of protocols to deploy and the number of tested configuration triplets. 
It is guaranteed that **t** ≤ 10,648.

Each of the next **t** lines contains three integers **a**, **b**, **c** (1 ≤ **a**, **b**, **c** ≤ **k**), representing a tested configuration triplet. No triplet is listed more than once in the input.
Furthermore, it is guaranteed that for every triplet in the input, the sum **a** + **b** + **c** is at most 3**k**, and the product **a** × **b** × **c** is at least 1.

## Output

If a valid deployment of **k** protocols exists, print `YES` on the first line. Then, print **k** lines, each containing the three integers `a b c` of a selected triplet. Any selection satisfying all conditions is accepted, and the selected triplets may be printed in any order.

If no valid deployment exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 1 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, both tested triplets use backup channel 1. It is impossible to select two triplets without sharing a backup channel.
