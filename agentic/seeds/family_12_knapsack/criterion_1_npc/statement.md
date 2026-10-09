# Problem A — Portfolio Selection

Time limit: 5 s   Memory limit: 256 MB

## Description

An allocation board weighs **n** candidate initiatives, each with a cost and a value, against a fixed budget **B**. An initiative is funded in full or not at all — no partial funding. The board wants the funded subset whose total cost stays within B while the total value is as large as possible, and must report that maximum value together with a subset achieving it. Themes and sponsors are irrelevant; only costs, values, and the budget matter. The costs and values here span a wide range, so the value achievable at each budget level does not compress into a small table, and greedy value-per-cost picks do not in general reach the optimum. Report the maximum achievable total value within budget.

## Input

The first line contains two integers **n** and **B** (1 ≤ n ≤ 40, 0 ≤ B ≤ 40000000000).
Each of the next **n** lines contains two integers **cost** and **value** (1 ≤ cost ≤ 1000000000, 1 ≤ value ≤ 1000000000) for one investment.

## Output

On the first line print the maximum total value achievable within the budget.
On the second line print the 1-based indices of the chosen investments, separated by spaces (any subset achieving the maximum value with total cost ≤ B is accepted). If the best choice is to take nothing (maximum value 0), leave the second line blank.

## Examples

### Example 1

**Input**
```
4 10
2 3
3 4
4 5
5 6
```

**Output**
```
13
1 2 4
```

### Example 2

**Input**
```
3 1
5 100
6 100
7 100
```

**Output**
```
0

```

### Example 3

**Input**
```
1 5
3 7
```

**Output**
```
7
1
```

## Note

In Example 1, investments 1, 2, and 4 cost 2+3+5 = 10 (within budget) and give value 3+4+6 = 13. In Example 2, every investment costs more than the budget, so nothing can be taken.
