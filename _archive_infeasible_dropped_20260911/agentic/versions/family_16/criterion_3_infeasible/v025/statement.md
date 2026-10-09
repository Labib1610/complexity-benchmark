# Pipeline Configuration Validator

Time limit: 2 s   Memory limit: 256 MB

## Description

You are writing a diagnostic tool for a manufacturing pipeline. The pipeline must fulfill **j** orders within a strict operational window of **T** minutes. 

The manufacturing process consists of two sequential stages:
1. **Forming** (Stage 1)
2. **Painting** (Stage 2)

Each order must first be formed, and only after forming is complete can it be painted. Each stage contains exactly one machine, meaning a stage can process only one order at a time.

Your diagnostic tool must analyze the configuration and report the critical violation that prevents the pipeline from operating within the **T**-minute window. The tool must check for the following two types of violations:

- **Individual Order Violation:** An order cannot possibly be completed within the operational window if its own forming time plus its painting time exceeds **T**. If order **i** (1-indexed) violates this, your tool must output `JOB i`.
- **Stage Capacity Violation:** A stage cannot process all orders if the sum of processing times for that stage across all **j** orders exceeds **T**. If stage **c** (where **c** is 1 for forming, or 2 for painting) violates this, your tool must output `LOAD c`.

The constraints of the test environment ensure that every provided configuration contains exactly one of these violations. Your task is to implement the diagnostic tool to identify and print the correct violation code.

## Input

The first line of the input contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000), representing the number of orders and the operational window in minutes.

The following **j** lines each contain two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000). The **i**-th of these lines specifies the forming time (**p1**) and painting time (**p2**) required for order **i**.

## Output

Print a single line containing the violation code: either `JOB i` if order **i** exceeds the operational window, or `LOAD c` if stage **c** exceeds the operational window.

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

In Example 1, the first order requires 70 + 60 = 130 minutes of continuous processing. Since this exceeds the 100-minute window, the tool outputs `JOB 1`.

In Example 2, no single order exceeds the 150-minute window. However, the forming stage (Stage 1) requires 50 + 50 + 50 + 50 = 200 minutes of total active work, which exceeds 150. Thus, the tool outputs `LOAD 1`.
