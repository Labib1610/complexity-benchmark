# Problem B — Quantum Entanglement Basis

Time limit: 2 s   Memory limit: 256 MB

## Description

A quantum computer relies on forming a complete entanglement basis. The system consists of three distinct component groups, each containing exactly **k** units:
- **k** photon emitters, numbered 1..k,
- **k** quantum filters, numbered 1..k,
- **k** detector arrays, numbered 1..k.

An entanglement triplet consists of exactly one emitter, one filter, and one detector. You are provided with a list of **t** experimentally verified triplets that can be successfully entangled.

Your objective is to select exactly **k** triplets from the verified list to form a complete basis. A valid basis must use every emitter exactly once, every filter exactly once, and every detector exactly once. The configuration space of selecting **k** items from **t** possibilities is vast, and you must identify a valid configuration from among the $\binom{t}{k}$ possible subsets of triplets.

The system's hardware specification enforces a strict physical alignment: each emitter is physically hardwired to exactly one unique filter. Consequently, in the list of verified triplets, any specific emitter is only ever listed with its dedicated filter, and no filter is dedicated to more than one emitter.

Determine whether a complete entanglement basis can be formed. If it is possible, output one such valid configuration.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of units in each component group, and the number of verified triplets.

Each of the following **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k) representing a verified triplet consisting of emitter **x**, filter **y**, and detector **z**. No triplet is listed more than once. As per the hardware specification, for any given emitter **x**, all triplets containing **x** will feature the same filter **y**, and different emitters will feature different filters.

## Output

If a complete entanglement basis can be formed, print `YES` on the first line. Then print **k** lines, each containing the three integers `x y z` of a chosen triplet from the basis (in any order). If multiple valid bases exist, any of them will be accepted.

If no valid basis can be formed, print `NO`.

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
