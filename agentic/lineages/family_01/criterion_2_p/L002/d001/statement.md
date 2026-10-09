# Module 2: Clearance Allocation

Time limit: 1 s   Memory limit: 256 MB

The annual company review process consists of three distinct modules executed in sequence. First, the HR analytics engine scans past incident reports to compile a list of personnel interactions that require strict oversight. 

Your task is to implement the second module: the clearance allocation processor. This processor receives the list of interactions and must assign each of the $n$ personnel a security clearance level of either `1` or `2`. To maintain operational safety, for each interaction between personnel $u$ and $v$ flagged by the HR engine, the product of the clearance level assigned to $u$ and the clearance level assigned to $v$ must be exactly 2.

If it is impossible to assign clearance levels in this manner, the processor must abort the workflow. Furthermore, whenever multiple valid assignments are possible, the compliance protocol requires the processor to output the one that yields the lexicographically smallest sequence of clearance levels (where the sequence is formed by the levels assigned to personnel 1 through $n$).

Finally, the output of your module is fed into the third module, the payroll system, which uses these clearance designations to apply shift differentials and finalize the weekly pay schedule.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of personnel and the number of interactions identified by the first module.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — a pair of personnel whose clearance levels must have a product of exactly 2.

## Output
If the clearance allocation processor cannot find any valid assignment, output a single line with `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1 \dots s_n$ (each either `1` or `2`), representing the clearance level assigned to each person from $1$ to $n$. This sequence must be the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```