# Problem A — Resource Triads

Time limit: 5 s   Memory limit: 256 MB

## Description

A research facility is planning **k** independent experiments. The facility employs exactly **k** data analysts (numbered 1 to **k**), operates exactly **k** GPU clusters (numbered 1 to **k**), and has scheduled exactly **k** computing weeks (numbered 1 to **k**).

Executing an experiment requires forming a triad consisting of one analyst, one GPU cluster, and one computing week. However, due to software dependencies and personnel availability, only certain specific combinations of an analyst, a cluster, and a week are technically viable. You will receive the comprehensive list of all viable triads.

The facility's operating mandate dictates strict resource efficiency: you must select exactly **k** viable triads to form the experiments such that every analyst is assigned to exactly one experiment, every GPU cluster is utilized for exactly one experiment, and every computing week hosts exactly one experiment.

Evaluate whether a schedule fulfilling this mandate can be constructed, and if so, output one valid configuration.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k), representing the number of available resources in each category and the total number of viable triads, respectively.
Each of the subsequent **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), indicating that analyst **x**, GPU cluster **y**, and computing week **z** form a viable triad. No triad is repeated in the input.

## Output

If a valid deployment schedule exists, print `YES` on the first line. Then, output **k** lines, each containing three integers `x y z` representing the analyst, GPU cluster, and computing week for one of the chosen experiments. If multiple valid configurations exist, any configuration that strictly uses every resource exactly once is acceptable. The chosen triads may be printed in any order.

If no such deployment schedule can be formed, print `NO` on a single line.

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

In Example 2, both viable triads require GPU cluster 1. Consequently, GPU cluster 2 can never be utilized, making it impossible to satisfy the operating mandate.
