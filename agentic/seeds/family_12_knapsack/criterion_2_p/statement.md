# Problem B — Divisible Portfolio

Time limit: 1 s   Memory limit: 256 MB

## Description

You are choosing among **n** investments. Investment **i** has a **cost** and a **value**. You have a total budget **B**. Each investment is **divisible**: you may buy any fraction of it (between 0 and 1). Buying a fraction **f** of investment **i** costs **f · cost** and returns **f · value**.

Spend at most **B** in total to maximize the total value obtained.

## Input

The first line contains two integers **n** and **B** (1 ≤ n ≤ 200000, 0 ≤ B ≤ 1000000000).
Each of the next **n** lines contains two integers **cost** and **value** (1 ≤ cost ≤ 1000000000, 1 ≤ value ≤ 1000000000) for one investment.

## Output

Print the maximum total value obtainable, rounded to exactly **6 digits** after the decimal point.

## Examples

### Example 1

**Input**
```
3 50
10 60
20 100
30 120
```

**Output**
```
240.000000
```

### Example 2

**Input**
```
1 1
3 10
```

**Output**
```
3.333333
```

### Example 3

**Input**
```
2 100
10 60
20 100
```

**Output**
```
160.000000
```

## Note

In Example 1, buy investments 1 and 2 whole (cost 30, value 160) and two-thirds of investment 3 (cost 20, value 80), for a total value of 240. In Example 3 the budget exceeds the total cost, so everything can be bought.
