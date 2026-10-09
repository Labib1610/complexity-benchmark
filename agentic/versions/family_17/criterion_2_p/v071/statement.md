# Problem B — Boolean State Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description
The system initialization sequence requires configuring a network of components. You are tasked with determining a valid state vector for $t$ potential signal pathways.

Each pathway can be assigned a boolean state: either activated (1) or disabled (0). Since there are $t$ pathways, the configuration space consists of $2^t$ possible assignments. The system contains $2q$ components, and the chosen assignment must satisfy a strict interference protocol. Specifically, for any component $k$, the sum of the states of all pathways connected to $k$ must be exactly 1. If the sum is 0, the component is dormant; if it is greater than 1, interference causes a critical failure.

In the preceding diagnostic phase, the system generated a structural log of the $t$ viable pathways. The components are indexed from 1 to $2q$. The log reveals that each viable pathway connects a component with an index $a \le q$ to a component with an index $b > q$.

Your task is to search the configuration space and decide whether the given log allows for a valid state assignment. If it does, output the activated pathways; otherwise, report that it is impossible.

## Input
The first line contains two integers $q$ and $t$ (1 ≤ $q$ ≤ 100000, 0 ≤ $t$ ≤ 400000), where $2q$ is the total number of components and $t$ is the number of viable pathways.
The following $t$ lines each contain two integers $a$ and $b$ (1 ≤ $a$ ≤ $q$ < $b$ ≤ $2q$), indicating a viable pathway between component $a$ and component $b$.

## Output
If there exists an assignment satisfying all constraints, print `YES` on the first line, followed by $q$ lines. Each of these lines must contain the two component IDs of an activated pathway. If no such assignment exists, print `NO`.

## Example

**Input**
```text
3 4
1 4
1 5
2 5
3 6
```

**Output**
```text
YES
1 4
2 5
3 6
```
