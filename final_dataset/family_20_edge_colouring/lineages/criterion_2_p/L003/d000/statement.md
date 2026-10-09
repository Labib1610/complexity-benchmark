# System Configuration for Exclusive Resource Locks

Time limit: 2 s   Memory limit: 256 MB

## Description
A high-performance computing cluster executes a batch of $m$ jobs. The cluster contains $n_L$ processing units (numbered 1 to $n_L$) and $n_R$ memory banks (numbered 1 to $n_R$). Each job specifies exactly one processing unit and exactly one memory bank that it must lock exclusively for its entire execution.

The system administrator must assign an execution phase (a positive integer) to each of the $m$ jobs. The constraints on this configuration are strict: if two jobs require the same processing unit, they cannot be assigned the same phase. Similarly, if two jobs require the same memory bank, they cannot be assigned the same phase. 

Let $\Delta$ be the peak contention of the batch—the maximum number of jobs that require any single specific processing unit or any single specific memory bank. Because a resource can only handle one job per phase, any valid configuration must use at least $\Delta$ phases. Your objective is to find a schedule that uses *exactly* $\Delta$ phases. 

The configuration space is vast, consisting of $\Delta^m$ possible phase assignments. You must navigate this massive search space to find a valid assignment where all resource conflict constraints are globally satisfied. Note that because every job requests exactly one resource from the processing pool and one from the memory pool, and no job requests two resources from the same pool, a valid configuration using exactly $\Delta$ phases is always guaranteed to exist.

You must output `YES` followed by a valid phase assignment for all $m$ jobs.

## Input
The first line contains three integers $n_L$, $n_R$, and $m$ ($1 \le n_L, n_R \le 100000$, $0 \le m \le 400000$).
The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le n_L$, $1 \le v \le n_R$), indicating that a job requires processing unit $u$ and memory bank $v$.

## Output
Print `YES` on the first line.
On the second line, print $m$ space-separated integers, each between $1$ and $\Delta$. The $i$-th integer represents the phase assigned to the $i$-th job in the input order.

## Example

### Input
```
3 3 4
1 1
1 2
2 1
3 3
```

### Output
```
YES
1 2 2 1
```
