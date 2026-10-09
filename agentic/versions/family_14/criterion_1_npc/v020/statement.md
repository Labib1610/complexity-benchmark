# Problem A — Diplomatic Translation

Time limit: 5 s   Memory limit: 256 MB

## Description

A galactic council includes representatives who speak various languages, indexed from 1 to **n**. Among these, **t** specific languages are designated as *primary*. The council must ensure that a concept originating in any primary language can be perfectly translated into every other primary language.

To facilitate this, the council can hire bilingual interpreters. Each available interpreter is certified in exactly two languages and requires a specific salary. Once hired, an interpreter can translate back and forth between their two languages as many times as needed. Translations can be chained: if an interpreter translates a concept from language A to language B, another interpreter can translate it from language B to language C. The council may also hire interpreters for non-primary languages if using them as intermediate translation steps results in a lower overall cost.

Find the minimum total salary the council must pay to hire a set of interpreters that allows full mutual translation between all primary languages.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the indices of the primary languages.
Each of the following **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that an interpreter is available to translate between language **u** and language **v** for a salary of **w**.
The available interpreters are guaranteed to be capable of establishing the required translations.

## Output

Print a single integer: the minimum total salary for the hired interpreters.

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

In Example 1, translating through the non-primary language 4 (salaries 1+1+1 = 3) is cheaper than hiring interpreters to translate between the three primary languages directly (which would cost 4). In Example 3, there is only one primary language, so no interpreters are needed.
