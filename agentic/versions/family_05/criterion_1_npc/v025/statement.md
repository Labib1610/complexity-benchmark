# Problem A — Quantum Entanglement Grids

Time limit: 5 s   Memory limit: 256 MB

## Description

You are tasked with calibrating a quantum communication grid. The system requires establishing exactly **k** independent entanglement channels. To form a single channel, you must link exactly one photon source, one reflection node, and one quantum detector.

The grid contains:
- **k** photon sources, labeled 1 through **k**.
- **k** reflection nodes, labeled 1 through **k**.
- **k** quantum detectors, labeled 1 through **k**.

Due to spatial alignment, only certain specific combinations of (photon source, reflection node, detector) can successfully entangle. You are given a list of **t** viable combinations.

Your goal is to select exactly **k** viable combinations such that every photon source, every reflection node, and every quantum detector is incorporated into exactly one chosen entanglement channel.

The experimental setup inherently guarantees the following structural properties about the list of viable combinations:
1. **Energy ceiling:** For any viable combination `(x, y, z)`, the sum of their numerical labels `x + y + z` is at most `3k`.
2. **Source capacity:** No single photon source is part of more than `k²` viable combinations.
3. **System scale:** The total number of viable combinations **t** does not exceed 10,648.

Determine if a complete calibration is possible. If it is, output one valid set of **k** combinations.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k³): the size of each component group and the number of viable combinations.
Each of the following **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), representing a viable combination of photon source **x**, reflection node **y**, and detector **z**. No combination is listed more than once.

## Output

If a valid selection of **k** entanglement channels exists, print `YES` on the first line. Then, print **k** lines, each containing the three integers `x y z` of a chosen channel. The channels may be printed in any order. Any valid selection that uses every component exactly once is accepted.

If no such selection is possible, print `NO`.

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

In Example 2, both viable combinations require reflection node 1, meaning reflection node 2 can never be utilized, so a complete calibration is impossible.
