# Problem A — Alchemical Resonance

Time limit: 5 s   Memory limit: 256 MB

## Description

You are an alchemist tasked with brewing **j** complex potions. Your laboratory contains **m** unique magical foci. Each potion is created through a fixed sequence of resonance phases; each phase requires exposing the potion to a specific focus for a certain number of seconds.

The laws of alchemy dictate:
- The resonance phases for a given potion must be performed in their listed order (a phase can only begin after the potion's previous phase has completely finished).
- Each magical focus can only be actively resonating with one potion at any given time.
- Once a resonance phase begins, it must run continuously to completion without any interruption.
- Between phases, a potion remains perfectly stable and can wait indefinitely.

You must orchestrate all resonance phases such that the time at which the **last** phase of the final potion completes is as small as possible. Report this minimum possible completion time.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes the requirements for one potion: an integer **o** (the number of resonance phases) followed by **o** pairs of integers `focus duration` (1 ≤ focus ≤ m, 1 ≤ duration ≤ 1000), listing the potion's phases in order.
The total number of phases across all potions is at most 50.

## Output

Print a single integer: the smallest possible time (in seconds) at which all potions are fully brewed.

## Examples

### Example 1

**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```

**Output**
```
8
```

### Example 2

**Input**
```
1 3
3 1 5 2 3 3 2
```

**Output**
```
10
```

### Example 3

**Input**
```
2 3
1 1 4
1 2 3
```

**Output**
```
4
```

## Note

In Example 1, two identical potions each require foci 1, 2, and 3 in sequence (for 2 seconds each); the second potion trails the first through the sequence of foci and finishes at 8 seconds. In Example 3, the two potions require different foci and can be resonated in parallel, finishing at 4 seconds.
