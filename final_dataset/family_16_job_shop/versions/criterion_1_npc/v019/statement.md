# Problem A — Alchemical Concoctions

Time limit: 5 s   Memory limit: 256 MB

## Description

An alchemist is preparing **j** complex elixirs using **m** specialized pieces of apparatus. Each elixir requires a strict sequence of brewing phases. For each phase, the elixir must be placed in a specific apparatus for a continuous number of minutes. The rules of alchemy dictate:

- An elixir's phases must be completed in their listed order (a phase can only begin after the elixir's preceding phase has completely finished).
- Each apparatus can only hold and process one elixir at a time.
- Once an apparatus begins a phase for an elixir, it must continue without pause until that phase is finished.

Plan the entire brewing process so that the time at which the **last** phase finishes is as small as possible. Report that smallest possible finish time.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one elixir: an integer **o** (the number of phases) followed by **o** pairs of integers `apparatus duration` (1 ≤ apparatus ≤ m, 1 ≤ duration ≤ 1000), listing the elixir's phases in order.
The total number of phases across all elixirs is at most 50.

## Output

Print a single integer: the smallest possible number of minutes at which all elixirs are completely brewed.

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

In Example 1, two identical elixirs each pass through apparatuses 1, 2, and 3 (2 minutes each); the second elixir trails the first through the sequence and finishes at 8 minutes. In Example 3 the two elixirs use different apparatuses and brew simultaneously, finishing at 4 minutes.
