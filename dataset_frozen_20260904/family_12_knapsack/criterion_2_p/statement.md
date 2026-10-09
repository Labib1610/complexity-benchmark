# Problem B — Portfolio Selection (Small Costs)

Time limit: 2 s   Memory limit: 256 MB

## Description

You are choosing among **n** investments. Investment **i** has a **cost** and a **value**. You have a total budget **B**. You may either take an investment whole or not take it at all — no partial investments.

Choose a subset of investments whose total cost does not exceed **B** so that the total value is as large as possible.

## Input

The first line contains two integers **n** and **B** (1 ≤ n ≤ 2000, 0 ≤ B ≤ 2000).
Each of the next **n** lines contains two integers **cost** and **value** (1 ≤ cost ≤ 100, 1 ≤ value ≤ 1000000000) for one investment.

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

This is the same 0/1 selection problem as Problem A. The only difference is that here the costs and the budget are small, which makes an efficient exact solution possible. In Example 1, investments 1, 2, and 4 cost 2+3+5 = 10 (within budget) and give value 3+4+6 = 13.
