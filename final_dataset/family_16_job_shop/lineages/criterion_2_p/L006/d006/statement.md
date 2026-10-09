# Problem B — Signal Processing Pipeline

Time limit: 1 s   Memory limit: 256 MB

## Description

You are optimizing a signal processing pipeline consisting of **j** different stages. The signal starts with an intensity of $V = 0$.

Each stage is characterized by two parameters: **p1** and **p2**.
When the signal passes through a stage, its current intensity $V$ is updated to a new intensity $V'$ according to the following formula:
$V' = \max(p2, V - p1 + p2)$

You must arrange all **j** stages into a single sequential pipeline of your choosing. Each stage must be used exactly once.

The overall "inefficiency rating" of your pipeline is defined as the sum of the **p1** parameters of all stages, plus the final signal intensity $V$ after passing through the entire pipeline.

Find an execution order for the stages that makes this inefficiency rating as small as possible. Report this minimum possible inefficiency rating.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the parameters for a stage.

## Output

Print a single integer: the minimum possible inefficiency rating.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 1, an optimal arrangement runs the stages in the order of the 3rd, 2nd, and 1st from the input.
- The sum of the **p1** parameters of all stages is $3 + 2 + 1 = 6$.
- The signal starts at $V = 0$.
- For the 3rd input stage ($p1=1, p2=3$): $V$ becomes $\max(3, 0 - 1 + 3) = \max(3, 2) = 3$.
- For the 2nd input stage ($p1=2, p2=4$): $V$ becomes $\max(4, 3 - 2 + 4) = \max(4, 5) = 5$.
- For the 1st input stage ($p1=3, p2=2$): $V$ becomes $\max(2, 5 - 3 + 2) = \max(2, 4) = 4$.
The final signal intensity $V$ is 4.
The inefficiency rating is $6 + 4 = 10$.