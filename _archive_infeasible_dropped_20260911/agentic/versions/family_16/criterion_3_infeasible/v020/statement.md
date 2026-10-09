# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A manufacturing plant is assigned **j** work orders. Each order must pass through two distinct stages of assembly. You are provided with the required duration for the first stage and the required duration for the second stage for each order.

The assembly process is subject to the following physical rules:
- An order can only enter the second stage after its first stage is entirely completed.
- The facility for the first stage can only process a single order at a time.
- The facility for the second stage can only process a single order at a time.
- There is a strict time limit, **T**, by which all **j** orders must be fully completed through both stages.

For every dataset provided in this problem, it is guaranteed that meeting the time limit **T** is impossible, regardless of how the orders are sequenced. Your objective is not to search for a valid schedule, but rather to output a short certificate that proves the time limit is unachievable.

Exactly one of the following two reasons will always apply to the given data. Output the certificate for the one that holds:

- **Individual order violation**: A specific order requires so much time across both stages that it cannot finish by **T**, even if it were the only order in the plant. Print `JOB i`, where **i** is the 1-based index of such an order.
- **Stage capacity violation**: A specific stage requires more total time across all orders than **T**, meaning that stage alone cannot finish its work by the time limit. Print `LOAD c`, where **c** is either 1 (for the first stage) or 2 (for the second stage).

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
The following **j** lines each contain two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000), representing the duration of the order on the first stage and the second stage, respectively.

## Output

Print a single line containing either `JOB i` (if the sum of **p1** and **p2** for order **i** exceeds **T**) or `LOAD c` (if the sum of durations for all orders on stage **c** exceeds **T**).

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, the first order requires 70 + 60 = 130 time units in sequence. Since 130 > 100, `JOB 1` proves the deadline is impossible. 
In Example 2, no single order exceeds 150 time units. However, the first stage must process 50 + 50 + 50 + 50 = 200 units of work in total. Since 200 > 150, `LOAD 1` serves as the certificate.
