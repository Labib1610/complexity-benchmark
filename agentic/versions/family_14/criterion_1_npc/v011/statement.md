# Universal Translation

Time limit: 5 s   Memory limit: 256 MB

## Description

A galactic federation has **n** known languages (numbered 1 to **n**). You are organizing an interstellar summit and must ensure that delegates speaking the **t** primary languages can all understand each other.

There are **m** freelance bilingual translators available for hire. Each translator is proficient in two specific languages and charges a one-time retainer fee to join your summit staff. Once hired, a translator can perform unlimited translations back and forth between their two languages.

You may also hire translators for languages outside the **t** primary ones, using those additional languages as intermediate stepping stones. For example, if you hire a translator between Primary Language A and Secondary Language X, and another between Secondary Language X and Primary Language B, delegates speaking A and B can communicate via X.

Find the minimum total retainer fee you must pay to hire a group of translators such that a message originating in any primary language can be translated (directly or through a chain of translators) into all other primary languages.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ 10, 1 ≤ **n** ≤ 100, 0 ≤ **m** ≤ **n**·(**n**−1)/2).
The second line contains **t** distinct integers: the IDs of the primary languages.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000): a translator proficient in languages **u** and **v** who charges a retainer fee of **w**.
The available translators are sufficient to ensure all primary languages can be connected.

## Output

Print a single integer: the minimum total retainer fee required to ensure all primary languages are mutually intelligible.

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

In Example 1, using language 4 as an intermediate pivot (hiring translators for 1-4, 2-4, and 3-4 at a total cost of 1+1+1 = 3) is cheaper than hiring translators to directly connect the three primary languages (which would cost 4). In Example 3, there is only one primary language, so no translators need to be hired.
