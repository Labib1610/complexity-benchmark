# Problem A — Boolean Equivalence Synthesis

Time limit: 5 s
Memory limit: 256 MB

## Description

You are analyzing a system of $n$ boolean variables, indexed $1$ to $n$.

You are provided with a target set $T$ containing $t$ critical variables. Additionally, there is a pool of $m$ available candidate equivalence relations. Each candidate relation enforces the condition that two specific variables $u$ and $v$ must have the same truth value (i.e., $x_u \iff x_v$), and incurs a computational cost $w$ if selected.

Your objective is to select a subset $C$ from the pool of candidates to form a constraint system.

For any chosen subset $C$, an assignment of truth values (True or False) to all $n$ variables is considered *globally valid* if it satisfies every relation in $C$. 
We define the *projected assignment space* on $T$ as the set of all truth-value combinations for the variables in $T$ that can be extended to at least one globally valid assignment.

Your selection $C$ is considered valid if and only if the size of the projected assignment space on $T$ is exactly 2.

Your task is to find a valid selection $C$ that minimizes the total sum of the costs of the selected relations.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ 10, 1 ≤ **n** ≤ 100, 0 ≤ **m** ≤ **n**·(**n**−1)/2).  
The second line lists **t** distinct integers representing the indices in the target set $T$.  
Following this, there are **m** lines. Each line provides three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), indicating that a candidate relation between variable **u** and variable **v** is available for a cost of **w**.  
It is guaranteed that the available relations provide at least one valid selection.

## Output

Output a single integer representing the minimum possible total cost of a valid selection $C$.

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

In Example 1, we can select $C$ consisting of the relations between (1, 4), (2, 4), and (3, 4), which incurs a total cost of 1 + 1 + 1 = 3. 
- The target set is $T = \{1, 2, 3\}$.
- With these relations, any globally valid assignment must satisfy $x_1 \iff x_4$, $x_2 \iff x_4$, and $x_3 \iff x_4$.
- This logically implies $x_1 \iff x_2 \iff x_3$.
- The projected assignment space on $T$ therefore contains exactly 2 combinations: all True, and all False.
This selection is valid and optimal. Selecting relations only among the target indices would incur a cost of at least 4.

In Example 3, the target set $T = \{1\}$ has only one index. We can select $C$ as an empty set of relations.
- Any assignment of truth values to the 3 variables is globally valid since there are no relations to violate.
- The projected assignment space on $T$ contains the combinations where $x_1$ is True, and where $x_1$ is False.
- The size of this space is exactly 2.
Thus, zero relations need to be selected, resulting in a cost of 0.