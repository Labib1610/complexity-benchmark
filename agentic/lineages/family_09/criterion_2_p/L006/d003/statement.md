# Problem B — Interference-Free Monitoring

Time limit: 2 s   Memory limit: 256 MB

## Description

An intricate clockwork assembly contains **n** gears (numbered 1 to **n**) and **m** engagement points. Each engagement point links two specific gears. 

The manufacturer guarantees a specific structural property of this assembly: the gears can be perfectly divided into two camps, and every engagement point connects one gear from each camp; no engagement point joins two gears in the same camp. (You are not provided with this division into camps; you must infer it from the connections if necessary).

Your task is to install diagnostic sensors on exactly **k** of these gears. The sensors will interfere with one another if placed on gears that are joined by an engagement point. Thus, no two gears selected for sensors can share an engagement point.

A valid sensor set is not restricted to being a subset of a single camp; solutions may contain gears from both camps. In fact, some assemblies have a maximum possible number of non-interfering sensors strictly larger than the size of either camp. Feasibility must therefore be evaluated from the exact engagement structure, not from camp sizes alone.

Given the target number **k**, determine if it is possible to choose exactly **k** distinct gears for sensor installation without any interference. If it is possible, output a valid selection.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the following **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing an engagement point between gear **u** and gear **v**. No engagement point is listed more than once. The assembly is guaranteed to satisfy the two-camp structural property described above.

## Output

If exactly **k** gears can be successfully selected, print `YES` on the first line. On the second line, print the **k** distinct gear numbers that form your selection, separated by spaces. Any valid selection of **k** mutually non-engaging gears will be accepted.

If no such selection is possible, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```