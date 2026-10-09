# Problem A — Resonance Calibration

Time limit: 5 s   Memory limit: 256 MB

## Description

A geological scanner operates in a subterranean grid. Every location in the grid is defined by a depth **x**, a latitude **y**, and a longitude **z**, each taking an integer value from 1 up to the grid's bounding dimension **k**.

The scanner has identified **t** resonance pockets at specific `(x, y, z)` locations. 

To calibrate the system, you must load a subset of the identified pockets into the scanner's memory bank. The memory bank has exactly **k** slots, and every slot must be filled with a distinct pocket from the identified list.

Once loaded, the scanner evaluates the spatial dispersion of the chosen subset to prevent harmonic feedback. The calibration is successful if and only if the selected pockets collectively span the entire spectrum of each spatial axis. Specifically:
- The set of depth coordinates (**x**) of the **k** chosen pockets must contain every integer from 1 to **k**.
- The set of latitude coordinates (**y**) of the **k** chosen pockets must contain every integer from 1 to **k**.
- The set of longitude coordinates (**z**) of the **k** chosen pockets must contain every integer from 1 to **k**.

Determine whether a successful calibration configuration of exactly **k** pockets is possible, and if so, report one valid selection.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the grid dimension and the number of identified resonance pockets.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), the coordinates of an identified resonance pocket. No location is listed more than once.

## Output

If a valid calibration configuration of exactly **k** pockets exists, print `YES` on the first line. Then, print **k** lines, each containing the three coordinates `x y z` of one selected pocket. Any selection satisfying the spatial dispersion rules is accepted, and the pockets may be printed in any order.

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

In Example 2, the grid dimension is 2, so the memory bank requires exactly 2 pockets. The two identified pockets are `(1, 1, 1)` and `(2, 1, 2)`. If both are loaded, we evaluate their spatial dispersion. Their latitude (**y**) coordinates are 1 and 1. The collection of latitude coordinates present in the memory bank consists only of the value 1, which fails to contain every integer from 1 to 2. Because the full spectrum of the latitude axis is not represented, the spatial dispersion check fails. Thus, a successful calibration is impossible.