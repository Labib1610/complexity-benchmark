# Problem A — Translating for the Delegated Languages

Time limit: 5 s   Memory limit: 256 MB

## Description

A summit features **n** languages (numbered 1..n). You can purchase translation modules to facilitate communication. Each module is listed as a pair of languages and a fee. Purchasing the module for languages `u` and `v` at fee `w` provides two one-way translation capabilities: from `u` to `v`, and from `v` to `u`. 

Among the languages, **t** are **delegated**. You must purchase a set of modules such that for every possible ordered pair of delegated languages $(A, B)$, a document can be translated from $A$ to $B$ through a sequence of one-way capabilities provided by your purchased modules. Languages that are not delegated may be used as intermediate steps in these sequences.

Find the minimum total fee required to purchase a valid set of modules.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the delegated languages.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000) representing a translation module between languages u and v available for fee w.
The available modules are enough to satisfy the requirement for all delegated languages.

## Output

Print a single integer: the minimum total fee to purchase a valid set of modules.

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

In Example 1, purchasing the modules involving the intermediate language 4 (total fee 1+1+1 = 3) allows documents to be translated between any ordered pair among 1, 2, and 3. This is cheaper than purchasing modules to translate between the three delegated languages directly (which would cost 4). In Example 3 there is only one delegated language, so no modules need to be purchased.