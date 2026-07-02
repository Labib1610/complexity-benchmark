# Problem C — Empty Budget

Time limit: 1 s   Memory limit: 256 MB

## Description

You are choosing among **n** investments. Investment **i** has a **cost** (a strictly positive amount) and a **value**. You have a total budget **B**, and you must select **at least one** investment whose total cost does not exceed **B**.

In the input you are given, the budget is **B = 0** while every investment costs a positive amount. Since any chosen investment would cost more than the budget allows, it is impossible to select even one.

Determine whether a valid selection of at least one investment exists.

## Input

The first line contains two integers **n** and **B** (1 ≤ n ≤ 200000, B = 0).
Each of the next **n** lines contains two integers **cost** and **value** (1 ≤ cost ≤ 1000000000, 1 ≤ value ≤ 1000000000) for one investment.

## Output

Print a single line containing `NO`, since no investment can be afforded within a budget of 0.

## Examples

### Example 1

**Input**
```
3 0
5 10
3 7
2 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
2 0
100 1
1 1
```

**Output**
```
NO
```

## Note

With a budget of 0 and every cost strictly positive, no investment can be selected.
