# Problem A — Array Configuration

Time limit: 5 s   Memory limit: 256 MB

## Description

You are configuring a satellite communication array. The array must be initialized with exactly **k** active channels.

You are provided with a catalog of **t** candidate channel configurations. Each candidate operates using a single frequency band, a single encryption key, and a single polarization mode. Each of these three parameters is identified by an integer from 1 to **k**. 

To prevent interference and ensure stable operation, the set of **k** chosen candidates must adhere to the following isolation rules:
- No two chosen candidates may share the same frequency band.
- No two chosen candidates may share the same encryption key.
- No two chosen candidates may share the same polarization mode.

Given the catalog, determine whether it is possible to select exactly **k** of the candidate configurations to serve as the active channels. If it is possible, report one valid selection.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the required number of active channels and the number of candidate configurations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing the frequency band, encryption key, and polarization mode of a candidate. No candidate configuration is listed more than once.

## Output

If a valid selection of **k** channels exists, print `YES` on the first line, then print **k** lines, each containing the three parameters `x y z` of one chosen channel. If there are multiple valid selections, you may output any of them. The channels may be printed in any order.

If no valid selection exists, print `NO`.

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

In Example 2, both candidate configurations use encryption key 1. Selecting both would violate the isolation rule, so it is impossible to activate 2 channels.
