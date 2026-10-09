# Directorate Drill Allocation

Time limit: 2 s   Memory limit: 256 MB

## Description
A facility directorate is preparing for a system-wide drill. This requires partitioning a pool of hardware assets into synchronized pairs. There are $2q$ assets in the inventory, assigned sequential identification numbers from $1$ up to $2q$. The pairing protocol mandates a rigid separation: any operational pair must consist of exactly one asset from the primary tier (identifiers $1$ to $q$) and exactly one asset from the secondary tier (identifiers $q+1$ to $2q$).

Because of firmware limitations, synchronization is only possible between specific primary and secondary assets. A complete registry of these certified links is provided. 

To prevent power grid overloads and logic faults, your deployment must adhere to the following safety constraints:
1. The registry guarantees that for every certified link between a primary asset $a$ and a secondary asset $b$, the condition $b - a \ge 1$ holds true.
2. The total number of active pairs in your final configuration must be strictly less than $q + 1$.

Your objective is to achieve a comprehensive deployment. You need to activate a subset of the certified links so that every single asset in the inventory is part of exactly one operational pair. No asset may remain unused, and no asset may participate in multiple pairs. Evaluate if the registry permits a deployment that meets all safety constraints and covers all $2q$ assets. If a valid configuration exists, output it. If it cannot be done, state that it is impossible.

## Input
The first line specifies two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), where $q$ dictates the tier sizes and $t$ is the number of certified links.
Each of the subsequent $t$ lines provides two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$). This indicates that primary asset $a$ can synchronize with secondary asset $b$.

## Output
If a comprehensive deployment can be achieved, output `YES` on the initial line. Following this, output exactly $q$ lines, each containing the two asset identifiers of an activated pair. If no such deployment can be formed, output `NO`.

## Example
### Input
```
3 5
1 4
1 5
2 4
2 6
3 5
```

### Output
```
YES
1 4
2 6
3 5
```
