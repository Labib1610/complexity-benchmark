# Asset Configuration Synthesis

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate is synthesizing an operational protocol for the upcoming drill. You are tasked with selecting a configuration from a massive space of possibilities. 

There are $2q$ distinct assets in total. The first $q$ assets are controllers (IDs $1$ through $q$), and the remaining $q$ assets are platforms (IDs $q+1$ through $2q$). You are provided with a certification log containing $t$ potential links. Each link explicitly connects one controller to one platform.

Your objective is to choose a subset of these $t$ links to form a complete operational protocol. Since there are $t$ potential links, there are $2^t$ possible configurations (subsets) to consider. A configuration is only valid if it meets the following strict constraints:
- **Full Coverage**: Every single asset (all controllers and all platforms) must be activated by the chosen protocol.
- **Zero Interference**: No asset may appear in more than one selected link.

Determine whether a valid configuration exists within the $2^t$ search space. If it does, extract and output the chosen links; otherwise, report that no protocol can be formed.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing an allowed link between controller $a$ and platform $b$.

## Output
If a valid configuration is possible, print `YES` followed by $q$ lines, each containing the two IDs of a selected link. If no valid configuration exists, print `NO`.

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
