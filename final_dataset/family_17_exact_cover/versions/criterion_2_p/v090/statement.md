# Workload Migration Plan

Time limit: 2 s
Memory limit: 256 MB

## Description
A datacenter is upgrading its infrastructure. There are $q$ outdated software modules (numbered $1$ to $q$) and $q$ next-generation execution nodes (numbered $q+1$ to $2q$).

An engineering audit has produced $t$ compatibility signatures. Each signature verifies that a particular outdated module can operate on a particular next-generation node.

Your task is to organize a full system upgrade. To do this, you must distribute the outdated modules among the next-generation nodes such that:
- Every outdated module is hosted by a next-generation node.
- No next-generation node hosts more than one outdated module.
- Every hosting arrangement is supported by an existing compatibility signature.

Because there are exactly $q$ modules and $q$ nodes, a successful upgrade will naturally utilize all available nodes.

Determine if a full system upgrade is achievable. If it is, output the allocations; otherwise, report that it cannot be done.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$). Here $q$ represents both the number of outdated modules and the number of next-generation nodes, while $t$ is the number of compatibility signatures.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), denoting a compatibility signature between outdated module $a$ and next-generation node $b$.

## Output
If a full system upgrade is achievable, print `YES` on the first line. Then, print $q$ lines, each containing two integers: the identifier of an outdated module and the identifier of the next-generation node hosting it.
If a full system upgrade cannot be achieved, print `NO`.

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
