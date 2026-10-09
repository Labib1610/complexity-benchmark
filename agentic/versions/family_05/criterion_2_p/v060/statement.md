# Orbital Frequency Allocation

Time limit: 2 s   Memory limit: 256 MB

## Description

A space agency manages a constellation of **k** satellites. The network relies on three sets of resources, each containing exactly **k** elements:

- **k** satellites, numbered 1 to k,
- **k** orbital slots, numbered 1 to k,
- **k** transmission frequencies, numbered 1 to k.

A valid transmission setup requires exactly one satellite, one orbital slot, and one frequency. You are provided with a list of viable setups `(x, y, z)`.

In this constellation, **each satellite is permanently stationed in exactly one orbital slot, and no two satellites occupy the same slot**. Therefore, the pairing between satellites and orbital slots is physically fixed. The only remaining operational choice is the assignment of frequencies.

Your task is to activate exactly **k** viable setups from the provided list such that every satellite, every orbital slot, and every frequency is used in **exactly one** activated setup. Determine if this network activation is possible, and if so, report one valid collection of setups.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of elements per resource category and the number of viable setups.
Each of the subsequent **t** lines provides three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a viable setup of satellite **x**, orbital slot **y**, and frequency **z**. No setup is listed more than once. For each satellite, every listed setup features the same orbital slot, and different satellites feature different orbital slots.

## Output

If a valid activation of **k** setups exists, print `YES` on the first line, then print **k** lines, each containing the three integers `x y z` of an activated setup (in any order). Any valid activation is accepted.

If no valid activation exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
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
2 2 1
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

In Example 2, both satellites can only operate on frequency 1, so frequency 2 can never be utilized.
