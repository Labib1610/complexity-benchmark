# Pipeline Stage 2: Safe Batch Selection

Time limit: 2 s   Memory limit: 256 MB

## Description

In our automated deployment pipeline, the process of deploying microservices to the testing environment is divided into three consecutive stages:

**Stage 1: Conflict Analysis.** A static analysis tool examines **n** available microservices (numbered 1 to **n**) and identifies **m** pairs that share a mutable database table. These are flagged as conflicting pairs. By design, the microservices implicitly belong to one of two architectural tiers (though their specific tier assignments are not provided to you). The analyzer guarantees that conflicts only ever occur between a microservice in one tier and a microservice in the other tier. Two microservices in the same tier never conflict. 

**Stage 2: Safe Batch Selection (Your Task).** The deployment coordinator receives the list of microservices and the conflicting pairs from Stage 1. It must select exactly **k** distinct microservices to form a "safe batch." A batch is safe if absolutely no two microservices within it conflict with each other. You must determine if such a batch can be formed, and if so, output the selection.

**Stage 3: Integration Testing.** The safe batch produced by Stage 2 is handed off to the container orchestration engine, which deploys them to an isolated cluster for performance testing.

Your software is only responsible for executing **Stage 2**. You will be given the output from Stage 1, and you must generate the exact batch selection required to initiate Stage 3.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
The following **m** lines provide the conflict data from Stage 1. Each line contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a conflicting pair of microservices. No pair is listed more than once. It is guaranteed that the pairs adhere to the two-tier structure described in Stage 1.

## Output

If a safe batch of exactly **k** microservices can be formed for Stage 3, print `YES` on the first line. On the second line, print the **k** distinct microservice numbers that form this batch, separated by spaces. If multiple safe batches of size **k** exist, any of them is accepted.

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
