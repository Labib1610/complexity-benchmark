# Problem A — Surface Treatment Cycles

Time limit: 5 s
Memory limit: 256 MB

## Description
A manufacturing facility is processing a batch of parts, which are uniquely identified by integers starting from 1 up to $3q$. These parts require a surface treatment inside a specialized chamber. 

The chamber operates in discrete cycles. During any single cycle, it must be loaded with exactly three parts. Due to chemical reactivity, you cannot arbitrarily group parts together. Instead, you are given a log of tested, safe configurations. Each configuration explicitly lists three parts that can safely share the chamber during a single cycle.

Your task is to select a series of configurations from the log to execute. The execution must satisfy the following operational rules:
- Every part in the batch must be loaded into the chamber for treatment.
- If a part is loaded into the chamber during more than one cycle, it will be destroyed by over-exposure.
- Only configurations from the provided log may be executed. 

You must determine if it is possible to execute a sequence of cycles that successfully treats the entire batch without destroying any parts.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 200$, $0 \le t \le 20000$). The total number of parts in the batch is exactly $3q$.
Each of the following $t$ lines contains three integers $a$, $b$, and $c$ ($1 \le a < b < c \le 3q$), representing one safe configuration from the log.

## Output
If a successful treatment plan can be formed, print `YES` on the first line. Then, output $q$ lines, each containing the three parts of one executed configuration.
If no such plan is possible, print `NO`.

## Examples
### Example 1
Input:
```
2 3
1 2 3
4 5 6
1 4 5
```
Output:
```
YES
1 2 3
4 5 6
```
