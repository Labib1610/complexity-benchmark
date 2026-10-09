# Problem A — Hiring Translators

Time limit: 5 s   Memory limit: 256 MB

## Description

A galactic council recognizes **n** languages (numbered 1..n). Certain pairs of languages can be bridged by hiring a bilingual interpreter at a given salary. Among the languages, **t** are **core** and must all end up able to communicate with each other through the interpreters you hire (directly or through intermediate languages). The remaining languages are optional relays: you may route translations through them if it helps, or ignore them.

Hire a set of interpreters of minimum total salary so that all core languages can communicate. Report that minimum total salary.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the core languages.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): an interpreter bridging languages u and v for a salary of w.
The available interpreters are enough to allow all core languages to communicate.

## Output

Print a single integer: the minimum total salary to allow all core languages to communicate.

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

In Example 1, routing translations through the optional relay language 4 (salaries 1+1+1 = 3) is cheaper than bridging the three core languages directly (which would cost 4). In Example 3 there is only one core language, so no interpreters are needed.
