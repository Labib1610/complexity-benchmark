# Phase II: Quarantine Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

The planetary defense initiative operates a sequential three-phase pipeline for handling recovered alien artifacts.

**Phase I: Threat Profiling** (Completed)
Sensors have scanned **n** distinct artifacts (numbered 1 to **n**) and mapped **m** pairwise resonant interactions. A resonance between two specific artifacts indicates that they will destabilize if stored together.

**Phase II: Quarantine Selection** (Your Task)
The logistics division must compile a payload of exactly **k** artifacts to be transported together in a single unshielded cargo bay. To guarantee structural integrity during transit, the selected payload must be completely stable: no resonance may exist between any two artifacts included in the payload.

**Phase III: Deconstruction** (Pending)
Upon arrival, the orbital forge will dismantle the payload to harvest rare materials. The automated deconstruction sequence relies entirely on receiving a valid payload from the previous step.

Your system is responsible exclusively for Phase II. Given the profiling data from Phase I, determine whether a stable payload of exactly **k** artifacts can be assembled. If successful, you must report which artifacts to load so that Phase III can proceed.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ **n** ≤ 46, 0 ≤ **m** ≤ **n**·(**n**−1)/2, 1 ≤ **k** ≤ **n**).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), representing a resonance between artifact **u** and artifact **v**. No resonance is listed more than once.

## Output

If a stable payload of exactly **k** artifacts can be formed, print `YES` on the first line. On the second line, print the **k** distinct artifact numbers that make up the payload, separated by spaces. If multiple valid payloads exist, you may output any one of them.

If it is impossible to form such a payload, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```
