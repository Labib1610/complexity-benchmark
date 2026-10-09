# Problem A — Calibration Matrices

Time limit: 5 s   Memory limit: 256 MB

## Description

A satellite communications array requires the calibration of exactly **k** distinct transmission channels. Each channel configuration is composed of three parameters: a frequency band, a modulation scheme, and an encryption key. For each parameter category, the available options are indexed by integers from 1 to **k**. The hardware capacity limits the number of channels **k** to at most 22.

Due to signal interference, only specific combinations of parameters are viable. The engineering team has certified exactly **t** approved configurations. Each approved configuration is given as a triplet `(x, y, z)`, meaning frequency band **x**, modulation scheme **y**, and encryption key **z** can be successfully combined.

To finalize the calibration, you must select exactly **k** configurations from the approved list. This selection must satisfy the following sequence-validation rule:
- Extract the frequency band from each of your **k** chosen configurations to form a list of **k** integers. If you sort this list in ascending order, the result must be exactly the sequence 1, 2, ..., **k**.
- Similarly, extracting and sorting the modulation schemes from your chosen configurations must yield exactly the sequence 1, 2, ..., **k**.
- Finally, extracting and sorting the encryption keys from your chosen configurations must also yield exactly the sequence 1, 2, ..., **k**.

Determine whether it is possible to select exactly **k** approved configurations that satisfy these conditions. If a valid set exists, provide it.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of options in each parameter category and the total number of approved configurations.
Each of the following **t** lines provides three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing an approved configuration utilizing frequency band **x**, modulation scheme **y**, and encryption key **z**. All listed configurations are distinct.

## Output

If a valid selection of **k** configurations can be formed, print `YES` on the first line. Then, output **k** lines, each containing the three integers `x y z` of one selected configuration. Any valid selection of **k** configurations that meets the sequence-validation rule is accepted; the chosen configurations may be printed in any order.

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

In Example 2, both approved configurations use modulation scheme 1. If both are selected, the extracted modulation schemes would be 1 and 1. Sorting them yields 1, 1, which does not match the required sequence 1, 2. Therefore, a valid selection is impossible.