# Problem A — Cloud Provisioning

Time limit: 5 s   Memory limit: 256 MB

## Description

A data center must provision **k** independent service clusters. A valid cluster specification is defined by a 3-tuple consisting of a physical host ID, a virtual environment ID, and a dedicated subnet ID.

The infrastructure provides exactly **k** IDs (numbered 1 to **k**) for each of the three resource categories. Due to hardware and network constraints, only a specific set of **t** cluster specifications are known to be stable. 

You must select exactly **k** specifications from the stable set to form your deployment. To ensure strict isolation and full utilization, your selection must not reuse or omit any resource. Specifically, if you isolate the physical host IDs from your chosen **k** specifications, they must collectively form a permutation of the integers 1 through **k**. The same requirement applies independently to the virtual environment IDs and the dedicated subnet IDs.

Determine whether such a deployment is possible, and if so, report one valid set of specifications.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of available IDs per resource category and the number of stable specifications.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a stable specification consisting of physical host **x**, virtual environment **y**, and dedicated subnet **z**. No specification is listed more than once.

## Output

If a valid deployment of **k** clusters exists, print `YES` on the first line. Then, print **k** lines, each containing three integers `x y z` representing the physical host, virtual environment, and dedicated subnet of one chosen specification. Any selection satisfying the constraints is accepted; the specifications may be printed in any order.

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

In Example 2, both stable specifications require virtual environment 1. Therefore, any selection will either reuse virtual environment 1 or omit virtual environment 2, making a valid deployment impossible.
