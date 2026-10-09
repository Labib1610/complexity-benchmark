# Problem C — Portfolio Selection: Certify Impossibility

Time limit: 2 s   Memory limit: 256 MB

## Description

You are choosing among **n** investments. Investment **i** has a **cost** (a strictly positive amount) and a **value**. You have a total budget **B**, and you must select **at least one** investment whose cost does not exceed **B**.

For every input in this problem it is **guaranteed that no investment is affordable** — every cost is strictly greater than the budget, so not even the cheapest one can be selected. Your job is not to search; it is to **prove** the impossibility with a short certificate that can be checked directly against the input.

Print a certificate of the form:

- `MIN m` — where **m** is an integer with **B < m** and **m ≤ every cost** (for example, m = the smallest cost). This proves that every investment costs more than the budget, so none can be selected.

## Input

The first line contains two integers **n** and **B** (1 ≤ n ≤ 100000, 1 ≤ B ≤ 1000000000).
Each of the next **n** lines contains two integers **cost** and **value** (1 ≤ cost ≤ 1000000000, 1 ≤ value ≤ 1000000000). Every cost is strictly greater than **B**.

## Output

Print a single line `MIN m`, where **m** is an integer satisfying **B < m ≤ (every cost)** — for instance, the minimum cost among all investments.

## Examples

### Example 1

**Input**
```
3 4
5 10
7 7
9 4
```

**Output**
```
MIN 5
```

### Example 2

**Input**
```
2 100
101 1
250 1
```

**Output**
```
MIN 101
```

## Note

In Example 1 the budget is 4 and the cheapest investment costs 5, so `MIN 5` proves every cost exceeds the budget. In Example 2 the cheapest cost is 101 > 100, so `MIN 101` is a valid certificate.
