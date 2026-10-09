# Problem A — Universal Translation Network

Time limit: 5 s
Memory limit: 256 MB

## Description

A global organization needs to ensure that documents can be translated between a specific set of **t** critical languages. 

There are **n** languages in total, numbered 1 to **n**. The organization can choose from **m** available bilingual contractors. Each contractor translates between exactly two languages and charges a fixed hiring fee. Once hired, a contractor can perform any number of translations between their two specific languages in either direction without additional cost. 

You may also hire contractors for non-critical languages if routing translations through them creates a cheaper overall chain (for example, translating from critical language A to non-critical language C, and then from C to critical language B).

Your objective is to hire a subset of contractors for the minimum total hiring fee so that a document starting in any of the **t** critical languages can be translated into any other critical language, possibly by passing through multiple hired contractors. 

Find the minimum total hiring fee required to achieve this.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers representing the identifiers of the critical languages.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a contractor is available to translate between language **u** and language **v** for a hiring fee of **w**.
The available contractors are always sufficient to make all critical languages mutually translatable.

## Output

Print a single integer: the minimum total hiring fee required.

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

In Example 1, hiring contractors to translate between languages 1 and 4, 2 and 4, and 3 and 4 costs 1 + 1 + 1 = 3. This allows a document in any of the three critical languages (1, 2, 3) to be translated to any other by passing through language 4. This is cheaper than hiring contractors to translate directly between the critical languages, which would cost at least 4. 

In Example 3, there is only one critical language, so no contractors need to be hired.
