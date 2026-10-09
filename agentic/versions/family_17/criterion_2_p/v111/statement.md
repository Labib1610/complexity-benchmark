# Complete Neutralization

Time limit: 2 s   Memory limit: 256 MB

## Description
A hazardous waste processing facility needs to neutralize a batch of volatile materials. The batch consists of $2q$ discrete samples, each assigned a unique identifier from $1$ to $2q$. 

You are provided with a database of $t$ possible fusion protocols. Each protocol specifies exactly two samples that can be reacted together to form an inert byproduct. The facility's control system must evaluate the power set of these $t$ available protocols. A configuration is defined by selecting a subset of these protocols. Since there are $t$ possible protocols, the configuration space contains $2^t$ candidates.

A candidate configuration is deemed successful only if it satisfies the exact cover constraint: the selected protocols must collectively consume all $2q$ samples, with each sample participating in exactly one protocol. Due to the chemical properties of the batch, the samples with identifiers $1$ through $q$ are acidic, while those from $q+1$ to $2q$ are alkaline. An inspection of the database reveals that every provided protocol pairs one acidic sample with one alkaline sample.

Determine whether a valid configuration exists within the $2^t$ search space. If it does, output the chosen protocols; otherwise, report that no configuration can be formed.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), denoting a protocol that reacts sample $a$ with sample $b$.

## Output
If a valid configuration is found in the search space, print `YES` on the first line. Then, print $q$ lines, each containing the two identifiers of a selected protocol. If no subset of protocols can satisfy the constraints, print `NO`.

## Example

### Input
```
3 4
1 4
2 5
3 6
1 5
```

### Output
```
YES
1 4
2 5
3 6
```
