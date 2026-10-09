# Problem A — Stable Synthesis

Time limit: 5 s   Memory limit: 256 MB

## Description

You are working with a set of **n** distinct protein markers (numbered 1 through **n**). Laboratory tests have identified **m** specific pairs of markers that are mutually reactive. If any mutually reactive pair is included in the same mixture, the mixture will denature and fail.

Your goal is to synthesize a stable mixture containing exactly **k** distinct markers. A mixture is considered stable if and only if no two markers within it are mutually reactive.

Given the reactivity data and the target size **k**, determine whether a stable mixture of exactly **k** markers can be formed, and if so, identify the markers to include.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ 1035, 1 ≤ k ≤ n). It is guaranteed that **m** does not exceed **n**·(**n**−1)/2.
Each of the following **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a mutually reactive pair of markers. No pair is listed more than once. Furthermore, for every given pair, the sum of their identifiers (**u** + **v**) will not exceed 2**n** − 1.

## Output

If a stable mixture of **k** markers exists, output `YES` on the first line. On the second line, output **k** distinct marker identifiers that form such a mixture, separated by spaces. If multiple stable mixtures exist, any valid one is accepted.

If no such mixture can be formed, output `NO`.

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
