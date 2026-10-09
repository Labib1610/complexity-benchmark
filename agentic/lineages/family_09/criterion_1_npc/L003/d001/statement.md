# Problem A — Thermal Test Vector

Time limit: 5 s   Memory limit: 256 MB

## Description

You are preparing a thermal diagnostic test for a newly fabricated microchip. The chip exposes **n** input pins (numbered 1 to n). Internally, the chip contains **m** thermal monitors.

Each monitor is connected to two distinct input pins. A monitor registers a safe state if at least one of its two connected pins is unpowered. If both of its connected pins are powered simultaneously, the monitor triggers an error.

For the diagnostic test, you are required to power exactly **k** distinct input pins, and leave the remaining **n**−**k** pins unpowered. To pass the test, every single one of the **m** monitors must register a safe state. Formally, you must choose a set of exactly **k** distinct pins to power such that for every listed monitor connected to pins **u** and **v**, at least one of **u** or **v** is not in your chosen set (equivalently, no monitor connects two powered pins).

Given the wiring of the monitors, determine if there is a valid test setup. If a valid setup exists, report one by listing the **k** pins that should be powered.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), indicating that a monitor is connected to input pins **u** and **v**. No two monitors are connected to the exact same pair of pins.

## Output

If a valid test setup exists, print `YES` on the first line. On the second line, print the numbers of the **k** distinct input pins that should be powered, separated by spaces. If there are multiple valid sets of exactly **k** pins that keep all monitors in a safe state, any such set is accepted.

If no such setup is possible, print `NO`.

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