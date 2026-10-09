# Problem A — Value Unification Protocol

Time limit: 5 s   Memory limit: 256 MB

## Description

A system contains **n** variables, numbered 1 to **n**. Initially, variable **i** holds the value **i**.

You are provided with **m** transformation rules. Each rule can be activated by paying a one-time cost of **w** energy units. Once a rule between variable **u** and variable **v** is activated, it allows you to assign the current value of variable **u** to variable **v**, or the current value of variable **v** to variable **u**. An activated rule can be applied an unlimited number of times in any sequence.

You are given a list of **t** target variables. Your objective is to activate a subset of rules such that, by applying the activated rules in some sequence, it is possible for all **t** target variables to simultaneously hold the exact same value. You may use any of the **n** variables and apply the activated rules as many times as needed to achieve this.

Determine the absolute minimum total energy cost required to activate such a set of rules.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers representing the identities of the target variables.
The next **m** lines each provide three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a rule between variable **u** and variable **v** can be activated for a cost of **w** energy units.
It is guaranteed that some subset of rules allows all target variables to be made equal.

## Output

Output a single integer representing the minimum total energy cost required.

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

In Example 1, activating rules that allow values to pass between variable 4 and variables 1, 2, and 3 costs 1 + 1 + 1 = 3. This allows variables 1, 2, and 3 to all hold the same value, costing less than activating rules directly between 1, 2, and 3 (which costs 2 + 2 = 4).

In Example 3, with one target variable, the condition is already met, so the minimum cost is 0.