# Module 2: Roster Allocation

Time limit: 1 s   Memory limit: 256 MB

The annual company review process consists of three distinct modules executed in sequence. First, the HR analytics engine scans past incident reports to compile a list of personnel who cannot work together. 

Your task is to implement the second module: the roster allocation processor. This processor receives the list of incompatibilities and must divide the $n$ personnel into exactly two operational blocks, designated Block 1 and Block 2. To ensure a safe environment, no two personnel flagged by the HR engine as incompatible can be assigned to the same block. 

If it is impossible to divide the personnel in this manner, the processor must abort the workflow. Furthermore, whenever multiple valid divisions are possible, the compliance protocol requires the processor to output the one that yields the lexicographically smallest sequence of block assignments (where the sequence is formed by the block numbers assigned to personnel 1 through $n$).

Finally, the output of your module is fed into the third module, the payroll system, which uses these block designations to apply shift differentials and finalize the weekly pay schedule.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of personnel and the number of incompatible pairs identified by the first module.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — a pair of personnel who cannot share the same operational block.

## Output
If the roster allocation processor cannot find any valid division, output a single line with `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1 \dots s_n$ (each either `1` or `2`), representing the block assigned to each person from $1$ to $n$. This sequence must be the lexicographically smallest valid assignment.

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
