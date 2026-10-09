# Problem A — Compound Synthesis

Time limit: 5 s   Memory limit: 256 MB

## Description

A laboratory is synthesizing complex compounds. The inventory contains **k** distinct base fluids (labeled 1 through **k**), **k** catalysts (labeled 1 through **k**), and **k** thermal profiles (labeled 1 through **k**).

When mixed, a specific base fluid, a single catalyst, and one thermal profile form a reaction. However, only certain specific combinations of these three elements are stable. You are provided with a database of **t** stable reactions.

A full batch of experiments consists of a series of reactions. In this batch, no two reactions may share the same base fluid, nor the same catalyst, nor the same thermal profile. At the same time, no base fluid, catalyst, or thermal profile can be left unused.

Your task is to determine whether it is possible to select exactly **k** stable reactions from the database to form a full batch. If a full batch can be formed, you must also provide the list of the **k** reactions that achieve this.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the number of each type of ingredient and the number of stable reactions in the database.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a stable reaction made of base fluid **x**, catalyst **y**, and thermal profile **z**. No reaction is listed more than once.

## Output

If a full batch can be formed, print `YES` on the first line, then print **k** lines, each containing the three integers `x y z` of one chosen reaction. Any valid full batch is accepted; the reactions may be printed in any order.

If no full batch can be formed, print `NO`.

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

In Example 2, both stable reactions require catalyst 1, leaving catalyst 2 impossible to consume.
