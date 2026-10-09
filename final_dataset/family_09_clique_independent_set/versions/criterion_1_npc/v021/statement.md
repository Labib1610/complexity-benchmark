# Problem A — Thermal Test Vector

Time limit: 5 s   Memory limit: 256 MB

## Description

You are preparing a thermal diagnostic test for a newly fabricated microchip. The chip exposes **n** input pins (numbered 1 to n). Internally, the chip contains **m** diagnostic two-input NAND gates.

Each NAND gate is wired directly to two distinct input pins. By definition, a NAND gate outputs a HIGH signal unless both of its input pins are driven HIGH, in which case it outputs a LOW signal. 

To avoid overheating the diagnostic circuit during the test, every single one of the **m** NAND gates must output a HIGH signal. At the same time, to draw enough power to activate the thermal sensors, you must drive exactly **k** of the input pins HIGH (and leave the remaining **n**−**k** pins LOW).

Given the wiring of the diagnostic gates, determine if there is a valid test vector. If a valid configuration exists, report one by listing the **k** pins that should be driven HIGH.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), indicating that a NAND gate is wired to input pins **u** and **v**. No two gates are wired to the exact same pair of pins.

## Output

If a valid test vector exists, print `YES` on the first line. On the second line, print the numbers of the **k** distinct input pins that should be driven HIGH, separated by spaces. If there are multiple valid sets of pins, any configuration that keeps all gates HIGH is accepted.

If no such configuration is possible, print `NO`.

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
