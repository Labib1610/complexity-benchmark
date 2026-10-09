# Problem A — Harmonious Delegation

Time limit: 5 s   Memory limit: 256 MB

## Description

A corporate department has **n** employees (numbered 1..n) and a record of **m** friction events. Each friction event involves a specific pair of employees who experienced a severe disagreement.

A project delegation is **harmonious** if no single friction event has both of its participants included in the delegation.

Given a target delegation size **k**, decide whether a harmonious delegation of exactly **k** employees exists, and if so report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing the two employees involved in a friction event. The input will never contain more than one friction event involving the same pair of employees (i.e., no pair of employees appears more than once, regardless of order).

## Output

If a harmonious delegation of **k** employees exists, print `YES` on the first line, then on the second line print **k** distinct employee numbers forming such a delegation, separated by spaces. Any delegation that satisfies the condition is accepted. Print the **k** delegation members (not the remaining employees).

If no such delegation exists, print `NO`.

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

## Note

A harmonious delegation ensures that for every recorded friction event, the delegation does not contain both of the involved employees. In Example 2, employees 1, 3, and 5 have no friction events among them. In Example 1, no three of the four employees can be selected without including both participants of at least one friction event.