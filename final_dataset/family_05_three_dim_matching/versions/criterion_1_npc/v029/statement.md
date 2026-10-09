# Problem A — Device Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

A factory must assemble **k** complete devices. The inventory contains distinct units across different component categories, with each category having exactly **k** units:

- **k** processors, numbered 1..k,
- **k** sensors, numbered 1..k,
- **k** transmitters, numbered 1..k.

A device consists of exactly one processor, one sensor, and one transmitter. Only certain configurations operate correctly together; you are given a list of compatible configurations `(x, y, z)`.

Choose exactly **k** compatible configurations so that every processor, every sensor, and every transmitter is utilized in **exactly one** chosen device.

Determine whether this is possible, and if so report one valid set of devices.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of units per category and the number of compatible configurations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a compatible configuration. No configuration is listed more than once.

## Output

If a valid selection of **k** devices exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one chosen device. Any selection in which every processor, sensor, and transmitter is utilized exactly once is accepted; the devices may be printed in any order.

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

In Example 2, both compatible configurations use sensor 1, so sensor 2 can never be covered.
