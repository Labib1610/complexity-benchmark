# Problem A — Translating for the Delegated Languages

Time limit: 5 s   Memory limit: 256 MB

## Description

A summit features **n** languages (numbered 1..n). Certain pairs of languages can be bridged by a bilingual translator at a given hiring fee. Among the languages, **t** are **delegated** and must all end up connected to each other through the translators you hire (directly or through intermediate languages). The remaining languages are optional intermediaries: you may route translations through them if it helps, or ignore them.

Hire a set of translators of minimum total fee so that all delegated languages are connected. Report that minimum total fee.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the delegated languages.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a bilingual translator bridging languages u and v at fee w.
The available translators are enough to connect all delegated languages.

## Output

Print a single integer: the minimum total fee to connect all delegated languages.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, routing translations through the optional intermediary language 4 (fees 1+1+1 = 3) is cheaper than bridging the three delegated languages directly (which would cost 4). In Example 3 there is only one delegated language, so no translators are needed.
