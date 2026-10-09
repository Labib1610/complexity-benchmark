# Pipeline Stage 2: Safe Batch Selection

Time limit: 2 s   Memory limit: 256 MB

## Description

In our automated deployment pipeline, the process of deploying microservices to the testing environment is divided into three consecutive stages.

**Stage 1: Conflict Analysis.** A static analysis tool examines **n** available microservices (numbered 1 to **n**) and identifies **m** pairs that share a mutable database table. These are flagged as conflicting pairs. The conflict relationship is symmetric: if microservice **u** conflicts with **v**, then **v** conflicts with **u**. The static analysis tool ensures a specific structural property regarding these conflicts: there are absolutely no odd-length cycles. That is, any sequence of distinct microservices that forms a closed loop of conflicts will always consist of an even number of microservices.

**Stage 2: Safe Batch Selection (Your Task).** The deployment coordinator receives the list of microservices and the conflicting pairs from Stage 1. It must select exactly **k** distinct microservices to form a "safe batch." A batch is safe if absolutely no two microservices within it conflict with each other. You must determine if such a batch can be formed, and if so, output the selection. If multiple valid safe batches of size **k** exist, any one of them is accepted.

**Stage 3: Integration Testing.** The safe batch produced by Stage 2 is deployed to an isolated cluster for performance testing.

Your software is only responsible for executing **Stage 2**. You will be given the output from Stage 1, and you must generate a valid batch selection.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
The following **m** lines provide the conflict data. Each line contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a conflicting pair of microservices. No pair is listed more than once. It is guaranteed that the conflict data contains no odd-length cycles, as verified by Stage 1.

## Output

If a safe batch of exactly **k** microservices can be formed, print `YES` on the first line. On the second line, print the **k** distinct microservice numbers that form this batch, separated by spaces. If multiple safe batches of size **k** exist, any of them is accepted.

If it is impossible to form a safe batch of size **k**, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```