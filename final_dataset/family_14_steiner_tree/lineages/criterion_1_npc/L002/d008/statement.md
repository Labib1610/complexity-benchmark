# Problem A — Subset Fragmentation

Time limit: 5 s
Memory limit: 256 MB

## Description
Consider a finite universe $E = \{1, 2, \dots, n\}$. 
You are given a target subset $T \subseteq E$ consisting of $t$ elements.

You are also provided with a pool of $m$ available pairs of elements from $E$. Each pair is specified by two distinct elements $\{u, v\}$ and has an associated activation cost $w$.

For any subset $Y \subseteq E$ and any set $A \subseteq E$, we say that $Y$ *splits* $A$ if $Y$ contains at least one element of $A$, but does not contain all elements of $A$. (Equivalently, $Y \cap A$ is a strictly proper, non-empty subset of $A$.)

Your objective is to activate a collection of the available pairs, forming a set $S$, such that the following condition is met:
Any subset $Y \subseteq E$ that splits the target set $T$ must also split at least one of the pairs in $S$.

Write a program to calculate the minimum total cost necessary to ensure this condition is met.

## Input
The first line contains three integers $n$, $m$, and $t$.
The size of the universe $n$ satisfies $1 \le n \le 100$. The number of available pairs $m$ satisfies $0 \le m \le n(n-1)/2$. The number of target elements $t$ satisfies $1 \le t \le 10$.

The second line contains $t$ distinct integers: the elements of the target subset $T$.

Each of the next $m$ lines contains three integers $u$, $v$, and $w$, representing an available pair $\{u, v\}$ that requires an activation cost of $w$. The integers $u$ and $v$ identify the two distinct elements involved ($1 \le u \le n$, $1 \le v \le n$, $u \neq v$). The cost $w$ satisfies $1 \le w \le 1000000$.

It is guaranteed that the available pairs are sufficient to ensure the condition can be met.

## Output
Print a single integer: the minimum total cost to ensure the target condition is met.

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
In Example 1, the target elements are 1, 2, and 3.
If we activate the pairs $\{1, 4\}$, $\{2, 4\}$, and $\{3, 4\}$, the set $S$ contains three pairs.
Suppose a subset $Y \subseteq \{1, 2, 3, 4\}$ splits $T = \{1, 2, 3\}$.
This means $Y$ contains at least one element of $\{1, 2, 3\}$ and omits at least one element of $\{1, 2, 3\}$.
We must check if $Y$ splits at least one pair in $S$.
If $Y$ does not split any pair in $S$, then for each pair in $S$, $Y$ must either contain both elements or neither.
Thus, $Y$ must contain 1 if and only if it contains 4 (from $\{1, 4\}$).
Similarly, $Y$ contains 2 if and only if it contains 4, and $Y$ contains 3 if and only if it contains 4.
This forces $Y$ to either contain all of $\{1, 2, 3, 4\}$ or none of them.
Consequently, $Y$ either contains all of $T$ or none of $T$, meaning $Y$ cannot split $T$.
This contradicts our assumption that $Y$ splits $T$. Thus, any $Y$ that splits $T$ must indeed split at least one pair in $S$.
The cost of this selection is $1+1+1=3$. This is more cost-effective than activating pairs directly among the target elements, which would cost at least 4.

In Example 3, there is only one target element: 1.
A set $Y$ splits $T = \{1\}$ if $Y$ contains some but not all elements of $T$. However, since $T$ has only one element, it is impossible for $Y$ to contain some but not all elements of $T$.
Thus, the condition "Any subset $Y$ that splits $T$ must also split at least one pair in $S$" is vacuously satisfied even if $S$ is empty.
No pairs need to be activated, resulting in a minimum cost of 0.