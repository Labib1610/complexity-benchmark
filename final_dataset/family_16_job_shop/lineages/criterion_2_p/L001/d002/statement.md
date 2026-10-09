# Consecutive Treatments

Time limit: 1 s   Memory limit: 256 MB

## Description

A dispatcher oversees **j** dossiers. For each dossier, you are given the duration of its initial review and the duration of its final sign-off.

The dispatcher must arrange all **j** dossiers into a single sequence. For any chosen sequence, the protocol evaluates the arrangement using the following mechanics:
- The dossier at position **k** in the sequence completes its initial review at a time equal to the sum of the initial review durations of all dossiers from position 1 to **k**.
- A "clearance metric" is then computed for each dossier. For the dossier at position **k**, this metric is its initial review completion time plus the sum of the final sign-off durations of all dossiers from position **k** to position **j** (inclusive).
- The actual time at which the entire sequence is completely signed off is mathematically equal to the maximum clearance metric among all **j** dossiers.

Arrange the sequence of dossiers to minimize this overall completion time. Output the smallest possible maximum clearance metric.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the durations of a dossier's initial review and final sign-off.

## Output

Print a single integer: the smallest possible maximum clearance metric that can be achieved by optimally arranging the sequence of dossiers.

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

In Example 1, one optimal sequence processes the dossiers in the order: the third dossier `(1, 3)`, then the second `(2, 4)`, then the first `(3, 2)`.
The clearance metrics are calculated as follows:
- For the dossier at position 1 `(1, 3)`: initial review completes at 1. The clearance metric is 1 + (3 + 4 + 2) = 10.
- For the dossier at position 2 `(2, 4)`: initial review completes at 1 + 2 = 3. The clearance metric is 3 + (4 + 2) = 9.
- For the dossier at position 3 `(3, 2)`: initial review completes at 1 + 2 + 3 = 6. The clearance metric is 6 + 2 = 8.
The maximum clearance metric for this sequence is max(10, 9, 8) = 10. No sequence can achieve a maximum clearance metric strictly less than 10.