# Problem B — Set System Activation

Time limit: 2 s
Memory limit: 256 MB

## Description

You are working with a universal set $U = \{1, 2, \dots, n\}$ and a specific target subset $T \subseteq U$ consisting of $t$ priority elements.

You are provided with a catalog of $m$ available pairs. Each available pair is a subset of exactly two elements $\{u, v\} \subset U$ and has an associated activation cost $w$.

Your objective is to activate a collection of these pairs to satisfy a structural requirement. Let $C$ be your chosen collection of activated pairs. The collection $C$ must satisfy the following property: 
For every possible subset $S \subset U$, if $S \cap T \neq \emptyset$ and $T \setminus S \neq \emptyset$, then there must exist at least one pair in $C$ that has exactly one element in $S$. (In other words, there must be some $\{u, v\} \in C$ such that $|\{u, v\} \cap S| = 1$).

You may activate pairs that do not contain any priority elements if they are needed to satisfy the condition.

You are given that $m = n - 1$. Furthermore, it is mathematically guaranteed that if you were to activate all $m$ available pairs, the property would hold for *all* non-empty proper subsets $S \subset U$ (meaning for any $S$ where $S \neq \emptyset$ and $U \setminus S \neq \emptyset$, there is at least one available pair $\{u, v\}$ such that $|\{u, v\} \cap S| = 1$).

Determine the minimum total activation cost required to choose a valid collection $C$ that satisfies the property for the target subset $T$.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1).
The second line lists **t** distinct integers representing the elements of the target subset $T$.
Following this are **m** lines, each containing three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000). These values indicate an available pair $\{u, v\}$ that can be activated at a cost of **w**.

## Output

Output a single integer representing the minimum possible total cost to activate a collection of pairs that satisfies the required property for $T$.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```