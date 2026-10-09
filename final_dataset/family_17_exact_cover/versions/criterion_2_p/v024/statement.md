# Workload Migration Plan

Time limit: 2 s
Memory limit: 256 MB

## Description
A datacenter must migrate workloads from $q$ legacy servers (identifiers $1$ through $q$) to $q$ new virtual machines (identifiers $q+1$ through $2q$).

Due to architecture differences, a legacy server can only run on a virtual machine if their hardware profiles are certified as compatible. You will be provided with a list of $t$ certified combinations, each indicating that a specific legacy server can safely migrate to a specific virtual machine.

A valid migration plan must execute a complete 1-to-1 transfer. This means every legacy server must be assigned to exactly one virtual machine, and every virtual machine must receive exactly one legacy server. Furthermore, every assigned pair in the plan must appear on the list of certified combinations.

Determine whether a complete migration plan exists that successfully pairs all $2q$ systems. If such a plan is possible, output the assignments; otherwise, report that it cannot be done.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of legacy servers (which is also the number of virtual machines) and the number of certified combinations.
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that legacy server $a$ is compatible with virtual machine $b$.

## Output
If a complete migration plan is possible, print `YES` on the first line. Then, print $q$ lines, each containing the two identifiers of one chosen pair in your plan.
If no such plan is possible, print `NO`.

## Example 1

### Input
```
3 4
1 4
2 4
2 5
3 6
```

### Output
```
YES
1 4
2 5
3 6
```

## Example 2

### Input
```
2 2
1 3
2 3
```

### Output
```
NO
```
